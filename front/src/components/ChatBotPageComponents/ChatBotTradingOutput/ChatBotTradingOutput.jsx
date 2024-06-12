import classes from "./ChatBotTradingOutput.module.css"
import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

// Register Chart.js components
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const ChatBotTradingOutput = () => {
  const [chartData, setChartData] = useState({});
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('https://api.coindesk.com/v1/bpi/historical/close.json')
      .then(response => response.json())
      .then(data => {
        const labels = Object.keys(data.bpi);
        const prices = Object.values(data.bpi);

        setChartData({
          labels,
          datasets: [
            {
              label: 'BTC Price',
              data: prices,
              fill: false,
              backgroundColor: 'rgba(75,192,192,0.2)',
              borderColor: 'rgba(75,192,192,1)',
            },
          ],
        });
        setLoading(false);
      });
  }, []);

  return (
    <>
      <section className={classes.container}>
        {loading ? (
          <p>Loading data...</p>
        ) : (
          <>
            <h2>BTC Price Chart</h2>
            <Line data={chartData} />
          </>
        )}
      </section>
    </>
  );
};

export default ChatBotTradingOutput;
