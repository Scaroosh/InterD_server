import React, { useState } from "react";
import axios from "axios";
import JSONPretty from "react-json-pretty";
import "react-json-pretty/themes/monikai.css"; // подключаем тему для react-json-pretty
import classes from "./CryptocurrencySearchOutput.module.css";

const CryptocurrencySearchOutput = () => {
  const [cryptoSymbol, setCryptoSymbol] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setLoading(true);

    try {
      const response = await axios.post(
        import.meta.env.VITE_SERVER_URL + "crypto/analyze",
        { crypto_symbol: cryptoSymbol }
      );
      setResult(response.data);
    } catch (err) {
      setError("Error fetching data. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={classes.container}>
      <form onSubmit={handleSubmit} className={classes.form}>
        <input
          type="text"
          className={classes.input}
          placeholder="Cryptocurrency Symbol"
          value={cryptoSymbol}
          onChange={(e) => setCryptoSymbol(e.target.value)}
          required
        />
        <button type="submit" className={classes.button}>
          Analyze
        </button>
      </form>
      {loading && <div className={classes.loading}>Loading...</div>}
      {error && <div className={classes.alert}>{error}</div>}
      {result && !loading && (
        <div className={classes.result}>
          <h6>Analysis Result</h6>
          <JSONPretty
            data={result}
            style={{ whiteSpace: "pre-wrap" }}
          ></JSONPretty>
        </div>
      )}
    </div>
  );
};

export default CryptocurrencySearchOutput;
