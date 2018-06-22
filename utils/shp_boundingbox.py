import geopandas as gpd
import sys

# Script that takes in a shapefile and outputs bounding boxes for each feature. Accepts buffer and cap_style arguments.

# Accepts 4 arguments:
#1 - input shapefile
#2 - buffer distance
#3 - 'cap_style' - see http://toblerity.org/shapely/shapely.geometry.html
#4 - output shapefile

input_geo = gpd.read_file(sys.stdin[1])
dist = int(sys.stdin[2])
cap = int(sys.stdin[3])

boundinggeo = input_geo[['geometry']].copy()
boundinggeo.geometry = [g.buffer(dist, cap_style=cap) for g in boundinggeo.geometry]
boundinggeo.to_file(sys.stdin[4])
