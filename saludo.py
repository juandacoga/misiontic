from datetime import datetime, date, time, timedelta
import calendar

now = datetime.now()


if(now.hour >= 6 and now.hour < 12):
    print('Buenos días')
if(now.hour >= 12 and now.hour < 18):
    print('Buenas tardes')
if(now.hour >= 18 or now.hour < 6):
    print('Buenas noches')