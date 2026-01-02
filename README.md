# ☁️ Auto weather data test

*Repo used to collect weather data from API for Balloon Project 2025-2027.*



## 🌟 Functionality

- Uses World Weather Online's API (www.worldweatheronline.com)
- Takes data (default from postcode CA13) in CSV format every 15 minutes (detached from hour due to high action traffic)
- Creates file every 15 minutes with data
- Uses os python module to sort files by day


## ℹ️ Data included

- observation time
- temperature (°C)
- windspeed (Km/h)
- wind direction (°)
- precipitation (mm)
- pressure (MB)
- visibility (km)
- cloud cover (%)


## 🚀 Usage

This system requires Github actions so will not work on a local system.

Requires API key for World Weather Online ( https://www.worldweatheronline.com/weather-api/api/api-t-and-c.aspx)

This is stored as an actions secret named "API_KEY"

## 💭 Contribution

This is a part of the balloon project and is a repo designed for collection of weather data

Link to main repo: 
https://github.com/jackt77/weatherBalloonProject/tree/main
