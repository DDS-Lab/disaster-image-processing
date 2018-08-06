import shapefile
import argparse

def getAreaExtents(polygon):

	sf = shapefile.Reader(polygon)
	coordinates = sf.bbox

	return coordinates


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('polygon')
	
	args = parser.parse_args()

	polygon = args.polygon

	print(getAreaExtents(polygon))
