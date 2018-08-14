import os
import argparse


def index_raster_directory(directory):

    command = "gdaltindex index.shp " + directory + "/*.tif"
    os.system(command)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    args = parser.parse_args()

    directory = args.directory
    index_raster_directory(directory)
