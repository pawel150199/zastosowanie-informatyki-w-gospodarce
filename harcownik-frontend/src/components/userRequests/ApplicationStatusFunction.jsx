/* eslint-disable */
import axios from "../../api/api";

import authHeader from "../../api/authHeader";

import "./UserRequests.css";

export const getBadgeApplicationStatus = async () => {
  try {
    const response = await axios.get(
      `/me/badge_reports`,
      authHeader()
    );
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
    const response = await axios.get(
      `/me/level_reports`,
      authHeader()
    );
    return response.data;
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};
