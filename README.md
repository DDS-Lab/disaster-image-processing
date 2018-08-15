# disaster-image-processing

For more information on this project, please visit the [project website](https://dds-lab.github.io/disaster-damage-detection/).

This is the pipeline for processing the image data, tiling the images, preparing the training, validation and test data and training the model in tensorflow.  There are separate processes for DigitalGlobe data and for NOAA data.  More details on the data used for this project can be found [here](https://github.com/DDS-Lab/disaster-image-processing/blob/master/data.md). 

### Process Flow

| DigitalGlobe | NOAA |
| --------------------- | --------------------|
|1. [digitalglobe_image_downloader folder](https://github.com/DDS-Lab/disaster-image-processing/tree/master/scripts/digitalglobe_image_downloader)|1. [downloadTiffs.sh]()|
|1.a. [digitalglobe_scraper.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/digitalglobe_image_downloader/digitalglobe_scraper.py)|2. [compressTiffs.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_utilities/compressTiffs.py)|
|1.b. [digitalglobe_tiff_Downloader.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/digitalglobe_image_downloader/digitalglobe_tiff_downloader.py)|3. [raster_indexing]()|
|1.c. [sort_images.py](https://github.com/DDS-Lab/harvey-data-processing/blob/script_cleaning/band_sorting/sort_images.py)|3.a. [indexRasters.py]()|
|2. [compressTiffs.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_utilities/compressTiffs.py)|3.b. [mosaicRasters.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/raster-processing/raster_mosaicking/mosaicRasters.py)|
|3. [utils folder](https://github.com/DDS-Lab/disaster-image-processing/tree/master/utils)|3.c. [selectParcelsByDamages.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/training-data-processing/training-data-processing/selectParcelsByDamages.py)|
|3.a. [concat_layers.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/concat_layers.py)|3.d. [selectBuildingsByParcels.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/training-data-processing/training-data-processing/selectBuildingsByParcels.py)|
|3.b. [geofunctions.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/geofunctions.py)|3.e. [createBuildingBoundingBoxes.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/training-data-processing/training-data-processing/createBuildingBoundingBoxes.py)
|3.c. [shp_boundingbox.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/shp_boundingbox.py)|4. [tileTiff.py](https://github.com/DDS-Lab/hyak_files/blob/master/tileTiff.py)|
|3.d. [shp_boundingbox2.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/shp_boundingbox2.py)|5. [tif_index_geojson.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/tif_index_geojson.py)|
|3.e. [shp_buffer.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/shp_buffer.py)|6. [convert2pix.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/convert2pix.py)|
|4. [filterNoValues.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/raster-processing/raster_sorting/filterNoValues.py)|7. [convert2pix.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/convert2pix.py)|
|5. [tileTiff.py](https://github.com/DDS-Lab/hyak_files/blob/master/tileTiff.py)|8.a. [train_test_split.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/train_test_split.py)|
|6. [tif_index_geojson.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/tif_index_geojson.py)|8.b. [split_geojson.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/split_geojson.py)|
|7. [convert2pix.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/convert2pix.py)|9.a. [plot_bbox.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox.py)|
|8.a. [train_test_split.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/train_test_split.py)|9.b. [plot_bbox_uid_small.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox_uid_small.py)|
|8.b. [split_geojson.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/split_geojson.py)|9.c. [identify_bad_lab.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/identify_bad_labels.py)|
|9.a. [plot_bbox.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox.py)|9.d. [delete_bad_labels.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/delete_bad_labels.py)|
|9.b. [plot_bbox_uid_small.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox_uid_small.py)|9.e. [fix_bbox.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/fix_bbox.ipynb)|
|9.c. [identify_bad_lab.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/identify_bad_labels.py)|9.f. [xView_Processing.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/xView_Processing.ipynb)|
|9.d. [delete_bad_labels.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/delete_bad_labels.py)|10. [aug_util.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/aug_util.py)|
|9.e. [fix_bbox.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/fix_bbox.ipynb)|11.a. [process_wv_ms_test.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_test.py)|
|9.f. [xView_Processing.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/xView_Processing.ipynb)|11.b. [process_wv_ms_train.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_train.py)|
|10. [aug_util.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/aug_util.py)||
|11.a. [process_wv_ms_test.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_test.py)||
|11.b. [process_wv_ms_train.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_train.py)||

### 1. Download data

Scrape the image files from digital globe and save them in a folder with points

### 2. Sort the image files

Separate 3 band and 1 band images into folders so that the 3 band image files can be used and the 1 band images removed

### 3. Compress images

Takes image files that are 3 TB and compresses to 60 GB

### 4. Create bounding boxes

[concat_layers.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/concat_layers.py) takes any number of shapefiles as arguments and outputs a merged

[geofunctions.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/geofunctions.py), [shp_boundingbox.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/shp_boundingbox.py), [shp_boundingbox2.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/shp_boundingbox2.py), [shp_buffer.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/utils/shp_buffer.py) transform lat long coordinates into pixels for a given image and can input a shapefile and creates a geojson with .00015 buffer around bounding boxes of each feature

### 5. Remove images that are completely NA

This reduces the size of our training data and also avoids confusing our model training since these images would be assigned a value regardless of whether there is a image data

### 6. Tile images

Clip the big tif images into smaller tiles (2048 x 2048) from left to right and top to bottom including a csv of the lat long ranges for each tif image

### 7. Index tiles to geojson

From the csv of lat long ranges per tif image and the geojson file of lat longs of bounding boxes with attached tif id produce a geojson of pixel ranges per bounding box with small tif id

### 8. Convert lat long to pixel coordinates

SSD requires the training data input as pixel coordinates

### 9. Split training data

Split the images and geojson file into training, validation and test subsets.  8:1:1

### 10. Debug dataset

Use ipython notebook to plot bounding boxes over the images (tiff files) to check for accuracy, render the bounding boxes over the tiff files to manually inspect, record bad labels, remove those bounding boxes from the geojson file

### 11. Data augmentation

Shift, flip and rotate the images as a way to add more training data

### 12. Feed training data to algorithm
Prepare input for the network

