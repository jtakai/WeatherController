from time import gmtime, strftime, localtime
from datetime import datetime

strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
lTime = localtime()
print("** localtime <",lTime, ">")

print("\n--> Gathering Data : GetTime")
now = datetime.now()
print("<", now, ">")
current_time = now.strftime("%H")
print("** Current Time =", int(current_time)-12)
#TASK: Need to solve Positional math for hours:minutes
#TASK: Need to return intelligent/formatted time data for position modules
print("\n--> GetTime complete")


