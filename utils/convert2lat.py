import geopandas as gpd
from shapely.ops import cascaded_union
import gdal
from os import listdir
from os.path import isfile, join, isdir
import sys

"""
This file accepts a GeoJSON file of bounding boxes with a geometry and
image ID column to output the pixel bounds of the bounding box in a string
column of the form '(minx, miny, maxx, maxy)'.

1st arg is the input path of the GeoJSON, 2nd argument is the smalltiff folder,
3rd is the output path.
"""

# Input a <.json> file path that has the bounding boxes in the geometry column
inputfile = sys.argv[1]

# Input a path to a folder of smalltiffs
tiffolder = sys.argv[2]

# Get a list of all the files in the tiffolder and its sub-folders
onlyfiles = []
for i in listdir(tiffolder):
    if isdir(join(tiffolder, i)):
        for x in listdir(join(tiffolder, i)):
            if isfile(join(tiffolder, i, x)) and x.endswith('.tif'):
                onlyfiles.append(join(i, x))

onlyfiles = set(onlyfiles)

"""
The comment below is to replace the code above if all images are in a single
folder.
"""
# onlyfiles = set([f for f in listdir(tiffolder) if isfile(join(tiffolder, f))
#                and f.endswith('.tif')])

# Set driver so gdal processes know that we are working with geotiffs
driver = gdal.GetDriverByName('GTiff')

# Make a copy of the bounding boxes json file to work with
geo_json = gpd.read_file(inputfile)
bounding_boxes = geo_json.copy()


def getTransform(img_id, x_min, y_min, x_max, y_max):
    """
        Define a function that transforms pixel coordinates into lat long for
        a given image
    """
    path = join(tiffolder, img_id)
    dataset = gdal.Open(path)
    transform = dataset.GetGeoTransform()
    width = dataset.RasterXSize
    height = dataset.RasterYSize
    minx_tif = transform[0]
    miny_tif = transform[3] + width * transform[4] + height * transform[5]
    maxx_tif = transform[0] + width * transform[1] + height * transform[2]
    maxy_tif = transform[3]
    xmin = ((maxx_tif - minx_tif) / width * x_min) + minx_tif
    xmax = ((maxx_tif - minx_tif) / width * x_max) + minx_tif
    ymin = ((maxy_tif - miny_tif) / width * y_min) + miny_tif
    ymax = ((maxy_tif - miny_tif) / width * y_max) + miny_tif
    #xmin = max([0, int((x_min - minx_tif) / pixelWidth)])
    #ymin = max([0, int((miny_tif - y_min) / pixelHeight)])
    #xmax = max([0, int((x_max - minx_tif) / pixelWidth)])
    #ymax = max([0, int((miny_tif - y_max) / pixelHeight)])
    print(minx_tif, miny_tif, maxx_tif, maxy_tif)
    print(xmin, ymin, xmax, ymax)
    return xmin, ymin, xmax, ymax


"""
Add to the input geojson a blank column that takes the pixel coordinates of
the bounding box
"""

geo_json['latlong'] = None
for index, entry in bounding_boxes.iterrows():
    """
        For every entry in the .geojson with bounding boxes, add to the 'bb'
        column a conversion from lat long to their 'pixel' coordinates
        according to their image (smalltif id)
    """
    bounds = [entry['pixels']]
    # print(entry['catalog_id'])
    #if bounds[0].type == 'MultiPolygon':
    #        allparts = [p.buffer(0) for p in min_max_coords[0]]
    #        min_max_coords[0] = cascaded_union(allparts)
    x_min, y_min, x_max, y_max = min_max_coords[0]
    # print(x,y)
    #x_min = min(x)
    #y_min = min(y)
    #x_max = max(x)
    #y_max = max(y)
    # print(x_min, y_min, x_max, y_max)
    tif_id = entry['image']
    # print('')
    # print(index)
    if tif_id in onlyfiles:
        pass
    else:
        continue
    out = getTransform(tif_id, x_min, y_max, x_max, y_min)
    geo_json.loc[index, 'latlong'] = str(out)

geo_json.to_file(sys.argv[3], driver='GeoJSON')
