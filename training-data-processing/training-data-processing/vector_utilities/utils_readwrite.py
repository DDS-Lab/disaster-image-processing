import geopandas as gpd

def loadFile(file_path):
    shape = gpd.GeoDataFrame(gpd.read_file(file_path))
    return shape


def writeFile(shape, new_file):
    shape.to_file(new_file)

