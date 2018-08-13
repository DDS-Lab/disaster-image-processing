import os
import argparse


def loadShapefile(shapefile, database, table, username, password):

    command = "shp2pgsql -I -s 4269 %s %s | psql -U %s -p %s -d %s" % (
        shapefile, table, username, password, database)
    os.system(command)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument()
    parser.add_argument()

    arguments = parser.parse_args()
