from osgeo import ogr, osr
import argparse


def read_in_vectors(shapefile):
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataSource = driver.Open(shapefile, 0)
    layer = dataSource.GetLayer()
    return layer


def read_in_crs(layer):
    sourceprj = layer.GetSpatialRef()
    targetprj = osr.SpatialReference()
    targetprj.ImportFromEPSG(4326)
    transform = osr.CoordinateTransformation(sourceprj, targetprj)
    return transform


def reproject_crs(feature, transform):
    pt = feature.GetGeometryRef()
    pt.Transform(transform)
    return pt


if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog="Type in directory of TIFs with this\
                                     script in the parent directory.")
    parser.add_argument('directory', help='The directory that the TIFs are in')
    parser.add_argument('method',
                        help='Warp, Merge, or Build VRT and Translate')
    args = parser.parse_args()
