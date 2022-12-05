###################ARCPY MODULE##########################
#Lead: Adrian K. 
#Support: n/a
#Notes: This section imports the output table with the calculations provided into
#an existing ArcGIS Project Geodatabase, converts it into a point feature class, adds
#the feature class to the map, and exports the results as a shapefile for dissimination
#Sources: Support from Karen Whillians (professor), Esri Website
#https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/xy-table-to-point.htm
#https://pro.arcgis.com/en/pro-app/latest/arcpy/mapping/map-class.htm
#########################################################

#Setting the workspace up
import os
import arcpy
cwd = os.getcwd()

def main(): 
    try:
        arcpy.env.workspace = (cwd + r"\A3Team7Project.gdb")
        # arcpy.env.overwriteOutput = True          #Turn this on if you wish to overwrite files instead of making copys,and remove the following While loop. 

        #Setting up ArcPy Mapping Module
        aprx = arcpy.mp.ArcGISProject(cwd + r"\A3Team7Project.aprx")
        Map1 = aprx.listMaps()[0]

        #Preparing the Table
        aFile = cwd + r"\A3Team7Output.csv" 
        output_gdb = cwd + r"\A3Team7Project.gdb"
        output_gdbALT = cwd + "\\A3Team7Project.gdb\\"
        A3T7_feature_class = "A3Team7"

        #Issue handling if there is an existing Feature Dataset in the geodatabase with the same name. 
        #Alternatively, this section can be removed and acrpy.env.overwriteOutput can be set to True
        while True:
            if arcpy.Exists(A3T7_feature_class):
                print("Warning! Renaming Feature Class. Advise removing previous versions of the A3Team7 file(s) from the geodatabase and Shapefile folder")
                A3T7_feature_class = A3T7_feature_class + "_copy"
            else:
                break

        # XYTable to Point - Converting the Table to a Point Feature Class
        # Without setting the optional spatial reference parameter, spatial reference will be WGS1984 by default
        x_coords = "Longitude"
        y_coords = "Latitude"
        arcpy.management.XYTableToPoint(aFile, A3T7_feature_class, x_coords, y_coords)

        #Adding the Point Feature Class to the Map
        class_to_add = output_gdbALT + A3T7_feature_class
        print(class_to_add)
        Map1.addDataFromPath(class_to_add)

        # #Converting and Exporting a FeatureClass for dissemination, then adding it to the Map
        arcpy.FeatureClassToShapefile_conversion(A3T7_feature_class, cwd + r"\ShapeFileDestination")
        A3T7ShapeFilePath = cwd + "\\ShapeFileDestination\\"
        A3T7ShapeFile = A3T7_feature_class
        FileExtension = ".shp"
        ShapeFileCombo = A3T7ShapeFilePath + A3T7ShapeFile + FileExtension
        Map1.addDataFromPath(ShapeFileCombo)

        #'Clean up and turn off the lights' - prevent ArcGIS project overwritting or file locks
        aprx.saveACopy(cwd + r"\A3Team7ProjectCOPY.aprx")
        del aprx
        print("A feature class has been added to your geodatabase, and a Shapefile has been added to the 'ShapeFileDesitnation' Folder")
    except Exception:
        print("There was an issue with the geospatial section of the project.")


if __name__ == '__main__':
    main()