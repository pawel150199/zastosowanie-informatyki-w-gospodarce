/* eslint-disable */
import axios from "axios";

import "./UserRequests.css";

export const getBadgeApplicationStatus = async () => {
  try {
    const response = await axios.get("http://localhost:8000/badge_reports/");
    console.log("Response Data: ", response.data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getLevelApplicationStatus = async () => {
  try {
    const response = await axios.get("http://localhost:8000/level_reports/");
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
