################### USER INTERFACE MODULE ##########################
#Lead: Becca C & Yingjia Y 
#Support: N/AS 
#Notes: This module includes all of the prompts for the user inputs and 
# outputs for the program. It is intended to be imported into the main 
# file. 
#Sources: N/A
####################################################################


#import the latlong/ city list 
import csv

# message for the program to print at the beginning
startMessage = """POTENTIAL SUNLIGHT EXPOSURE CALCULATOR FOR APARTMENT HUNTERS

This program will calculate statistical data about potential sunlight for a city/ area in Canada, based off spatial data, as well as the optical height (floor) of a dwelling (apartment).
This will aid apartment hunters in preventing selecting an apartment with less/ no sunlight exposure due to other buildings.
"""

# get the city data from the csv - written by YJ
with open("latlong.csv", newline="") as fo:
    city_reference_list = list(csv.reader(fo)) # read the file into a big list


def getInputForAnApartment ():
    '''Get all of the inputs for a single apartment.  There are three parts:
    Location - latitude, longitude, city_name. city_name is blank if they enter coordinates directly.  If they use a city name, they also enter the province and that gets included.
    Other Building - building_height, building_distance.  Both floats.
    Date - DayVal, DayOfFocus.  DayVal is an int and tells you how many days into the year the date is.  DayOfFocus is a string like "Feb 1"
    '''
    ### Some constants that are used in this function
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

    # This little function prompts the user for the latitude and longitude and returns them as floats, or returns them as "None" and asks the user to try again, if they can't be cast to floats
    def getLatLong ():
        user_Latitude = input("Please enter the decimal latitude: ")
        user_Longitude = input("Please enter the decimal longitude: ")

        # Make them floats.  If it doesn't work, return None for both values.
        try:
            user_Latitude = float(user_Latitude)
            user_Longitude = float(user_Longitude)
        except ValueError:
            print("Please enter both the latitude and longitude as numeric values (use decimal units).  Try again:\n")

            # The while loop to get the location info keeps running if the lat/long are None,
            #   so if we couldn't make them numbers, make them None so that the loop will go again and the user can try entering the values again
            return None, None

        return user_Latitude, user_Longitude

    # Get inputs inside a loop so that user can try again if they enter invalid info
    while (user_Latitude is None or user_Longitude is None):
        # Ask them how they want to enter the info
        locationType = input("Would you like to select from a list of Canadian cities, or provide the latitude/longitude coordinates? (city/coords): ")
        
        # If they want to enter coordinates directly, just do that
        if locationType == "coords":
            user_Latitude, user_Longitude = getLatLong()

        # If they want to enter a city name, we check if we have it in the list, and if not then they have to enter coordinates
        elif locationType == "city":
            city_name = input("Please enter the Canadian city the prospective apartment is located in: ")
            city_name = city_name.upper()  # make the city name uppercase because the list of cities is uppercase
            #######province = input("Please enter the Canadian province/territory the prospective apartment is located in: ")
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
            
            city_name = city_name + ", " ##+ province.upper()  # add the province name to the city for display purposes

        # If they enter something else, we ask them to try again
        else:
            print("Please reply with 'city' or 'coords' to decide how to input the location\n")


    ### Get data for other building ###
    building_height = None
    building_distance = None

    # Get inputs inside a loop so that user can try again if they enter invalid info
    while(building_distance is None or building_height is None):
        building_height = input("Please enter the height of the closest south facing adjacent building, in meters: ")
        building_distance = input("Please enter the distance between the two buildings in meters: ")

        # Try to make them numbers
        try:
            building_height = float(building_height)
            building_distance = float(building_distance)

        # If the inputs can't be made into numbers, tell the user to try again
        except ValueError:
            # The while loop to get the info keeps running if the values are None,
            #   so if we couldn't make them numbers, make them None so that the loop will go again and the user can try entering the values again
            building_height = None
            building_distance = None
            print("Please enter both the building height and building distance as numeric values in meters.  Try again:\n")


    ### get date that user is focused on ###
    # Starts not defined
    DayVal = None

    # loop lets them try again if they enter invalid values
    while (DayVal is None):
        # Try to enter values and get the DayVal
        try:
            # Ask the user for the month and day and make them into ints
            user_FocusMonth = input("Please enter the month you would like to calculate sunlight exposure for: ")
            user_FocusDay = input("Please enter the day you would like to calculate sunlight exposure for, as a number (1-31): ")
            user_FocusMonth = user_FocusMonth.lower()  # make it lowercase because the monthNumberFromEnglishName dictionary is all lowercase

            # If we recognize the text as the name of a month, convert it to a number
            if user_FocusMonth in monthNumberFromEnglishName.keys():
                user_FocusMonth = monthNumberFromEnglishName[user_FocusMonth]

            # otherwise, its hopefully a number
            else:
                user_FocusMonth = int(user_FocusMonth)
                if user_FocusMonth not in range(1,13):  # its 13 because the last number is not included - this makes sure its in 1-12 inclusive
                    raise ValueError("The month must be in the range 1-12!")

            # Day must be a number
            user_FocusDay = int(user_FocusDay)
            if user_FocusDay not in range(1, daysInEachMonth[user_FocusMonth - 1] + 1):  # checks that day is in the range for that month (e.g. no feb 31)
                raise ValueError("The day must be in the range 1-31!")

            # Get the "day of the year" by adding up all the days in the months up to (not including) the focus month, and then adding the days
            # ASSUMPTION: not a leap year
            DayVal = sum(daysInEachMonth[:user_FocusMonth - 1]) + user_FocusDay

        # If it didn't work, reset everything to None and tell them to try again
        except ValueError:
            user_FocusMonth = None
            user_FocusDay = None
            DayVal = None
            print("The month and day must be entered in a readable format (e.g. 'aug' or '8' for month, day must be a number 1-31).  Please try again!\n")
    
    # DayOfFocus - human readable date string for the output
    DayOfFocus = monthNames[user_FocusMonth - 1] + " " + str(user_FocusDay)

    ### return all the inputs for a single location ###
    return user_Latitude, user_Longitude, city_name, building_height, building_distance, DayOfFocus, DayVal


