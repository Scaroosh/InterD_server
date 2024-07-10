import React, { useState } from "react";
import Plot from "react-plotly.js";
import axios from "axios";
import classes from "./ChatBotChart.module.css";

const ChatBotChart = () => {
  const [ticker, setTicker] = useState();
  const [days, setDays] = useState();
  const [plotData, setPlotData] = useState({});
  const [selectedIndicators, setSelectedIndicators] = useState({
    volume: true,
    rsi: true,
    macd: true,
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    if (name === "ticker") {
      setTicker(value);
    } else if (name === "days") {
      setDays(value);
    }
  };

  const handleIndicatorChange = (event) => {
    const { name, checked } = event.target;
    setSelectedIndicators((prevState) => ({
      ...prevState,
      [name]: checked,
    }));
  };

  const fetchData = async () => {
    try {
      const response = await axios.post(
        import.meta.env.VITE_SERVER_URL + "api/data",
        {
          ticker,
          days,
          indicators: selectedIndicators,
        }
      );
      setPlotData(JSON.parse(response.data));
    } catch (error) {
      console.error("Error fetching plot data:", error);
    }
  };

  const handleKeyPress = (event) => {
    if (event.key === "Enter") {
      fetchData();
    }
  };

  return (
    <div className={classes.container}>
      <div className={classes.inputGroup}>
        <p></p>
        <input
          className={classes.input}
          type="text"
          name="ticker"
          value={ticker}
          onChange={handleInputChange}
          onKeyPress={handleKeyPress}
          placeholder={"Coin Name: like->AAPL"}
        />
        <input
          className={classes.input}
          type="number"
          name="days"
          value={days}
          onChange={handleInputChange}
          onKeyPress={handleKeyPress}
          placeholder={"Days:"}
        />
        <button onClick={fetchData}>Load Data</button>
      </div>
      <div className={classes.checkboxGroup}>
        <label>
          <input
            type="checkbox"
            name="volume"
            checked={selectedIndicators.volume}
            onChange={handleIndicatorChange}
          />
          Volume
        </label>
        <label>
          <input
            type="checkbox"
            name="rsi"
            checked={selectedIndicators.rsi}
            onChange={handleIndicatorChange}
          />
          RSI
        </label>
        <label>
          <input
            type="checkbox"
            name="macd"
            checked={selectedIndicators.macd}
            onChange={handleIndicatorChange}
          />
          MACD
        </label>
      </div>
      {plotData.data && (
        <div className={classes.plotContainer}>
          <Plot
            data={plotData.data}
            layout={plotData.layout}
            style={{ width: "100%", height: "640px" }}
          />
        </div>
      )}
    </div>
  );
};

export default ChatBotChart;
