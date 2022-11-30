import os
import arcpy
cwd = os.getcwd()
arcpy.env.workspace = (cwd + r"\TesterProjectAK.gdb")
aprx = arcpy.mp.ArcGISProject(cwd + r"\TesterProjectAK.aprx")
Map1 = aprx.listMaps()[0]
newfile = cwd + r"\TestTable1.csv" 
out_gdb = cwd + r"\TesterProjectAK.gdb"
out_feature_class = "AKTesterClass"

x_coords = "Longitude"
y_coords = "Latitude"
arcpy.management.XYTableToPoint(newfile, out_feature_class, x_coords, y_coords)

class_to_add = out_gdb + r"\AKTesterClass"
Map1.addDataFromPath(class_to_add)

aprx.saveACopy(cwd + r"\TesterProjectAK4.aprx")
del aprx
