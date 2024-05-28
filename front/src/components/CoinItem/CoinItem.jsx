import classes from "./CoinItem.module.css"
import polygonIcon from "@/assets/icons/polygon.svg"
const CoinItem = () => {
    return (
        <section>
            <ul className={classes.card_container}>
                <li className={classes.coin_item_card}>
                    <p className={classes.title}>Silver</p>
                    <div className={classes.hidden_things}>
                        <p className={classes.change}>growth expected</p>
                        <span className={classes.price}><img src={polygonIcon} alt="polygonIcon"/>+0,99%</span>
                    </div>
                </li>
                <li className={classes.coin_item_card}>
                    <p className={classes.title}>Ethereum</p>
                    <div className={classes.hidden_things}>
                        <p className={classes.change}>growth expected</p>
                        <span className={classes.price}><img src={polygonIcon} alt="polygonIcon"/>+30,46%</span>
                    </div>
                </li>
                <li className={classes.coin_item_card}>
                    <p className={classes.title}>Solana</p>
                    <div className={classes.hidden_things}>
                        <p className={classes.change}>growth expected</p>
                        <span className={classes.price}><img src={polygonIcon} alt="polygonIcon"/>+23,26%</span>
                    </div>
                </li>
                <li className={classes.coin_item_card}>
                    <p className={classes.title}>Avax</p>
                    <div className={classes.hidden_things}>
                        <p className={classes.change}>growth expected</p>
                        <span className={classes.price}><img src={polygonIcon} alt="polygonIcon"/>+27,95%</span>
                    </div>
                </li>
            </ul>
        </section>
    )
}

export default CoinItem