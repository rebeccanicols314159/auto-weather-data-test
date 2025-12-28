import requests
import csv
import os

def updateURL():
    '''
    File DATA.txt containing:
        1 - location
        2 - number of days
    ''' 
    DATA = open("DATA.txt")

    API_KEY = os.environ["API_KEY"]
    PLACE = DATA.readline()
    NUMBER = DATA.readline()
    FORMAT = 'csv'
    url = f"https://api.worldweatheronline.com/premium/v1/weather.ashx?key={API_KEY}&q={PLACE}&num_of_days={NUMBER}&format={FORMAT}"

    DATA.close()
    return url

def getweatherdata(url):
    response = requests.get(url)
    if response.status_code == 200: #Check API running
        with open('weatherdata.csv','w',newline='') as f:
            f.write(response.text)
        fields = []
        rows = []
        with open('weatherdata.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)  # Reader object
            next(csvreader)
            for field in range(3):
                for i in range(2):
                    next(csvreader)
                fields.append(next(csvreader))
            next(csvreader)
            for row in csvreader:     # Read rows
                rows.append(row)
        data = []
        for i in range(len(fields)): #Removing #s
            if fields[i][0][0] == '#':
                fields[i][0] = fields[i][0][1:]
        for group in range(len(fields)):
            data.append(dict(zip(fields[group],rows[group])))
        return data
    else:
        raise Exception("API error :",response.status_code)

URL = updateURL()

#Example request
#weatherdata = getweatherdata(URL)
#print(weatherdata)
#print(f'Temperature {weatherdata["current_condition"][0]["temp_C"]}°C')