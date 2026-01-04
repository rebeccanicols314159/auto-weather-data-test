import WeatherDataCollecterCSV as wdc
from datetime import datetime

data = wdc.getweatherdata(wdc.URL)
wanteddata = ['observation_time','temp_C','windspeedKmph','winddirDegree','precipMM','pressureMB','visibilityKm','cloudcover'] #Select data wanted - change to txt file later?

def getfilename():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
    name = (f'weather-data-{timestamp}.txt')
    return name

def intofile(fname,dta):
    with open(fname,"w") as f:
        tofile = []
        for i in range(len(wanteddata)):
            tofile.append(f'{wanteddata[i]},{dta[i]}')
        tofile = ("\n".join(tofile))
        f.write(tofile)

def selectdata(alldata):
    datalist = []
    for i in wanteddata:
        datalist.append(alldata[0].get(i))
    return datalist

def makedatafile():
    filename = getfilename()
    wanted = selectdata(data)
    intofile(filename,wanted)

#Testing
print(data)
print(wanteddata)
print(selectdata(data))