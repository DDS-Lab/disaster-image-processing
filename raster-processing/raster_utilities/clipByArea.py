import os
import argparse
import glob


def clipByArea(raster, polygon):

    raster_in = raster
    raster_out = raster.split('.')[0] + "_clipped.tif"

    command =  "gdalwarp -dstnodata -0 -co COMPRESS=JPEG -cutline %s %s %s" % (polygon, raster_in, raster_out)
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
        clipByArea(file, shapefile)
