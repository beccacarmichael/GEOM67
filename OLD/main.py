###################Main Program ##########################
#ApartmentSeekerSunlightCalculator.py
#Lead: Becca 
#Support: Adrian Koornneef
#Notes: This section imports and executes the various necessary parts of the program. 
#For additional program notes, see the readme file
#########################################################


SummSolstice_DayVal = 172
WintSolstice_DayVal = 355

# Print start message to welcome user to program
print(becca_userInterface.startMessage)

# Get all the input data
user_wants_gbd, user_GISProjectPath, user_GISProjectName, user_GISMapName, user_FeatureName, DayOfFocus_list, DayVal_list, latitude_list, longitude_list, city_name_list, building_height_list, building_distance_list = becca_userInterface.getUserInputs()

# Empty lists to hold all the results
FocusDay_MinimumHeight_list = []
SummSolstice_MinimumHeight_list = []
WintSolstice_MinimumHeight_list = []
FocusDay_SunlightHours_list = []
SummSolstice_SunlightHours_list = []
WintSolstice_SunlightHours_list = []

# Loop through all the info for each apartment and calculate the results
for (DayOfFocus, DayVal, latitude, longitude, city_name, building_height, building_distance) in zip(DayOfFocus_list, DayVal_list, latitude_list, longitude_list, city_name_list, building_height_list, building_distance_list):
    # Minimum height calculations for the apartment
    FocusDay_MinimumHeight = calculations.calculateApartmentHeight(DayVal, latitude, building_height, building_distance)
    SummSolstice_MinimumHeight = calculations.calculateApartmentHeight(SummSolstice_DayVal, latitude, building_height, building_distance)
    WintSolstice_MinimumHeight = calculations.calculateApartmentHeight(WintSolstice_DayVal, latitude, building_height, building_distance)

    # Sunlight hours calculations for the apartment
    FocusDay_SunlightHours = calculations.calculateSunlightHours(DayVal, latitude, longitude)
    SummSolstice_SunlightHours = calculations.calculateSunlightHours(SummSolstice_DayVal, latitude, longitude)
    WintSolstice_SunlightHours = calculations.calculateSunlightHours(WintSolstice_DayVal, latitude, longitude)

    # Append results for the apartment to the lists of results
    FocusDay_MinimumHeight_list.append(FocusDay_MinimumHeight)
    SummSolstice_MinimumHeight_list.append(SummSolstice_MinimumHeight)
    WintSolstice_MinimumHeight_list.append(WintSolstice_MinimumHeight)
    FocusDay_SunlightHours_list.append(FocusDay_SunlightHours)
    SummSolstice_SunlightHours_list.append(SummSolstice_SunlightHours)
    WintSolstice_SunlightHours_list.append(WintSolstice_SunlightHours)

# Save the results in a csv
# YJ_OutputTable.saveCSV(FocusDay_MinimumHeight, SummSolstice_MinimumHeight, WintSolstice_MinimumHeight, FocusDay_SunlightHours, SummSolstice_SunlightHours, WintSolstice_SunlightHours)

# Use the csv to generate a .gdb
# ArcPyScript()

# Display the results to the user
becca_userInterface.displayResults(latitude_list, longitude_list, city_name_list, DayOfFocus_list, FocusDay_MinimumHeight_list, SummSolstice_MinimumHeight_list, WintSolstice_MinimumHeight_list, FocusDay_SunlightHours_list, SummSolstice_SunlightHours_list, WintSolstice_SunlightHours_list)

print()
print("-----------------------------------------------------------------------------------------")
print("Program complete. Please run again if you wish to complete for another location.")