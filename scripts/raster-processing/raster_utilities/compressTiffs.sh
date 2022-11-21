cd noaa_images/
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