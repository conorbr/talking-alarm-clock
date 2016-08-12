# Text To Speech Module

from gtts import gTTS

def download(message, outfile='message.mp3'):
    """
    Download a Google Text to Speech MP3 of the string `message`.
    Output defaults to message.mp3
    """
    # Test: create an mp3
    test = gTTS(text=message, lang='en')
    test.save(outfile)

