import requests
import csv

import logging
import logging.handlers
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    API_KEY = os.environ["API_KEY"]
except KeyError:
    API_KEY = "Token not available!"
    #logger.info("Token not available!")
    #raise

def updateURL():
    '''
    File DATA.txt containing:
        1 - API key
        2 - location
    ''' 
    DATA = open("DATA.txt")

    API_KEY = DATA.readline()
    PLACE = DATA.readline()
    NUMBER = '1'
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