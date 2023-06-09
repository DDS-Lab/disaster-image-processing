'''
chipImage.py

This script takes either an individual tif image file or a folder of tif image files and chips the
images into smaller chips, which can then be used as training/testing data for deep learning
neural networks.

Author: Jungmin Ahn
'''

'''Import packages'''

import rasterio
import geopandas as gpd
import pandas as pd
import numpy as np
from PIL import Image
from ast import literal_eval
import os
import tensorflow as tf
import io

'''Define image, GDF and folder directories'''

mytif = './image_tiles/1/20170830aC0952830w294630n_1_2.tif'
gdf = gpd.read_file(open('./image_tiles/1/boundingboxes-all-damagearea-pixelcoords.geojson'))
folder = './image_tiles/1'

'''Define and create (if necessary) directories where chip images and TFRecords will be stored'''

dir_images = './image_tiles/chips/images'
dir_records = './image_tiles/chips/tf_records'

for dir in [dir_images, dir_records]:
  if not os.path.exists(dir):
    os.makedirs(dir)

def get_image_resources(tif):
  '''
  Obtains the tif file name, rasterio image object, and the array represenation of the given tif file.

  Parameters
  ----------
  tif: str
    The file path to the tif file to extract information from

  Returns
  -------
  tif_name: str
    The name of the tif file extracted from the given file path
  img: DatasetReader
    The Rasterio representation of the tif file
  image_array: ndarray
    The array representation of the image of the tif file with dimensions (H, W, C):
    H = Height of image
    W = Width of image
    C = Number of color channels in the image
  '''
  img = rasterio.open(tif, 'r')
  tif_name = tif.split('/')[3]
  image = Image.open(tif)
  image_array = np.array(image)
  return tif_name, img, image_array

def get_coordinates(img, tif_name):
  '''
  Compiles all the coordinates of the bounding boxes of the given image into an array.

  Parameters
  ----------
  img: DatasetReader
    The image file that you would like to extract the bounding box coordinates from
  tif_name: str
    The filename of the tif file associated with the image defined above

  Returns
  -------
  coordinates: ndarray
    The array of the coordinates of the bounding boxes in the image with dimensions (N, 4)
  '''
  extent = [img.bounds[0], img.bounds[2], img.bounds[1], img.bounds[3]]
  xmin, xmax, ymin, ymax = extent
  gdf_array = gdf.cx[xmin:xmax, ymin:ymax]
  gdf_array_filtered = gdf_array[gdf_array['image'].str.contains(tif_name)]
  coordinates = np.array(gdf_array_filtered['bb'].apply(literal_eval).to_list())
  return coordinates

def get_classes(img, tif_name):
  '''
  Compiles all the classes of the bounding boxes of the given image into an array.

  Parameters
  ----------
  img: DatasetReader
    The image file that you would like to extract the bounding box classes from
  tif_name: str
    The filename of the tif file associated with the image defined above

  Returns
  -------
  coordinates: ndarray
    The array of the classes of each bounding box with dimensions (N, 1)
  '''
  extent = [img.bounds[0], img.bounds[2], img.bounds[1], img.bounds[3]]
  xmin, xmax, ymin, ymax = extent
  gdf_array = gdf.cx[xmin:xmax, ymin:ymax]
  gdf_array_filtered = gdf_array[gdf_array['image'].str.contains(tif_name)]
  tif_classes = gdf_array_filtered['damageleve']
  tif_classes = tif_classes.reset_index(drop = True)
  classes = np.empty((len(tif_classes)), dtype = object)
  for i in range(len(tif_classes)):
    classes[i] = tif_classes[i]
  return classes

