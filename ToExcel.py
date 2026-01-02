import pandas as pd
import os

os.chdir(f'{os.getcwd()}/data_files')
rtdir = os.getcwd()
folders = os.listdir()

for i in folders:
    if not "weather_data" in i:
        folders.remove(i)

def getinfo(fders):
    flist = []
    for folder in fders:
        os.chdir(f'{rtdir}/{folder}')
        for file in os.listdir():
            with open(file,encoding="latin-1") as f:
                sdate = f.read().split()
                sdate = ['date',folder[13:]] + sdate
                flist.append(sdate)
    return flist

def makedict(info):
    columns = ['date','observation_time','temp_C', 'windspeedKmph', 'winddirDegree', 'precipMM', 'pressureMB', 'visibilityKm', 'cloudcover']
    entries = []
    for i in columns:
        exec(f'{i} = []')
        for j in info:
            exec(f'{i}.append(j[j.index(i)+1])')
        entries.append(eval(i))
    infodict = dict(zip(columns,entries))
    return infodict
        

def makefile(datadict):
    df = pd.DataFrame(datadict)
    os.chdir(rtdir)
    df.to_excel('All_data.xlsx')

#Example request
#a = getinfo(folders)
#b = makedict(a)
#makefile(b)