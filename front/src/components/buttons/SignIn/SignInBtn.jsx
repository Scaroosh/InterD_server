import classes from "./SignInBtn.module.css"

const SignInBtn = () => {
    return(
        <>
            <button className={classes.sign_in} type={"submit"}>Sign In</button>
        </>
    )
}

export default SignInBtn