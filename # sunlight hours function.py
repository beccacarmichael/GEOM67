# sunlight hours function
import math

def sunlighthourstatistics (user_Latitude):

    #latitude = 76
    #dayVal = 1   
        
    CalculationsList=[]
    for d in range(1,365):
        sunlighthour=2*((1/15)*(180/math.pi)*(math.acos(((math.pi/180)*(-math.tan(float(user_Latitude)*(math.pi/180))*((math.tan(((23.44*(math.pi/180))*((math.sin(((360/365)*(math.pi/180)*(d+284))))))))))))))
        sunlighthour=round(float(sunlighthour),2)
        CalculationsList.append(sunlighthour)

    #min,max,avg,sum
    minhour=min(CalculationsList)
    maxhour=max(CalculationsList)
    avghour=sum(CalculationsList)/len(CalculationsList)
    sumhour=sum(CalculationsList)

    return minhour,maxhour,avghour,sumhour

print("sum is",sunlighthourstatistics(76,1))


