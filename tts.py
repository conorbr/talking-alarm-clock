# google's text to speach module
from gtts import gTTS

def download(message, outfile='message.mp3'):
    # Test: create an mp3
    message = gTTS(text=message, lang='en')
    message.save(outfile)
