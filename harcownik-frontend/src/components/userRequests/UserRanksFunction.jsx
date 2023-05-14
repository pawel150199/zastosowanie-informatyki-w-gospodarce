/* eslint-disable */
import axios from "axios";

import "./UserRequests.css";
import authHeader from "../../api/authHeader";

export const getLevel = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/level_reports",
      authHeader()
    );
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const postLevelRaports = async (level, userId) => {
  try {
    const response = await axios.post(
      "http://localhost:8000/level_reports/",
      {
        title: level,
        status: "zgłoszona",
        user_id: userId,
      },
      authHeader()
    );
  } catch (error) {
    console.error(error);
  }
};
