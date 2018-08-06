import argparse
import os
import csv


def isRasterEmpty(file):
    dataset = gdal.Open(file)
    raster_band = dataset.GetRasterBand(1)
    array = np.array(raster_band.ReadAsArray())

    if np.max(array) > 0:
        print("OK")
        empty = False
    else:
        print("PROBLEM")
        empty = True

    return empty



def areRastersEmpty(directory):
    total_list = []

    for file in os.listdir(directory):
        empty = isRasterEmpty(directory + "/" + file)
        if empty == True:
            result = "Problem"
        else:
            result = "OK"
        single_list = [file, result]
        total_list.append(single_list)

    return total_list


def createList(list):

    with open("novalues_list.csv", "w") as f:
        wr = csv.writer(f)
        wr.writerows(list)



def deleteFiles(file_list):

    for file in file_list:
        command = "rm %s" % file
        os.system(command)

def deleteFile(file):

    command = "rm %s" % file
    os.system(command)


def delete



if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='Type in directory of TIFs with this script in the parent directory.')
    parser.add_argument('directory', help='The directory that the TIFs are in')
    args = parser.parse_args()

    directory = args.directory

    for filename in directory:
        file = directory + "/" + filename
        if isRasterEmpty(file):
            deleteFile(file)
        else:
            continue



