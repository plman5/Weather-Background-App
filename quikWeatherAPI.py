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

with open('censusKey.txt') as f:
    censusKey=f.read()
state=6
#censusStateTable=urllib.request.urlopen(urllib.request.Request(f'https://api.census.gov/data/2021/acs/acs1?get=NAME&for=state&key={censusKey}'))
census=urllib.request.urlopen(urllib.request.Request(f'https://api.census.gov/data/2021/acs/acs1?get=NAME,B01001_001E&for=place&in=state:{str(state).zfill(2)}&key={censusKey}'))
censusBytes=census.read()
censusStr=censusBytes.decode('utf8')
census.close()
censusJson=json.loads(censusStr)
print(censusJson)