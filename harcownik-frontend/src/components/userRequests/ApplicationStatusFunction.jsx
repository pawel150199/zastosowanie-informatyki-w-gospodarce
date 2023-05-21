/* eslint-disable */
import axios from "axios";

import authHeader from "../../api/authHeader";

import "./UserRequests.css";

export const getBadgeApplicationStatus = async () => {
  try {
    const response = await axios.get(
      `http://localhost:8000/me/badge_reports`,
      authHeader()
    );
    console.log("me/badge_reports:", response.data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getLevelApplicationStatus = async () => {
  try {
    const response = await axios.get(
      `http://localhost:8000/me/level_reports`,
      authHeader()
    );
    console.log("me/level_reports:", response.data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
