!/bin/bash
## Job Name
#SBATCH --job-name=filter_na
## Resources
## Nodes
#SBATCH --nodes=1
## Tasks per node (Slurm assumes you want to run 28 tasks per node unless expli$
#SBATCH --ntasks-per-node=28
## Walltime (hr:min:sec)
#SBATCH --time=24:00:00
## Memory per node
#SBATCH --mem=240G
## Specify the working directory for this job
#SBATCH --workdir=/gscratch/choe/dssg/data
#SBATCH --mail-type=ALL

module load anaconda3_4.3.1
source activate dssg

gdalbuildvrt noaa_images.tif noaa_images/*.tif
gdalwarp -of GTiff -co COMPRESS=JPEG  -co TILE=YES -multi -dstnodata -999 -cutline ../training_data/counties/affected-counties-clipped-by-parcels-dissolved.shp -crop_to_cutline noaa_images.vrt noaa_images.tif
gdal_retile.py -raster_processing/tiling/tiles raster_processing/tiling/noaa_images.vrt