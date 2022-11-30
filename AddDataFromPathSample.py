# https://pro.arcgis.com/en/pro-app/latest/arcpy/mapping/map-class.htm
import os
import arcpy
cwd = os.getcwd()
aprx = arcpy.mp.ArcGISProject(cwd + r"\TesterProjectAK.aprx")
Map1 = aprx.listMaps()[0]
newfile = cwd + r"\TestTable1.csv" 
Map1.addDataFromPath (newfile)
aprx.saveACopy(cwd + r"\TesterProjectAK2")
del aprx
