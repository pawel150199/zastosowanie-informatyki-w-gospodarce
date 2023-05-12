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
    console.log("Rank response:", response.data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const postLevelRaports = async (level, userID) => {
  try {
    const response = await axios.post(
      "http://localhost:8000/level_reports/",
      {
        title: level,
        status: "zgłoszona",
        user_id: userID,
      },
      authHeader()
    );
    console.log(response);
  } catch (error) {
    console.error("Error sending report:", response);
  }
};
