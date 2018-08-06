"""
Digital Globe raster images were mixed between 3 banded and 1 banded.
For our work, we only wanted 3 banded. As such, we needed to remove
1 banded images from our working directory. This script takes an entire
directory of rasters and removes any rasters that aren't 3 banded into
another directory.
"""

import os
from osgeo import gdal
import argparse


def is_raster_three_bands(raster):
    """
    Takes a tif image file, opens it as a GDAL raster,
    counts how many raster bands, and returns a true value
    if there are three bands
    """
    image = gdal.Open(raster)
    number_bands = image.RasterCount
    if number_bands == 3:
        return True
    else:
        return False


def move_file(filename, folderpath):
    """
    Moves a file to a new folder
    """
    os.system("mv " + filename + " " + folderpath)


def is_raster_directory_three_bands(directory_name, new_directory_name):
    """
    Sorts through entire directory and moves one banded images
    into another directory
    """
    for filename in os.listdir(directory_name):
        if is_raster_three_bands(filename) is False:
            move_file(filename, new_directory_name)


if __name__ == "__main__":
    """
    Usage:
    ------

    python fileOneBands.py ../data/digitalglobe_images ../data/onebanded_digitalglobe_images

    """
    parser = argparse.ArgumentParser('Specify directory to remove non three\
     banded images into a new specified directory')
    parser.add_argument('all_images_directory')
    parser.add_argument('nonthreeband_images_directory')

    arguments = parser.parse_args()
    all_images_directory = arguments.all_images_directory
    nonthreeband_images_directory = arguments.nonthreeband_images_directory

    is_raster_directory_three_bands(all_images_directory,
                                    nonthreeband_images_directory)
