import { configureStore } from "@reduxjs/toolkit";
import authSlice from "./auth";

const store = configureStore({ reducer: { user: authSlice } });

export default store;
