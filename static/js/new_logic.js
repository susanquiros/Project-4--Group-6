d3.select("#clickMe").on("click", function (e) {
  let sel1 = d3.select("#selDataset1").property("value");
  let sel2 = d3.select("#selDataset2").property("value");
  let sel3 = d3.select("#selDataset3").property("value");
  console.log(sel1,sel2,sel3)
  console.log(`/api/winedata/${sel1},${sel2},${sel3}`)
  d3.json(`http://127.0.0.1:5000/api/winedata/${sel1},${sel2},${sel3}`).then(function (data) {
    d3.select(".result").text(data['Recommended 1']);
    d3.select(".result2").text(data['Recommended 2']);
    console.log(data)
    
    // d3.select()
  });

  
// });

// d3.select("#clickMe").on("click", () => {
  confetti("tsparticles", {
    angle: 90,
    count: 25,
    position: { x: 50, y: 50 },
    spread: 90,
    startVelocity: 60,
    decay: 0.9,
    gravity: 1,
    drift: 0,
    ticks: 200,
    colors: ["#fff", "#f00"],
    shapes: ["square", "circle"],
    scalar: 1,
    zIndex: 2000,
    disableForReducedMotion: true
    });
});