import math

def SunlightCalculator():
    DayVal = 1
    user_Latitude = 21

    HoursofSunlight = 2*((1/15)*(180/math.pi)*(math.acos(((math.pi/180)*(-math.tan(float(user_Latitude)*(math.pi/180))*((math.tan(((23.44*(math.pi/180))*((math.sin(((360/365)*(math.pi/180)*(DayVal+284))))))))))))))
    HoursofSunlight = round(float(HoursofSunlight),2)
