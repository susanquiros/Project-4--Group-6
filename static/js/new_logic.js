d3.select("#clickMe").on("click", function (e) {
  let sel1 = d3.select("#selDataset1").property("value");
  let sel2 = d3.select("#selDataset2").property("value");
  let sel3 = d3.select("#selDataset3").property("value");
  console.log(sel1,sel2,sel3)
  console.log(`/api/winedata/${sel1},${sel2},${sel3}`)
  d3.json(`http://127.0.0.1:5000/api/winedata/${sel1},${sel2},${sel3}`).then(function (data) {
    d3.select(".result").text(data['Recommended 1']);
    d3.select(".result2").text(data['Recommended 2']);
    
    // d3.select()
  });

  
});
