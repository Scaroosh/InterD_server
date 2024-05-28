import classes from "./Header.module.css"
import BurgerMenu from "@/components/BurgerMenu/BurgerMenu.jsx";
import MenuAction from "@/components/MenuAction/MenuAction.jsx";
import {NavLink} from "react-router-dom";

function Header() {
    return (
        <header className={classes.header}>
            <p className={classes.title}>
                <NavLink to={"/main_page"}>Automatic Trading Bot</NavLink>
            </p>


            <span className={classes.menu_action}><MenuAction/></span>
            <span className={classes.burger_menu}><BurgerMenu/></span>
        </header>
    )
}

export default Header