import argparse
import os


def tileTiff(tiff_file):

    command0 = "mkdir image_tiles"
    command1 = "gdal_retile.py -v -r bilinear -levels 1 -ps 20000 20000 -co TILED=YES -co COMPRESS=JPEG -targetDir image_tiles " + tiff_file
    os.system(command0)
    os.system(command1)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='')
    parser.add_argument('tiff_file')

    args = parser.parse_args()

    tiff_file = args.tiff_file
    tileTiff(tiff_file)
