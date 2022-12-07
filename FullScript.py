################### ApartmentSeekerSunlightCalculator.py ##########################
#ApartmentSeekerSunlightCalculator.py
#Authors: Adrian Koornneef, Becca Charmichael, Chris Boom, Yingjia Ye
#Last Updated: Dec-06-2022

#Reading notes: 
# Program notes included throughout the script in various modules
# Detailed notes are provided in readme file found in the program main folder
# Program notes are provided in each module / function section
# Main Program function begins after functions / modules

#Purpose: This program will calculate the minimum required floor height for apartment hunters to prevent full shade at various times of year
#given provide geospatial data. This program will also calculate statistical information about the amount of sunlight hours the user
#can expect to receive, given the same geospatial information. 

# Contributions: See individual module heading section for code contributions.
# Modules:
# - Min Height calculator function: Chris / Yingjia
# - Day of focus sunlight calculator function: Chris / Yingjia
# - User interface: Becca / Yingjia
# - Sunlight hour statistics function: Chris
# - ArcPy: Adrian
# - Display results: Becca
# - Main program: Adrian / team 
# - Output table: Yingjia
# Additional contributions not identified in individual code section:
# - Topic brainstorming leads: Yingjia, Adrian
# - Initial math feasibility check lead: Yingjia
# - Extensive algorithm testing (project design): Chris
# - Initial python algorithm drafting and debugging: Yingjia
# - Debugging: Chris, Yingjia
# - Github repository management: Becca
# - Proofreading, spelling and formatting error check: Becca & Yingjia
# - Readme: Adrian
# - Code formatting for neatness: Adrian
# - Meetings lead: Adrian
# - Testing lead: Adrian

#Sources: -Formulas:
#     -Sunrise and Sunset Time Calculator | Sunrise Equation. (n.d.). Had2Know. Retrieved November 15, 2022, from https://www.had2know.org/society/sunrise-sunset-time-calculator-formula.html
#     -Honsberg, C. B., & Bowden, S. G. (2019). Elevation Angle | PVEducation. https://www.pveducation.org/pvcdrom/properties-of-sunlight/elevation-angle
#     -Honsberg, C. B., & Bowden, S. G. (2019). Declination Angle | PVEducation. https://www.pveducation.org/pvcdrom/properties-of-sunlight/declination-angle
# -Support from Karen Whillians (professor) 
# -Esri Website:
#     -https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/xy-table-to-point.htm
#     -https://pro.arcgis.com/en/pro-app/latest/arcpy/mapping/map-class.htm
##################################################################################

#Import Modules
import math
import os
import arcpy

#Import the lat/long city list - the list was written by Yingjia Ye 
# https://www.latlong.net/category/cities-40-15.html
# https://www.get-direction.com/cities-lat-long.html?country=canada-2&offset=435 
import csv

################### MIN HEIGHT CALCULATOR FUNCTION ###############################
#Lead: Chris B. 
#Support: Yingjia Y 
#Notes: This section calculates the minimum height of apartment needed to get sunlight on any given day 
#Sources: See Readme file
##################################################################################

def minimumheight(user_Latitude,building_distance,building_height,DayVal):
    """This function does three calculations to return the required height of the users inputted building. 
    Calculation 1 is of declination angle given users day of focus. 
    Calculation 2 is of the elevation angle 
    Calculation 3 is of the minimum height of the building rounded to two decimal places
    Returns values above 0, else it returns 0"""
    FocusDay_DeclinationAngle=-23.45*math.cos((math.pi/180)*(360/365)*(DayVal+10))     
    ElevationAngle=90-float(user_Latitude)+float(FocusDay_DeclinationAngle)    
    minimumheight=building_height-(math.tan((math.pi/180)*ElevationAngle))*building_distance
    minimumheight=round(minimumheight,2)
    if minimumheight > 0:
        return minimumheight
    else:
        return 0

################### DAY OF FOCUS SUNLIGHT HOUR FUNCTION ##########################
#Lead: Chris B. 
#Support: Yingjia Y 
#Notes: This section calculates the possible amount of sunlight hours for one day
#Sources: See Readme file 
##################################################################################

