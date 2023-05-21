/* eslint-disable */
import axios from "axios";

import "./UserRequests.css";
import authHeader from "../../api/authHeader";

export const getLevel = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/me/level_reports",
      authHeader()
    );
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const postLevelRaports = async (level, userId, status) => {
  try {
    const response = await axios.post(
      "http://localhost:8000/me/level_reports/",
      {
        title: level,
        status: status,
        user_id: userId,
      },
      authHeader()
    );
    console.log("postLevelRaport:", response);
  } catch (error) {
    console.error(error);
  }
};
