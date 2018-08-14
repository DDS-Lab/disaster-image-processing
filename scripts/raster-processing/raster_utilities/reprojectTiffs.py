"""

"""
import os
import argparse


def reproject_raster(raster, epsg):
    """

    """
    epsg = str(epsg)
    raster_in = raster
    raster_out = raster.split(".")[0] + "_reprojected_" + epsg + ".tif"
    command = "gdalwarp -t_srs EPSG:%s -co\
     COMPRESS=JPEG %s %s" % (epsg, raster_in, raster_out)
    os.system(command)


def reproject_directory(directory, epsg):
    """

    """
    epsg = str(epsg)

    for filename in os.listdir(directory):
        file = directory + "/" + filename
        reproject_raster(file, epsg)


if __name__ == "__main__":
    """

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('epsg')
    args = parser.parse_args()

    file = args.file
    epsg = args.epsg

    if os.path.isfile(file):
        reproject_raster(file, epsg)
    if os.path.isdir(file):
        reproject_directory(file, epsg)
