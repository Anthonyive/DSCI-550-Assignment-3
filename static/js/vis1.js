const DUMMY_DATA = [
  { id: 'd1', value: 10, region: 'USA'},
  { id: 'd2', value: 11, region: 'India'},
  { id: 'd3', value: 2, region: 'China'},
  { id: 'd4', value: 3, region: 'Germany'},
  { id: 'd5', value: 5, region: 'Japan'},
];

const container = d3.select('#vis1')
  .classed('container jumbotron text-center', true)
  .style('border', '1px solid red');

container.selectAll('.bar')
  .data(DUMMY_DATA)
  .enter()
  .append('div')
  .classed('bar', true)
  .attr('width', '50px')
  .style('height');