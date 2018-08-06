#!/bin/bash

python selectParcelsByDamages.py training_data/ parcels/ damages/ shp affected_parcels
python selectBuildingsByParcels.py training_data/ structures/ affected_parcels/ shp affected_structures
python createBuildingBoundingBoxes.py training_data/ affected_structures/ affected_structures_bb





