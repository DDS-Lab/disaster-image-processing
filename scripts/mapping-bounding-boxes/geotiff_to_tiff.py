'''
convert geotiff to tiff
'''

import numpy as np
import csv
#import matplotlib, copy, skimage, os, tifffile
from skimage import io, draw
import gdal
import os
from PIL import Image
import os.path



# take absolute path of geotiff dir
def convert_geotiff_tiff(geotiff_dir, tiff_dir):
    files = [os.path.join(geotiff_dir, f) for f in os.listdir(geotiff_dir)]
    for f in files:
        if not f.endswith('tif'):
            continue
        tilename = f.split('/')[-1]
        # debug
        print('tilemame: ', tilename)
        # check file exits
        temp_f = os.path.join(tiff_dir, tilename)
        print(temp_f)
        if os.path.exists(temp_f):
            print('file exits, skip')
            continue
        ds = gdal.Open(f)
        arr1 = ds.GetRasterBand(1).ReadAsArray()
        arr2 = ds.GetRasterBand(2).ReadAsArray()
        arr3 = ds.GetRasterBand(3).ReadAsArray()
        stacked = np.stack((arr1, arr2, arr3), axis = 2)
        # create new tiff image
        im = Image.fromarray(stacked)
        new_tiff = os.path.join(tiff_dir, tilename)
        im.save(new_tiff)


def main():
  geotiff_dir = '../image_tiles_aws'
  tiff_dir = '../converted_image_tiles_aws'
  convert_geotiff_tiff(geotiff_dir, tiff_dir)


if __name__ == '__main__':
  main()
