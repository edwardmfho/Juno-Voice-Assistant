# Juno Voice Assistant

Juno is a simple "rule-based" voice assistant built using Python.

## Installation

Clone this [repository](https://github.com/edwardmfho/Juno-Voice-Assistant/) using the following commands on terminal or command prompt. Juno was built using Python 3.7, and requires the following packages to run:

```bash
pip install requests
pip install pyttsx3
pip install speech_recognition
pip install pywhatkit
pip install python-twitter
```
You'd also required to register for [Open Weather Map](https://openweathermap.org/current) to generate an API key, in order to fetch weather data. Furthermore you would need a Twitter Developer Account to use the (future) twitter function of Juno.


## Usage

By running the `main.py`, Juno will be able to listen to your commands, including finding a music on YouTube, checking current weather, and later I will look into adding tools to let Juno to tweet for you. 
```python
python main.py
```

By saying `shut down` verbally, Juno will stop and exit.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
