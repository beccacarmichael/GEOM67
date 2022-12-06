import math
import csv
with open("latlong.csv", newline="")as fo:
    freader=list(csv.reader(fo))
    # print(len(freader))
    cityn=input("enter cityn: ")
    cityn=cityn.upper()  
    flag=True
      
    for row in freader:
        if cityn in row:
            flag=False
            latitude=row[1]
            longi=row[2]
            print(latitude, longi)
            break
    if flag:
        latitude=input("enter lat: ")
        longi=input("long: ")
        print(latitude, longi)

adjacentbuildingheight=30 # will change to input later, now just for convinience 
buildingdistance=20
eachlevelheight=3
#latitude=40

day=int(input("enter a day, Jan1-->day=1: "))

declinationangle=-23.45*math.cos((math.pi/180)*(360/365)*(day+10))
elevationangle=90-float(latitude)+float(declinationangle)
minimumheight=adjacentbuildingheight-(math.tan((math.pi/180)*elevationangle))*buildingdistance
minimumheight=round(minimumheight,2)

#print("minimum height to receive sunlight in ",cityn, "is ", minimumheight)



summaryhour=input("do you want to get the summary of sunlighthour in a year of your chosen city?y/n: ")
if summaryhour== "y":
    
    alist=[]
    for d in range(1,366,100): #set to 100 for now, change later
        sunlighthour=(1/15)*(180/math.pi)*(math.acos(((math.pi/180)*(-math.tan(float(latitude)*(math.pi/180))*((math.tan(((23.44*(math.pi/180))*((math.sin(((360/365)*(math.pi/180)*(d+284)))))))))))))
        sunlighthour=round(float(sunlighthour),2)
        alist.append(sunlighthour)
    print(alist)
    sumhour=sum(alist)
    minhour=min(alist)
    maxhour=max(alist)
    avghour=sum(alist)/len(alist)

    print("sum is",sumhour,"min hour is",minhour,"max hour is", maxhour, "avg hour is", avghour)

