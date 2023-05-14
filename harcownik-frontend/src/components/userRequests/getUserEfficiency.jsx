/* eslint-disable */
import axios from "axios";

import "./UserRequests.css";
import authHeader from "../../api/authHeader";

export const getBadgeGroups = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/badges/groups",
      authHeader()
    );
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getBadges = async (group) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/badges/group/${group}`,
      authHeader()
    );
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const postBadge = async (data, userID, badgeID) => {
  try {
    const response = await axios.post(
      "http://localhost:8000/badge_reports/",
      {
        title: data,
        status: "zgłoszona",
        user_id: userID,
        badge_id: badgeID,
      },
      authHeader()
    );
  } catch (error) {
    console.error(error);
  }
};
