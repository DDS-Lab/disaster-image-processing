import geopandas as gpd
import sys

# Script that takes in a shapefile and outputs bounding boxes for each feature. Accepts buffer and cap_style arguments.

# Accepts 4 arguments:
#1 - input shapefile
#2 - output shapefile

input_geo = gpd.read_file(sys.argv[1])

geocopy = input_geo.copy()
geocopy.geometry = [g.centroid for g in geocopy.geometry]
geocopy.to_file(sys.argv[2])
