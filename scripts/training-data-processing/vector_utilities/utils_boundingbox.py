import geopandas as gpd
import argparse


def load_file(file_path):
    shape = gpd.GeoDataFrame(gpd.read_file(file_path))
    return shape


def create_bounding_boxes(file_path, new_file):
    layer = load_file(file_path)
    polygons = gpd.GeoSeries(layer.geometry)
    bounding_boxes = polygons.envelope
    bounding_boxes.to_file(new_file)
    return bounding_boxes


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file_path')
    parser.add_argument('new_file')

    arguments = parser.parse_args()
    file_path = arguments.file_path
    new_file = arguments.new_file

    create_bounding_boxes(file_path, new_file)
