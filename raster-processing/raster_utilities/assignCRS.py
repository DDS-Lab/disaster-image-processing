import os
import argparse




def assignCRS(raster, epsg=4326):

    epsg = str(epsg)
    raster_in = raster
    raster_out = raster.split(".")[0] + "_reprojected_" + epsg + ".tif"
    command = "gdal_translate -a_srs EPSG:%s %s %s" % (epsg, raster_in, raster_out)
    os.system(command)






if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='Type in directory of TIFs with this script in the parent directory.')
    parser.add_argument('directory', help='The directory that the TIFs are in')
    parser.add_argument('epsg')
    args = parser.parse_args()

    directory = args.directory
    epsg = args.epsg

    for filename in os.listdir(directory):
        file = directory + "/" + filename
        assignCRS(file, epsg)