def getUserInputs ():
    '''Get inputs for as many apartments as the user wants, using the "getInputForAnApartment" function.
    Also ask them if they want a .gbd and if they do, get the necessary information for it'''

    ### Get all the values for the locations ###
    # Empty lists to hold the inputs
    latitude_list = []
    longitude_list = []
    city_name_list = []
    building_height_list = []
    building_distance_list = []
    DayOfFocus_list = []
    DayVal_list = []

    # Get inputs for apartments until they decide to stop entering values
    while (True):
        # Get inputs for an apartment
        user_Latitude, user_Longitude, city_name, building_height, building_distance, DayOfFocus, DayVal = getInputForAnApartment()
        latitude_list.append(user_Latitude)
        longitude_list.append(user_Longitude)
        city_name_list.append(city_name)
        building_height_list.append(building_height)
        building_distance_list.append(building_distance)
        DayOfFocus_list.append(DayOfFocus)
        DayVal_list.append(DayVal)

        # Let them break the loop if they want, or keep going
        end = input("Do you want to stop entering values (Y/N)? ") 
        print()
        if end.upper() == 'Y' :
            break


    ### get .gbd options ###
    # default values
    user_wants_gbd = False
    user_GISProjectPath = ""
    user_GISProjectName = ""
    user_GISMapName = ""
    user_FeatureName = ""

    # Ask user if they want the .gbd
    wants_gdb_input = input("Would you like to export the results as a .gdb? Yes or No: ")
    
    # If they want it, set user_wants_gdb to true and ask them for all the details
    if wants_gdb_input.lower() == "yes" or wants_gdb_input.lower() == "y" :
        user_wants_gbd = True

        user_GISProjectPath = input("Enter the project path: ")
        user_GISProjectName = input("Enter the project name: ")
        user_GISMapName = input("Enter the project map name: ")
        user_FeatureName = input("Enter the project feature name: ")

        print("A .gdb file will be generated")
    
    # If they don't want it, leave the default (blank) values
    else:
        print("A .gbd file will not be generated")

    return user_wants_gbd, user_GISProjectPath, user_GISProjectName, user_GISMapName, user_FeatureName, DayOfFocus_list, DayVal_list, latitude_list, longitude_list, city_name_list, building_height_list, building_distance_list
    

