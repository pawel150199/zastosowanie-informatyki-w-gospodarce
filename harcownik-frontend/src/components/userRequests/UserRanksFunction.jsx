/* eslint-disable */
import axios from "axios";

import "./UserRequests.css";

export const getLevel = async () => {
  try {
    const response = await axios.get("http://localhost:8000/level_reports");
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const postLevelRaports = async (level) => {
  try {
    const response = await axios.post("http://localhost:8000/level_reports/", {
      title: level,
      status: "zgłoszona",
      user_id: 1,
    });
    console.log("Posted Report: ", response);
  } catch (error) {
    console.error("Error sending report:", response);
  }
};
