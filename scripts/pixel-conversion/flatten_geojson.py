'''
This script get the output of Sean's QGIS process and flattens the output in
order to be runnable on other scripts
'''
import argparse
import geopandas as gpd


def keep_rows_with_values(df, row_name):
    df_temp = df[['id', 'damagelevel', 'geometry', row_name]].dropna()
    df_temp.columns = ['id', 'damagelevel', 'geometry', 'image']
    return df_temp


parser = argparse.ArgumentParser()
parser.add_argument('input', help="name the geojson you want flat")
parser.add_argument('output', help="name what you want it called")
args = parser.parse_args()

df = gpd.read_file('../data_training/boundingboxes/' + args.input)

dates = ['files_0827', 'files_0828', 'files_0829', 'files_0830', 'files_0831',
         'files_0901', 'files_0902', 'files_0903']
flat_df = gpd.GeoDataFrame(columns=['id', 'damagelevel', 'geometry', 'image'])
for date in dates:
    temp_df = keep_rows_with_values(df, date)
    flat_df = flat_df.append(temp_df, ignore_index=True)
flat_df.id = flat_df.index

flat_df.to_file('../data_training/boundingboxes/' + args.output,
                driver='GeoJSON')
