import React, { useState } from "react";
import classes from "./BurgerMenu.module.css"
import MenuAction from "@/components/MenuAction/MenuAction.jsx";
const BurgerMenu = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleMenu = () => {
        setIsOpen(!isOpen);
    };

    return (
        <div>
            <div className={classes.burger_icon} onClick={toggleMenu}>
                {/* Иконка бургера: можно использовать текстовый символ или иконку */}
                <div>{isOpen ? "✖" : "☰"}</div>
            </div>
            {isOpen && (
                <div className={classes.menu}>
                    <MenuAction/>
                </div>
            )}
        </div>
    );
};

export default BurgerMenu;
