import classes from "./ChatBotPage.module.css";
import TemplatePage from "@/components/TemplatePage/TemplatePage.jsx";
import CryptocurrencySearchOutput from "@/components/ChatBotPageComponents/CryptocurrencySearchOutput/CryptocurrencySearchOutput.jsx";
import ChatBotActionButtons from "@/components/ChatBotPageComponents/ChatBotActionButtons/ChatBotActionButtons.jsx";
import ChatBotChart from "@/components/ChatBotPageComponents/ChatBotPageComponents/ChatBotChart/ChatBotChart.jsx";

const ChatBotPage = () => {
  return (
    <TemplatePage>
      <section>
        <p className={classes.title}>Crypto Analyzer</p>

        <CryptocurrencySearchOutput />

        <p className={classes.title}>Automated cryptocurrency trading</p>
        <ChatBotActionButtons />

        <p className={classes.title}>Chart</p>
        <ChatBotChart />
      </section>
    </TemplatePage>
  );
};

export default ChatBotPage;
