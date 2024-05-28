import classes from "./MenuAction.module.css";
import { NavLink } from "react-router-dom";
import userIcon from "@/assets/icons/user_icon.svg";

const MenuAction = () => {
  return (
    <section className={classes.container}>
      <ul className={classes.user_action_table}>
        <li className={classes.user_action_list}>
          <NavLink className={classes.user_action_list_text} to={"/coins_page"}>
            Coins
          </NavLink>
        </li>
        <li className={classes.user_action_list}>
          <NavLink className={classes.user_action_list_text} to={"/news_page"}>
            News
          </NavLink>
        </li>
        <li className={classes.user_action_list}>
          <NavLink
            className={classes.user_action_list_text}
            to={"/inventory_page"}
          >
            Inventory
          </NavLink>
        </li>
      </ul>

      <NavLink to={"/account_page"}>
        <img src={userIcon} alt="user_icon" />
      </NavLink>
    </section>
  );
};

export default MenuAction;
