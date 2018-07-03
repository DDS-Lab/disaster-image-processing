import geopandas as gpd
import pandas as pd
import sys

layer_list = []
for f in sys.argv[1:]:
    layer_list.append(gpd.read_file(f))

output_layer = pd.concat([x for x in layer_list])
output_layer.to_file('concat_layer')
