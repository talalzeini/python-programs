# pip install datetime
import datetime as dt

birthday = dt.datetime(2001, 1, 23)
time_alive = dt.datetime.today() - birthday
print(time_alive.days)