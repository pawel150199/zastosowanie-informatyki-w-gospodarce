/* eslint-disable */
import axios from "axios";

import authHeader from "../../api/authHeader";

import "./UserRequests.css";

export const getBadgeApplicationStatus = async (userID) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/badge_reports/user/${userID}`,
      authHeader()
    );
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getLevelApplicationStatus = async (userID) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/level_reports/user/${userID}`,
      authHeader()
    );
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
