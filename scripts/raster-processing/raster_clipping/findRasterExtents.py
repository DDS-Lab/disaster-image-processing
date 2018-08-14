import shapefile
import argparse


def get_area_extents(polygon_file):

    sf = shapefile.Reader(polygon_file)
    coordinates = sf.bbox

    return coordinates


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('polygon')
    args = parser.parse_args()
    polygon = args.polygon

    print(get_area_extents(polygon))
