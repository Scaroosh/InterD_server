import React, { useState } from "react";
import styles from "./ChatBotСonfiguration.module.css";

const ChatBotСonfiguration = () => {
  const [parameters, setParameters] = useState({
    cryptocurrency: "",
    tradeAmount: 0,
    strategy: "",
    interval: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setParameters((prevParameters) => ({
      ...prevParameters,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submitted parameters:", parameters);
  };

  return (
    <section className={styles.container}>
      <h2>Automated Cryptocurrency Trading Configuration</h2>
      <form onSubmit={handleSubmit}>
        <div className={styles.formGroup}>
          <label htmlFor="cryptocurrency">Cryptocurrency:</label>
          <input
            type="text"
            id="cryptocurrency"
            name="cryptocurrency"
            value={parameters.cryptocurrency}
            onChange={handleChange}
          />
        </div>
        <div className={styles.formGroup}>
          <label htmlFor="tradeAmount">Trade Amount:</label>
          <input
            type="number"
            id="tradeAmount"
            name="tradeAmount"
            value={parameters.tradeAmount}
            onChange={handleChange}
          />
        </div>
        <div className={styles.formGroup}>
          <label htmlFor="strategy">Trading Strategy:</label>
          <select
            id="strategy"
            name="strategy"
            value={parameters.strategy}
            onChange={handleChange}
          >
            <option value="">Select strategy...</option>
            <option value="scalping">Scalping</option>
            <option value="swing">Swing Trading</option>
            <option value="day">Day Trading</option>
          </select>
        </div>
        <div className={styles.formGroup}>
          <label htmlFor="interval">Trading Interval:</label>
          <select
            id="interval"
            name="interval"
            value={parameters.interval}
            onChange={handleChange}
          >
            <option value="">Select interval...</option>
            <option value="1h">1 hour</option>
            <option value="4h">4 hours</option>
            <option value="1d">1 day</option>
          </select>
        </div>
        <button type="submit">Submit</button>
      </form>
    </section>
  );
};

export default ChatBotСonfiguration;