def SunlightCalculator(DayVal,user_Latitude):
    """This function calculates the hours of sunlight given a day of focus, and latitude, rounded to two decimal places."""
    HoursofSunlight = 2*(1/15)*(180/math.pi)*math.acos((-math.tan((math.pi/180)*user_Latitude))*(math.tan((math.pi/180)*23.44*math.sin((360/365)*(DayVal+284)*(math.pi/180)))))
    HoursofSunlight = round(float(HoursofSunlight),2)
    return HoursofSunlight

########################## USER INTERFACE MODULE #################################
#Lead: Becca C & Yingjia Y 
#Notes: This section includes all of the prompts for the user input for the program to get all of the apartment data,
# and the DayValu calculator which calculates how many days into the year the selected date is.    
#Assumptions: the calculation is not being made for a leap year
#################################################################################

def getInputForAnApartment ():
    '''Get all of the inputs for a single apartment.  There are three parts:
    Location - latitude, longitude, city_name. city_name is blank if they enter coordinates directly.  If they use a city name, they also enter the province and that gets included.
    Other Building - building_height, building_distance.  Both floats.
    Date - DayVal, DayOfFocus.  DayVal is an int and tells you how many days into the year the date is.  DayOfFocus is a string like "Feb 1"
    '''

    #Get the city data from the csv - written by YJ
    with open("latlong.csv", newline="") as fo:
        city_reference_list = list(csv.reader(fo)) # read the file into a big list

    ### Constants that are used in this function - days in each month and assigning months - written by BC 
    daysInEachMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthNumberFromEnglishName = {
        "jan": 1,
        "january": 1,
        "feb": 2,
        "february": 2,
        "mar": 3,
        "march": 3,
        "apr": 4,
        "april": 4,
        "may": 5,
        "jun": 6,
        "june": 6,
        "jul": 7,
        "july": 7,
        "aug": 8,
        "august": 8,
        "sep": 9,
        "sept": 9,
        "september": 9,
        "oct": 10,
        "october": 10,
        "nov": 11,
        "november": 11,
        "dec": 12,
        "december": 12
    }
    monthNames = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"]
    print("Please answer the following questions with information regarding the prospective apartment:")

    ### Get location data for apartment ###
    user_Latitude = None
    user_Longitude = None
    city_name = ""

    #Prompt for the latitude and longitude (returned  as floats, or returns them as "None" and asks the user to try again, if they can't be cast to floats)
    def getLatLong ():
        user_Latitude = input("Please enter the decimal latitude (ex: 55.74994204): ")
        user_Longitude = input("Please enter the decimal longitude (ex: -97.86662093): ")

        try:
            user_Latitude = float(user_Latitude)
            user_Longitude = float(user_Longitude)
        except ValueError:
            print("Please enter both the latitude and longitude as numeric values (use decimal units).  Try again:\n")

            return None, None
        if user_Latitude <-66.5 or user_Latitude > 66.5 or user_Longitude > 180 or user_Longitude < -180: 
            print("Please enter meaningful latitude and longitude values. ")
            print("Latitude (decimal degree) between -65.5 and 65.5. Longitude (decimal degree) between -180 and 180 degrees.")
            return None, None 
        return round(user_Latitude, 8), round(user_Longitude, 8)

    while (user_Latitude is None or user_Longitude is None):
        locationType = input("Would you like to select from a list of Canadian cities, or provide the latitude/longitude coordinates? (city/coords): ")
        
        #If user wants to enter just coordinates 
        if locationType == "coords":
            user_Latitude, user_Longitude = getLatLong()

        #If they want to enter a city name, we check if we have it in the (latlong csv by YJ), and if not then they have to enter coordinates
        elif locationType == "city":
            city_name = input("Please enter the Canadian city the prospective apartment is located in: ")
            city_name = city_name.upper()  
            foundCity = False
            for city_data in city_reference_list:
                if city_name == city_data[0]:
                    user_Latitude = float(city_data[1])
                    user_Longitude = float(city_data[2])
                    foundCity = True
                    break
            
            if not foundCity:
                print("That city isn’t in the system")
                user_Latitude, user_Longitude = getLatLong()

        else:
            print("Please reply with 'city' or 'coords' to decide how to input the location\n")

    ### Get data for other building - written by YJ and BC ###
    building_height = None
    building_distance = None

    while(building_distance is None or building_height is None):
        building_height = input("Please enter the height of the closest south facing adjacent building, in meters: ")
        building_distance = input("Please enter the distance between the two buildings in meters: ")

        try:
            building_height = float(building_height)
            building_distance = float(building_distance)

        #If the inputs can't be made into numbers, tell the user to try again
        except ValueError:
            #If we couldn't make them numbers, make them None so that the loop will go again and the user can try entering the values again
            building_height = None
            building_distance = None
            print("Please enter both the building height and building distance as numeric values in meters.  Try again:\n")

    ### DayValu calculator (which calculates how many days into the year the selected date is) and get the date that user is focused on - written by BC ###
    #Starts not defined
    DayVal = None

    while (DayVal is None):
        try:
            #Ask the user for the month and day and make them into ints
            user_FocusMonth = input("Please enter the month you would like to calculate sunlight exposure for: ")
            user_FocusDay = input("Please enter the day you would like to calculate sunlight exposure for, as a number (1-31): ")
            user_FocusMonth = user_FocusMonth.lower()  

            #If we recognize the text as the name of a month, convert it to a number
            if user_FocusMonth in monthNumberFromEnglishName.keys():
                user_FocusMonth = monthNumberFromEnglishName[user_FocusMonth]

            #Otherwise, its hopefully a number
            else:
                user_FocusMonth = int(user_FocusMonth)
                if user_FocusMonth not in range(1,13): 
                    raise ValueError("The month must be in the range 1-12!")

            #Day must be a number
            user_FocusDay = int(user_FocusDay)
            if user_FocusDay not in range(1, daysInEachMonth[user_FocusMonth - 1] + 1):  # checks that day is in the range for that month (e.g. no feb 31)
                raise ValueError("The day must be in the range 1-31!")

            #Get the "day of the year" by adding up all the days in the months up to (not including) the focus month, and then adding the days
            DayVal = sum(daysInEachMonth[:user_FocusMonth - 1]) + user_FocusDay

        #If it didn't work, reset everything to None and tell them to try again
        except ValueError:
            user_FocusMonth = None
            user_FocusDay = None
            DayVal = None
            print("The month and day must be entered in a readable format (e.g. 'aug' or '8' for month, day must be a number 1-31).  Please try again!\n")
    
    #DayOfFocus - human readable date string for the output
    DayOfFocus = monthNames[user_FocusMonth - 1] + " " + str(user_FocusDay)

    ### return all the inputs for a single location ###
    return user_Latitude, user_Longitude, city_name, building_height, building_distance, DayOfFocus, DayVal


