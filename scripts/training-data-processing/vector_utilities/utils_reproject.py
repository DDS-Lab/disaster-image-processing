from osgeo import ogr, osr
import argparse

def readInVectors(shapefile):
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataSource = driver.Open(shapefile, 0)  # 0 means read-only, 1 means writeable
    layer = dataSource.GetLayer()
    return layer


def readInCRS(layer):
    sourceprj = layer.GetSpatialRef()
    targetprj = osr.SpatialReference()
    targetprj.ImportFromEPSG(4326)
    transform = osr.CoordinateTransformation(sourceprj, targetprj)
    return transform


def reprojectCRS(feature, transform):
    pt = feature.GetGeometryRef()
    pt.Transform(transform)
    return pt


if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='Type in directory of TIFs with this script in the parent directory.')
    parser.add_argument('directory', help='The directory that the TIFs are in')
    parser.add_argument('method', help='Warp, Merge, or Build VRT and Translate')
    args = parser.parse_args()




