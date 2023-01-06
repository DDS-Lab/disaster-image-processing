cd noaa_images
PATH+=:/root/miniconda3/bin
for f in *.tar
do
  tar -xvf $f
  directoryname=$(basename $f .tar)
  mkdir -p $directoryname
  mv *.tif $directoryname
  rm $f
  python compressTiffs.py $directoryname "${directoryname}_compressed" JPEG 2
  gdaltindex "${directoryname}.shp" "${directoryname}_compressed"/*.tif
done