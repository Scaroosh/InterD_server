import TemplatePage from "@/components/TemplatePage/TemplatePage.jsx";
import classes from "./Coins.module.css";
import CoinsPrice from "@/components/CoinsPageCompanents/CoinsPrice/CoinsPrice.jsx";
import BuySell from "@/components/CoinsPageCompanents/BuySell/BuySell.jsx";
const Coins = () => {
    return(
        <TemplatePage>
            <p className={classes.title}>Buy cryptocurrency.</p>
            <div className={classes.container}>
                <CoinsPrice/>
                <BuySell/>
            </div>
        </TemplatePage>
    )
}

export default Coins;