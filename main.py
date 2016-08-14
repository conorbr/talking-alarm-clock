# Raspi Alarm Clock
# Grayson Pike, 2016

import subprocess
import os
import tts
import date_time
import forecast
import bitcoin

NAME = "Grayson"

def main():

    # Assign output strings
    greeting = "Good " + date_time.get_current_greet_time() + ", " + NAME + ". "
    time_and_date = "It's " + date_time.get_current_time() + ", " + date_time.get_current_day_of_week() + ", " + \
                    "the " + date_time.get_current_day() + " of " + date_time.get_current_month() + ", 2016. "
    weather = forecast.get_weather()
    if not weather:
        weather_string = "Failed to retrieve weather conditions."
    else:
        weather_string = "Today in " + weather['city'] + ", it's currently " + str(weather['temp']) + " degrees. " + \
                         "Today will be " + weather['condition'] + " with a high of " + weather['high'] + " and a low at " + \
                         weather['low'] + " degrees. Humidity is at " + weather['humidity'] + " percent. "
    bitcoin_price = bitcoin.get_bitcoin_price()
    if not bitcoin_price:
        bitcoin_string = "Failed to retrieve bitcoin price information."
    else:
        bitcoin_string = "The Bitcoin Price Index stands at " + "%.2f" % bitcoin_price + " US dollars."

    # Generate and play TTS
    print "GREETING: " + greeting
    print "TIME & DATE: " + time_and_date
    print "WEATHER: " + weather_string
    print "BITCOIN: " + bitcoin_string
    tts.download(greeting + time_and_date, outfile="greeting.mp3")
    tts.download(weather_string, outfile="weather.mp3")
    tts.download(bitcoin_string, outfile="bitcoin.mp3")
    subprocess.call("avplay -nodisp -autoexit greeting.mp3", shell=True)
    subprocess.call("avplay -nodisp -autoexit weather.mp3", shell=True)
    subprocess.call("avplay -nodisp -autoexit bitcoin.mp3", shell=True)

    # Remove MP3 file
    os.remove("greeting.mp3")
    os.remove("weather.mp3")
    os.remove("bitcoin.mp3")

main()
