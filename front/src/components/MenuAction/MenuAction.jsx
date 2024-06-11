import classes from "./MenuAction.module.css";
import { NavLink } from "react-router-dom";
import userIcon from "@/assets/icons/user_icon.svg";
import { IoIosLogOut } from "react-icons/io";
import { userLogOut } from "../../store/auth";
import { useDispatch } from "react-redux";

const MenuAction = () => {
  const dispatch = useDispatch();

  const onSubmit = () => {
    dispatch(userLogOut({}));
  };

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
      <IoIosLogOut style={{ fontSize: "2em" }} onClick={onSubmit}></IoIosLogOut>
    </section>
  );
};

export default MenuAction;
