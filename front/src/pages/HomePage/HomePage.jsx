import TemplatePage from "@/components/TemplatePage/TemplatePage.jsx";
import {NavLink} from "react-router-dom";
import classes from "./HomePage.module.css"
function HomePage() {
    return (
        <TemplatePage>
            <div className={classes.container}>
                <NavLink className={classes.test_btn} to={"/login"}>login</NavLink>
                <NavLink className={classes.test_btn} to={"/registration"}>register</NavLink>
            </div>
        </TemplatePage>
    )
}

export default HomePage