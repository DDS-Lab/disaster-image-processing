import gdal
import argparse

def isInArea(vrt):

    dataset = gdal.Open(vrt)
    filelist = dataset.GetFileList()

    # writes it to a new file
    with open("vrt_list.txt", 'w') as f:
        for line in filelist[1:]:
            f.write(str(line) + "\n")
    f.close()



if __name__ == "__main__":

    parser = argparse.ArgumentParser(epilog='')
    parser.add_argument('vrt')

    args = parser.parse_args()

    vrt = args.vrt

    isInArea(vrt)
