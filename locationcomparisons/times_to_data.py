import json
import os

RTDIR = os.getcwd()
FILENAME = "SeaWeather.json"
TEMPFILENAME = "TempDataStorage.json"

# Store as dict

''' Flight time: [weather data time, weather data]'''

def combinelists(times,weather):
    #Times = the dictionary simulationtime:weathertime
    #Weather = the dictionary weathertime:weather
    
    bigdict = {}

    for i in times.keys():
        try: bigdict[i] = weather[times[i]]
        except: bigdict[i] = "NOTFOUND"

    return bigdict


#Take in data: nearesttimes

os.chdir("./locationcomparisons/flightdata")
with open(TEMPFILENAME,"r") as f:
    weathertimes = json.load(f)
os.chdir(RTDIR)

# Data: weather

''' Requires the weather data files (as json or text files)
Also requires times from dict (get values) ='''

with open('data.json','r') as f:
    weatherdata = json.load(f)

wdataformatted = {}
for i in weatherdata:
    j = i.copy()
    j.popitem()
    wdataformatted[i["time"][:-5]] = j

# Function
#print(wdataformatted)
print(combinelists(weathertimes,wdataformatted))
x = combinelists(weathertimes,wdataformatted)
#To json

os.chdir(f"{RTDIR}/locationcomparisons")
with open(FILENAME,"w") as f:
    f.write(json.dumps(x))