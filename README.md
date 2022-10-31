# disaster-image-processing

For more information on this project, please visit the [project website](https://dds-lab.github.io/disaster-damage-detection/).

This is the pipeline for processing the image data, tiling the images, preparing the training, validation and test data and training the model in tensorflow.  There are separate processes for DigitalGlobe data and for NOAA data.  More details on the data used for this project can be found [here](https://github.com/DDS-Lab/disaster-image-processing/blob/master/data.md). 

### Process Flow

| DigitalGlobe | NOAA |
| --------------------- | --------------------|
|1. [digitalglobe_image_downloader folder](https://github.com/DDS-Lab/disaster-image-processing/tree/master/scripts/digitalglobe_image_downloader)|1. [downloadTiffs.sh](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_downloading/downloadTiffs.sh)|
|1.a. [digitalglobe_scraper.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/digitalglobe_image_downloader/digitalglobe_scraper.py)|2. [compressTiffs.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_utilities/compressTiffs.py)|
|1.b. [digitalglobe_tiff_Downloader.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/digitalglobe_image_downloader/digitalglobe_tiff_downloader.py)|3.a. [indexRasters.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_indexing/indexRasters.py)|
|1.c. [filterOneBands.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_sorting/filterOneBands.py)|3.b. [mosaicRasters.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_mosaicking/mosaicRasters.py)|
|2. [compressTiffs.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_utilities/compressTiffs.py)|3.c. [selectParcelsByDamages.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/training-data-processing/training_set_creation/selectParcelsByDamages.py)|
|3.a. [concat_layers.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/concat_layers.py)|3.d. [selectBuildingsByParcels.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/training-data-processing/training_set_creation/selectBuildingsByParcels.py)|
|3.b. [geofunctions.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/geofunctions.py)|3.e. [createBuildingBoundingBoxes.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/training-data-processing/training_set_creation/createBuildingBoundingBoxes.py)|
|3.c. [shp_boundingbox.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/shp_boundingbox.py)|4. [tileTiff.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_tiling/tileTiff.py)|
|3.d. [shp_boundingbox2.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/shp_boundingbox2.py)|5. [tif_index_geojson.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/tif_index_geojson.py)|
|3.e. [shp_buffer.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/shp_buffer.py)|6. [convert2pix.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/convert2pix.py)|
|3.f. [filterNoValues.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_sorting/filterNoValues.py)|7.a. [train_test_split.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/train_test_split.py)|
|4. [tileTiff.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_tiling/tileTiff.py)|7.b. [split_geojson.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/split_geojson.py)|
|5. [tif_index_geojson.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/tif_index_geojson.py)|8.a. [plot_bbox.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox.py)|
|6. [convert2pix.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/convert2pix.py)|8.b. [plot_bbox_uid_small.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox_uid_small.py)|
|7.a. [train_test_split.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/train_test_split.py)|8.c. [identify_bad_lab.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/identify_bad_labels.py)|
|7.b. [split_geojson.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/split_geojson.py)|8.d. [delete_bad_labels.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/delete_bad_labels.py)|
|8.a. [plot_bbox.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox.py)|8.e. [fix_bbox.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/fix_bbox.ipynb)|
|8.b. [plot_bbox_uid_small.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox_uid_small.py)|8.f. [xView_Processing.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/xView_Processing.ipynb)|
|8.c. [identify_bad_lab.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/identify_bad_labels.py)|9. [aug_util.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/aug_util.py)|
|8.d. [delete_bad_labels.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/delete_bad_labels.py)|10.a. [process_wv_ms_test.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_test.py)|
|8.e. [fix_bbox.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/fix_bbox.ipynb)|10.b. [process_wv_ms_train.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_train.py)|
|8.f. [xView_Processing.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/xView_Processing.ipynb)||
|9. [aug_util.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/aug_util.py)||
|10.a. [process_wv_ms_test.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_test.py)||
|10.b. [process_wv_ms_train.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_train.py)||

### 1. Download data

Scrape the image files from source websites and save them in a folder.  For DigitalGLobe sorting the image files into 3 band and 1 band folders is required. 

***The following instructions are for NOAA only:***

Run `sudo bash downloadTiffs.sh` on Ubuntu to download the image files after installing the provided file.

All the files combined will be around 60GB; it is recommended to use a hard drive to ensure that you have enough storage. If you have not used Ubuntu before on your device, you will need to run `sudo apt-get install wget` on Ubuntu.

You may need to delete carriage return characters if the files are not being downloaded properly (e.g. the files are downloaded instantly instead of taking around 5-6 minutes). To do this, run `sed "s/$(printf '\r')\$//" downloadTiffs.sh > downloadTiffs2.sh && mv downloadTiffs2.sh downloadTiffs.sh` on Ubuntu.

### 2. Compress images

Takes image files.  For DigitalGlobe this takes 3 TB and compresses to 60 GB.

### 3. Processing image files

Apply appropriate utility script as necessary based on observations of the data.

### 4. Tile images

Clip the big tif images into smaller tiles (2048 x 2048) from left to right and top to bottom including a csv of the lat long ranges for each tif image.

### 5. Index tiles to geojson

From the csv of lat long ranges per tif image and the geojson file of lat longs of bounding boxes with attached tif id produce a geojson of pixel ranges per bounding box with small tif id.

### 6. Convert lat long to pixel coordinates

SSD requires the training data input as pixel coordinates.

### 7. Split training data

Split the images and geojson file into training, validation and test subsets (8:1:1).

### 8. Debug dataset

Use ipython notebook to plot bounding boxes over the images (tiff files) to check for accuracy, render the bounding boxes over the tiff files to manually inspect, record bad labels, remove those bounding boxes from the geojson file.

### 9. Data augmentation

Shift, flip and rotate the images as a way to add more training data.

### 10. Feed training data to algorithm

Prepare input for the network.

