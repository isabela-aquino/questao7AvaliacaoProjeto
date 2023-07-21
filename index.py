import pandas as pd

order = "https://raw.githubusercontent.com/Data-Science-Research/edital_avaliacao/main/order.csv"
mainCategory = "https://raw.githubusercontent.com/Data-Science-Research/edital_avaliacao/main/mainCategory.csv"
order = pd.read_csv(order, sep=";", header=0)
mainCategory = pd.read_csv(mainCategory, sep=";", header=0)

merge_df = order.merge(mainCategory, how='inner',
                      left_on=['page 1 (main category)'],
                      right_on=['id'])

roupas_distintas_por_categoria = merge_df.groupby('mainCategory')['page 2 (clothing model)'].nunique()
categorias = roupas_distintas_por_categoria.index.tolist()
num_modelos_distintos = roupas_distintas_por_categoria.tolist()

script = f'''
    var categorias = {categorias};
    var numModelosDistintos = {num_modelos_distintos};

    var svgWidth = 600;
    var svgHeight = 400;

    var svg = d3.select("#grafico")
      .append("svg")
      .attr("width", svgWidth)
      .attr("height", svgHeight);

    var margin = {{ top: 20, right: 20, bottom: 50, left: 50 }};
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
'''

with open('script.js', 'w') as file:
    file.write(script)