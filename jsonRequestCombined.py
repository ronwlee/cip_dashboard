import json
import requests

def get_weather() :
    # request Cupertino weather data in json format
    url = "http://wttr.in/Cupertino?format=j1"

    # do a get on the url - note the .content part is the json data
    data = requests.get(url)

    # load the json data into a weather dictionary
    weather = json.loads(data.content)
    return weather

weather = get_weather()

print("The current temperature is", weather['current_condition'][0]['temp_F'])
