const fs = require("fs");
const path = require("path");

const baseDir = "./data_files";
let output = [];

fs.readdirSync(baseDir).forEach(folder => {
  const folderPath = path.join(baseDir, folder);

  if (fs.lstatSync(folderPath).isDirectory()) {
    fs.readdirSync(folderPath).forEach(file => {
      if (!file.endsWith(".txt")) return;

      const filePath = path.join(folderPath, file);
      const content = fs.readFileSync(filePath, "utf-8").split("\n");

      let record = {};

      // Parse key-value pairs
      content.forEach(line => {
        const [key, value] = line.split(",");
        if (key && value) {
          record[key.trim()] = value.trim();
        }
      });

      // Extract timestamp from filename
      const match = file.match(/weather-data-(\d{4}-\d{2}-\d{2})_(\d{2})-(\d{2})-(\d{2})/);

      if (match) {
        const [_, date, hh, mm, ss] = match;
        record.time = new Date(`${date}T${hh}:${mm}:${ss}`).toISOString();
      }

      // Remove redundant field
      delete record.observation_time;

      // Convert numeric values
      for (let key in record) {
        if (!isNaN(record[key])) {
          record[key] = Number(record[key]);
        }
      }

      output.push(record);
    });
  }
});

// Sort chronologically
output.sort((a, b) => new Date(a.time) - new Date(b.time));

// Save
fs.writeFileSync("data.json", JSON.stringify(output, null, 2));