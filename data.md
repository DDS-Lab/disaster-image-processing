# Data documentation

1. The data used in this project was derived from the Digital Globe Open Data Program under Creative Commons 4.0 License

    a. Large tif images were downloaded from here:  https://www.digitalglobe.com/opendata/hurricane-harvey/post-event

    b. The geojson with vector damage data crowdsourced through Tomnod (TOMNOD20170915) was found here: 

      https://www.digitalglobe.com/opendata/hurricane-harvey/vector-data

      (documentation of how that was manipulated)

2. Parcel data was collected by contacting each County Appraisal District Office and can be accessed here: 

      https://github.com/DDS-Lab/disaster-image-processing/blob/master/Parcel%20Data%20for%20Affected%20Counties%20-%20Sheet1.csv

3. Data with flood maps and ground truth damages was collected from the Federal Emergency Management Agency (FEMA) here:  

      https://data.femadata.com/NationalDisasters/

4. Building footprints were retrieved from Microsoft here:  

      https://github.com/Microsoft/Open-Maps/wiki/Microsoft-Building-Footprint-Release

5. Aerial imagery data was collected from the National Oceanic and Atmospheric Association:  

      https://storms.ngs.noaa.gov/storms/harvey/index.html#7/28.400/-96.690

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
