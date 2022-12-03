#import cities
cities = {"calgary": [1,1]}  # placeholder for when we have the actual list of city coordinates imported

startMessage = """POTENTIAL SUNLIGHT EXPOSURE CALCULATOR FOR APARTMENT HUNTERS

This program will calculate statistical data about potential sunlight for a city/ area in Canada, based off spatial data, as well as the optical height (floor) of a dwelling (apartment).
This will aid apartment hunters in preventing selecting an apartment with less/ no sunlight exposure due to other buildings.
"""

def getUserInputs ():
    '''This function prompts the user to enter various pieces of information, and returns the inputs that the program needs:
    
    user_FocusMonth
    user_FocusDay             
    user_GISProjectPath       
    user_GISProjectName       
    user_GISMapName           
    user_FeatureName           
    DayVal                    
    user_Latitude             
    user_Longitude            
    City_Name        
    building_height
    building_distance         
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

    while (user_Latitude is None or user_Longitude is None):
        locationType = input("Would you like to select from a list of Canadian cities, or provide the latitude/longitude coordinates? (city/coords): ")
        if locationType == "coords":
            user_Latitude, user_Longitude = getLatLong()

        elif locationType == "city":
            province = input("Please enter the Canadian province/territory the prospective apartment is located in: ")
            city_name = input("Please enter the Canadian city the prospective apartment is located in: ")
            city_name = city_name.lower()  # make the city name lowercase because the list of cities is lowercase
            if city_name not in cities.keys():
                print("That city isn’t in the system")
                user_Latitude, user_Longitude = getLatLong()

            else:
                user_Latitude = cities[city_name][0]
                user_Longitude = cities[city_name][1]

        else:
            print("Please reply with 'city' or 'coords' to decide how to input the location\n")


    ### Get other building data ###
    askUserForInput = True
    while(askUserForInput):
        building_height = input("Please enter the height of the closest south facing adjacent building, in meters: ")
        building_distance = input("Please enter the distance between the two buildings in meters: ")

        try:
            building_height = float(building_height)
            building_distance = float(building_distance)
            # If the two lines above are successful, the values are now numbers and we don't need to ask again for input
            askUserForInput = False
        except ValueError:
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

    
    ### return all the inputs ###
    return DayOfFocus, DayVal, user_FocusDay, user_wants_gbd, user_GISProjectPath, user_GISProjectName, user_GISMapName, user_FeatureName, user_Latitude, user_Longitude, city_name, building_height, building_distance


### This is just for testing. When the file is imported this code will not run ###
if __name__ == "__main__":
    print(startMessage)
    DayOfFocus, DayVal, user_FocusDay, user_wants_gbd, user_GISProjectPath, user_GISProjectName, user_GISMapName, user_FeatureName, user_Latitude, user_Longitude, city_name, building_height, building_distance = getUserInputs()

    print("\n")
    print("DayOfFocus is: ", DayOfFocus)
    print("DayVal is: ", DayVal)
    print("user_FocusDay is: ", user_FocusDay)
    print("user_wants_gbd is: ", user_wants_gbd)
    print("user_GISProjectPath is: ", user_GISProjectPath)
    print("user_GISProjectName is: ", user_GISProjectName)
    print("user_GISMapName is: ", user_GISMapName)
    print("user_FeatureName is: ", user_FeatureName)
    print("user_Latitude is: ", user_Latitude)
    print("user_Longitude is: ", user_Longitude)
    print("city_name is: ", city_name)
    print("building_height is: ", building_height)
    print("building_distance is: ", building_distance)
