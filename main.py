# Raspi Alarm Clock
# Grayson Pike, 2016

import subprocess
import os
import tts
import date_time
import forecast

NAME = "Grayson"

def main():

    # Assign output strings
    greeting = "Good " + date_time.get_current_greet_time() + ", " + NAME + ". "
    time_and_date = "It's " + date_time.get_current_time() + ", " + date_time.get_current_day_of_week() + ", " + \
                    "the " + date_time.get_current_day() + " of " + date_time.get_current_month() + ", 2016. "
    weather = forecast.get_weather()
    weather_string = "Today in " + weather['city'] + ", it's currently " + str(weather['temp']) + " degrees. " + \
                     "Today will be " + weather['condition'] + " with a high of " + weather['high'] + " and a low at " + \
                     weather['low'] + " degrees. Humidity is at " + weather['humidity'] + " percent. "

    # Generate and play TTS
    print "GREETING: " + greeting
    print "TIME & DATE: " + time_and_date
    print "WEATHER: " + weather_string
    tts.download(greeting, outfile="greeting.mp3")
    tts.download(time_and_date, outfile="timedate.mp3")
    tts.download(weather_string, outfile="weather.mp3")
    subprocess.call("avplay -nodisp -autoexit greeting.mp3", shell=True)
    subprocess.call("avplay -nodisp -autoexit timedate.mp3", shell=True)
    subprocess.call("avplay -nodisp -autoexit weather.mp3", shell=True)

    # Remove MP3 file
    os.remove("greeting.mp3")
    os.remove("timedate.mp3")
    os.remove("weather.mp3")

main()
