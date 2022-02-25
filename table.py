#!/usr/bin/python3

# https://web.archive.org/web/20130122033117/http://www.gandraxa.com/length_of_day.xml 



import datetime
from suntime import Sun, SunTimeException
from datetime import datetime, date, timedelta

latitude = 42.0572
longitude = 87.812985

sun = Sun(latitude, longitude)


f= open("/home/pi/sunrise_set/srss.txt","a+")



for day in range(1, 28):
   test = date(2021, 9, day)
   print (test)
   
   today_sr = sun.get_sunrise_time(test)
   today_asr = today_sr - timedelta(hours=1, minutes=45)
   today_ss = sun.get_sunset_time(test)
   today_ass = today_ss + timedelta(hours=1, minutes=45) 

   daylight = today_ss - today_sr 
   print(daylight)

   print('Today at Jeffs the sun rose at {} {} and set at {} {} UTC. '.
         format(today_sr.strftime('%H:%M'), today_asr.strftime('%H:%M'), today_ss.strftime('%H:%M'), today_ass.strftime('%H:%M')))
   
   f.write(" Sunrise time = ")
   f.write(str(today_sr))
   f.write(" Sunset time = ")
   f.write(str(today_ss))
   f.write("\n")
   
f.close()

