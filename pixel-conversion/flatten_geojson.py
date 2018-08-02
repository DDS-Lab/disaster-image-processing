'''
This script get the output of Sean's QGIS process and flattens the output in
order to be runnable on other scripts
'''

import geopandas as gpd


def keep_rows_with_values(df, row_name):
    df_temp = df[['id', 'damagelevel', 'geometry', row_name]].dropna()
    df_temp.columns = ['id', 'damagelevel', 'geometry', 'image']
    return df_temp


df = gpd.read_file('data_training/boundingboxes/boundingboxes_damaged.geojson')

dates = ['files_0827', 'files_0828', 'files_0829', 'files_0830', 'files_0831',
         'files_0901', 'files_0902', 'files_0903']
flat_df = gpd.GeoDataFrame(columns=['id', 'damagelevel', 'geometry', 'image'])
for date in dates:
    temp_df = keep_rows_with_values(df, date)
    flat_df = flat_df.append(temp_df, ignore_index=True)
flat_df

flat_df.to_file('data_training/boundingboxes/boundingboxes_flat.geojson',
                driver='GeoJSON')
