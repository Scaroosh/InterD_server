import classes from "./LoginPage.module.css";
import { useForm } from "react-hook-form";
import SignUpBtn from "@/components/buttons/SignUp/SignUpBtn.jsx";
import SignInBtn from "@/components/buttons/SignIn/SignInBtn.jsx";
import React, { act, useState } from "react";
import TemplatePage from "@/components/TemplatePage/TemplatePage.jsx";
import axios from "axios";
import store from "../../store/store";
import { userLogin } from "../../store/auth";
import { useDispatch } from "react-redux";
const LoginPage = () => {
  // noinspection JSUnusedLocalSymbols
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();

  const dispatch = useDispatch();

  const onSubmit = async (data) => {
    const formattedData = {
      email: data.email,
      username: data.login,
      password: data.password,
    };
    const response = await axios.post(
      import.meta.env.VITE_SERVER_URL + "auth/login",
      formattedData
    );
    const action = dispatch(userLogin({ payload: response.data.user_id }));
    if (action.type == "auth/userLogin" && action.payload) {
      window.open("/");
    }
  };

  const [showPassword, setShowPassword] = useState(false);

  return (
    <TemplatePage>
      <section className={classes.login_page}>
        <div className={classes.container}>
          <p className={classes.title}>Sign In</p>

          <form onSubmit={handleSubmit(onSubmit)} className={classes.form}>
            <label className={classes.label_text}>Email or Login</label>
            <input
              className={classes.input_form + " " + classes.email_icon}
              type={"email"}
              placeholder={"example@gmail.com"}
              {...register("email", { required: true })}
            />
            {errors.email?.type === "required" && (
              <p role="alert" className={classes.error}>
                This field is required
              </p>
            )}
            <label className={classes.label_text}>Password</label>
            <div className={classes.inputContainer}>
              <input
                className={classes.input_form}
                type={showPassword ? "text" : "password"}
                placeholder={"password"}
                {...register("password", { required: true })}
              />
              <i
                className={`fa ${showPassword ? "fa-eye-slash" : "fa-eye"} ${
                  classes.icon
                }`}
                onClick={() => setShowPassword(!showPassword)}
              />
            </div>
            {errors.password?.type === "required" && (
              <p role="alert" className={classes.error}>
                This field is required
              </p>
            )}
            <div className={classes.btn_align}>
              <SignUpBtn />
              <SignInBtn />
            </div>
          </form>
          <p className={classes.forgot_password_text}>Forgot your password?</p>
        </div>
      </section>
    </TemplatePage>
  );
};

export default LoginPage;
