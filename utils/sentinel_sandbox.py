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

inputfile = '/Users/Chris/Desktop/hey/dssg/lol.json'
tiffolder = '/Users/Chris/Desktop/hey/dssg/sample_tiff/'
image_lat_longs_w_id = '/Users/Chris/Desktop/hey/dssg/tifRange-tiles-run-1.csv'
onlyfiles = set([f for f in listdir(tiffolder) if isfile(join(tiffolder, f)) and f.endswith('.tif')])

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

def getTransform(img_id, x_min, y_min, x_max, y_max):
	path = tiffolder + img_id
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
	data = band.ReadAsArray()
	xmin = max([0, int((x_min - xOrigin) / pixelWidth)])
	ymin = max([0, int((yOrigin - y_min ) / pixelHeight)])
	xmax = max([0, int((x_max - xOrigin) / pixelWidth)])
	ymax = max([0, int((yOrigin - y_max ) / pixelHeight)])
	return xmin, ymin, xmax, ymax

'''

'''

for _, entry in bounding_boxes.loc[0:10].iterrows():
	min_max_coords = [entry['geometry']]
	x, y = min_max_coords[0].exterior.coords.xy
	print(x,y)
	x_min = min(x)
	y_min = min(y)
	x_max = max(x)
	y_max = max(y)
	print(x_min, y_min, x_max, y_max)
	tif_id = entry['tif_id']
	if tif_id in onlyfiles: 
		pass
	else:
		continue
	out = getTransform(tif_id, x_min, y_min, x_max, y_max)
	print(out)



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