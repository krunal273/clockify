// @ts-nocheck
// const request = new XMLHttpRequest()

// request.open('GET', '/fetch-data', true)
// request.onload = function () {

//     const data = JSON.parse(this.response)

//     if (request.status >= 200 && request.status < 400) {
//         console.log(data);
//     } else {
//         console.log('error')
//     }
// }

// request.send()



// set the dimensions and margins of the graph
const margin = {
        top: 10,
        right: 30,
        bottom: 90,
        left: 40
    },
    width = 460 - margin.left - margin.right,
    height = 450 - margin.top - margin.bottom;

// append the svg object to the body of the page
const svg = d3.select("#display-chart")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform",
        "translate(" + 100 + "," + margin.top + ")");


// Parse the Data
d3.json("/fetch-data").then(data => {

    data = data.data;
    console.log(data);

    // format the data
    data.forEach(function (d, i) {
        d.startTime = (new Date(d.startTime)).toDateString().toString() + " " + i;
    });

    // X axis
    const x = d3.scaleBand()
        .range([0, width])
        .domain(data.map(function (d) {
            return d.startTime;
        }))
        .padding(0.2);
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))
        .selectAll("text")
        .attr("transform", "translate(-10,0)rotate(-45)")
        .style("text-anchor", "end");

    // Add Y axis
    const y = d3.scaleLinear()
        .domain([0, 500])
        .range([height, 0]);
    svg.append("g")
        .call(d3.axisLeft(y));


    //  X axis label
    svg.append("text")
        .attr("text-anchor", "end")
        .attr("x", 350)
        .attr("y", height + margin.top + 50)
        .text("Date");


    // Y axis label:
    svg.append("text")
        .attr("text-anchor", "end")
        .attr("transform", "rotate(-90)")
        .attr("y", -margin.left)
        .attr("x", -margin.top)
        .text("Seconds")


    // Bars
    svg.selectAll("mybar")
        .data(data)
        .enter()
        .append("rect")
        .attr("x", function (d) {
            return x(d.startTime);
        })
        .attr("width", x.bandwidth())
        .attr("fill", "#c6d2d9")
        // no bar at the beginning thus:
        .attr("height", function (d) {
            return height - y(0);
        }) // always equal to 0
        .attr("y", function (d) {
            return y(0);
        })



    // Bars seconds text
    svg.selectAll("mybar").append('text')
        .data(data)
        .enter()
        .append("text")
        .attr("class", "text-second")
        .text(function (d) {
            return d.totalTime + " s"
        })
        .attr("x", function (d, i) {
            return x(d.startTime) + 20;
        })
        .attr("y", function (d, i) {
            return y(d.totalTime) - 10;
        });

    // Animation
    svg.selectAll("rect")
        .transition()
        .duration(800)
        .attr("y", function (d) {
            return y(d.totalTime);
        })
        .attr("height", function (d) {
            return height - y(d.totalTime);
        })
        .delay(function (d, i) {
            console.log(i);
            return (i * 100)
        })

})


// d3.json("/fetch-data").then(data => {

// })