# Raspi Alarm Clock
# Grayson Pike, 2016

import subprocess
import os
import tts
import date_time
import forecast
import bitcoin
import news

NAME = "Conor"

def main():

    # Assign output strings
    greeting = "Good " + date_time.get_current_greet_time() + ", " + NAME + ". "
    time_and_date = "It's " + date_time.get_current_time() + ", " + date_time.get_current_day_of_week() + ", " + \
                    "the " + date_time.get_current_day() + " of " + date_time.get_current_month() + ", 2017. ."

    weather = forecast.get_weather()
    if not weather:
        weather_string = "Failed to retrieve weather conditions."
    else:
        weather_string = "Today in " + weather['city'] + ", it's currently " + str(weather['temp']) + " degrees. " + \
                         "Today will be " + weather['condition'] + " with a high of " + weather['high'] + " and a low at " + \
                         weather['low'] + " degrees. Humidity is at " + weather['humidity'] + " percent. "
    news_string = "And now the news...." + news.get_news()

    # Generate and play TTS
    print "GREETING: " + greeting
    print "TIME & DATE: " + time_and_date
    print "WEATHER: " + weather_string

    tts.download(greeting + time_and_date, outfile="greeting.mp3")
    tts.download(weather_string, outfile="weather.mp3")
    tts.download(news_string, outfile="news.mp3")

    #get mp3 files
    subprocess.call("omxplayer -o local greeting.mp3", shell=True)
    subprocess.call("omxplayer -o local weather.mp3", shell=True)
    subprocess.call("omxplayer -o local news.mp3", shell=True)

    # Remove MP3 files
    os.remove("greeting.mp3")
    os.remove("weather.mp3")
    os.remove("news.mp3")

main()
