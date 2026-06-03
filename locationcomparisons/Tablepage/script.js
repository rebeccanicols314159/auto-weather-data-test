// Need to import data here
/* async function getData(file) {
    const response = await fetch(file);
    const data = await response.json();
    return data
}

const weatherstuff = './locationcomparisons/SeaWeather.json'
const jsonData = await getData(weatherstuff) */

//Let's try again shall we
/*const fs = require('fs');
try{
    //Read file syncronously (whatever that means)
    const data = fs.readFileSync('SeaWeather.json','utf-8')
} catch (err) {
    console.error("Error reading file:", err)
} */

//Another attempt
/*const os = require('node:os')
os.
const data = require('./SeaWeather.json')
console.log(data)*/

//Again
/*fetch("./SeaWeather.json")
    .then(response => response.json())
    .then(jsonData => console.log(jsonData))
    .catch(error => console.error('Error fetching data:', error));*/

// Generating table
function generateTable(data) {
    if (!data || data.length === 0) return "Error finding data.";
    const table = document.createElement('table')

    //Headers
    const headerRow = document.createElement('tr');
    const firstkey = Object.keys(data)[0]
    const keys = Object.keys(data[firstkey]);
    keys.unshift("Date and time")
    keys.forEach(key => {
        const th = document.createElement('th');
        th.textContent = key.charAt(0).toUpperCase() + key.slice(1); //Capitalise
        headerRow.appendChild(th);
    });
    table.appendChild(headerRow);
    
    //Rows
    const rowData = Object.entries(data)
    console.log(rowData)
    rowData.forEach(item=> {
        //const makeRow = [["Date and time",item[0]]].concat(Object.entries(item[1]))
        const makeRow = item[1]
        makeRow["Date and time"] = item[0]
        const row = document.createElement('tr');
        keys.forEach(key => {
            const td = document.createElement('td')
            console.log(typeof key)
            console.log(typeof makeRow)
            console.log(makeRow[key])
            td.textContent = makeRow[key] || ""; //Apparently this will fill empty table fields with a blank
            //console.log(item[0].concat(Object.entries(item[1])))
            row.appendChild(td);
        });
        table.appendChild(row);
    });
    return table
}

//Trying to render table inside fetch
const container = document.getElementById('table-container')

async function doThing(params) {
    try {
        const response = await fetch('https://raw.githubusercontent.com/rebeccanicols314159/auto-weather-data-test/dataprocessing/locationcomparisons/SeaWeather.json')
        const jsonData = await response.json();
        console.log(jsonData)
        const table = generateTable(jsonData);
        if (table) container.appendChild(table);
    }   catch (error) {
        console.error(error)
    }
}

doThing();
/*const table = generateTable(jsonData);
if (table) container.appendChild(table);*/

// Render table
/*const container = document.getElementById('table-container')
const table = generateTable(jsonData);
if (table) container.appendChild(table);*/