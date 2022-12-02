import csv
################### OUTPUT TABLE MODULE ###################
#EXPORT relevant variables as individual columns in a single row, with headers, in a.csv
################### OUTPUT TABLE MODULE ###################
def main():
    cityname_list=[] #create empty list for each entry
    latitude_list=[]
    longitude_list=[]
    # DayOfFocus=[]
    # DayOfFocusHeight=[]
    # DayofFocusHour=[]
    # WinterHeight=[]
    # SummerHeight=[]
    # AnnualTotalSunlightHour=[]
    # AnnualAvgSunlightHour=[]
    # AnnualMinHour=[]
    # AnnualMaxHour=[]


    while True:
        City_Name=input("enter cityn: ")
        City_Name=City_Name.upper()  # upper case input, match the cityname in the csv file
        cityname_list.append(City_Name)  # append user input to cityname list
        with open("latlong.csv", newline="")as fo:
            freader=list(csv.reader(fo)) # read the file into a big list
            flag=True
            for row in freader: # for small list in big list
                if City_Name in row: # if cityname is found in the small list [cityname,latitude,longitude]
                    flag=False
                    user_Latitude=row[1] #latitude would be at position [1]
                    latitude_list.append(user_Latitude) #append latitude to latitude list
                    user_Longitude=row[2] #longitude would be at position [2]
                    longitude_list.append(user_Longitude) #append longitude to longitude list
                    break

            if flag:
                user_Latitude=input("not found, enter lat: ") # if cityname is not found in the small list, ask for input manually
                latitude_list.append(user_Latitude) #append input_latitude to latitude list
                user_Longitude=input("not found, enter long: ")
                longitude_list.append(user_Longitude)#append input_longitude to longitude list
    
            #print(cityname,latitude,longitude)
        end = input("Do you want to stop entering values (Y/N)? ") 
        print()
        if  end.upper() == 'Y' :
            break

    alist=zip(cityname_list,latitude_list,longitude_list) # combine small lists into a big list
    myheader=['City_Name','Latitude','Longitude','DayOfFocus','DayOfFocusHeight','DayofFocusHour','WinterHeight','SummerHeight','AnnualTotalSunlightHour','AnnualAvgSunlightHour','AnnualMinHour','AnnualMaxHour']
    with open('output.csv','w',newline='') as newfile: #csv file name can be changed later, when we finalize it
        writer=csv.writer(newfile)
        writer.writerow(myheader)
        writer.writerows(alist)

if __name__ == '__main__':
    main()