################### SUNLIGHT HOUR STATISTICS  ###################################
#Lead: Chris B.
#Support: Yingjia Y 
#Notes: This section calculates the minimum, maximum, average and sum of possible sunlight hours 
#Sources: See Readme file
##################################################################################

def sunlighthourstatistics (user_Latitude):
    """This function provides basic statistics. The calculation of sunlight hours is looped 365 times. It creates a lists of 365 min,max,avg,sum values."""
          
    CalculationsList=[]
    for d in range(1,366):
        sunlighthour=2*(1/15)*(180/math.pi)*math.acos((-math.tan((math.pi/180)*user_Latitude))*(math.tan((math.pi/180)*23.44*math.sin((360/365)*(d+284)*(math.pi/180)))))
        CalculationsList.append(sunlighthour)

    minhour=min(CalculationsList)
    maxhour=max(CalculationsList)
    avghour=sum(CalculationsList)/len(CalculationsList)
    sumhour=sum(CalculationsList)

    return minhour,maxhour,avghour,sumhour


############################### ARCPY MODULE ######################################
#Lead: Adrian K. 
#Notes: This section imports the output table with the calculations provided into
#an existing ArcGIS Project Geodatabase, converts it into a point feature class, adds
#the feature class to the map, and exports the results as a shapefile for dissemination. This section 
# will make a new "copy" of the feature class and shapefile each time it is run and 'save as' in a copy of the ArcGIS Project.
# It is recommended best practice that the user removes or renames previous versions of the feature classes / shapefiles between
# each run. 
#Assumption: Geospatial data will be provided in WGS 1984 Geocordinate System. 
#Sources: Support from Karen Whillians (professor), Esri Website
#https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/xy-table-to-point.htm
#https://pro.arcgis.com/en/pro-app/latest/arcpy/mapping/map-class.htm
##################################################################################

