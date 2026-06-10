# Comparing data

**The purpose of this part of the project is to compare the flight simulation data with the weather data, to find weather conditions optimal for launch.**

## Input data

### Flight simulation data

- See [/flightdata](./flightdata)
- Contains 3 json files: one with all simulations which resulted in a final location on land, one for those which finished in the sea, and one with all simulations.

### Weather data

Well if you haven't seen those files yet then you need to look more closely.


## Functionality

### Entry matching

Consists of a python script:
- Creates a list of timestamps of times at which weather data was collected using strptime in the datetime module.
- Creates a similar list of simulation times.
- For each simulation time, finds the closest weather data collection using abs and datetime.
- Stores the result as a dictionary named times, where keys are the simulation times and values are weather data times.
- Outputs this data to a json file [./flightdata/TempDataStorage.json](./flightdata/TempDataStorage.json), currently stored in [./flightdata](./flightdata/)

## Data collecting

Consists of a python script [times_to_data.py](times_to_data.py)
- Fill this in later

## Creating a table

3 files stored in [./Tablepage](./Tablepage/)
- Uses an async function to extract json data.
- Plots a table which is drawn on html.


## To do:

- Finish README sections above.
- Finish timestodata to extract in a good format, find missing data etc.
- Fix table formatting.
- Visualise - plotly (js/html?)
- Create stats on data