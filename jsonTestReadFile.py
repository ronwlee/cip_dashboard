import json
import requests

with open("weather.json", 'r') as f:
    weather = json.load(f)

print("The current temperature is", weather['current_condition'][0]['temp_F'])
print(weather['current_condition'])