def chip_image(img, coords, classes, filename, shape=(256,256)):
  '''
  Produces and saves chips (small samples) of a given image.

  Parameters
  ----------
  img: ndarray
    The array representation of the image with dimensions (H, W, C):
    H = Height of image
    W = Width of image
    C = Number of color channels in the image
  coords: ndarray
    The array of the coordinates of the bounding boxes in the image with dimensions (N, 4)
  classes: ndarray
    The array of the classes of each bounding box with dimensions (N, 1)
  filename: str
    The filename of the image to be chipped
  shape: tuple, optional(default = (256, 256))
    The dimensions of the chips to be produced in pixels

  Returns
  -------
  images: ndarray
    The array representation of the chips with dimensions (H, W, C):
    H = Height of chip
    W = Width of chip
    C = Number of color channels in the chip
  total_boxes: dict
    Contains an (N, 4) array of the coordinates of the bounding boxes in the chips
  total_classes: dict
    Contains an (N, 1) array of the classes of each bounding box
  '''
  height,width,_ = img.shape
  wn,hn = shape

  w_num,h_num = (int(width/wn),int(height/hn))
  images = np.zeros((w_num*h_num,hn,wn,3))
  total_boxes = {}
  total_classes = {}

  k = 0
  for i in range(w_num):
    for j in range(h_num):
      x = np.logical_or(np.logical_and((coords[:,0]<((i+1)*wn)),(coords[:,0]>(i*wn))),
                        np.logical_and((coords[:,2]<((i+1)*wn)),(coords[:,2]>(i*wn))))
      out = coords[x]

      y = np.logical_or(np.logical_and((out[:,1]<((j+1)*hn)),(out[:,1]>(j*hn))),
                        np.logical_and((out[:,3]<((j+1)*hn)),(out[:,3]>(j*hn))))
      outn = out[y]

      out_final = np.transpose(np.vstack((np.clip(outn[:,0]-(wn*i),0,wn),
                                          np.clip(outn[:,1]-(hn*j),0,hn),
                                          np.clip(outn[:,2]-(wn*i),0,wn),
                                          np.clip(outn[:,3]-(hn*j),0,hn))))
      box_classes = classes[x][y]

      if out_final.shape[0] != 0:
        total_boxes[k] = out_final
        total_classes[k] = box_classes
      else:
        total_boxes[k] = np.array([[0,0,0,0]])
        total_classes[k] = np.array([0])

      chip = img[hn*j:hn*(j+1),wn*i:wn*(i+1),:3]
      images[k]=chip

      chip_image = Image.fromarray(chip)
      tif_filename = filename.split('/')[3].split('.')[0]
      chip_image.save("./image_tiles/chips/images/" + str(tif_filename) + "_" + str(k + 1) + ".png")

      k = k + 1

  return images.astype(np.uint8),total_boxes,total_classes

def save_results(images, boxes, classes):
  '''
  Saves data regarding the chips, bounding boxes in the chips and classes of each bounding box as arrays.

  Parameters
  ----------
  images: ndarray
    The array representation of the chips with dimensions (H, W, C):
    H = Height of chip
    W = Width of chip
    C = Number of color channels in the chip
  boxes: dict
    Contains an (N, 4) array of the coordinates of the bounding boxes in the chips
  classes: dict
    Contains an (N, 1) array of the classes of each bounding box

  Returns
  -------
  images_array: ndarray
    The array representation of the chips with dimensions (H, W, C):
    H = Height of chip
    W = Width of chip
    C = Number of color channels in the chip
  boxes_array: ndarray
    The array of the coordinates of the bounding boxes in the chip with dimensions (N, 4)
  classes_array: ndarray
    The array of the classes of each bounding box with dimensions (N, 1)
  '''
  images_array = []
  boxes_array = []
  classes_array = []

  for i in images:
    images_array.append(i)
  for b in boxes:
    boxes_array.append(boxes[b])
  for c in classes:
    classes_array.append(classes[c])

  images_array = np.array(images_array)
  boxes_array = np.array(boxes_array)
  classes_array = np.array(classes_array)

  return images_array, boxes_array, classes_array

def to_tf_example(img, boxes, class_num):
  '''
  Converts a single image with respective boxes into a TFExample.  Multiple TFExamples make up a TFRecord.

  Arguments
  ---------
  img: nparray
    The array representation of the image with dimensions (H, W, C):
    H = Height of image
    W = Width of image
    C = Number of color channels in the image
  boxes: nparray
    The array of the coordinates of the bounding boxes in the image with dimensions (N, 4)
  class_num: nparray
    The array of the classes of each bounding box with dimensions (N, 1)

  Returns
  -------
  example: TFExample
    A TFExample containing encoded image data, scaled bounding boxes with classes, and other metadata
  '''
  encoded = convertToJpeg(img)

  width = img.shape[0]
  height = img.shape[1]

  xmin = []
  ymin = []
  xmax = []
  ymax = []
  classes = []
  classes_text = []

  for ind,box in enumerate(boxes):
    xmin.append(box[0] / width)
    ymin.append(box[1] / height)
    xmax.append(box[2] / width)
    ymax.append(box[3] / height)
    classes.append(bytes(str(class_num[ind]), 'utf-8', errors = 'ignore'))

  example = tf.train.Example(features=tf.train.Features(feature={
          'image/height': int64_feature(height),
          'image/width': int64_feature(width),
          'image/encoded': bytes_feature(encoded),
          'image/format': bytes_feature('jpeg'.encode('utf8')),
          'image/object/bbox/xmin': float_list_feature(xmin),
          'image/object/bbox/xmax': float_list_feature(xmax),
          'image/object/bbox/ymin': float_list_feature(ymin),
          'image/object/bbox/ymax': float_list_feature(ymax),
          'image/object/class/label': bytes_list_feature(classes),
  }))

  return example

