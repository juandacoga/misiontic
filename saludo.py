from datetime import datetime, date, time, timedelta
import calendar

now = datetime.now()


if(now.hour >= 6 and now.hour < 12):
    print('Buenos días')
elif(now.hour >= 12 and now.hour < 18):
    print('Buenas tardes')
else:
    print('Buenas noches')