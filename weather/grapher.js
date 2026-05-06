fetch("data.json")
  .then(res => res.json())
  .then(data => {
    const trace = {
      x: data.map(d => d.time),
      y: data.map(d => d.temp_C),
      type: "scatter"
    };

    Plotly.newPlot("graph", [trace]);
  });