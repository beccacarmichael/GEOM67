################################## APARTMENT SEEKER SUNLIGHT CALCULATOR README ##################################
ApartmentSeekerSunlightCalculator.py
Readme section lead: Adrian Koornneef
################################################################################################################

#################### AUTHORS ####################################
Adrian Koornneef, Chris Boom, Becca Charmicael, Yingjia Ye
#################################################################

#################### PURPOSE ####################################
This program will calculate the minimum required floor height for apartment hunters to prevent full shade at various times of year
given provide geospatial data. This program will also calculate statistical information about the amount of sunlight hours the user
can expect to receive, given the same geospatial information. 
#################################################################

#################### RESULTS ####################################
The results will be provide as a .csv file for the user to read. The results will also be added into an ArcGIS project and
geodatabase, provided in the program folder. A copy of a .shp will also be made available in the 'ShapefileDestination' folder
for easy dissemination. 
#################################################################

#################### ASSUMPTIONS AND LIMITATIONS ################
-   The program will assume a 365-day calendar year and will not account for leap years.
-   Summer and winter solstice are hard-coded to days 172 and 355 respectively
-   Apartment height calculations are only relevant for the northern hemisphere. Additional work required for southern hemisphere.
-   Any lat and long can be provided, but picking a city from a list feature is only applicable to Canadian cities
-	Minimum apartment height calculations are based on receiving at least one hour of potential daylight exposure during 
    the day of focus, winter solstice, and summer solstice; not full days of exposure.
-   Apartment height calculations assume south facing windows in the Northern hemisphere.
-   Calculations for potential sunlight exposure are based on the geographic area of focus, 
    the program will not calculate hours of potential sunlight in the apartment itself. 
-   Hours of potential sunlight for an area are accurate within approximately 30 minutes per day. Calculations become less
    accurate at extreme latitudes. 
-   Height and distance calculations will be meters.
-   Calculations are for potential hours of sunlight, and can’t account for overcast days, storms, etc.
-   Geospatial data will be provided in WGS 1984 Geocordinate System.
-   Average sunlight hours and total sunlight hours produces very similar results, as a result of the number of potential hours averaging over the course of the year.  
###############################################################

################### IDENTIFIED BUGS ###########################
Shapefiles truncate the header name in the attribute table. Doesn't occur in Feature Class file. 
###############################################################

###################### TEST FILES #############################
Test files can be found in the test file folder for output csv.'s and .shp files. 
Test feature classes can be found in the geodatabase. 
###############################################################

#################### INPUTS ###################################
List of Canadian cities .csv (see sources for more information)
Inputs required from user: 
    - Lat / Long cooridinates or name of Canadian city for desired apartment location
    - Day of study (i.e. FocusDay)
    - Height of southern influencing building
    - Distance of southern influencing building from desired apartment location
    - Confirmation when the user wishes to end adding apartment locations
    - Confirmation if the user would like geospatial project compelte
#################################################################

#################### Outputs ###################################
Values provided:
    - Minimum apartment height for the day of focus, to receive at least 1 hour of sunlight
    - Minimum apartment height at winter solstice (i.e. shortest day of the year)
    - Minimum apartmennt height at summer solistice (i.e. longest day of the year)
    - Hours of potential sunlight expected at the provided location (not inside the apartment itself) for day of focus
    - Hours of potential sunlight expected at the provided location for winter solstice 
    - Hours of potential sunlight expected at the provided location for summer solstice
    - Average number of potential sunlight hours expected throughout the year at the provided location
    - Total number of potential sunlight hours expected throughout the year at the provided location
Values are provided as text in the terminal interface
Values are provided as an output .csv
Values are provided in an attribute table in a point feature class in the ArcGIS geodatabase
Values are  provided in an attribute table of a shapefile in the 'ShapefileDestination' folder
Feature layer and shapefile are added to the active environment of a map in ArcGIS project in a saved copy
#################################################################

#################### CONTRIBUTIONS ############################
See individual module heading section for code contributions.
Additional contirbutions not identified in individual code section:
- Topic brainstorming leads: Yingjia, Adrian
- Initial math feasibility check lead: Yingjia
- Extensive algroithm testing (project design): Chris
- Initial python algroithm drafting and debugging: Yingjia
- Debugging: Chris, Yingjia
- Github repository management: Becca
- Readme: Adrian
- Code formatting for neatness: Adrian
- Meetings lead: Adrian
#################################################################

#################### SOURCES ##################################
-Formulas:
    -Sunrise and Sunset Time Calculator | Sunrise Equation. (n.d.). Had2Know. Retrieved November 15, 2022, from https://www.had2know.org/society/sunrise-sunset-time-calculator-formula.html
    -Honsberg, C. B., & Bowden, S. G. (2019). Elevation Angle | PVEducation. https://www.pveducation.org/pvcdrom/properties-of-sunlight/elevation-angle
    -Honsberg, C. B., & Bowden, S. G. (2019). Declination Angle | PVEducation. https://www.pveducation.org/pvcdrom/properties-of-sunlight/declination-angle
-Support from Karen Whillians (professor) 
-Esri Website:
    -https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/xy-table-to-point.htm
    -https://pro.arcgis.com/en/pro-app/latest/arcpy/mapping/map-class.htm
###############################################################
