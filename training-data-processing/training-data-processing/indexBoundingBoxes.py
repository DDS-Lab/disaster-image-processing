from qgis.core import *
import glob, os, processing


#Set Up QGIS
QgsApplication.setPrefixPath("/usr/bin/qgis", True)
qgs = QgsApplication([], False)
qgs.initQgis()


layer = QgsVectorLayer(data_source, layer_name, provider_name)


sys.path.append('C:/OSGEO4~1/apps/qgis/python/plugins')
from processing.core.Processing import Processing
Processing.initialize()
from processing.tools import *

layer1 = "path/to/point_shapefile.shp"
layer2 = "path/to/polygon_shapefile.shp"
result = "path/to/output_shapefile.shp"

general.runalg("qgis:joinattributesbylocation", layer1, layer2, u'intersects', 0, 0, '', 1, result)


#Exit QGIS
qgs.exitQgis()
