import datetime
#print current datetime
cur_datetime=datetime.datetime.now()
print("Current datetime:",cur_datetime)

#convert string int datetime object
str="Feb 25 2020 4:20PM"
str_1=datetime.datetime.strptime(str,"%b %d %Y %I:%M%p")
print(str_1)

#subtract a week from given date
given_date=datetime.datetime(2023,2,25)
time_delta=datetime.timedelta(days=7)
print("New_date:",given_date-time_delta)

#print date following format: Tuesday 25 February 2020
give_date=datetime.datetime(2023,2,25)
res_date=give_date.strftime("%A %d %B %Y")
print(res_date)

#find the day of week of given date
give=datetime.datetime(2020,7,26)
print(give.strftime("%A"))

#Add a week(7days) and 12 hours to given date
user=datetime.datetime(2023,3,22,10,0,0)
time_delta1=datetime.timedelta(days=7,hours=12)
res=user+time_delta1
print(res.strftime("%Y-%m-%d %I:%M:%S"))

#print current time in milliseconds
import time
milli=int(round(time.time()*1000))
print(milli)

#Convert datetime into string
g=datetime.datetime(2023,2,25)
f=g.strftime("%Y-%m-%d %H:%M:%S")
print(f)

#calculate the date 4 months from current date
c=datetime.datetime.now()
td=datetime.timedelta(4*365/12)
r=c+td
print(r.strftime("%Y-%m-%d"))

#Calculate number of days between two given date
g1=datetime.datetime(2023,2,25).date()
g2=datetime.datetime(2023,9,17).date()
if g1>g2:
    delta=g1-g2
else:
    delta=g2-g1
print(delta.days)

