import numpy as np
from osgeo import gdal, gdal_array
import argparse
import os
import csv


def isRasterEmpty(file, output_array="No"):
    dataset = gdal.Open(file)
    raster_band = dataset.GetRasterBand(1)
    array = np.array(raster_band.ReadAsArray())

    if output_array == "Yes":
        print(array)
    else:
        pass

    if np.max(array) > 0:
        print("OK")
        empty = False
    else:
        print("PROBLEM")
        empty = True

    return empty



def areRastersEmpty(directory):
    total_list = []

    for file in os.listdir(directory):
        empty = isRasterEmpty(directory + "/" + file)
        if empty == True:
            result = "Problem"
        else:
            result = "OK"
        single_list = [file, result]
        total_list.append(single_list)

    return total_list


if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='Type in directory of TIFs with this script in the parent directory.')
    parser.add_argument('directory', help='The directory that the TIFs are in')
    args = parser.parse_args()

    directory_name = args.directory
    list = areRastersEmpty(directory_name)

    with open("novalues_list.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerows(list)