def displayResultsForAnApartment (user_Latitude, user_Longitude, city_name, DayOfFocus, FocusDay_MinimumHeight, SummSolstice_MinimumHeight, WintSolstice_MinimumHeight, FocusDay_SunlightHours, SummSolstice_SunlightHours, WintSolstice_SunlightHours):
    '''Output the results for an apartment in three parts: The apartment info, minimum height results, and hours of sunlight results'''
    print("\n------------------------------------------------------------------------------------------------------------")

    # First part - apartment info
    print("\nThe results for the prospective apartment are as follows:")
    print("    Latitude:       ", user_Latitude)
    print("    Longitude:      ", user_Longitude)
    print("    City:           ", city_name)
    print("    Date:           ", DayOfFocus)

    # Second part - minimum height results
    print("\nTo get at least 1 hour of sunlight, the minimum height (in meters) of the prospective apartment must be:")
    print("    On your chosen date:         ", FocusDay_MinimumHeight)
    print("    On the winter solstice:      ", WintSolstice_MinimumHeight)
    print("    On the summer solstice:      ", SummSolstice_MinimumHeight)

    # Third part - hours of sunlight results
    print("\nThe potential hours of sunlight for " + city_name + " is:")
    print("    On your chosen date:         ", FocusDay_SunlightHours)
    print("    On the winter solstice:      ", WintSolstice_SunlightHours)
    print("    On the summer solstice:      ", SummSolstice_SunlightHours)


def displayResults (latitude_list, longitude_list, city_name_list, DayOfFocus_list, FocusDay_MinimumHeight_list, SummSolstice_MinimumHeight_list, WintSolstice_MinimumHeight_list, FocusDay_SunlightHours_list, SummSolstice_SunlightHours_list, WintSolstice_SunlightHours_list):
    '''Display the results for a list of apartments, by repeatedly using the "displayResultsForAnApartment" function'''
    for (user_Latitude, user_Longitude, city_name, DayOfFocus, FocusDay_MinimumHeight, SummSolstice_MinimumHeight, WintSolstice_MinimumHeight, FocusDay_SunlightHours, SummSolstice_SunlightHours, WintSolstice_SunlightHours) in zip(latitude_list, longitude_list, city_name_list, DayOfFocus_list, FocusDay_MinimumHeight_list, SummSolstice_MinimumHeight_list, WintSolstice_MinimumHeight_list, FocusDay_SunlightHours_list, SummSolstice_SunlightHours_list, WintSolstice_SunlightHours_list):
        displayResultsForAnApartment(user_Latitude, user_Longitude, city_name, DayOfFocus, FocusDay_MinimumHeight, SummSolstice_MinimumHeight, WintSolstice_MinimumHeight, FocusDay_SunlightHours, SummSolstice_SunlightHours, WintSolstice_SunlightHours)
        
    print("\n------------------------------------------------------------------------------------------------------------\n")
    

### This is just for testing. When the file is imported this code will not run ###
if __name__ == "__main__":
    print(startMessage)
    user_wants_gbd, user_GISProjectPath, user_GISProjectName, user_GISMapName, user_FeatureName, DayOfFocus_list, DayVal_list, latitude_list, longitude_list, city_name_list, building_height_list, building_distance_list = getUserInputs()

    print("\n")
    print("DayOfFocus is: ", DayOfFocus_list)
    print("DayVal_list is: ", DayVal_list)
    print("latitude_list is: ", latitude_list)
    print("longitude_list is: ", longitude_list)
    print("city_name_list is: ", city_name_list)
    print("building_height_list is: ", building_height_list)
    print("building_distance_list is: ", building_distance_list)

    print("\n.gbd settings:")
    print("user_wants_gbd is: ", user_wants_gbd)
    print("user_GISProjectPath is: ", user_GISProjectPath)
    print("user_GISProjectName is: ", user_GISProjectName)
    print("user_GISMapName is: ", user_GISMapName)
    print("user_FeatureName is: ", user_FeatureName)
