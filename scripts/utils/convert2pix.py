import geopandas as gpd
from shapely.ops import cascaded_union
import shapely.wkt
from os import listdir
from os.path import isfile, join, isdir
import sys
import numpy as np
from osgeo import gdal

tiffolder = "./image_tiles/1"

# Get a list of all the files in the tiffolder and its sub-folders
onlyfiles = set([f for f in listdir(tiffolder) if isfile(join(tiffolder, f)) and f.endswith('.tif')])

driver = gdal.GetDriverByName('GTiff')

# Obtain json file and make a copy
gdf = gpd.read_file(open('./image_tiles/1/boundingboxes-all-damagearea-pixelcoords.geojson'))
gdf_test = gdf.copy()

# Transforms geospatial coordinates to pixel coordinates
def getTransform(img_id, x_min, y_min, x_max, y_max):
  path = join(tiffolder, img_id)
  dataset = gdal.Open(path)
  transform = dataset.GetGeoTransform()
  xOrigin = transform[0]
  yOrigin = transform[3]
  pixelWidth = transform[1]
  pixelHeight = -transform[5]
  xmin = max([0, int((x_min - xOrigin) / pixelWidth)])
  ymin = max([0, int((yOrigin - y_min) / pixelHeight)])
  xmax = max([0, int((x_max - xOrigin) / pixelWidth)])
  ymax = max([0, int((yOrigin - y_max) / pixelHeight)])
  return xmin, ymin, xmax, ymax

gdf_test['bb'] = None
for index, entry in gdf_test.iterrows():
  curr_coords = list(gdf['geometry'].iloc[index].geoms)
  x, y = curr_coords[0].exterior.coords.xy
  x_min = min(x)
  y_min = min(y)
  x_max = max(x)
  y_max = max(y)
  tif_id = entry['image']
  # Remove the "[date]/" part of tif_id to match the onlyfiles file format
  tif_name = tif_id.split("/")[1]
  if tif_name in onlyfiles:
    pass
  else:
    continue
  # All tiles, including the ones I actually have, won't trigger the getCondition function
  out = getTransform(tif_name, x_min, y_max, x_max, y_min)
  gdf_test.loc[index, 'bb'] = str(out)

gdf_test.to_file("./image_tiles/1/boundingboxes-all-damagearea-pixelcoords-updated.geojson", driver='GeoJSON')
