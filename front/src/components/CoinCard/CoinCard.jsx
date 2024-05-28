import classes from "./CoinCard.module.css"
import CryptoDisplay from "@/components/CryptoDisplay/CryptoDisplay.jsx";

const CoinCard = () => {
    return(
        <section className={classes.container}>
            <ul className={classes.card_table}>
                <li className={classes.card}>
                    <div className={classes.card_center}>
                        <p className={classes.card_title}>BTC</p>
                        <div className={classes.card_text}>
                            <p>-Parameters</p>
                            <p>-Profit/Losses</p>
                        </div>
                    </div>
                </li>
                <li className={classes.card}>
                    <div className={classes.card_center}>
                        <p className={classes.card_title}>BTC</p>
                        <div className={classes.card_text}>
                            <p>-Parameters</p>
                            <p>-Profit/Losses</p>
                        </div>
                    </div>
                </li>
                <li className={classes.card}>
                    <div className={classes.card_center}>
                        <p className={classes.card_title}>BTC</p>
                        <div className={classes.card_text}>
                            <p>-Parameters</p>
                            <p>-Profit/Losses</p>
                        </div>
                    </div>
                </li>
                <li className={classes.black_card}>
                    <div className={classes.card_center}>
                        <p className={classes.card_title_black}>Select coin to see the balance</p>
                        <div className={classes.card_text_black}>
                            <p>(After parameters selection)</p>
                        </div>
                    </div>

                </li>
            </ul>

            <div>
                <CryptoDisplay/>
            </div>
        </section>
    )
}

export default CoinCard