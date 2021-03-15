# Backbones
import speech_recognition as sr
import pyttsx3

# Functions
from datetime import datetime
import pywhatkit
import twitter

from weather_tools import current_weather

# Configurations file
from configs import twitter_cred


listener = sr.Recognizer()
engine = pyttsx3.init()

# Configurations
owner = 'Edward'

# Twitter API
twitter_settings = twitter_cred

twitter_api = twitter.Api(consumer_key=twitter_settings['consumer_key'],
		                  consumer_secret=[consumer_secret],
		                  access_token_key=[access_token],
		                  access_token_secret=[access_token_secret])


def listen_sound():
	song = AudioSegment.from_wav("sounds/sound.wav")
	play(song)


def talk(text):
	engine.say(text)
	engine.runAndWait()



# Play Music Command

def play_music(song):
	song = song.replace('on ', '')

	if 'youtube' in song:
		song = song.replace('youtube ', '')
		talk('Playing'  + song + 'on YouTube.')
		pywhatkit.playonyt(song)

	elif 'spotify' in song:
		song = song.replace('youtube ', '')

# Weather

def check_weather(command):
	if 'now' in command:
		weather_info = current_weather()
		message = 'Here in {}, there\'s {} now. The temperature is at {} degree, feels like {} degree, the \
				   current humidity is at {} percent.'.format(weather_info['location'],weather_info['weather'],
				   						 weather_info['temp'], weather_info['feels_like'], weather_info['humidity'])
		print(message)
		talk(message)

def twitter_post():
	with sr.Microphone() as source:
		voice = listener.listen(source)
		print('listening for twitter_post...')
		command = listener.recognize_google(voice)
		command = command.lower()
		print(command)
		if 'never mind' in command:
			talk('ok')
		else:
			print('it works')
			pass

			

# Handling All Commands

def command_handler(command):
	if 'play' in command:
		print('Detect \'play\' keyword')
		song = command.replace('play ', '')
		play_music(song)

	elif 'weather' in command:
		print('Detect \'weather\' keyword')
		check_weather(command)

	elif 'Twitter' in command:
		print('Detect \'tweet\' keyword')
		twitter_post()


# Listen to Hey

def take_command():
	while True:
		try:
			with sr.Microphone() as source:
				print('listening...')
				voice = listener.listen(source)
				command = listener.recognize_google(voice)
				command = command.lower()

				if 'hey' in command:
					command = command.replace('hey ', '')
					talk('Hey' + owner)

					try:
						print('listening for command...')
						voice = listener.listen(source)
						
						command = listener.recognize_google(voice)
						command = command.lower()

						print(command)

						if 'shut down' in command:
							talk('Good Bye. Shutting down.')
							break
						elif 'never mind' in command:
							print(command)
							talk('okay.')
						else:
							print('Command Received')
							command_handler(command)

					except:
						talk('Sorry, I can\'t hear what you say.')
						break

				elif 'shut down' in command:
					talk('Good Bye. Shutting down.')
					break

				elif 'nevermind' in command:
					talk('okay.')
		except:
			pass


# Main Function

def main():

	take_command()


if __name__ == "__main__":
	main()