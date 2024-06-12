import React, { useState } from "react";
import axios from "axios";
import classes from "./CryptocurrencySearchOutput.module.css";

const CryptocurrencySearchOutput = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [cryptoInfo, setCryptoInfo] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async () => {
    setLoading(true);
    setError(null);
    setCryptoInfo(null);

    try {
      // Replace with a suitable API endpoint for cryptocurrency information
      const response = await axios.get(
        `https://api.coingecko.com/api/v3/coins/${searchTerm.toLowerCase()}`
      );
      setCryptoInfo(response.data);
    } catch (err) {
      setError("Could not fetch data. Please check the cryptocurrency name.");
    }

    setLoading(false);
  };

  return (
    <section className={classes.container}>
      <div className={classes.searchContainer}>
        <input
          type="text"
          placeholder="Enter cryptocurrency name"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>
      {loading && <p>Loading...</p>}
      {error && <p className={classes.error}>{error}</p>}
      {cryptoInfo && (
        <div className={classes.cryptoInfo}>
          <h2>{cryptoInfo.name} ({cryptoInfo.symbol.toUpperCase()})</h2>
          <p>Current Price: ${cryptoInfo.market_data.current_price.usd}</p>
          <p>Market Cap: ${cryptoInfo.market_data.market_cap.usd}</p>
          <p>24h High: ${cryptoInfo.market_data.high_24h.usd}</p>
          <p>24h Low: ${cryptoInfo.market_data.low_24h.usd}</p>
        </div>
      )}
    </section>
  );
};

export default CryptocurrencySearchOutput;
