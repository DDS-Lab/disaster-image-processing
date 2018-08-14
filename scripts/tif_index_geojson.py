import pandas as pd
import json
import geopandas as gpd

tomnod = gpd.read_file("DG_final_v2.geojson")
tifRange = pd.read_csv("tifRange-tiles-run-1.csv", header=None,
                       names=['tif_id', 'minxy','maxxy'])

# catalog_id == complete_c

def process_tup(tup):
    return [float(ele) for ele in (tup.strip('()').split(','))]


for i in range(len(tifRange)):
    tifRange.at[i,'catalog_id'] = (tifRange.iloc[i]['tif_id'].split(sep = "_")[1])
    tifRange.at[i, 'minxy'] = process_tup(tifRange.iloc[i]["minxy"])
    tifRange.at[i, 'maxxy'] = process_tup(tifRange.iloc[i]["maxxy"])


for i in range(len(tomnod)):
    x = tomnod.iloc[i]['label']
    if x == "Flooded / Damaged Building":
        tomnod.at[i,'type_id'] = '1'
    elif x == "Flooded / Blocked Road":
        tomnod.at[i,'type_id'] = '2'
    elif x == "Trash Heap":
        tomnod.at[i,'type_id'] = '3'
    elif x == "Blocked Bridge":
        tomnod.at[i,'type_id'] = '4'


tomnod['tif_id'] = ""
bad_list = []
for index_tomnod, row_tomnod in tomnod.iterrows():
    if index_tomnod % 1000 == 0:
        print('tomnod row: ', index_tomnod)
    tifRange_temp = tifRange[tifRange.catalog_id == row_tomnod['complete_c']]
    for index_tif, row_tif in tifRange_temp.iterrows():
        if row_tif['minxy'][0] <= row_tomnod['geometry'].exterior.coords.xy[0][4] <= row_tif['maxxy'][0] \
            and row_tif['minxy'][1] <= row_tomnod['geometry'].exterior.coords.xy[1][4] <= row_tif['maxxy'][1]:
            if tomnod.at[index_tomnod, 'tif_id'] == "":
                tomnod.at[index_tomnod, 'tif_id'] = row_tif["tif_id"]
                print ('yaaas')
            elif tomnod.at[index_tomnod, 'tif_id'] != "":
                tomnod = tomnod.append(tomnod.iloc[index_tomnod], ignore_index=True)
                tomnod.at[index_tomnod, 'tif_id'] = row_tif["tif_id"]
        # else:
            # bad_list.append([row_tomnod.name, row_tomnod['geometry'], row_tif['minxy'], row_tif['maxxy'], row_tomnod['complete_c']])
    


tomnod_out = tomnod[['label', 'type_id', 'complete_c', 'tif_id', 'geometry']]
tomnod_out.columns = ["label", "TYPE_ID", "CAT_ID", "IMAGE_ID", 'geometry']


# def df_to_geojson(df, properties, lat='latitude', lon='longitude'):
#     geojson = {'type':'FeatureCollection', 'features':[]}
#     for _, row in df.iterrows():
#         feature = {'type':'Feature',
#                    'properties':{},
#                    'geometry':{'type':'Point',
#                                'coordinates':[]}}
#         feature['geometry']['coordinates'] = [row[lon],row[lat]]
#         for prop in properties:
#             feature['properties'][prop] = row[prop]
#         geojson['features'].append(feature)
#     return geojson


# cols = list(tomnod_out.columns)
# geojson = df_to_geojson(tomnod_out, cols, lat = 'tomnod_y', lon = 'tomnod_x')

# output_filename = 'coordinateandtif.geojson'
# with open(output_filename, 'w') as output_file:
#     json.dump(geojson, output_file, indent=2)

tomnod_out.to_file('coordinateandtif.geojson', driver='GeoJSON')
