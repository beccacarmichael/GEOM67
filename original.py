import math


with open('latlong.txt','r') as f:
    lines=f.readlines()
    city=[]
    lat=[]
    long=[]
    for l in lines:
        alist=l.split()
        city.append(alist[0])
        lat.append(alist[1])
        long.append(alist[2])
    cityn=input("enter cityn: ")
    cityn=cityn.upper()
    for i in range(len(city)):
        if cityn == city[i]:
            latitude=float(lat[i])
            longi=float(long[i])

adjacentbuildingheight=30 # will change to input later, now just for convinience 
buildingdistance=20
eachlevelheight=3
#latitude=40

day=int(input("enter a day, Jan1-->day=1: "))

declinationangle=-23.45*math.cos((math.pi/180)*(360/365)*(day+10))
elevationangle=90-latitude+declinationangle
minimumheight=adjacentbuildingheight-(math.tan((math.pi/180)*elevationangle))*buildingdistance
minimumheight=round(minimumheight,2)

#print("minimum height to receive sunlight in ",cityn, "is ", minimumheight)



summaryhour=input("do you want to get the summary of sunlighthour in a year of your chosen city?y/n: ")
if summaryhour== "y":
    
    alist=[]
    for d in range(1,366,100): #set to 100 for now, change later
        sunlighthour=(1/15)*(180/math.pi)*(math.acos(((math.pi/180)*(-math.tan(latitude*(math.pi/180))*((math.tan(((23.44*(math.pi/180))*((math.sin(((360/365)*(math.pi/180)*(d+284)))))))))))))
        sunlighthour=round(float(sunlighthour),2)
        alist.append(sunlighthour)
    print(alist)
    sumhour=sum(alist)
    minhour=min(alist)
    maxhour=max(alist)
    avghour=sum(alist)/len(alist)

    print("sum is",sumhour,"min hour is",minhour,"max hour is", maxhour, "avg hour is", avghour)
