# Raspi Alarm Clock
# Grayson Pike, 2016

import subprocess
import os
import tts
import date_time

def main():

    # Assign output strings
    greeting = "Good " + ("morning" if date_time.is_morning() else "afternoon") + ". "
    time_and_date = "It's " + date_time.get_current_time() + ", " + date_time.get_current_day_of_week() + ". "
    forecast = "The current temperature is 90 degrees. The high for today is 102 degrees with a low of 75. "

    # Generate and play TTS
    message = greeting + time_and_date
    print "MESSAGE: " + message
    tts.download(message)
    subprocess.call("avplay -nodisp -autoexit message.mp3", shell=True)

    # Remove MP3 file
    os.remove("message.mp3")

main()
