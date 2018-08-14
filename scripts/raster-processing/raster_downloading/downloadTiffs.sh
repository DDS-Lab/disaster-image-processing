#!/bin/bash

mkdir noaa_images
cd noaa_images

wget https://ngsstormviewer.blob.core.windows.net/harvey/20170827_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170828a_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170828b_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170829a_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170829b_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170830_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170831a_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170831b_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170901a_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170901b_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170901c_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170902a_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170902b_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170902c_RGB.tar
wget https://ngsstormviewer.blob.core.windows.net/harvey/20170903a_RGB.tar

for f in *.tar
do
  tar -xvf $f
  directoryname=$(basename $f .tar)
  mkdir $directoryname
  mv *.tif $directoryname
  rm $f
  newdirectoryextension='_compressed'
  newdirectoryname=$directoryname$newdirectoryextension
  path(){
    echo $newdirectoryname
  }
  python compressTiffs.py $directoryname $(path) JPEG 2
  gdaltindex $(path) $newdirectoryname'.shp'
done
