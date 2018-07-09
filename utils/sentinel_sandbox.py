#import sentinelhub as stnl
import numpy as np
import geopandas as gpd
from shapely.geometry import shape, Polygon, MultiPolygon, MultiLineString
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as plt_polygon
from fiona.crs import from_epsg
import csv
import gdal
from os import listdir
from os.path import isfile, join

#from mpl_toolkits.basemap import Basemap  # Avaliable here: https://github.com/matplotlib/basemap

inputfile = '/Users/Chris/Desktop/hey/dssg/test2.json'
tiffolder = '/Users/Chris/Desktop/hey/dssg/sample_tiff/'
image_lat_longs_w_id = '/Users/Chris/Desktop/hey/dssg/tifRange-tiles-run-1.csv'
onlyfiles = [f for f in listdir(tiffolder) if isfile(join(tiffolder, f)) and f.endswith('.tif')]

with open(image_lat_longs_w_id, 'r') as f:
	reader = csv.reader(f)
	next(reader)
	image_ids = [r for r in reader]

testd = image_ids[0]

#smalltiffidfile = '/Users/Chris/Desktop/hey/dssg/tifRange-tiles-run-1.csv'
# image_lat_longs_w_id = csv.DictReader(open("image_id_ll.csv"))
driver = gdal.GetDriverByName('GTiff')

## get id of imag
geo_json = gpd.read_file(inputfile)
study_area = geo_json.copy()

def getTransform(img_id):
	path = tiffolder + '/' + img_id
	print(path)
	dataset = gdal.Open(path)
	band = dataset.GetRasterBand(1)
	cols = dataset.RasterXSize
	rows = dataset.RasterYSize
	transform = dataset.GetGeoTransform()
	xOrigin = transform[0]
	yOrigin = transform[3]
	pixelWidth = transform[1]
	pixelHeight = -transform[5]
	return xOrigin, yOrigin, pixelWidth, pixelHeight, cols, rows

def convert(xOrigin, yOrigin, pixelWidth, pixelHeight, cols, rows):
	data = band.ReadAsArray(0, 0, cols, rows)
	for point in points_list:
	    col = int((point[0] - xOrigin) / pixelWidth)
	    row = int((yOrigin - point[1] ) / pixelHeight)
    return row,col, data[row][col]


transformations = {}
for img_id in onlyfiles:
	print(img_id)
	xOrigin, yOrigin, pixelWidth, pixelHeight, cols, rows = getTransform(img_id)
	transformations[img_id] = [xOrigin, yOrigin, pixelWidth, pixelHeight, cols, rows]

for entry in study_area['geometry'][0:10]:
	min_max_coords = [entry.bounds]
	img_id = entry['img_id']
	entry['geometry']
	transform = transformations[img_id]
	xOrigin = transform[0]
	yOrigin = transform[1]
	pixelWidth = transform[2]
	pixelHeight = transform[3]
	cols = transform[4]
	rows = transform[5]
	convert(xOrigin, yOrigin, pixelWidth, pixelHeight, cols, rows)



'''

print(study_area['geometry'])


'''

# filename = "/home/zeito/pyqgis_data/aleatorio.tif"
'''
dataset = gdal.Open(filename)
band = dataset.GetRasterBand(1)

cols = dataset.RasterXSize
rows = dataset.RasterYSize

transform = dataset.GetGeoTransform()

xOrigin = transform[0]
yOrigin = transform[3]
pixelWidth = transform[1]
pixelHeight = -transform[5]

data = band.ReadAsArray(0, 0, cols, rows)

for 
points_list = [ (355278.165927, 4473095.13829), (355978.319525, 4472871.11636) ] #list of X,Y coordinates

for point in points_list:
    col = int((point[0] - xOrigin) / pixelWidth)
    row = int((yOrigin - point[1] ) / pixelHeight)

    print row,col, data[row][col]
 '''