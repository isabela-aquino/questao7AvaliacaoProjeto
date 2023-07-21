
    var categorias = ['blouses', 'sale', 'skirts', 'trousers'];
    var numModelosDistintos = [59, 82, 34, 43];

    var svgWidth = 600;
    var svgHeight = 400;

    var svg = d3.select("#grafico")
      .append("svg")
      .attr("width", svgWidth)
      .attr("height", svgHeight);

    var margin = { top: 20, right: 20, bottom: 50, left: 50 };
    var chartWidth = svgWidth - margin.left - margin.right;
    var chartHeight = svgHeight - margin.top - margin.bottom;

    var xScale = d3.scaleBand()
      .domain(categorias)
      .range([0, chartWidth])
      .padding(0.2);

    var yScale = d3.scaleLinear()
      .domain([0, d3.max(numModelosDistintos)])
      .range([chartHeight, 0]);

    var xAxis = d3.axisBottom(xScale);
    var yAxis = d3.axisLeft(yScale);

    var chart = svg.append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    chart.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + chartHeight + ")")
      .call(xAxis);

    chart.append("g")
      .attr("class", "y axis")
      .call(yAxis);

    chart.selectAll(".bar")
      .data(numModelosDistintos)
      .enter()
      .append("rect")
      .attr("class", "bar")
      .attr("x", (d, i) => xScale(categorias[i]))
      .attr("y", d => yScale(d))
      .attr("width", xScale.bandwidth())
      .attr("height", d => chartHeight - yScale(d))
      .attr("fill", "steelblue");
