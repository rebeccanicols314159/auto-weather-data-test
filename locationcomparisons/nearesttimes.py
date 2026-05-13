from datetime import datetime
import os
import json

JSONFILENAME = 'SeaPredictions.json'
TEMPFILENAME = 'TempDataStorage.json'

def getweatherdates():
    os.chdir(f'{os.getcwd()}/data_files')
    rtdir = os.getcwd()
    folders = os.listdir()
    for i in folders.copy():
        if not "weather_data" in i:
            folders.remove(i)
    
    datelist = []
    for folder in folders:
        os.chdir(f'{rtdir}/{folder}')
        for file in os.listdir():
            if 'weather-data' in file:
                dattim = file[13:32]
                datelist.append(dattim)

    for i in range(len(datelist)):
        datelist[i] = datetime.strptime(datelist[i], "%Y-%m-%d_%H-%M-%S")

    os.chdir(f'{rtdir}/{os.pardir}')
    return datelist

def getsimulationdates():
    os.chdir(f'{os.getcwd()}/locationcomparisons/flightdata')
    with open(JSONFILENAME) as f:
        fulldata = json.load(f)
    
    datelist = []
    dates = fulldata.keys()
    for i in dates:
        times = fulldata.get(i).keys()
        for j in times:
            datelist.append(f'{i}-{j}')
    
    for i in range(len(datelist)):
        datelist[i] = datetime.strptime(datelist[i], "%Y-%m-%d-%H:%M:%S")
    return datelist



def listtodatetime(times):
    for i in times:
        pass


def nearest_time(target_time, time_list):
    """
    Finds the nearest time in a list of times to a target time.

    Parameters:
    target_time (datetime): The time to compare against.
    time_list (list of datetime): A list of times to search through.

    Returns:
    datetime: The time from the list that is closest to the target time.
    """
    res = min(time_list, key=lambda x: abs(x - target_time))

    return res


wdates = getweatherdates()
simdates = getsimulationdates()

times = {}
for i in simdates:
    times[str(i)] = nearest_time(i,wdates).isoformat()

#print(times)
jsondata = json.dumps(times, indent=4, default=str)
print(jsondata)

with open(TEMPFILENAME,"w") as f:
    f.write(jsondata)