def GeoSpatialFunction(): 
    """Add the output table as a point feature class in a geodatabase, add to the map, and export a shapefile for dissemination"""
    cwd = os.getcwd()
    try:
        arcpy.env.workspace = (cwd + r"\A3Team7Project.gdb")
        # arcpy.env.overwriteOutput = True          #Turn this on if you wish to overwrite files instead of making copies,and remove the following While loop. 

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

        #XYTable to Point - Converting the Table to a Point Feature Class
        #Without setting the optional spatial reference parameter, spatial reference will be WGS1984 by default
        x_coords = "Longitude"
        y_coords = "Latitude"
        arcpy.management.XYTableToPoint(aFile, A3T7_feature_class, x_coords, y_coords)

        #Adding the Point Feature Class to the Map
        class_to_add = output_gdbALT + A3T7_feature_class
        print(class_to_add)
        Map1.addDataFromPath(class_to_add)

        #Converting and Exporting a FeatureClass for dissemination, then adding it to the Map
        arcpy.FeatureClassToShapefile_conversion(A3T7_feature_class, cwd + r"\ShapeFileDestination")
        A3T7ShapeFilePath = cwd + "\\ShapeFileDestination\\"
        A3T7ShapeFile = A3T7_feature_class
        FileExtension = ".shp"
        ShapeFileCombo = A3T7ShapeFilePath + A3T7ShapeFile + FileExtension
        Map1.addDataFromPath(ShapeFileCombo)

        #Clean up and turn off the lights' - prevent ArcGIS project overwriting or file locks
        aprx.saveACopy(cwd + r"\A3Team7ProjectCOPY.aprx")
        del aprx
        print("A feature class has been added to your geodatabase, and a Shapefile has been added to the 'ShapeFileDestination' Folder")
    except Exception:
        print("There was an issue with the geospatial section of the project.")

######################### DISPLAY APARTMENT RESULTS ###############################
#Lead: Becca C.
#Notes: This section displays all of the in-program outputs including the user inputs and calculated values for each apartment. 
##################################################################################

def displayResultsForAnApartment (user_Latitude, user_Longitude, city_name, DayOfFocus, FocusDay_MinimumHeight, SummSolstice_MinimumHeight, WintSolstice_MinimumHeight, FocusDay_SunlightHours, AnnualTotalSunlight, AnnualAvgSunlight, AnnualMin, AnnualMax):
    '''Output the results for an apartment in three parts: The apartment info, minimum height results, and hours of sunlight results'''
    print("\n------------------------------------------------------------------------------------------------------------")

    #First part - apartment info
    print("\nThe results for the prospective apartment are as follows:")
    print("    Latitude:       ", user_Latitude)
    print("    Longitude:      ", user_Longitude)
    print("    City:           ", city_name)
    print("    Date:           ", DayOfFocus)

    #Second part - minimum height results
    print("\nTo get at least 1 hour of sunlight, the minimum height (in meters) of the prospective apartment must be:")
    print("    On your chosen date:           ", FocusDay_MinimumHeight)
    print("    On the winter solstice:        ", WintSolstice_MinimumHeight)
    print("    On the summer solstice:        ", SummSolstice_MinimumHeight)

    #Third part - hours of sunlight results
    print("\nThe potential hours of sunlight for " + city_name + " is:")
    print("    On your chosen date:           ", FocusDay_SunlightHours)
    print("    On the day with the most sun:  ", AnnualMax)
    print("    On the day with the least sun: ", AnnualMin)
    print("    On average in a day:           ", AnnualAvgSunlight)
    print("    In total throughout the year:  ", AnnualTotalSunlight)

