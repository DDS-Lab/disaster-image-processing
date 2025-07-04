# disaster-image-processing

## Interactive Jupyter Notebooks

### Full Image Bounding Box Visualization
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DDS-Lab/disaster-image-processing/34dbdea7b2d6f99db1130fa3f103cd0b4915fe7f?urlpath=lab%2Ftree%2Fnotebooks%2Fraster-processing%2FBuildingMarker.ipynb)

### Chip Bounding Box Visualization
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DDS-Lab/disaster-image-processing/34dbdea7b2d6f99db1130fa3f103cd0b4915fe7f?urlpath=lab%2Ftree%2Fnotebooks%2Fraster-processing%2FChipPlotting.ipynb)

For more information on this project, please visit the [project website](https://dds-lab.github.io/disaster-damage-detection/).

This is the pipeline for processing the image data, tiling the images, preparing the training, validation and test data and training the model in tensorflow.  There are separate processes for DigitalGlobe data and for NOAA data.  More details on the data used for this project can be found [here](https://github.com/DDS-Lab/disaster-image-processing/blob/master/data.md). 

## Process Flow

| DigitalGlobe | NOAA |
| --------------------- | --------------------|
|1. [digitalglobe_image_downloader folder](https://github.com/DDS-Lab/disaster-image-processing/tree/master/scripts/digitalglobe_image_downloader)|1. [downloadTiffs.sh](https://github.com/DDS-Lab/disaster-image-processing/blob/jminahn/scripts/raster-processing/raster_downloading/downloadTiffs.sh)|
|1.a. [digitalglobe_scraper.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/digitalglobe_image_downloader/digitalglobe_scraper.py)|2.a. [compressTiffs.sh](https://github.com/DDS-Lab/disaster-image-processing/blob/jminahn/scripts/raster-processing/raster_utilities/compressTiffs.sh)|
|1.b. [digitalglobe_tiff_Downloader.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/digitalglobe_image_downloader/digitalglobe_tiff_downloader.py)|2.b. [compressTiffs.py](https://github.com/DDS-Lab/disaster-image-processing/blob/jminahn/scripts/raster-processing/raster_utilities/compressTiffs.py)|
|1.c. [filterOneBands.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_sorting/filterOneBands.py)|3.a. [indexRasters.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_indexing/indexRasters.py)|
|2. [compressTiffs.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_utilities/compressTiffs.py)|3.b. [mosaicRasters.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_mosaicking/mosaicRasters.py)|
|3.a. [concat_layers.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/concat_layers.py)|3.c. [selectParcelsByDamages.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/training-data-processing/training_set_creation/selectParcelsByDamages.py)|
|3.b. [geofunctions.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/geofunctions.py)|3.d. [selectBuildingsByParcels.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/training-data-processing/training_set_creation/selectBuildingsByParcels.py)|
|3.c. [shp_boundingbox.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/shp_boundingbox.py)|3.e. [createBuildingBoundingBoxes.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/training-data-processing/training_set_creation/createBuildingBoundingBoxes.py)|
|3.d. [shp_boundingbox2.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/shp_boundingbox2.py)|4. [tileTiff.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_tiling/tileTiff.py)|
|3.e. [shp_buffer.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/shp_buffer.py)|5. [tif_index_geojson.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/tif_index_geojson.py)|
|3.f. [filterNoValues.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_sorting/filterNoValues.py)|6.a. [convert2pix.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/convert2pix.py)|
|4. [tileTiff.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/raster-processing/raster_tiling/tileTiff.py)|6.b. [BuildingMarker.ipynb](https://github.com/DDS-Lab/disaster-image-processing/blob/2022-update/notebooks/raster-processing/BuildingMarker.ipynb)|
|5. [tif_index_geojson.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/tif_index_geojson.py)|7.a. [chipImage.py](https://github.com/DDS-Lab/disaster-image-processing/blob/2022-update/chipImage.py)|
|6. [convert2pix.py](https://github.com/DDS-Lab/disaster-image-processing/blob/master/scripts/utils/convert2pix.py)|7.b. [ChipPlotting.ipynb](https://github.com/DDS-Lab/disaster-image-processing/blob/2022-update/ChipPlotting.ipynb)|
|7.a. [train_test_split.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/train_test_split.py)|8.a. [train_test_split.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/train_test_split.py)|
|7.b. [split_geojson.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/split_geojson.py)|8.b. [split_geojson.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/split_geojson.py)|
|8.a. [plot_bbox.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox.py)|9.a. [plot_bbox.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox.py)|
|8.b. [plot_bbox_uid_small.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox_uid_small.py)|9.b. [plot_bbox_uid_small.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/plot_bbox_uid_small.py)|
|8.c. [identify_bad_lab.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/identify_bad_labels.py)|9.c. [identify_bad_lab.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/identify_bad_labels.py)|
|8.d. [delete_bad_labels.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/delete_bad_labels.py)|9.d. [delete_bad_labels.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/delete_bad_labels.py)|
|8.e. [fix_bbox.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/fix_bbox.ipynb)|9.e. [fix_bbox.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/fix_bbox.ipynb)|
|8.f. [xView_Processing.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/xView_Processing.ipynb)|9.f. [xView_Processing.ipynb](https://github.com/DDS-Lab/harvey_data_process/blob/master/xView_Processing.ipynb)|
|9. [aug_util.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/aug_util.py)|10. [aug_util.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/aug_util.py)|||
|10.a. [process_wv_ms_test.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_test.py)|11.a. [process_wv_ms_test.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_test.py)||
|10.b. [process_wv_ms_train.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_train.py)|11.b. [process_wv_ms_train.py](https://github.com/DDS-Lab/harvey_data_process/blob/master/process_wv_ms_train.py)|


### 1. Download data

Scrape the image files from source websites and save them in a folder.  For DigitalGLobe sorting the image files into 3 band and 1 band folders is required. 

**The following instructions are for NOAA only:**

Run `sudo bash downloadTiffs.sh` on Ubuntu to download the image files after installing the provided file.

All the files combined will be around 60GB; it is recommended to use a hard drive to ensure that you have enough storage. If you have not used Ubuntu before on your device, you will need to run `sudo apt-get install wget` in order to be able to run the file.

You may need to delete carriage return characters if the files are not being downloaded properly (e.g. the files are downloaded instantly). To do this, run `sed "s/$(printf '\r')\$//" downloadTiffs.sh > downloadTiffs2.sh && mv downloadTiffs2.sh downloadTiffs.sh` on Ubuntu.

Each file takes roughly 5-7 minutes to download; please be patient!

### 2. Compress images

Takes image files.  For DigitalGlobe this takes 3 TB and compresses to 60 GB.

Please install both files and ensure that they are in the same directory. You will only need to run `compressTiffs.sh`, as it will call `compressTiffs.py`.

You will need Miniconda in your Ubuntu terminal in order to run Python files (we chose Miniconda over Anaconda since Miniconda does not come with any Python packages, which saves us file space which would otherwise be taken up by unnecessary packages). Please go [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html) for instructions on how to install Miniconda on Ubuntu. We recommend downloading the latest version.

Once you have installed Miniconda, you must take the following steps to activate it in Ubuntu:

- Run `sudo -s`.
- Enter the password associated with your account in Ubuntu.
- **First-time only:** Run `export PATH=”root/miniconda3/bin:$PATH”` in the terminal. This will ensure that Ubuntu points to your Miniconda directory.

You then must install the GDAL package (preferably in a virtual environment). To set up your virtual environment, run `conda create -n [env_name] python=[version]` (we recommend Python 3.9). You can then activate it anytime by running `source activate [env_name]` and disable it with `source deactivate`.

Install the GDAL package by running `conda install -c conda-forge gdal` while your virtual environment is active.

You may get a syntax error when you run `downloadTiffs.sh`. To fix this, run `vi compressTiffs.sh` -> `:set ff=unix` -> `wq!`

`compressTiffs.sh` will automatically go to the folder where the tar files are located, so ensure that the Shell and Python files are located in the directory directly before the `noaa_images` folder, which should have been created when you ran `downloadTiffs.sh`.

### 3. Processing image files

Apply appropriate utility script as necessary based on observations of the data.

### 4. Tile images

Clip the big tif images into smaller tiles (2048 x 2048) from left to right and top to bottom including a csv of the lat long ranges for each tif image.

### 5. Index tiles to geojson

From the csv of lat long ranges per tif image and the geojson file of lat longs of bounding boxes with attached tif id produce a geojson of pixel ranges per bounding box with small tif id.

### 6. Convert lat long to pixel coordinates

SSD requires the training data input as pixel coordinates.

You can verify that both the geospatial and pixel coordinates result in the correct bounding boxes being plotted in `BuildingMarker.ipynb`. You can manually select a tile of your choice, or test a random tile from your tiles folder.

### 7. Chip tif files

Convert the tif files to chips-- smaller images that can be used for train/test sets.

### 8. Split training data

Split the images and geojson file into training, validation and test subsets (8:1:1).

### 9. Debug dataset

Use ipython notebook to plot bounding boxes over the images (tiff files) to check for accuracy, render the bounding boxes over the tiff files to manually inspect, record bad labels, remove those bounding boxes from the geojson file.

### 10. Data augmentation

Shift, flip and rotate the images as a way to add more training data.

### 11. Feed training data to algorithm

Prepare input for the network.

