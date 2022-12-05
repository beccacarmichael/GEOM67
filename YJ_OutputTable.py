import csv
################### OUTPUT TABLE MODULE ###################
#EXPORT relevant variables as individual columns in a single row, with headers, in a.csv
################### OUTPUT TABLE MODULE ###################
import math

def bheight(l_titude):
    dayy=int(input("enter day:"))
    buildingdistance=int(input("buulding d: "))
    adjacentbuildingheight=int(input("buildingheight:)"))
    declinationangle=-23.45*math.cos((math.pi/180)*(360/365)*(dayy+10))
    elevationangle=90-l_titude+declinationangle
    minimumheight=adjacentbuildingheight-(math.tan((math.pi/180)*elevationangle))*buildingdistance
    return minimumheight

################### OUTPUT TABLE MODULE ###################
#EXPORT relevant variables as individual columns in a single row, with headers, in a.csv
################### OUTPUT TABLE MODULE ###################
def main():
    cityname=[] #create empty list for each entry
    latitude=[]
    longitude=[]
    # DayOfFocus=[]
    DayOfFocusHeight=[]
    # DayofFocusHour=[]
    # WinterHeight=[]
    # SummerHeight=[]
    # WinterHeight=[]
    # AnnualTotalSunlightHour=[]
    # AnnualAvgSunlightHour=[]
    # AnnualMinHour=[]
    # AnnualMaxHour=[]


    while True:
        cityn=input("enter cityn: ")
        cityn=cityn.upper()  # upper case input, match the cityname in the csv file
        cityname.append(cityn)  # append user input to cityname list
        with open("latlong.csv", newline="")as fo:
            freader=list(csv.reader(fo)) # read the file into a big list
            flag=True
            for row in freader: # for small list in big list
                if cityn in row: # if cityname is found in the small list [cityname,latitude,longitude]
                    flag=False
                    filelatitude=row[1] #latitude would be at position [1]
                    filelatitude=float(filelatitude)
                    latitude.append(filelatitude) #append latitude to latitude list
                    filelongi=row[2] #longitude would be at position [2]
                    filelongi=float(filelongi)
                    longitude.append(filelongi) #append longitude to longitude list
                    break

            if flag:
                filelatitude=float(input("not found, enter lat: ")) # if cityname is not found in the small list, ask for input manually
                latitude.append(filelatitude) #append input_latitude to latitude list
                filelongi=float(input("not found, enter long: "))
                longitude.append(filelongi)#append input_longitude to longitude list
    
            #print(cityname,latitude,longitude)
            for index in range(1):
                filelatitude = latitude[index]        
                mheight=bheight(filelatitude)
                DayOfFocusHeight.append(mheight)  


        end = input("Do you want to stop entering values (Y/N)? ") 
        print()
        if  end.upper() == 'Y' :
            break

    myheader=['CityName','Latitude','Longitude','DayOfFocus','DayOfFocusHeight','DayofFocusHour','WinterHeight','SummerHeight','WinterHeight','AnnualTotalSunlightHour','AnnualAvgSunlightHour','AnnualMinHour','AnnualMaxHour']

    with open('output.csv','w',newline='') as newfile:
        writer=csv.writer(newfile)
        writer.writerow(myheader)
        for i in range(len(latitude)):
            writer.writerow([cityname[i],latitude[i],longitude[i],DayOfFocusHeight[i]])



if __name__ == '__main__':
    main()