def convertToJpeg(im):
  '''
  Converts an image array into an encoded JPEG string.

  Arguments
  ---------
  im: nparray
    The array representation of the image with dimensions (H, W, C):
    H = Height of image
    W = Width of image
    C = Number of color channels in the image

  Returns
  -------
  f.getvalue(): bytes
    An encoded byte string containing the converted JPEG image
  '''
  with io.BytesIO() as f:
    im = Image.fromarray(im)
    im.save(f, format='JPEG')
    return f.getvalue()

def create_tf_record(output_filename, images, boxes, features):
  '''
  Creates a TFRecord file from examples.

  Arguments
  ---------
  output_filename: str
    Path to where output file is saved
  images: nparray
    The array representation of the image with dimensions (H, W, C):
    H = Height of image
    W = Width of image
    C = Number of color channels in the image
  boxes: nparray
    The array of the coordinates of the bounding boxes in the image with dimensions (N, 4)
  features: nparray
    The array of the classes of each bounding box with dimensions (N, 1)
  '''
  writer = tf.io.TFRecordWriter(output_filename)
  k = 0
  for idx, image in enumerate(images):
    print('On image %d of %d' %((idx + 1), len(images)))

    tf_example = to_tf_example(image,boxes[idx],features[idx])
    if np.array(tf_example.features.feature['image/object/bbox/xmin'].float_list) is not None:
      writer.write(tf_example.SerializeToString())
      k = k + 1

  print("TFRecord file successfully created!")
  writer.close()

def int64_feature(value):
  '''
  Adds an integer feature to a TFExample.

  Arguments
  ---------
  value: int
    The value to be added to a TFExample

  Returns
  -------
  tf.train.Feature(int64_list=tf.train.Int64List(value=[value])): Feature
    The value programmed to be implemented to a TFExample
  '''
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def int64_list_feature(value):
  '''
  Adds an integer list feature to a TFExample.

  Arguments
  ---------
  value: list
    The value to be added to a TFExample

  Returns
  -------
  tf.train.Feature(int64_list=tf.train.Int64List(value=value)): Feature
    The value programmed to be implemented to a TFExample
  '''
  return tf.train.Feature(int64_list=tf.train.Int64List(value=value))

def bytes_feature(value):
  '''
  Adds an byte feature to a TFExample.

  Arguments
  ---------
  value: bytes
    The value to be added to a TFExample

  Returns
  -------
  tf.train.Feature(bytes_list=tf.train.BytesList(value=[value])): Feature
    The value programmed to be implemented to a TFExample
  '''
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def bytes_list_feature(value):
  '''
  Adds an byte list feature to a TFExample.

  Arguments
  ---------
  value: list
    The value to be added to a TFExample

  Returns
  -------
  tf.train.Feature(bytes_list=tf.train.BytesList(value=value)): Feature
    The value programmed to be implemented to a TFExample
  '''
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=value))

def float_list_feature(value):
  '''
  Adds an float list feature to a TFExample.

  Arguments
  ---------
  value: list
    The value to be added to a TFExample

  Returns
  -------
  tf.train.Feature(float_list=tf.train.FloatList(value=value)): Feature
    The value programmed to be implemented to a TFExample
  '''
  return tf.train.Feature(float_list=tf.train.FloatList(value=value))

def image_chipping(tif):
  '''
  Chips a single tif file.

  Arguments
  ---------
  tif: str
    The directory to the tif file to be chipped
  '''
  tif_name, image, image_array = get_image_resources(tif)
  coordinates = get_coordinates(image, tif_name)
  classes = get_classes(image, tif_name)
  images, boxes, classes = chip_image(image_array, coordinates, classes, tif)
  images_array, boxes_array, classes_array = save_results(images, boxes, classes)
  tif_filename = tif.split('/')[3].split('.')[0]
  create_tf_record(dir_records + '/' + tif_filename + '.tfrecords', images_array, boxes_array, classes_array)

def chip_folder(folder):
  '''
  Chips a folder of tif files.

  Arguments
  ---------
  folder: str
    The directory to the folder whose tif files are to be chipped
  '''
  for filename in os.listdir(folder):
    f = os.path.join(folder, filename)
    ext = os.path.splitext(f)[-1].lower()
    if os.path.isfile(f) and ext == ".tif":
      print(f)
      image_chipping(f)

'''
Please comment out one or the other one of these function calls in order to ensure that your tif
file(s) are properly chipped!
'''

image_chipping(mytif)
# chip_folder(folder)

'''
Notes:
- See if NumPy can read TFRecords (tfrecord dataset)
- Have an option to have one big TFRecord instead of individual TFRecords
- Have an option to keep the NumPy format (.npy) (will need to merge TFRecords)
  - PyTorch can read TFRecords
  - Show how to extract labels and other information from TFRecords (in Jupyter Notebook)
- Add a README file to describe the uploaded files
  - What level are the tifs in? What size are the chips? etc.
  - Document the size of zip folders/files
'''