from sys import stdin
from datetime import datetime, timedelta

readtime = stdin.readline().strip()

d = datetime.strptime(readtime, "%I:%M %p")

for i in range(3,7):
    newdate = d - i* timedelta(0,0,0,0,90)
    print( datetime.strftime(newdate, "%I:%M %p") )
