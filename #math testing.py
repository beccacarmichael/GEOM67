#math testing
import math

latitude = 43

# attempt 1, values are not correct

summaryhour=input("do you want to get the summary of sunlighthour in a year of your chosen city?y/n: ")
if summaryhour== "y":
    
    alist=[]
    for d in range(1,365):
        sunlighthour=(1/15)*(180/math.pi)*(math.acos(((math.pi/180)*(math.tan(float(latitude)*(math.pi/180))*((math.tan(((23.44*(math.pi/180))*((math.sin(((360*(d+284)/365*(math.pi/180))))))))))))))
        sunlighthour=round(float(sunlighthour),2)
        alist.append(sunlighthour)
    print(alist)
    sumhour=sum(alist)
    minhour=min(alist)
    maxhour=max(alist)
    avghour=sum(alist)/len(alist)

    print("sum is",sumhour,"min hour is",minhour,"max hour is", maxhour, "avg hour is", avghour)






# ## ATTEMPT 2, breaking it down, not working at all, int error




# summaryhour=input("do you want to get the summary of sunlighthour in a year of your chosen city?y/n: ")
# if summaryhour== "y":
    
#     alist=[]
#     for d in range(1,366,190): #set to 100 for now, change later
#         calculation1 = math.sin((math.pi/180)(360(d+284)/365))
#         # calculation2 = calculation1 * math.tan((math.pi/180)*(23.44))
#         # calculation3 = math.acos(math.radians(calculation2))
#         # calulation4 = -math.tan((math.pi/180)*(latitude)) * -1
#         # sunlighthour = (1/15) * calculation3
#         # sunlighthour = round(float(sunlighthour),2)
#         # (1/15)*(180/math.pi)*(math.acos(((math.pi/180)*(-math.tan((math.pi/180)*(latitude))*((math.tan((math.pi/180)*(23.44))*((math.sin((math.pi/180)*(360(d+284)/365))))))))))
#     sumhour=sum(alist)
#     minhour=min(alist)
#     maxhour=max(alist)
#     avghour=sum(alist)/len(alist)


    

    print("sum is",sumhour,"min hour is",minhour,"max hour is", maxhour, "avg hour is", avghour)


#(1/15)*(180/math.pi)*(math.acos(((math.pi/180)*(-math.tan(float(latitude)*(math.pi/180))*((math.tan(((23.44*(math.pi/180))*((math.sin((((360/365)*(math.pi/180))*(d+284)))))))))))))

# (1/15) * math.acos(math.radians(math.tan * latitude) * math.sin(math.radians(360(d+284)/365))) newest
# calculation1 = math.sin(math.radians(360(d+284)/365))
#         calculation2 = calculation1 * math.tan(math.radians(23.44))
#         calculation3 = math.acos(math.radians(calculation2    ))
#         calulation4 = -math.tan(math.radians(latitude)) * -1
#         sunlighthour = (1/15) * calculation3
#         sunlighthour = round(float(sunlighthour),2)


# (1/15)  *   math.acos(-math.tan(math.radians(float(latitude)))*(math.tan(23.44*math.sin(math.radians(360(d+284)/365)))

# calculation1 = math.sin(math.radians(360(d+284)/365))
# calculation2 = calculation1 * math.tan(math.radians(23.44))
# calculation3 = math.acos(math.radians(calculation2))
# sunlighthour = (1/15) * calculation3
# sunlighthour = round(float(sunlighthour),2)
# alist.append(sunlighthour)