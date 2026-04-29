# Weather Data Dashboard

This project visualises weather data collected over time and stored as `.txt` files. The data is processed into a single structured dataset and displayed using an interactive web dashboard.

**This file, alongside much of the code and structure in this section of the project, was written by ChatGPT**

---

## 📊 Features

* Interactive graphing of weather variables
* Multi-select dashboard (plot multiple variables at once)
* Data updates on page refresh
* Lightweight setup (no backend required)

---

## 📁 Project Structure

```
/data/                # Raw data folders (grouped by date)
/scripts/             # Data processing scripts (optional)
/data.json            # Generated dataset used by the dashboard
/index.html           # Main dashboard
```

---

## 📥 Data Format

Each raw data file is stored as key-value pairs:

```
observation_time,05:52 PM
temp_C,3
windspeedKmph,9
winddirDegree,77
precipMM,0.0
pressureMB,1032
visibilityKm,10
cloudcover,100
```

Filenames contain the timestamp:

```
weather-data-2025-12-28_17-51-36.txt
```

The timestamp is extracted from the filename during processing.

---

## ⚙️ Data Processing

Raw `.txt` files are converted into a single `data.json` file using a script.

Each entry in `data.json` looks like:

```json
{
  "time": "2025-12-28T17:51:36.000Z",
  "temp_C": 3,
  "windspeedKmph": 9,
  "pressureMB": 1032,
  "cloudcover": 100
}
```

Steps:

1. Read all data files
2. Extract timestamp from filename
3. Parse key-value pairs
4. Convert to numeric values
5. Sort chronologically
6. Output to `data.json`

---

## 🌐 Running the Dashboard

1. Open `index.html` in a browser
   or
2. Host using GitHub Pages

The dashboard will:

* Load `data.json`
* Display selectable variables
* Plot graphs interactively

---

## 🔄 Updating Data

To update the dashboard:

1. Add new `.txt` files to the data folders
2. Run the processing script
3. Commit and push changes
4. Refresh the webpage

---

## 🚀 Future Improvements

* Automatic data processing (GitHub Actions)
* Date range filtering
* Live updating without refresh
* Improved UI/UX (themes, layout)
* Data export options

---

## 📜 License

This project is open-source and free to use.
