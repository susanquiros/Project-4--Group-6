d3.select("#clickMe").on("click", function (e) {
  let sel1 = d3.select("#selDataset1").property("value");
  let sel2 = d3.select("#selDataset2").property("value");
  let sel3 = d3.select("#selDataset3").property("value");
  d3.json(`/api/winedata/${sel1},${sel2},${sel3}`).then(function (data) {
    console.log(data);
    // d3.select()
  });
});