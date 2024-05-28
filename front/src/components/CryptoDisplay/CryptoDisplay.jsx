import React from 'react';
import classes from './CryptoDisplay.module.css'; // Import as a module

const CryptoDisplay = () => {
    return (
        <>
            <p className={classes.title}>Bitcoin/U.S. Dollar</p>
            <p className={classes.crypto_details}>Spot • Crypto</p>
            <div className={classes.value_table}>
                <p className={classes.price}>620<span>90</span> USD</p>
                <p className={classes.percent}>557 (0.91%)</p>
            </div>
            <p className={classes.market_status}>Market <span>•</span> Open</p>
        </>
    );
}

export default CryptoDisplay;
