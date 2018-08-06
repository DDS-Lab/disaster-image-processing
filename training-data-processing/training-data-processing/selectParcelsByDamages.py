import geopandas as gpd
from geopandas.tools import sjoin
import argparse
import glob
import os
import progressbar

def loadFile(file_path):
    shape = gpd.GeoDataFrame(gpd.read_file(file_path))
    return shape


def polysWithPoints(polygons, points, new_file):
    polygons = loadFile(polygons)
    points = loadFile(points)
    polysWithPoints = sjoin(polygons, points, op='contains')
    polysWithPoints.to_file(new_file)
    return polysWithPoints


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
    parser.add_argument('path_polygons')
    parser.add_argument('path_points')
    parser.add_argument('file_extension')
    parser.add_argument('new_directory')

    arguments = parser.parse_args()

    path_base = arguments.path_base
    path_polygons = arguments.path_polygons
    path_points = arguments.path_points
    file_extension = arguments.file_extension
    new_directory = arguments.new_directory

    full_path_polygons = path_base + path_polygons
    full_path_points = path_base + path_points

    list_polygons = createListOfFiles(full_path_polygons, file_extension)
    list_points = createListOfFiles(full_path_points, file_extension)

    names = pullNamesFromDirectory(full_path_points, file_extension)
    files = zipTogetherFileLists(list_polygons, list_points, names)

    new_directory = path_base + "/" + new_directory
    os.system("mkdir " + new_directory)

    bar = progressbar.ProgressBar(max_value=len(names))

    for file_number, file in enumerate(files):
        new_file = "affected_parcels_" + file[2] + "." + file_extension
        polysWithPoints(file[0], file[1], new_file)
        os.system("mv affected_parcels_" + file[2] + ".* " + new_directory)
        bar.update(file_number)


