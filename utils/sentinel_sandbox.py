import sentinelhub as stnl
import numpy as np
import geopandas as gpd
from shapely.geometry import shape, Polygon, MultiPolygon, MultiLineString
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as plt_polygon
#from mpl_toolkits.basemap import Basemap  # Avaliable here: https://github.com/matplotlib/basemap

inputfile = '/Users/Chris/Desktop/hey/dssg/test2.json'

geo_json = gpd.read_file(inputfile)
study_area = geo_json[["geometry"]].copy()

print(study_area)
print(type(study_area))



for coord in np.asarray(study_area.exterior.coords):
	print(stnl.geo_utils.wgs84_to_utm(coord[0], coord[1]))