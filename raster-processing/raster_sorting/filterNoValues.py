import numpy as np
from osgeo import gdal
import argparse
import os
import csv


def is_raster_empty(file):
    raster = gdal.Open(file)
    raster_band = raster.GetRasterBand(1)
    band_array = np.array(raster_band.ReadAsArray())

    if np.max(band_array) > 0:
        print("OK")
        empty = False
    else:
        print("PROBLEM")
        empty = True

    return empty


def are_rasters_empty(directory):
    total_list = []

    for file in os.listdir(directory):
        empty = is_raster_empty(directory + "/" + file)

        if empty:
            result = "Problem"
        else:
            result = "OK"
        single_list = [file, result]
        total_list.append(single_list)

    return total_list


def create_file_list(list):

    with open("novalues_list.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerows(list)


def delete_files(file_list):

    for file in file_list:
        command = "rm %s" % file
        os.system(command)


def delete_file(file):

    command = "rm %s" % file
    os.system(command)


def move_file(filename, folderpath):
    """
    Moves a file to a new folder
    """
    os.system("mv " + filename + " " + folderpath)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='Type in directory of TIFs with\
    this script in the parent directory.')
    parser.add_argument('directory', help='The directory that the TIFs are in')
    args = parser.parse_args()

    directory = args.directory

    for filename in directory:
        file = directory + "/" + filename
        if is_raster_empty(file):
            delete_file(file)
        else:
            continue
