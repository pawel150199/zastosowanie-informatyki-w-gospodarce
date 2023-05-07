/* eslint-disable */
import axios from "axios";

import "./UserRequests.css";

export const getBadgeGroups = async () => {
  try {
    const response = await axios.get("http://localhost:8000/level_reports");
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getBadges = async () => {
  try {
    const response = await axios.get("http://localhost:8000/badges");
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const postBadge = async (data) => {
  try {
    const response = await axios.post("http://localhost:8000/badge_reports/", {
      title: data,
      status: "zgłoszona",
      user_id: 1,
      badge_id: 3,
    });
    console.error(response);
  } catch (error) {
    console.error("Error sending report: ", response);
  }
};
