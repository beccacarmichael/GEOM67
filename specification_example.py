print("""POTENTIAL SUNLIGHT EXPOSURE CALCULATOR FOR APARTMENT HUNTERS

This program will calculate statistical data about potential sunlight for a city/ area in Canada, based off spatial data, as well as the optical height (floor)  Toroof a dwelling (apartment). This will aid apartment hunters in preventing selecting an apartment with less/ no sunlight exposure due to other buildings.
""")

print("Part 1: Calculating Apartment Height")
input("Please enter the Canadian city the perspective apartment is located in: ") 
input("Please enter the neighbouring building’s height in meters: ")
input("Please enter the distance between buildings in meters: ")
input("Please enter the day of the year you would like to calculate sunlight exposure on.  The day must be entered in the Day – of Year (DOY) numbering system, meaning January 1 will be 1 and December 31 will be 365. It is recommended you first calculate the sunlight exposure on the summer solstice (most sunlight exposure) day 172 (June 21) or the winter solstice (the least sunlight exposure) day 355 (December 21). ")

print("The calculated height for the apartment given is:  <calculated height>")

print("\nPart 2: Calculating Possible Sunlight Hours at the perspective apartment. ")
print("In that city, there are <calculated number of hours> possible hours of sunlight at the perspective apartment")
