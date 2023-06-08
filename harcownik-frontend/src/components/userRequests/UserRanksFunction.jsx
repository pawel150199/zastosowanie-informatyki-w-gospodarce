/* eslint-disable */
import axios from "../../api/api";

import "./UserRequests.css";
import authHeader from "../../api/authHeader";

/*
Component providing function for communication with database. 
*/

export const getLevel = async () => {
  try {
    const response = await axios.get("/me/level_reports", authHeader());
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const postLevelRaports = async (level, userId, status) => {
  try {
    const response = await axios.post(
      "/me/level_reports/",
      {
        title: level,
        status: status,
        user_id: userId,
      },
      authHeader()
    );
    console.log("postLevelRaport:", response);
    window.location.reload();
  } catch (error) {
    console.error(error);
  }
};
