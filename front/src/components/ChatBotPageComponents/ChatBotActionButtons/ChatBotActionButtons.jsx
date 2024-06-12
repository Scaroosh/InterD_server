import classes from "./ChatBotActionButtons.module.css"

const ChatBotActionButtons = () => {
    return(
        <>
            <div className={classes.container}>
                <button className={classes.buttons}>start</button>
                <button className={classes.buttons}>stop</button>
                <button className={classes.buttons}>pause</button>
                <button className={classes.buttons}>remove</button>
            </div>
        </>
    )
}


export default ChatBotActionButtons;