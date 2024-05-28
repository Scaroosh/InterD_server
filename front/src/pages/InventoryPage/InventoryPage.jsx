import TemplatePage from "@/components/TemplatePage/TemplatePage.jsx";
import CoinItem from "@/components/CoinItem/CoinItem.jsx";
import SearchBar from "@/components/SearchBar/SearchBar.jsx";
import classes from "./InventoryPage.module.css";
import Items from "@/components/Items/Items.jsx";
import store from "../../store/store";
import axios from "axios";
import { useEffect, useState } from "react";

const InventoryPage = () => {
  const [coins, setCoins] = useState([]);
  const meStatus = localStorage.getItem("meStatus");
  const meId = localStorage.getItem("meId");
  if (!meStatus) {
    console.log("Authentification required");
  } else {
    useEffect(() => {
      async function fetchUserCoins() {
        const formattedData = {
          id: meId,
        };
        const response = await axios.post(
          import.meta.env.VITE_SERVER_URL + "coinbase/get_coins",
          formattedData
        );
        setCoins(response.data.coins);
      }
      fetchUserCoins();
    }, []);
  }
  return (
    <TemplatePage>
      <div>
        <CoinItem />
        <p className={classes.title}>Assets</p>
        <SearchBar />
        <Items coins={coins} />
      </div>
    </TemplatePage>
  );
};

export default InventoryPage;
