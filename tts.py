# Text To Speech Module

from gtts import gTTS

def main():

	# Test: create an mp3
	test = gTTS(text='Hello, World.', lang='en')
	test.save("test.mp3")

main()