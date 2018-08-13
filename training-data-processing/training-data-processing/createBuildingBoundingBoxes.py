import geopandas as gpd
import argparse
import os
import glob
import progressbar


def loadFile(file_path):
    shape = gpd.GeoDataFrame(gpd.read_file(file_path))
    return shape


def createBoundingBox(file, new_name):
    affected_structures = loadFile(file)
    polygons = gpd.GeoSeries(affected_structures.geometry)
    bounding_boxes = gpd.GeoSeries(polygons.envelope)
    bounding_boxes.to_file(new_name)
    return bounding_boxes


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


def zipTogetherFileLists(directory, file_names):
    files = list(zip(directory, file_names))
    return files



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument('directory')
    parser.add_argument('new_directory')

    arguments = parser.parse_args()
    path = arguments.path
    directory = arguments.directory
    new_directory = arguments.new_directory

    files = glob.glob(directory + "/*.shp")
    names = pullNamesFromDirectory(directory, "/*.shp")
    files_list = zipTogetherFileLists(files, names)

    new_directory = path + "/" + new_directory
    os.system("mkdir " + new_directory)

    bar = progressbar.ProgressBar(max_value=len(names))

    for file_number, file in enumerate(files_list):
        new_name = "boundingbox_" + file[1] + ".shp"
        createBoundingBox(file[0], new_name)
        os.system("mv boundingbox_" + file[1] + ".* " + new_directory)
        bar.update(file_number)
