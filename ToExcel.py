import pandas as pd
import os

os.chdir(f'{os.getcwd()}/data_files')
rtdir = os.getcwd()
folders = os.listdir()

for i in folders.copy():
    if not "weather_data" in i:
        folders.remove(i)

def getinfo(fders):
    flist = []
    for folder in fders:
        os.chdir(f'{rtdir}/{folder}')
        for file in os.listdir():
            with open(file) as f:
                if 'weather-data' in file:
                    sdate = f.read().split()
                    sdate = ['date',folder[13:]] + sdate
                    flist.append(sdate)
    return flist

def makedict(info):
    columns = ['date','observation_time','temp_C', 'windspeedKmph', 'winddirDegree', 'precipMM', 'pressureMB', 'visibilityKm', 'cloudcover']
    infodict = {col: [] for col in columns}

    for entry in info:
        for col in columns:
            infodict[col].append(entry[columns.index(col)])
    return infodict
        

def makefile(datadict):
    df = pd.DataFrame(datadict)
    os.chdir(rtdir)
    df.to_excel('All_data.xlsx')

#Example request
a = getinfo(folders)
b = makedict(a)
makefile(b)