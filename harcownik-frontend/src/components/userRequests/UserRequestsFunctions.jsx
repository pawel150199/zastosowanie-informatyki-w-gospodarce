/* eslint-disable */
import axios from "../../api/api";

import "./UserRequests.css";
import authHeader from "../../api/authHeader";

/*
Component providing function for communication with database. 
*/

export const getLevel = async () => {
  try {
    const response = await axios.get("/me/level_reports", authHeader());
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const postLevelRaports = async (level, userId, status) => {
  try {
    const response = await axios.post(
      "/me/level_reports/",
      {
        title: level,
        status: status,
        user_id: userId,
      },
      authHeader()
    );
    console.log("postLevelRaport:", response);
    window.location.reload();
  } catch (error) {
    console.error(error);
  }
};

export const getBadgeApplicationStatus = async () => {
  try {
    const response = await axios.get(`/me/badge_reports`, authHeader());
    return response.data;
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};

export const getLevelApplicationStatus = async () => {
  try {
    const response = await axios.get(`/me/level_reports`, authHeader());
    return response.data;
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};

export const getBadgeGroups = async () => {
  try {
    const response = await axios.get("/badges/groups", authHeader());
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getBadges = async (group) => {
  try {
    const response = await axios.get(`/badges/group/${group}`, authHeader());
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
    window.location.reload();
  } catch (error) {
    console.error(error);
  }
};
