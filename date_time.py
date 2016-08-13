# Current Date and Time Module

import datetime
import calendar

def get_ordinal_string(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        return str(day) + "th"
    return str(day) + ["st", "nd", "rd"][day % 10 - 1]

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

def get_current_day():
    return get_ordinal_string(datetime.datetime.now().day)

def get_current_month():
    return calendar.month_name[ datetime.datetime.now().month ]

def get_current_greet_time():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "morning"
    elif hour < 18:
        return "afternoon"
    else:
        return "evening"

