# sunlight hours function
import math

def sunlighthourstatistics (user_Latitude):

    #latitude = 43
    #dayVal = 1   
        
    CalculationsList=[]
    for d in range(1,365):
        sunlighthour=2*(1/15)*(180/math.pi)*math.acos((-math.tan((math.pi/180)*43.6))*(math.tan((math.pi/180)*23.44*math.sin((360/365)*(d+284)*(math.pi/180)))))
        sunlighthour=round(float(sunlighthour),2)
        CalculationsList.append(sunlighthour)

    #min,max,avg,sum
    minhour=min(CalculationsList)
    maxhour=max(CalculationsList)
    avghour=round(sum(CalculationsList)/len(CalculationsList),2)
    sumhour=round(sum(CalculationsList),2)

    return minhour,maxhour,avghour,sumhour

print("Minimum Sunlight is",sunlighthourstatistics(43)[0])
print("Maximum Sunlight is",sunlighthourstatistics(43)[1])
print("Average Sunlight is",sunlighthourstatistics(43)[2])
print("Total Yearly Hours of Sunlight",sunlighthourstatistics(43)[3])



