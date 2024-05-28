import classes from "./CoinsPrice.module.css"

const CoinsPrice = () => {
    return(
        <section className={classes.container}>
            <ul className={classes.price_table}>
                <li><p>BNB</p></li>
                <li className={classes.price}>
                    <p>608,947USD</p>
                    <p className={classes.gold_ring}>+4,16%</p>
                </li>
            </ul>
            <ul className={classes.price_table}>
                <li><p>BTC</p></li>
                <li className={classes.price}>
                    <p>69444,20USD</p>
                    <p className={classes.gold_ring}>-0,32%</p>
                </li>
            </ul>
            <ul className={classes.price_table}>
                <li><p>ETH</p></li>
                <li className={classes.price}>
                    <p>3733,71USD</p>
                    <p className={classes.gold_ring}>+8,68%</p>
                </li>
            </ul>
        </section>
    )
}

export default CoinsPrice