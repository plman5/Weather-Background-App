import requests
import json
import urllib.request
import pandas as pd

# weather=urllib.request.urlopen(urllib.request.Request('https://api.weather.gov/points/39.7456,-97.0892'))
# weatherBytes=weather.read()
# weatherStr=weatherBytes.decode('utf8')
# weather.close()
# weatherJson=json.loads(weatherStr)
# weather2=urllib.request.urlopen(urllib.request.Request(weatherJson["properties"]["forecastHourly"]))
# weatherBytes2=weather2.read()
# weatherStr2=weatherBytes2.decode('utf8')
# weather2.close()
# weatherJson2=json.loads(weatherStr2)
# print(weatherJson2["properties"]["periods"][0]["shortForecast"])
#
with open('censusKey.txt') as f:
    censusKey=f.read()
state=6
#censusStateTable=urllib.request.urlopen(urllib.request.Request(f'https://api.census.gov/data/2021/acs/acs1?get=NAME&for=state&key={censusKey}'))
# for i in range(60):
#     census = urllib.request.urlopen(urllib.request.Request(
#         f'https://api.census.gov/data/2021/acs/acs1?get=NAME,B01001_001E&for=place&in=state:{str(i).zfill(2)}&key={censusKey}'))
#     censusBytes=census.read()
#     censusStr=censusBytes.decode('utf8')
#     census.close()
#
#     data = pd.DataFrame(censusStr, columns=["NAME","B01001_001E","state","place"])
#     print(data)

    #censusJson=json.loads(censusStr)
    # with open(f'censusDump/censusState{i}.json', 'w+') as f:
    #     f.write(censusStr)


#import all files in censusUmp as python lists
# for i in range(100):
#     print(i)
#     with open(f'censusDump/censusState{i}.json', 'r+') as f:
#         data=f.read()
#         data=data.split('\n')
#         for i in range(len(data)):
#             if len(data[i])!=0:
#                 data[i]=data[i].split('","')
#                 data[i][0]=data[i][0][2:]
#                 print(data[i])
#                 tmp=[data[i][0],data[i][1]]
#                 data[i]='["'+'","'.join(tmp).replace(', ',',')+'"],'
#                 print(data[i])
#
#         data=data[1:]
#         f.seek(0)
#         f.truncate()
#         data='\n'.join(data)
#         data='['+data[:-1]+']'
#         print(data)
#         f.write(data)

# walk through censusDump using os.walk
import os
bigList=[]
for root, dirs, files in os.walk("censusDump"):
    for file in sorted(files):
        if file.endswith(".json"):
            #print(os.path.join(root, file))
            with open(os.path.join(root, file), 'r') as f:
                data=f.read()
                data=data.split('\n')
                tmp=[]
                state=''
                for i in range(len(data)):
                    if len(data[i])!=0:
                        #get the cities and put them in an array
                        data[i]=data[i].split('"')
                        data[i][1]=data[i][1].split(',')
                        tmp.append(data[i][1][0])
                        state=data[i][1][1]
                print(f'"{state}":{str(sorted(tmp))},')
#bigList))


print('done')