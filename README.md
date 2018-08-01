# disaster-damage-detection

## Pipeline

### Process Flow

1. [automatic_downloader folder](https://github.com/DDS-Lab/disaster-image-processing/tree/master/automatic-image-downloader)

	a. [scraper.py](https://github.com/DDS-Lab/disaster-image-processing/blob/automatic-image-downloader/automatic-image-downloader/automatic_downloader/scraper.py)
	
	b. [tiffDownloader.py](https://github.com/DDS-Lab/disaster-image-processing/blob/automatic-image-downloader/automatic-image-downloader/automatic_downloader/tiffDownloader.py)

2. [sort_images.py](https://github.com/DDS-Lab/harvey-data-processing/blob/script_cleaning/band_sorting/sort_images.py)

3. [compressTiffs.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/raster-processing/compressTiffs.py)

4. [utils folder](https://github.com/DDS-Lab/disaster-image-processing/tree/master/utils)

	a. [concat_layers.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/concat_layers.py)

	b. [geofunctions.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/geofunctions.py)

	c. [shp_boundingbox.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/shp_boundingbox.py)

	d. [shp_boundingbox2.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/shp_boundingbox2.py)

	e. [shp_buffer.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/shp_buffer.py)

5. [filterNoValues.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/raster-processing/filter-no-values/filterNoValues.py)

6. [tileTiff.py](https://github.com/DDS-Lab/hyak_files/blob/master/tileTiff.py)

7. [tif_index_geojson.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/tif_index_geojson.py)

8. [convert2pix.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/convert2pix.py)

9. 	a. [train_test_split.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/train_test_split.py)
	
	b. [split_geojson.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/split_geojson.py)

10.	a. [plot_bbox.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox.py)
	
	b. [plot_bbox_uid_small.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox_uid_small.py)
	
	c. [identify_bad_lab.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/identify_bad_labels.py)
	
	d. [delete_bad_labels.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/delete_bad_labels.py)
	
	e. [fix_bbox.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/fix_bbox.ipynb)
	
	f. [xView_Processing.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/xView_Processing.ipynb)

11. [aug_util.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/aug_util.py)

12. a. [process_wv_ms_test.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_test.py)
	
	b. [process_wv_ms_train.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_train.py)
	

### 1. Download data from Digital Globe

Scrape the image files from digital globe and save them in a folder with points

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

Split the images and geojson file into training, validation and test subsets.  8:1:1

### 10. Debug dataset

Use ipython notebook to plot bounding boxes over the images (tiff files) to check for accuracy
Render the bounding boxes over the tiff files to manually inspect, record bad labels, remove those bounding boxes from the geojson file

### 11. Data augmentation

Shift, flip and rotate the images as a way to add more training data

### 12. Feed training data to algorithm

Prepare input for the network
