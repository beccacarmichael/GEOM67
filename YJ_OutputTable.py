import csv
################### OUTPUT TABLE MODULE ###################
#EXPORT relevant variables as individual columns in a single row, with headers, in a.csv
################### OUTPUT TABLE MODULE ###################
def main():
    cityname=[] #create empty list for each entry
    latitude=[]
    longitude=[]
    # DayOfFocus=[]
    # DayOfFocusHeight=[]
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
                    latitude.append(filelatitude) #append latitude to latitude list
                    filelongi=row[2] #longitude would be at position [2]
                    longitude.append(filelongi) #append longitude to longitude list
                    break

            if flag:
                input_latitude=input("not found, enter lat: ") # if cityname is not found in the small list, ask for input manually
                latitude.append(input_latitude) #append input_latitude to latitude list
                input_longi=input("not found, enter long: ")
                longitude.append(input_longi)#append input_longitude to longitude list
    
            #print(cityname,latitude,longitude)
            end = input("Do you want to stop entering values (Y/N)? ") 
            print()
            if  end.upper() == 'Y' :
                break

    alist=zip(cityname,latitude,longitude) # combine small lists into a big list
    myheader=['CityName','Latitude','Longitude','DayOfFocus','DayOfFocusHeight','DayofFocusHour','WinterHeight','SummerHeight','WinterHeight','AnnualTotalSunlightHour','AnnualAvgSunlightHour','AnnualMinHour','AnnualMaxHour']
    with open('output.csv','w',newline='') as newfile: #csv file name can be changed later, when we finalize it
        writer=csv.writer(newfile)
        writer.writerow(myheader)
        writer.writerows(alist)

if __name__ == '__main__':
    main()
