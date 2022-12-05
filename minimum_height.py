import math


#this is to get your minimum appartment height

def minimumheight(user_Latitude,building_distance,building_height,DayVal):

    # test values
    # user_latitude = 71
    # building_distance = 25
    # building_height = 25
    # DayVal = 1
    
    FocusDay_DeclinationAngle=-23.45*math.cos((math.pi/180)*(360/365)*(DayVal+10)) #declination angle calculation    
    ElevationAngle=90-float(user_Latitude)+float(FocusDay_DeclinationAngle) #elevation angle calculation    
    minimumheight=building_height-(math.tan((math.pi/180)*ElevationAngle))*building_distance #MinimumHeight calculation
    minimumheight=round(minimumheight,2) #Rounding Final Answer

    return minimumheight

print('This is a test of minimum height', minimumheight(71,25,25,1))

   #still need it for winterSol_minHeight, Summsol_MinHeight
