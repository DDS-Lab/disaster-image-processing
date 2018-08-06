import os
import argparse
import glob


def clip_by_area(raster_file, polygon_file):

    raster_in = raster_file
    raster_out = raster_in.split('.')[0] + "_clipped.tif"

    command = "gdalwarp -dstnodata -999 -co COMPRESS=JPEG -cutline \
    %s %s %s" % (polygon_file, raster_in, raster_out)
    os.system(command)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='')
    parser.add_argument('tiff_directory')
    parser.add_argument('clip_shapefile')

    args = parser.parse_args()

    directory = args.tiff_directory
    shapefile = args.clip_shapefile

    files = glob.glob(directory + "/*.tif")

    for file in files:
        clip_by_area(file, shapefile)
