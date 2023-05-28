/* eslint-disable */
import axios from "../../api/api";

import "./UserRequests.css";
import authHeader from "../../api/authHeader";

export const getBadgeGroups = async () => {
  try {
    const response = await axios.get(
      "/badges/groups",
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
      `/badges/group/${group}`,
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
      "/me/badge_reports/",
      {
        title: data,
        status: status,
        user_id: userID,
        badge_id: badgeID,
      },
      authHeader()
    );
    console.log("postBadge:", response);
    window.location.reload();
  } catch (error) {
    console.error(error);
  }
};
