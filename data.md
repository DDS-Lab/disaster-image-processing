# Data documentation

| Data Type| Source|Generation Method|Format|File Size Order|License|
| -------------- | ----------- | ------------ | ------------- |-------------- | ------------- |
| Imagery|[DigitalGlobe](https://www.digitalglobe.com/opendata/hurricane-harvey/post-event)| Satellite(RGB)|GeoTIFF|~3 TB|Creative Commons 4.0|
| Imagery|[NOAA](https://storms.ngs.noaa.gov/storms/harvey/index.html#7/28.400/-96.690)|Aerial(RGB)|GeoTIFF|~60 GB|[US Government Works](https://www.usa.gov/government-works)|
| Damage Annotations|[TOMNOD](https://www.digitalglobe.com/opendata/hurricane-harvey/vector-data)|Crowdsourced|Vector|~1 MB|Creative Commons 4.0|
| Damage Annotations|[FEMA](https://data.femadata.com/NationalDisasters/)|Assessed by FEMA|Vector|~20 MB|[US Government Works](https://www.usa.gov/government-works)|
| Building Footprints|[Oak Ridge National Lab](https://data.femadata.com/NationalDisasters/)|Proprietary Algorithm|Vector|~2 GB|[US Government Works](https://www.usa.gov/government-works)|
| Building Footprints|[Microsoft](https://github.com/Microsoft/Open-Maps/wiki/Microsoft-Building-Footprint-Release)| Proprietary Algorithm|Vector|~3 GB|Open Data Commons Open Database License|
|Parcel Data|[Affected County Appraisal Districts](https://github.com/DDS-Lab/disaster-image-processing/blob/master/Parcel%20Data%20for%20Affected%20Counties%20-%20Sheet1.csv)<sup>superscript</sup> Parcel data was collected by contacting each County Appraisal District Office.|Assessed by Appraisers|Vector|~1 GB|Variable|



3. Data with flood maps and ground truth damages was collected from the Federal Emergency Management Agency (FEMA) here:  

      https://data.femadata.com/NationalDisasters/




      (Include our geojson file and what we’ve changed
        Manually removed data
        List of removed of bounding boxes (from An))

6. The processed data is available via the PostGIS Server:  

# Data organization

project_folder/    
      |- data/
         |- url_tif_list.txt
         |- digitalglobe_images_directory/
         |- onebanded_digitalglobe_images/
         |- layer1.shp
         |- layer2.shp
         |- mergedlayer.shp
         |-
         |-
         |-
         |- tifffolder/
         |- geojson of bounding boxes geometry and image id
         |- geojson of bounding boxes with pixel bounds in a string column
