from datetime import datetime
from datetime import timedelta
from pysolar.solar import * 
import pytz
#import GPSFix
import sys
sys.path.insert(0, '/home/pi/Tools/FetchGPS')
import FetchGPS


#latitude = 42.0572
#longitude = -87.812985

latitude = FetchGPS.GPSLat
longitude = FetchGPS.GPSLong


now = datetime.datetime.now(pytz.timezone('UTC'))

angle = get_altitude(latitude, longitude, now)

with open('/home/pi/Tools/SunRiseSet/SunRiseSet.txt', 'w') as f:

     f.write(f"The current time is: {now}, and the sun angle is: {angle}\n")
     #print(f"The current time is: {now}, and the sun angle is: {angle}")
     #print()
     
     if angle < -12:
     
        current_conditions = 'dark'
     
     else:
     
       current_conditions = 'daylight' 
     
     f.write(f"Current Conditions: {current_conditions}\n")
     #print(f"Current Conditions: {current_conditions}")
     #print()
     
     we_know_the_next_sunrise = False
     we_know_the_next_sunset = False
     
     start_date = now
     end_date = now + timedelta(days=1.5)
     delta = datetime.timedelta(minutes=5)
     
     while start_date <= end_date:
     
         angle = get_altitude(latitude, longitude, start_date)
     
         if current_conditions == 'dark':
            # fetch sunrise
            if angle > -12 and we_know_the_next_sunrise == False:
               next_sunrise = start_date
               we_know_the_next_sunrise = True
               f.write(f"The next nautical sunrise occurs at: {next_sunrise}\n") 
               #print(f"The next nautical sunrise occurs at: {next_sunrise}") 
               #print()
     
            # fetch_sunset
            if angle < -12 and we_know_the_next_sunrise == True and we_know_the_next_sunset == False:
               next_sunset = start_date
               we_know_the_next_sunset = True
               f.write(f"The next nautical sunset occurs at: {next_sunset}\n")
               #print(f"The next nautical sunset occurs at: {next_sunset}")
               #print()
               break
     
         if current_conditions == 'daylight':
            # fetch sunset
            if angle < -12 and we_know_the_next_sunset == False:
               next_sunset = start_date
               we_know_the_next_sunset = True
               f.write(f"The next nautical sunset occurs at: {next_sunset}\n") 
               #print(f"The next nautical sunset occurs at: {next_sunset}") 
               #print()
     
            # fetch_sunrise
            if angle > -12 and we_know_the_next_sunset == True and we_know_the_next_sunrise == False:
               next_sunrise = start_date
               we_know_the_next_sunrise = True
               f.write(f"The next nautical sunrise occurs at: {next_sunrise}\n")
               #print(f"The next nautical sunrise occurs at: {next_sunrise}")
               #print()
               break
     
         ##print(start_date, angle)
         start_date += delta
