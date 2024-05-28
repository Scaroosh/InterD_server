import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  user: { id: 1, user_id: null, status: "anonymous" },
};

export const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    userLogin: (state, action) => {
      const userId = action.payload.payload;
      state.user.user_id = userId;
      state.user.status = "loggedIn";
      localStorage.setItem("meId", userId);
      localStorage.setItem("meStatus", "loggedIn");
    },
  },
});

export const { userLogin } = authSlice.actions;

export default authSlice.reducer;
