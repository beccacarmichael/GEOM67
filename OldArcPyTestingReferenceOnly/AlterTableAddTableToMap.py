#https://pro.arcgis.com/en/pro-app/latest/tool-reference/conversion/table-to-table.htm
import os
import arcpy
cwd = os.getcwd()
aprx = arcpy.mp.ArcGISProject(cwd + r"\TesterProjectAK.aprx")
Map1 = aprx.listMaps()[0]
newfile = cwd + r"\TestTable1.csv" 
out_gdb = cwd + r"\TesterProjectAK.gdb"

#May need a Try/Except clause to cover if the table already exists.
arcpy.TableToTable_conversion(newfile, out_gdb, 'TempTable')
gdb_table = arcpy.mp.Table(cwd + r"\TesterProjectAK.gdb\TempTable")
Map1.addTable(gdb_table)

aprx.saveACopy(cwd + r"\TesterProjectAK3.aprx")
del aprx

