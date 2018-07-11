import geopandas as gpd
import sys

# Script that takes in a shapefile and outputs bounding boxes for each feature. Accepts buffer and cap_style arguments.

# Accepts 3 arguments:
#1 - input shapefile
#2 - output shapefile
#3 - buffer size

input_geo = gpd.read_file(sys.argv[1])
distance = float(sys.argv[3])

boundinggeo = input_geo.copy()
boundinggeo.geometry = [g.buffer(distance, cap_style=3) for g in boundinggeo.geometry]
outname = sys.argv[2]
boundinggeo.to_file(outname, driver='GeoJSON')