def displayResults (latitude_list, longitude_list, city_name_list, DayOfFocus_list, FocusDay_MinimumHeight_list, SummSolstice_MinimumHeight_list, WintSolstice_MinimumHeight_list, FocusDay_SunlightHours_list, AnnualTotalSunlightHour, AnnualAvgSunlightHour, AnnualMinHour, AnnualMaxHour):
    '''Display the results for a list of apartments, by repeatedly using the "displayResultsForAnApartment" function'''
    for (user_Latitude, user_Longitude, city_name, DayOfFocus, FocusDay_MinimumHeight, SummSolstice_MinimumHeight, WintSolstice_MinimumHeight, FocusDay_SunlightHours, AnnualTotalSunlight, AnnualAvgSunlight, AnnualMin, AnnualMax) in zip(latitude_list, longitude_list, city_name_list, DayOfFocus_list, FocusDay_MinimumHeight_list, SummSolstice_MinimumHeight_list, WintSolstice_MinimumHeight_list, FocusDay_SunlightHours_list, AnnualTotalSunlightHour, AnnualAvgSunlightHour, AnnualMinHour, AnnualMaxHour):
        displayResultsForAnApartment(user_Latitude, user_Longitude, city_name, DayOfFocus, FocusDay_MinimumHeight, SummSolstice_MinimumHeight, WintSolstice_MinimumHeight, FocusDay_SunlightHours, AnnualTotalSunlight, AnnualAvgSunlight, AnnualMin, AnnualMax)
        
    print("\n------------------------------------------------------------------------------------------------------------\n")

############################## MAIN PROGRAM #######################################
#Lead: Adrian K.
#Support: All (completed together, w/ Adrian inputting, various parts taken out of other modules )
#Notes: See Readme file
#Sources: See Readme file
#####################################################################################

