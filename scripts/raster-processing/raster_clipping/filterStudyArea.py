import os
import argparse
import glob
from osgeo import gdal, ogr
import shapefile

def getAreaExtents(polygon):

    sf = shapefile.Reader(polygon)
    coordinates = sf.bbox

    return coordinates


def createVRT(directory, coordinates):

	coordinate1 = str(coordinates[0])
	coordinate2 = str(coordinates[2])
	coordinate3 = str(coordinates[1])
	coordinate4 = str(coordinates[3])

	directory_structure = directory + '*.tif'

	command = "gdalbuildvrt -te %s %s %s %s output.vrt %s" % (coordinate1, coordinate2, coordinate3, coordinate4, directory_structure)

	os.system(command)



def isInArea(vrt):

    dataset = gdal.Open(vrt)
    filelist = dataset.GetFileList()

    with open("vrt_list.txt", 'w') as f:
        for line in filelist[1:]:
            f.write(str(line) + "\n")
    f.close()



if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='')
    parser.add_argument('directory')
    parser.add_argument('polygon')

    args = parser.parse_args()

    directory = args.directory
    polygon = args.polygon

    coordinates = getAreaExtents(polygon)
    createVRT(directory, coordinates)
    isInArea("output.vrt")

