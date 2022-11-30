#Setting the workspace up
import os
import arcpy
cwd = os.getcwd()
arcpy.env.workspace = (cwd + r"\TesterProjectAK.gdb")

#Setting up ArcPy Mapping Module
aprx = arcpy.mp.ArcGISProject(cwd + r"\TesterProjectAK.aprx")
Map1 = aprx.listMaps()[0]

#Preparing the Table
newfile = cwd + r"\TestTable1.csv" 
out_gdb = cwd + r"\TesterProjectAK.gdb" #Can probably come out
out_feature_class = "AKTesterClass"

#XYTable to Point - Converting the Table to a Point Feature Class
x_coords = "Longitude"
y_coords = "Latitude"
arcpy.management.XYTableToPoint(newfile, out_feature_class, x_coords, y_coords)

#Adding the Point Feature Class to the Map
class_to_add = out_gdb + r"\AKTesterClass"
Map1.addDataFromPath(class_to_add)

#Converting and Exporting a FeatureClass, then adding it to the Map
arcpy.FeatureClassToShapefile_conversion(out_feature_class, cwd + r"\ShapeFileDestination")
NewShapeFile = cwd + r"\ShapeFileDestination\AKTesterClass.shp"
Map1.addDataFromPath(NewShapeFile)

#Clean up after yourself and turn off the lights
aprx.saveACopy(cwd + r"\TesterProjectAK5.aprx")
del aprx
