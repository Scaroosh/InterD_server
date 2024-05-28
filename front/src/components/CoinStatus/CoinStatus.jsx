import classes from "./CoinStatus.module.css"
import diagrams from "@/assets/diagrams.png"

const CoinStatus = () => {
    return(
        <div className={classes.container}>
            <img id={classes.diagram_img} src={diagrams} alt="diagrams"/>
            <div>
                <p className={classes.title}>Key Stats</p>
                <div className={classes.table_container}>
                    <ul>
                        <li>Volume</li>
                        <li>Average Volume(30D)</li>
                        <li>Trading volume 24h</li>
                        <li>Market Capitalization</li>
                        <li>Fully  diluted market cap</li>
                        <li>Volume/Market Cap</li>
                        <li>Circulating supply</li>
                    </ul>
                    <ul>
                        <li>336.12</li>
                        <li>1.79K</li>
                        <li>28.33B</li>
                        <li>1.21T</li>
                        <li>1.29T</li>
                        <li>0.0234</li>
                        <li>19.70M</li>
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default CoinStatus