# Raspi Alarm Clock
# Grayson Pike, 2016

import subprocess
import os
import tts

def main():

    # Temporary testing strings
    greeting = "Good morning. It is 8 AM, Saturday the 13th, 2016."
    forecast = "The current temperature is 90 degrees. The high for today is 102 degrees with a low of 75."

    # Generate and play TTS
    tts.download(greeting + " " + forecast)
    subprocess.call("avplay -nodisp -autoexit message.mp3", shell=True)

    # Remove MP3 file
    os.remove("message.mp3")

main()
