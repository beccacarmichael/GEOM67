
################################## APARTMENT SEEKER SUNLIGHT CALCULATOR README ##################################
ApartmentSeekerSunlightCalculator.py
Section lead: Adrian Koornneef


#################### AUTHORS ####################
Adrian Koornneef, Chris Boom, Becca Charmicael, Yingjia Ye

#################################################

#################### PURPOSE ####################
This program will calculate the minimum required floor height for apartment hunters to prevent full shade at various times of year
given provide geospatial data. This program will also calculate statistical information about the amount of sunlight hours the user
can expect to receive, given the same geospatial information. 
#################################################

#################### RESULTS ####################
The results will be provide as a .csv file for the user to read. The results will also be added into an ArcGIS project and
geodatabase, provided in the program folder. A copy of a .shp will also be made available in the 'ShapefileDestination' folder
for easy dissemination. 
#################################################

#################### ASSUMPTIONS ################
#-  The program will assume a 365-day calendar year and will not account for leap years.
#-	Minimum apartment height calculations are based on receiving at least one hour of potential daylight exposure during 
the day of focus.
#-  Winter solstice, and summer solstice; not full days of exposure.
#-  Apartment height calculations assume south facing windows in the Northern hemisphere.
#-  Calculations for potential sunlight exposure are based on the geographic area of focus, 
the program will not calculate hours of potential sunlight in the apartment itself. 
#-  Hours of potential sunlight for an area are accurate within approximately 30 minutes per day. Calculations become less
accurate at extreme latitudes. 
#-  Height and distance calculations will be meters.
#-  Calculations are for potential hours of sunlight, and can’t account for overcast days, storms, etc.
#-  Geospatial data will be provided in WGS 1984 Geocordinate System. 
#################################################

###################### TEST FILES ###############
#TBD TEAM


#################################################

#################### SOURCES ####################


#################################################
