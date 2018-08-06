import os

os.system("raster2pgsql -s 4326 -d -I -C -M -R -l 4 /home/duncan/rasters/andes/altglob2a.tif -F -t 1000x1000 globcov1000x1000|psql -d latam2")