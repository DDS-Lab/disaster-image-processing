import geopandas as gpd
import pandas as pd
import sys

"""
This script takes any number of shapefiles as arguments and outputs a merged
shapefile containing the features of both.

The resulting file is called 'concat_layer' and is output to the current
directory.
"""

layer_list = []
for f in sys.argv[1:]:
    layer_list.append(gpd.read_file(f))

output_layer = pd.concat([x for x in layer_list])
output_layer.to_file('concat_layer')
