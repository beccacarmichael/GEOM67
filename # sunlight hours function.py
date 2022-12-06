# sunlight hours function
import math


user_latitude = 43.6


def sunlighthourstatistics (user_Latitude):

    #dayVal = 1   
        
    CalculationsList=[]
    for d in range(1,365):
        sunlighthour=2*(1/15)*(180/math.pi)*math.acos((-math.tan((math.pi/180)*user_Latitude))*(math.tan((math.pi/180)*23.44*math.sin((360/365)*(d+284)*(math.pi/180)))))
        sunlighthour=round(float(sunlighthour),2)
        CalculationsList.append(sunlighthour)

    #min,max,avg,sum
    minhour=min(CalculationsList)
    maxhour=max(CalculationsList)
    avghour=sum(CalculationsList)/len(CalculationsList)
    sumhour=sum(CalculationsList)

    return minhour,maxhour,avghour,sumhour

print("sum is",sunlighthourstatistics(76,1))


