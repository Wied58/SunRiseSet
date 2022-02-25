from datetime import datetime
from pysolar.solar import * 
import pytz


latitude = 42.0572
longitude = 87.812985



for hour in range(1, 24):


   without_timezone = datetime.datetime(2022, 2, 6, hour, 00, 00, 0)
   timezone = pytz.timezone("UTC")
   with_timezone = timezone.localize(without_timezone)
   print(with_timezone)


   #print(get_azimuth(latitude, longitude, with_timezone))
   print(get_altitude(latitude, longitude, with_timezone))
   print()
