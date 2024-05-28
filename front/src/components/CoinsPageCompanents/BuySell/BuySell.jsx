import classes from "./BuySell.module.css"
const BuySell = () => {
    return(
        <>
            <div className={classes.trade_container}>
                <ul className={classes.trade_table}>
                    <li><p className={classes.trade_buy}>BUY</p></li>
                    <div className={classes.verticalLine}></div>
                    <li><p className={classes.trade_sell}>SELL</p></li>
                </ul>
                <span className={classes.line}></span>


                <ul className={classes.trade_option_container}>
                    <li>
                        <p>BUY</p>
                        <select className={classes.trade_option}>
                            <option value="option1"> ***</option>
                            <option value="option2"> ***</option>
                        </select>
                    </li>
                    <li>
                        <p>SELL</p>
                        <select className={classes.trade_option}>
                            <option value="option1"> ***</option>
                            <option value="option2"> ***</option>
                        </select>
                    </li>
                </ul>
            </div>

        </>
    )
}

export default BuySell