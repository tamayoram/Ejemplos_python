
from datetime import datetime

birthday=datetime(1982,4,22)
print(birthday.year)
print(birthday.month)
print(birthday.weekday())

datetime.now()

datetime(2020,1,1)-datetime(2019,1,1)
datetime.now()-datetime(1982,4,22)

parsed_date=datetime.strptime('Jan 15, 2018','%b %d, %Y')
parsed_date.month

date_string=datetime.strftime(datetime.now(),'%b %d, %Y')
print (date_string)
