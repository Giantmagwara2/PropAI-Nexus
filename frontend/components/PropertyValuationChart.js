import Plot from 'react-plotly.js';

export default function PropertyValuationChart() {
  return (
    <Plot
      data={[{
        x: ['2021', '2022', '2023'],
        y: [250000, 270000, 290000],
        type: 'scatter',
        mode: 'lines+markers',
        marker: {color: 'blue'},
      }]}
      layout={{ title: 'Property Value Over Time' }}
    />
  );
}
