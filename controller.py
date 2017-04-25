
import fcntl, socket, struct, dweepy, time, platform, random
import main
import schedule
import time
import clock
import json
import threading

dweet_controller = dweet_controller = 'talking_alarm_set_time'
globvar = "00:00"

def job():  #for testing purposes
    print("I'm working...")

def set_time_manually(): #for testing purposes
    dweepy.dweet_for(dweet_controller, {'time_hour': '18','time_minute': '45'})


def set_alarm_time(): #check for updates in alarm time via dweet
    dweet = dweepy.get_latest_dweet_for(dweet_controller)
    parsed_data = json.dumps(dweet)
    json_object = json.loads(parsed_data)
    time_hour = translatedObject = json_object[0]['content']['time_hour']
    time_minute = translatedObject = json_object[0]['content']['time_minute']
    s = ":"
    sequence = (str(time_hour), str(time_minute))
    alarm_time = s.join(sequence)

    global globvar    # use global variable to store time dweet
    globvar = alarm_time
    print globvar
    return;

def trigger_alarm():
  year, month, day, hour, minute, seconds = time.strftime("%Y,%m,%d,%H,%M,%s").split(',')
  time_now = hour + ":" + minute
  time_alarm = globvar
  if time_now == globvar:
      main.main()
  else:
      print time_now
      print time_alarm
      time.sleep(1)





# schedule.every(1).minutes.do(set_time_manually)
schedule.every(1).minutes.do(set_alarm_time)
threading.Timer(30.0, trigger_alarm).start()


while 1:
    schedule.run_pending()
    time.sleep(1)
