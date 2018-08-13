"""
The Digital Globe images we

"""

import os
import argparse


def compress_tif(original_tif, compression_method="JPEG", predictors=2, new_directory="compressed/"):
    """
    This function takes an uncompressed GeoTIFF and compresses it with one of
    four compression methods:

        - Packbits
        - JPEG
        - Deflate
        - LZW

    For LZW and Deflate, you can choose the number of predictors.

    :param original_tif: The uncompressed GeoTIFF to be compressed
    :param new_tif: The new compressed GeoTIFF
    :param compression_method: Packbits, JPEG, Deflate, or LZW
    :param predictors: Default is 2
    :return: Creates a new compressed TIF in directory folder
    """

    new_tif_base = original_tif.split('.')[0]
    packbit_base = "_packbit_compressed.tif"
    jpeg_base = "_jpeg_compressed.tif"
    deflate_base = "_deflate_compressed.tif"
    lzw_base = "_lzw_compressed.tif"

    command_packbits = "gdal_translate -of GTiff -co COMPRESS=PACKBITS -co TILED=YES " + original_tif + " " + new_tif_base + packbit_base
    command_jpeg = "gdal_translate -co COMPRESS=JPEG -co TILED=YES " + original_tif + " " + new_tif_base + jpeg_base
    command_deflate = "gdal_translate -of GTiff -co COMPRESS=DEFLATE -co PREDICTOR=" + str(predictors) + " -co TILED=YES " + original_tif + " " + new_tif_base + deflate_base
    command_lzw = "gdal_translate -of GTiff -co COMPRESS=LZW -co PREDICTOR=" + str(predictors) + " -co TILED=YES " + original_tif + " " + new_tif_base + lzw_base

    command_mv = "mv " + new_tif_base

    if compression_method == "JPEG":
        os.system(command_jpeg)
        os.system(command_mv + jpeg_base + " " + new_directory)
    elif compression_method == "Packbits":
        os.system(command_packbits)
        os.system(command_mv + packbit_base + " " + new_directory)
    elif compression_method == "Deflate":
        os.system(command_deflate)
        os.system(command_mv + deflate_base + " " + new_directory)
    elif compression_method == "LZW":
        os.system(command_lzw)
        os.system(command_mv + lzw_base + " " + new_directory)


def compress_directory(directory_name, new_directory, compression_method="JPEG", predictors=2):
    '''
    Takes a directory of GeoTIFFs and makes a new directory of compressed GeoTIFFs. Make sure script is ran from
    the parent directory that TIFFs are located in. Compression methods are JPEG, Deflate, Packbits, or LZW. Predictors for Deflate
    and LZW are defaulted at 2.
    :param directory_name: Working directory full of uncompressed TIFFs
    :param new_directory_name: New directory to be populated with compressed TIFs
    :param compression_method: JPEG, Packbits, Deflate, or LZW
    :param predictors: Default is 2
    :return: A new directory populated with compressed TIFFs
    '''

    if os.path.exists(new_directory) is False:
        os.mkdir(new_directory)
    else:
        pass

    for filename in os.listdir(directory_name):

        file = directory_name + "/" + filename
        compress_tif(file, compression_method, predictors)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='Type in directory of TIFs with this script in the parent directory.')
    parser.add_argument('directory', help='The directory that the TIFs are in')
    parser.add_argument('method', default='JPEG')
    parser.add_argument('predictors', default=2)
    args = parser.parse_args()

    directory_name = args.directory
    compression_method = args.method
    predictors = args.predictors

    compress_directory(directory_name, compression_method, predictors)
