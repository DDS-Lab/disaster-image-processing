import geopandas as gpd
import pandas as pd
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]
x_translation, y_translation = int(sys.argv[3]), int(sys.argv[4])
img_x_size, img_y_size = int(sys.argv[5]), int(sys.argv[6])
pixel_column_name = sys.argv[7]

def testBounds(pt, translate, bound_pxl):
	new_pt = pt + translate
	if new_pt > bound_pxl:
		new_pt = bound_pxl
	if new_pt < 0:
		new_pt = 0
	return new_pt

def getBigTifID(input_path, output_path):
	input_geo = gpd.read_file(input_path)
	geo = input_geo.copy()
	big_tif_id_column = []
	for b in geo['IMAGE_ID']:
		split = b.split('_')
		val = split[1] + '_' + split[2]
		big_tif_id_column.append(val)
	input_geo['BIG_TIF_ID'] = big_tif_id_column
	input_geo.to_file(output_path, driver='GeoJSON')

def translatePixels(input_path, x_translation, y_translation, img_x_size, img_y_size, pixel_column_name):
	input_geo = gpd.read_file(input_path)
	geo = input_geo.copy()
	x_translation = int(x_translation)
	y_translation = int(y_translation)
	img_x_size = int(img_x_size)
	img_y_size = int(img_y_size)
	translated_column = []
	for b in geo[pixel_column_name]:
		split = b.strip('()').split(', ')
		x_min, y_min, x_max, y_max = [int(x) for x in split]
		x_min = testBounds(x_min, x_translation, img_x_size)
		x_max = testBounds(x_max, x_translation, img_x_size)
		y_min = testBounds(y_min, y_translation, img_y_size)
		y_max = testBounds(y_max, y_translation, img_y_size)
		new = '(' + str(x_min) + ',' + str(y_min) + ',' + str(x_max) + ',' + str(y_max) + ')'
		translated_column.append(new)
	return translated_column

def merge(BigTifTranslation, input_geojson, output_path):
	TranslationData = pd.read_csv(BigTifTranslation, engine='python')
	input_geo = gpd.read_file(input_geojson)
	end = pd.merge(input_geo, TranslationData, on='BIG_TIF_ID', how='outer')
	end.to_file(output_path, driver='GeoJSON')






