cat novalues_list.txt | while read line
do
    find /media/seanandrewchen/seanchen_ssd/raster-data/compressed | grep $line | xargs rm -f
done
