cities = {"calgary": [1,1]}  # placeholder for when we have the actual list of city coordinates imported
monthNumbers = {
    "JAN": 0,
    "FEB": 1,
    "MAR": 2,
    "APR": 3,
    "MAY": 4,
    "JUN": 5,
    "JUL": 6,
    "AUG": 7,
    "SEP": 8,
    "OCT": 9,
    "NOV": 10,
    "DEC": 11
}


print("""POTENTIAL SUNLIGHT EXPOSURE CALCULATOR FOR APARTMENT HUNTERS

This program will calculate statistical data about potential sunlight for a city/ area in Canada, based off spatial data, as well as the optical height (floor) of a dwelling (apartment). This will aid apartment hunters in preventing selecting an apartment with less/ no sunlight exposure due to other buildings.
""")

print("Please answer the following questions with information regarding the prospective apartment:")


print("Part 1: Calculating Apartment Height")

# Get location
user_latitude = None
user_longitude = None
while (user_latitude is None or user_longitude is None):
    locationType = input("Would you like to select from a list of Canadian cities, or provide the latitude/longitude coordinates? (city/coords): ")
    if locationType == "coords":
        user_latitude = input("Please enter the decimal latitude: ")
        user_longitude = input("Please enter the decimal longitude: ")

    elif locationType == "city":
        province = input("Please enter the Canadian province/territory the prospective apartment is located in: ")
        city_name = input("Please enter the Canadian city the prospective apartment is located in: ")
        if city_name not in cities.keys():
            print("That city isn’t in the system")
            user_latitude = input("Please enter the decimal latitude: ")
            user_longitude = input("Please enter the decimal longitude: ")
        else:
            user_latitude = cities[city_name][0]
            user_longitude = cities[city_name][1]

    else:
        print("Please reply with 'city' or 'coords' to decide how to input the location\n")


# Get other building
building_height = input("Please enter the height of the closest south facing adjacent building, in meters: ")
building_distance = input("Please enter the distance between the two buildings in meters: ")


# Options for results
date = input("Please enter the month and day of year you would like to calculate sunlight exposure for. Please enter this information in the following format - JAN 01, FEB 02, etc.: ")
try:
    user_FocusMonth = monthNumbers[date.split(" ")[0].upper()]
    user_FocusDay = int(date.split(" ")[1])
except Exception as e:
    print(e)
    # TODO handle this and let the user try the entry again
print("Would you like to export the results as a .gdb? Yes or No: ")



print("The calculated height for the apartment given is:  <calculated height>")

print("\nPart 2: Calculating Possible Sunlight Hours at the perspective apartment. ")
print("In that city, there are <calculated number of hours> possible hours of sunlight at the perspective apartment")




