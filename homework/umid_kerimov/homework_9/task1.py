import datetime

conversion_time = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(conversion_time, '%b %d, %Y - %H:%M:%S')
print(python_date.strftime('%B'))
print(python_date.strftime('%d.%m.%Y, %I:%M'))
