import TemplatePage from "@/components/TemplatePage/TemplatePage.jsx";
import classes from "./NewsPage.module.css";
import { useEffect, useState } from "react";

const NewsPage = () => {
  const [ticker, setTicker] = useState("BTC");
  const [source, setSource] = useState("YahooFinance");
  const [news, setNews] = useState([]);
  const [modalContent, setModalContent] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const fetchData = async (event) => {
    event.preventDefault();
    const url = import.meta.env.VITE_SERVER_URL + "news/get_news";
    const requestBody = {
      ticker: ticker,
      source: source,
      max_articles: 5,
    };

    try {
      const response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(requestBody),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setNews(data.articles[0].articles);
    } catch (error) {
      console.error("Problem with fetch operation:", error);
    }
  };

  const openModal = (article) => {
    setModalContent(article);
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const handleOverlayClick = (e) => {
    if (e.target.className.includes("modalOverlay")) {
      closeModal();
    }
  };

  return (
    <TemplatePage>
      <div className={classes.container}>
        <h1>News</h1>
        <form onSubmit={fetchData}>
          <input
            type="text"
            className={classes.searchBar}
            value={ticker}
            onChange={(e) => setTicker(e.target.value)}
            placeholder="Enter Ticker"
            required
            disabled
          />
          <select
            value={source}
            onChange={(e) => setSource(e.target.value)}
            className={classes.sourceSelect}
          >
            <option value="YahooFinance">Yahoo Finance</option>
            <option value="CryptoNews">Crypto News</option>
          </select>
          <button type="submit">Get News</button>
        </form>
        <div className={classes.cardsContainer}>
          {news.map((article, index) => (
            <div
              key={index}
              className={classes.card}
              onClick={() => openModal(article)}
            >
              <div className={classes.header}>{article.title}</div>
            </div>
          ))}
        </div>
        {isModalOpen && modalContent && (
          <div className={classes.modalOverlay} onClick={handleOverlayClick}>
            <div className={classes.modal} onClick={(e) => e.stopPropagation()}>
              <button onClick={closeModal} className={classes.closeButton}>
                ✖
              </button>
              <div className={classes.modalContent}>
                <h2>{modalContent.title}</h2>
                <p>{modalContent.text}</p>
                <p>Sentiment: {modalContent.sentiment}</p>
                <p>Polarity: {modalContent.sentiment_polarity.toFixed(3)}</p>
                <a
                  href={modalContent.url}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  source reference
                </a>
              </div>
            </div>
          </div>
        )}
      </div>
    </TemplatePage>
  );
};

export default NewsPage;
