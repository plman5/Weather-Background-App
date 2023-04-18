import requests
import json
import urllib.request

weather=urllib.request.urlopen(urllib.request.Request('https://api.weather.gov/points/39.7456,-97.0892'))
weatherBytes=weather.read()
weatherStr=weatherBytes.decode('utf8')
weather.close()
weatherJson=json.loads(weatherStr)
weather2=urllib.request.urlopen(urllib.request.Request(weatherJson["properties"]["forecastHourly"]))
weatherBytes2=weather2.read()
weatherStr2=weatherBytes2.decode('utf8')
weather2.close()
weatherJson2=json.loads(weatherStr2)
print(weatherJson2["properties"]["periods"][0]["shortForecast"])
