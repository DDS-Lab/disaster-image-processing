import os
import argparse
import geopandas as gpd


def ogr_clip(clip_layer, input_layer, output_layer):

    command = "ogr2ogr -clipsrc %s %s %s" % (
        clip_layer, output_layer, input_layer)
    os.system(command)


def gpd_clip(clip_layer, input_layer):

    def read_layer(file):

        return gpd.GeoDataFrame(gpd.read_file(file))

    clip_layer = read_layer(clip_layer)
    input_layer = read_layer(input_layer)

    output_file = gpd.overlay(input_layer, clip_layer, how='intersection')

    return output_file


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('clip')
    parser.add_argument('input_layer')
    parser.add_argument('output_layer')
    parser.add_argument('method')

    arguments = parser.parse_args()

    clip = arguments.clip
    input_layer = arguments.input_layer
    output_layer = arguments.output_layer
    method = arguments.method

    if method == "OGR":
        ogr_clip(clip, input_layer, output_layer)
    elif method == "GeoPandas":
        gpd_clip(clip, input_layer)
    else:
        print("Please pick a method!")
