import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from "@/pages/HomePage/HomePage.jsx";
import AboutPage from "@/pages/AboutPage/AboutPage.jsx";
import NonePage from "@/pages/NonePage.jsx";
import LoginPage from "@/pages/LoginPage/LoginPage.jsx";
import RegistrationPage from "@/pages/RegistrationPage/RegistrationPage.jsx";
import MainPage from "@/pages/MainPage/MainPage.jsx";
import NewsPage from "@/pages/NewsPage/NewsPage.jsx";
import InventoryPage from "@/pages/InventoryPage/InventoryPage.jsx";
import Coins from "@/pages/CoinsPage/Coins.jsx";
import AccountPage from "@/pages/AccountPage/AccountPage.jsx";
import ChatBotPage from "@/pages/ChatBotPage/ChatBotPage.jsx";

export default function Routers() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="*" element={<NonePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/registration" element={<RegistrationPage />} />
        <Route path="/main_page" element={<MainPage />} />
        <Route path="/news_page" element={<NewsPage />} />
        <Route path="/inventory_page" element={<InventoryPage />} />
        <Route path="/coins_page" element={<Coins />} />
        <Route path="/account_page" element={<AccountPage />} />
        <Route path="/chat_bot" element={<ChatBotPage/>}/>
      </Routes>
    </BrowserRouter>
  );
}
