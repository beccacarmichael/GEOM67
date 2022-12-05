import math

#this provides Sunlight Hours for 1 day

def SunlightCalculator(DayVal,user_Latitude):

    HoursofSunlight = 2*((1/15)*(180/math.pi)*(math.acos(((math.pi/180)*(-math.tan(float(user_Latitude)*(math.pi/180))*((math.tan(((23.44*(math.pi/180))*((math.sin(((360/365)*(math.pi/180)*(DayVal+284))))))))))))))
    HoursofSunlight = round(float(HoursofSunlight),2)

    return HoursofSunlight

print('this is a day of focus test', SunlightCalculator(32,70))


# DayVal = 32
# user_Latitude = 70
# result = SunlightCalculator(DayVal, user_Latitude)
# print(result)