import geopandas as gpd
from geopandas.tools import sjoin
from shapely.geometry.polygon import Polygon
from shapely.geometry.multipolygon import MultiPolygon
import argparse
import glob
import os
import progressbar


def loadFile(file_path):
    shape = gpd.GeoDataFrame(gpd.read_file(file_path))
    return shape


def removeMultipolygons(geodataframe):
    df_in = geodataframe
    df_out = gpd.GeoDataFrame(columns=df_in.columns)
    for idx, row in df_in.iterrows():
        if type(row.geometry) == Polygon:
            df_out = df_out.append(row, ignore_index=True)
        else:
            continue
    return df_out


def polygonsInPolygons(contained_polygons, container_polygons, new_file):
    contained_polygons = loadFile(contained_polygons)
    container_polygons = loadFile(container_polygons)
    selected_contained_polygons = sjoin(contained_polygons, container_polygons, op='within')
    selected_contained_polygons = removeMultipolygons(selected_contained_polygons)
    selected_contained_polygons.to_file(new_file)
    return selected_contained_polygons


def createListOfFiles(directory, file_extension):
    files = glob.glob(directory + "/*." + file_extension)
    return files


def pullNamesFromDirectory(directory, file_extension):

    def pullNameFromFile(string):
        string = string.split('_')[-1]
        string = string.split('.')[0]
        return string

    names = []

    files = glob.glob(directory + "/*." + file_extension)

    for file in files:
        names.append(pullNameFromFile(file))

    return names


def createFileNames(names, modifier, extension):

    file_names = []

    for name in names:

        new_name = modifier + "_" + name + "." + extension
        file_names.append(new_name)

    return file_names


def zipTogetherFileLists(directory_one, directory_two, file_names):
    files = list(zip(directory_one, directory_two, file_names))
    return files


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('path_base')
    parser.add_argument('path_polygons_contained')
    parser.add_argument('path_polygons_container')
    parser.add_argument('file_extension')
    parser.add_argument('new_directory')

    arguments = parser.parse_args()

    path_base = arguments.path_base
    path_polygons_contained = arguments.path_polygons_contained
    path_polygons_container = arguments.path_polygons_container
    file_extension = arguments.file_extension
    new_directory = arguments.new_directory

    full_path_polygons_container = path_base + path_polygons_container
    full_path_polygons_contained = path_base + path_polygons_contained

    list_polygons_container = createListOfFiles(full_path_polygons_container, file_extension)
    list_polygons_contained = createListOfFiles(full_path_polygons_contained, file_extension)

    names = pullNamesFromDirectory(full_path_polygons_container, file_extension)
    files = zipTogetherFileLists(list_polygons_contained, list_polygons_container, names)

    new_directory = path_base + "/" + new_directory
    os.system("mkdir " + new_directory)

    bar = progressbar.ProgressBar(max_value=len(names))

    for file_number, file in enumerate(files):
        new_file = "affected_structures_" + file[2] + "." + file_extension
        polygonsInPolygons(file[0], file[1], new_file)
        os.system("mv affected_structures_" + file[2] + ".* " + new_directory)
        bar.update(file_number)