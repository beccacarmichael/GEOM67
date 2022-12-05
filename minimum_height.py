import math


#this is to get your minimum appartment height

def minimumheight():

    #placeholder values
    user_latitude = 71
    building_distance = 25
    building_height = 25
    DayVal = 1


    #declination angle calculation
    FocusDay_DeclinationAngle=-23.45*math.cos((math.pi/180)*(360/365)*(DayVal+10))
    #elevation angle calculation
    ElevationAngle=90-float(user_latitude)+float(FocusDay_DeclinationAngle)
    #MinimumHeight calculation
    minimumheight=building_height-(math.tan((math.pi/180)*ElevationAngle))*building_distance
    #Rounding Final Answer
    minimumheight=round(minimumheight,2)

   #still need it for winterSol_minHeight, Summsol_MinHeight
