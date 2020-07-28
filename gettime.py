from datetime import datetime

def GetTime():
    print("\n--> Gathering Data : GetTime")
    now = datetime.now()
    print("<", now, ">")
    current_time = now.strftime("%H:%M")
    print("** Current Time =", current_time)
    #TASK: Need to solve Positional math for hours:minutes
    #TASK: Need to return intelligent/formatted time data for position modules
    print("\n--> GetTime complete")
    return
