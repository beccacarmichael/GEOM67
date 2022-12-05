# sunlight hours function
import math

def sunlighthour ():
    latitude = 76
    dayVal = 1
    summaryhour=input("do you want to get the summary of sunlighthour in a year of your chosen city?y/n: ")
    if summaryhour== "y":
        
        CalculationsList=[]
        for d in range(1,366,dayVal):
            #this is the sunlight hour calculation
            sunlighthour=2*((1/15)*(180/math.pi)*(math.acos(((math.pi/180)*(-math.tan(float(latitude)*(math.pi/180))*((math.tan(((23.44*(math.pi/180))*((math.sin(((360/365)*(math.pi/180)*(d+284))))))))))))))
            sunlighthour=round(float(sunlighthour),2)
            CalculationsList.append(sunlighthour)
        print(CalculationsList)

        #min,max,avg,sum
        minhour=min(CalculationsList)
        maxhour=max(CalculationsList)
        avghour=sum(CalculationsList)/len(CalculationsList)
        sumhour=sum(CalculationsList)

        print("sum is",sumhour,"min hour is",minhour,"max hour is", maxhour, "avg hour is", avghour)


