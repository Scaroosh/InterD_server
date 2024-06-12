import classes from "./ChatBotPage.module.css"
import TemplatePage from "@/components/TemplatePage/TemplatePage.jsx";
import CryptocurrencySearchOutput
    from "@/components/ChatBotPageComponents/CryptocurrencySearchOutput/CryptocurrencySearchOutput.jsx";
import ChatBotActionButtons from "@/components/ChatBotPageComponents/ChatBotActionButtons/ChatBotActionButtons.jsx";
import ChatBotСonfiguration from "@/components/ChatBotPageComponents/ChatBotСonfiguration/ChatBotСonfiguration.jsx";
import ChatBotTradingOutput from "@/components/ChatBotPageComponents/ChatBotTradingOutput/ChatBotTradingOutput.jsx";

const ChatBotPage = () => {
    return(
        <TemplatePage>
            <section>
                <p className={classes.title}>cryptocurrency searching</p>


                <CryptocurrencySearchOutput/>

                <p className={classes.title}>automated cryptocurrency trading</p>
                <ChatBotСonfiguration/>
                <ChatBotActionButtons/>
                <ChatBotTradingOutput/>
            </section>
        </TemplatePage>
    )
}


export default ChatBotPage