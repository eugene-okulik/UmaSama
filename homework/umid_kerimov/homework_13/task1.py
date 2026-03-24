import os
import re
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')

with open(file_path) as data_file:
    content = data_file.read()

    dates = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}', content)

    date1 = datetime.fromisoformat(dates[0])
    print(date1 + timedelta(weeks=1))

    date2 = datetime.fromisoformat(dates[1])
    print(date2.strftime('%A'))

    date3 = datetime.fromisoformat(dates[2])
    print((datetime.now() - date3).days)