def main():
    """This is the main program, which calls various functions from different modules"""

    startMessage = """POTENTIAL SUNLIGHT EXPOSURE CALCULATOR FOR APARTMENT HUNTERS
    This program will calculate statistical data about potential sunlight for a city/ area in the Northern Hemisphere, based off spatial data, as well as the optical height (floor) of a dwelling (apartment).
    This will aid apartment hunters in preventing selecting an apartment with less/ no sunlight exposure due to other buildings.
    """
    print(startMessage)

    ### Get all the values for the locations ###
    #Empty lists to hold the inputs
    latitude_list = []
    longitude_list = []
    city_name_list = []
    building_height_list = []
    building_distance_list = []
    DayOfFocus_list = []
    DayVal_list = []
    DayOfFocusHeight=[]
    SummerHeight=[]
    WinterHeight=[]
    DayofFocusHour=[]
    AnnualTotalSunlightHour=[]
    AnnualAvgSunlightHour=[]
    AnnualMinHour=[]
    AnnualMaxHour=[]
    #Hard Coding Wint/Summer Solstice
    SummSolstice_DayVal = 172
    WintSolstice_DayVal = 355

    #Get inputs for apartments until they decide to stop entering values
    while (True):
        #Get inputs for an apartment
        user_Latitude, user_Longitude, city_name, building_height, building_distance, DayOfFocus, DayVal = getInputForAnApartment()
        latitude_list.append(user_Latitude)
        longitude_list.append(user_Longitude)
        city_name_list.append(city_name)
        building_height_list.append(building_height)
        building_distance_list.append(building_distance)
        DayOfFocus_list.append(DayOfFocus)
        DayVal_list.append(DayVal)

        #Let the user break the loop if they wish, or keep going
        end = input("Do you want to stop entering values (Y/N)? ") 
        print()
        if end.upper() == 'Y' :
            break
        
    ### get shp options ###
    #default values
    user_wants_shp = False

    #Ask user if they want to perform the geospatial functions 
    wants_shp_input = input("Would you like to perform geospatial functions with ArcGIS Pro? Yes or No: ")

    #If they want it, set user_wants_shp to true and ask them for all the details
    if wants_shp_input.lower() == "yes" or wants_shp_input.lower() == "y" :
        user_wants_shp = True
        print("A feature class and shapefile file will be generated")

    #If they don't want it, leave the default (blank) values
    else:
        print("A feature class and shapefile file will not be generated")

    #Call the necessary functions to complete each calculation, for each location provided by the user
    numberOfapartments = len(latitude_list)
    for i in range(numberOfapartments):
        #Establish temporary variables that can be written over for each iteration of the loop.
        user_LatitudeTemp = latitude_list[i]
        building_distanceTemp =  building_distance_list[i]
        building_heightTemp = building_height_list[i]
        DayValTemp = DayVal_list[i]
        
        #Focus Day Minimum Height
        FocusDay_MinHeight = minimumheight(user_LatitudeTemp, building_distanceTemp, building_heightTemp, DayValTemp)
        DayOfFocusHeight.append(FocusDay_MinHeight)
        
        #Winter Solstice Height
        WintSol_MinHeight = minimumheight(user_LatitudeTemp, building_distanceTemp, building_heightTemp, WintSolstice_DayVal)
        WinterHeight.append(WintSol_MinHeight)
        
        #Summer Solstice Height
        SummSol_MinHeight = minimumheight(user_LatitudeTemp, building_distanceTemp, building_heightTemp, SummSolstice_DayVal)
        SummerHeight.append(SummSol_MinHeight)
        
        #Calculate number of sunlight hours, day of focus
        FocusDay_SunlightHours = SunlightCalculator(DayValTemp, user_LatitudeTemp)
        DayofFocusHour.append(FocusDay_SunlightHours)
    
        #Calculate sunlight hour statistics
        minhour = sunlighthourstatistics(user_LatitudeTemp)[0]
        AnnualMinHour.append(minhour)
        maxhour = sunlighthourstatistics(user_LatitudeTemp)[1]
        AnnualMaxHour.append(maxhour)
        avghour = sunlighthourstatistics(user_LatitudeTemp)[2]
        AnnualAvgSunlightHour.append(avghour)
        sumhour = sunlighthourstatistics(user_LatitudeTemp)[3]
        AnnualTotalSunlightHour.append(sumhour)

    ################### MAIN PROGRAM - OUTPUT TABLE  ################################
    #Lead: Yingjia Y.
    #Notes: This section writes to a csv file which contains the user inputs and calculated values. 
    #################################################################################

    myheader=['CityName','Latitude','Longitude','DayOfFocus','DayOfFocusHeight','DayofFocusHour','WinterHeight','SummerHeight','AnnualTotalSunlightHour','AnnualAvgSunlightHour','AnnualMinHour','AnnualMaxHour']

    with open('A3Team7Output.csv','w',newline='') as newfile:
        writer=csv.writer(newfile)
        writer.writerow(myheader)
        for i in range(numberOfapartments):
            writer.writerow([city_name_list[i],latitude_list[i],longitude_list[i],DayOfFocus_list[i],DayOfFocusHeight[i],DayofFocusHour[i],WinterHeight[i],SummerHeight[i],AnnualTotalSunlightHour[i],AnnualAvgSunlightHour[i],AnnualMinHour[i],AnnualMaxHour[i]])
   
   ###################### MAIN PROGRAM - CONTINUED ###################################
    displayResults (latitude_list, longitude_list, city_name_list, DayOfFocus_list, DayOfFocusHeight, SummerHeight, WinterHeight, DayofFocusHour, AnnualTotalSunlightHour, AnnualAvgSunlightHour, AnnualMinHour, AnnualMaxHour)

    #Call the ArcPy Module
    if user_wants_shp == True: 
        GeoSpatialFunction()

    #Output messaging
    print()
    print("\n------------------------------------------------------------------------------------------------------------\n")
    print("Program complete. Please run again if you wish to complete for another location.")

#Call to begin the main program
if __name__ == '__main__':
    main()
