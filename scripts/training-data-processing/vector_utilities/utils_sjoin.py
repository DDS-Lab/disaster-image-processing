import geopandas as gpd
from geopandas.tools import sjoin

def loadFile(file_path):
    shape = gpd.GeoDataFrame(gpd.read_file(file_path))
    return shape


def writeFile(shape, new_file):
    shape.to_file(new_file)


def polysWithPoints(polygons, points, new_file):
    polygons = loadFile(polygons)
    points = loadFile(points)
    polysWithPoints = sjoin(polygons, points, op='contains')
    polysWithPoints.to_file(new_file)
    return polysWithPoints


def polygonsInPolygons(contained_polygons, container_polygons, new_file):
    contained_polygons = loadFile(contained_polygons)
    container_polygons = loadFile(container_polygons)
    selected_contained_polygons = sjoin(contained_polygons, container_polygons, op='within')
    selected_contained_polygons.to_file(new_file)
    return selected_contained_polygons

