function loadChart(chart, endpoint) {
  $.ajax({
    url: endpoint,
    type: "GET",
    dataType: "json",
    success: (jsonResponse) => {
      // Extract data from the response
      const title = jsonResponse.title;
      const labels = jsonResponse.data.labels;
      const datasets = jsonResponse.data.datasets;

      // Reset the current chart
      chart.data.datasets = [];
      chart.data.labels = [];

      // Load new data into the chart
      chart.options.title.text = title;
      chart.options.title.display = true;
      chart.data.labels = labels;
      datasets.forEach(dataset => {
        chart.data.datasets.push(dataset);
      });
      console.log(chart)
      // chart.options.scales.yAxes.type = "linear";
      // chart.options.scales.yAxes.min = 0;
      chart.options.scales.yAxes = [{
            ticks: {
                suggestedMin: 0,
                suggestedMax: 5,
                stepSize: 1
            }
        }]
      // chart.options.scales.yAxes.ticks.stepSize = 1;
      chart.update();
    },
    error: () => console.log("Failed to fetch chart data from " + endpoint + "!")
  });
}
