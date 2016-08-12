# Current Date and Time Module

import datetime
import calendar

def get_current_time():
    pm = False
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute

    # Convert to 12 hour time
    if hour == 0:
        hour = 12
    elif hour > 11:
        pm = True
        hour -= 12

    # If single digit minute, add 'oh' to the beginning
    if minute < 10:
        minute = "0" + str(minute)
    
    return str(hour) + " " + str(minute) + " " + ("PM" if pm else "AM")

def get_current_day_of_week():
    return calendar.day_name[ datetime.date.today().weekday() ]

def is_morning():
    return datetime.datetime.now().hour < 12

