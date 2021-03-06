import os
import argparse


def assign_crs(raster, epsg=4326):

    epsg = str(epsg)
    r_in = raster
    r_out = raster.split(".")[0] + "_reprojected_" + epsg + ".tif"
    command = "gdal_translate -a_srs EPSG:%s %s %s" % (epsg, r_in, r_out)
    os.system(command)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Assign CRS to TIFs')
    parser.add_argument('directory', help='The directory that the TIFs are in')
    parser.add_argument('epsg')
    args = parser.parse_args()

    directory = args.directory
    epsg = args.epsg

    for filename in os.listdir(directory):
        file = directory + "/" + filename
        assign_crs(file, epsg)
