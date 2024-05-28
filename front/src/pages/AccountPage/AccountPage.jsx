import classes from "./AccountPage.module.css";
import { useForm } from "react-hook-form";
import React, { useState } from "react";
import TemplatePage from "@/components/TemplatePage/TemplatePage.jsx";
import axios from "axios";
import { useDispatch } from "react-redux";

const AccountPage = () => {
  // noinspection JSUnusedLocalSymbols
  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm();

  const dispatch = useDispatch();

  const saveKeys = async (event) => {
    const meId = localStorage.getItem("meId");
    event.preventDefault();
    const formData = watch();
    if (meId) {
      const data = {
        id: meId,
        api_key: formData.api_key,
        api_secret: formData.api_secret,
      };
      const response = await axios.post(
        import.meta.env.VITE_SERVER_URL + "coinbase/save_keys",
        data
      );
      console.log(response);
    }
  };

  const deleteKeys = async (event) => {
    event.preventDefault();
    const meId = localStorage.getItem("meId");
    if (!meId) {
      console.log("You are not logged In");
    } else {
      const data = {
        id: meId,
      };
      const response = await axios.post(
        import.meta.env.VITE_SERVER_URL + "coinbase/delete_keys",
        data
      );
      console.log(response);
    }
  };

  const [showPassword, setShowPassword] = useState(false);

  return (
    <TemplatePage>
      <section className={classes.account_page}>
        <div className={classes.container}>
          <p className={classes.title}>Save Credentials</p>

          <form className={classes.form}>
            <label className={classes.label_text}>API Key</label>
            <input
              className={classes.input_form + " " + classes.key}
              type={"text"}
              placeholder={"organizations/***"}
              {...register("api_key", { required: true })}
            />
            {errors.key?.type === "required" && (
              <p role="alert" className={classes.error}>
                This field is required
              </p>
            )}
            <label className={classes.label_text}>API Secret</label>
            <div className={classes.inputContainer}>
              <input
                className={classes.input_form}
                type={showPassword ? "text" : "password"}
                placeholder={"-----BEGIN EC PRIVATE KEY-----\\***"}
                {...register("api_secret", { required: true })}
              />
              <i
                className={`fa ${showPassword ? "fa-eye-slash" : "fa-eye"} ${
                  classes.icon
                }`}
                onClick={() => setShowPassword(!showPassword)}
              />
            </div>
            {errors.secret?.type === "required" && (
              <p role="alert" className={classes.error}>
                This field is required
              </p>
            )}
            <div className={classes.btn_align}>
              <button
                className={classes.button}
                type={"Save keys"}
                onClick={saveKeys}
              >
                Save Keys
              </button>
              <button
                className={classes.button}
                type={"Delete keys"}
                onClick={deleteKeys}
              >
                Delete Keys
              </button>
            </div>
          </form>
        </div>
      </section>
    </TemplatePage>
  );
};

export default AccountPage;
