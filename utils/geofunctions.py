import geopandas as gpd
import pandas as pd
import sys
import numpy as np
from shapely.geometry import shape, Polygon, MultiPolygon, MultiLineString
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as plt_polygon
from fiona.crs import from_epsg
import csv
import gdal
from os import listdir
from os.path import isfile, join

def concat_layers(list_of_paths, output_path):
	layer_list = []
	for f in list_of_paths:
	    layer_list.append(gpd.read_file(f))
	output_layer = pd.concat([x for x in layer_list])
	output_layer.to_file(output_path)

# Define a function that transforms lat long coordinates into pixels for a given image
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
	xmax = max([0, int((x_max - xOrigin) / pixelWidth)])~/
	ymax = max([0, int((yOrigin - y_max ) / pixelHeight)])
	return xmin, ymin, xmax, ymax

# Script that takes in a shapefile and outputs bounding boxes for each feature. Accepts buffer and cap_style arguments.
# Accepts 2 arguments:
#1 - input shapefile path
#2 - output shapefile path
def getEnvelope(input_shp_path, output_shp_path):
	input_geo = gpd.read_file(input_shp_path)
	boundinggeo = input_geo[['geometry']].copy()
	boundinggeo.geometry = [g.envelope for g in boundinggeo.geometry]
	boundinggeo.to_file(output_shp_path)

# Script that takes in a shapefile and outputs bounding boxes for each feature. Accepts buffer and cap_style arguments.
# Accepts 3 arguments:
#1 - input shapefile
#2 - output shapefile
#3 - buffer size. Capstyle is set to 3 so that you get a square of constant 'radius' of 'distance'
def getBuffer(input_shp_path, output_shp_path, distance):
	input_geo = gpd.read_file(input_shp_path)
	distance = float(distance)
	boundinggeo = input_geo.copy()
	boundinggeo.geometry = [g.buffer(distance, cap_style=3) for g in boundinggeo.geometry]
	outname = output_shp_path + '.geojson'
	boundinggeo.to_file(outname, driver='GeoJSON')


