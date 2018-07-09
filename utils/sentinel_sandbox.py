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

inputfile = '/Users/Chris/Desktop/hey/dssg/coordinateandtif.json'
tiffolder = '/Users/Chris/Desktop/hey/dssg/sample_tiff/'
image_lat_longs_w_id = '/Users/Chris/Desktop/hey/dssg/tifRange-tiles-run-1.csv'
onlyfiles = [f for f in listdir(tiffolder) if isfile(join(tiffolder, f)) and f.endswith('.tif')]

with open(image_lat_longs_w_id, 'r') as f:
	reader = csv.reader(f)
	next(reader)
	image_ids = [r for r in reader]

testd = image_ids[0]
img_ids_only = set()
for i in image_ids:
	img_ids_only.add(i[0])

#smalltiffidfile = '/Users/Chris/Desktop/hey/dssg/tifRange-tiles-run-1.csv'
# image_lat_longs_w_id = csv.DictReader(open("image_id_ll.csv"))
driver = gdal.GetDriverByName('GTiff')

## Read json file and get all entries
geo_json = gpd.read_file(inputfile)
bounding_boxes = geo_json.copy()

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
	return xOrigin, yOrigin, pixelWidth, pixelHeight, cols, rows, band

def convert(xOrigin, yOrigin, pixelWidth, pixelHeight, cols, rows, band):
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

for _, entry in bounding_boxes.ix[0:10].iterrows():
	min_max_coords = [entry['geometry'].bounds]
	tif_id = entry['tif_id']
	if tif_id not in img_ids_only or tif_id not in onlyfiles:
		print('hey')
		pass
	transform = transformations[tif_id]
	xOrigin = transform[0]
	yOrigin = transform[1]
	pixelWidth = transform[2]
	pixelHeight = transform[3]
	cols = transform[4]
	rows = transform[5]
	band = transform[6]
	convert(xOrigin, yOrigin, pixelWidth, pixelHeight, cols, rows, band)



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