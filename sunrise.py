#!/usr/bin/python3

import datetime
from suntime import Sun, SunTimeException
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

print(now)

latitude = 42.0572
longitude = 87.812985

sun = Sun(latitude, longitude)

# Get today's sunrise and sunset in UTC


#f= open("/home/pi/sunrise_set/srss.txt","a+")



now = datetime.now()

current_time = now.strftime("%H:%M:%S")


today_sr = sun.get_sunrise_time()
today_ss = sun.get_sunset_time()

print("Current Time =", current_time, end = " ")
print('Today at Jeffs the sun rose at {} and set at {} UTC'.
      format(today_sr.strftime('%H:%M'), today_ss.strftime('%H:%M')))

f.write("Current Time = ")
f.write(current_time)
f.write(" Sunrise time = ")
f.write(str(today_sr))
f.write(" Sunset time = ")
f.write(str(today_ss))
f.write("\n")

f.close()
