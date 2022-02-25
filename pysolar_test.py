from datetime import datetime
from pysolar.solar import * 
#import datetime

#latitude = 42.206 
#longitude = -87.382
latitude = 42.0572
longitude = 87.812985

#date = datetime.datetime(2020, 2, 18, 5, 13, 1, 130320, tzinfo=datetime.timezone.utc) 
date = datetime.datetime(2020, 2, 18, 5, 13, 1, tzinfo=datetime.timezone.utc) 
print(date)


print(get_altitude(latitude, longitude, date))
print(get_azimuth(latitude, longitude, date))

#now = datetime.datetime.now()
#print(now)
#current_time = now.strftime("%Y-%m-%d:%H:%M:%S")
#print(current_time)
#
#print(get_altitude(latitude, longitude, current_time))
#print(get_azimuth(latitude, longitude, current_time))
