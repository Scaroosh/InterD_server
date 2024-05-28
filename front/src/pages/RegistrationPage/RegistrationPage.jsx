import { useForm } from "react-hook-form";
import React, { useState } from "react";
import classes from "./RegistrationPage.module.css";
import SignUpBtn from "@/components/buttons/SignUp/SignUpBtn.jsx";
import SignInBtn from "@/components/buttons/SignIn/SignInBtn.jsx";
import TemplatePage from "@/components/TemplatePage/TemplatePage.jsx";
import axios from "axios";

const RegistrationPage = () => {
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();

  const onSubmit = async (data) => {
    const formattedData = {
      email: data.email,
      username: data.login,
      password: data.password,
    };
    const response = await axios.post(
      import.meta.env.VITE_SERVER_URL + "auth/register",
      formattedData
    );
    console.log(response);
  };

  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  return (
    <TemplatePage>
      <section className={classes.login_page}>
        <div className={classes.container}>
          <p className={classes.title}>Sign In</p>

          <form onSubmit={handleSubmit(onSubmit)} className={classes.form}>
            <label className={classes.label_text}>Email</label>
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

            <label className={classes.label_text}>Login</label>
            <input
              className={classes.input_form + " " + classes.user_icon}
              type={"text"}
              placeholder={"Login"}
              {...register("login", { required: true })}
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
                placeholder={"********"}
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

            <label className={classes.label_text}>Confirm Password</label>
            <div className={classes.inputContainer}>
              <input
                type={showConfirmPassword ? "text" : "password"}
                className={classes.input_form}
                placeholder="********"
                {...register("passwordConfirmation", {
                  required: "Confirm password is required",
                  validate: (value) =>
                    value === watch("password") || "The passwords do not match",
                })}
                aria-invalid={errors.passwordConfirmation ? "true" : "false"}
                id={errors.passwordConfirmation ? classes.errorInput : ""}
              />
              <i
                className={`fa ${
                  showConfirmPassword ? "fa-eye-slash" : "fa-eye"
                } ${classes.icon}`}
                onClick={() => setShowConfirmPassword(!showConfirmPassword)}
              />
            </div>

            {errors.passwordConfirmation && (
              <p role="alert" className={classes.error}>
                {errors.passwordConfirmation.message}
              </p>
            )}

            <div className={classes.btn_align}>
              <SignUpBtn />
              <SignInBtn />
            </div>
          </form>
        </div>
      </section>
    </TemplatePage>
  );
};

export default RegistrationPage;
