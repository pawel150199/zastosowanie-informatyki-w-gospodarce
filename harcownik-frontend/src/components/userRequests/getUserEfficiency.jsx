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

export const postBadge = async (data, userID, badgeID, status) => {
  try {
    const response = await axios.post(
      "http://localhost:8000/me/badge_reports/",
      {
        title: data,
        status: status,
        user_id: userID,
        badge_id: badgeID,
      },
      authHeader()
    );
    console.log("postBadge:", response);
  } catch (error) {
    console.error(error);
  }
};
