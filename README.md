# THIS BRANCH IS FOR CLEANING THE REPO!!!

# Test commit

# disaster-damage-detection

## Pipeline

### Process Flow

1. [automatic_downloader folder](https://github.com/DDS-Lab/disaster-damage-detection/tree/master/automatic-image-downloader)

	a. [scraper.py](https://github.com/DDS-Lab/disaster-damage-detection/blob/automatic-image-downloader/automatic-image-downloader/automatic_downloader/scraper.py)

	b. [tiffDownloader.py](https://github.com/DDS-Lab/disaster-damage-detection/blob/automatic-image-downloader/automatic-image-downloader/automatic_downloader/tiffDownloader.py)

2. [sort_images.py](https://github.com/DDS-Lab/harvey-data-processing/blob/script_cleaning/band_sorting/sort_images.py)

3. [compressTiffs.py](https://github.com/DDS-Lab/disaster-damage-detection/blob/master/raster-processing/compressTiffs.py)

4. [utils folder](https://github.com/DDS-Lab/disaster-damage-detection/tree/master/utils)

	a. [concat_layers.py](https://github.com/DDS-Lab/disaster-damage-detection/blob/master/utils/concat_layers.py)

	b. [geofunctions.py](https://github.com/DDS-Lab/disaster-damage-detection/blob/master/utils/geofunctions.py)

	c. [shp_boundingbox.py](https://github.com/DDS-Lab/disaster-damage-detection/blob/master/utils/shp_boundingbox.py)

	d. [shp_boundingbox2.py](https://github.com/DDS-Lab/disaster-damage-detection/blob/master/utils/shp_boundingbox2.py)

	e. [shp_buffer.py](https://github.com/DDS-Lab/disaster-damage-detection/blob/master/utils/shp_buffer.py)

5. [filterNoValues.py](https://github.com/DDS-Lab/disaster-damage-detection/blob/master/raster-processing/filter-no-values/filterNoValues.py)

6. [tileTiff.py](https://github.com/DDS-Lab/hyak_files/blob/master/tileTiff.py)

7.

8. [index-geojson.ipynb](https://github.com/DDS-Lab/disaster-damage-detection/blob/Index-geojson-tifs/Index-geojson.ipynb)

9. [convert2pix.py](https://github.com/DDS-Lab/disaster-damage-detection/blob/master/utils/convert2pix.py)

10.
11.
12.

### 1. Download data from Digital Globe

Scrape the image files from digital globe and saves them in a folder with points

### 2. Sort the image files

Separate 3 band and 1 band images into folders

### 3. Compress images

### 4. Create bounding boxes

Using points in shapefile format produce a geojson with .00015 buffer around bounding boxes

### 5. Remove images that are completely NA

### 6. Tile images

Clip the big tif images into smaller tiles (2048 x 2048) from left to right and top to bottom including a csv of the lat long ranges for each tif image

### 7. Index tiles to geojson

From the csv of lat long ranges per tif image and the geojson file of lat longs of bounding boxes with attached tif id produce a geojson of pixel ranges per bounding box with small tif id

### 8. Convert lat long to point coordinates

### 9. Split training data

### 10. Debug dataset

### 11. Data augmentation

### 12. Feed training data to algorithm

Start with a small network to tune parameters, then switch to a larger networks
