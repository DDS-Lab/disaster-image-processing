import argparse
import os


def tile_tiff(tiff_file):

    command0 = "mkdir image_tiles"
    command1 = "gdal_retile.py -v -r bilinear -levels 1 -ps 2048 2048 -co\
     TILED=YES -co COMPRESS=JPEG -targetDir image_tiles " + tiff_file
    if os.path.exists("image_tiles"):
        os.system(command1)
    else:
        os.system(command0)
        os.system(command1)


def tile_directory(directory):

    for file in os.listdir(directory):
        tile_tiff(directory + "/" + file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='')
    parser.add_argument('tiff_file')

    args = parser.parse_args()
    tiff = args.tiff_file

    if os.path.isfile(tiff):
        tile_tiff(tiff)
    if os.path.isdir(tiff):
        tile_directory(tiff)
