import requests

from utils import k_to_celsius
from configs import open_weather_api_key


def current_weather():
	params = {
	'cityname': 'Sydney',
	'statecode': '2000',
	'countrycode' : '036',
	'api_key' : open_weather_api_key
	}
	current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={},{},{}&appid={}'.format(params['cityname'], params['statecode'], params['countrycode'], params['api_key'])
	response = requests.get(current_weather_url).json()

	weather_info = {
		'weather' : response['weather'][0]['description'],
		'location' : params['cityname'], 
		'temp' : k_to_celsius(response['main']['temp']),
		'feels_like' : k_to_celsius(response['main']['feels_like']),
		'humidity' : response['main']['humidity']
	}


	return weather_info


def next_7days_weather(location):
	pass