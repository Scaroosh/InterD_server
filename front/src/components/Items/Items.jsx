import classes from "./Items.module.css";

const Items = ({ coins }) => {
  return (
    <>
      <div>
        <ul className={classes.container}>
          {coins.map((coin) => {
            return (
              <li className={classes.item}>
                <p className={classes.title}>{coin.currency}</p>
                <div className={classes.price_container}>
                  <p className={classes.price}>{coin.value}</p>
                </div>
              </li>
            );
          })}
        </ul>
      </div>
    </>
  );
};

export default Items;
