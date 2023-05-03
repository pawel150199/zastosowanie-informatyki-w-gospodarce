/* eslint-disable */
import axios from "axios";

export const getLevelApplications = async () => {
  try {
    const response = await axios.get("http://localhost:8000/level_reports/");
    console.log("GetLevelApplications", response);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getBadgesApplications = async () => {
  try {
    const response = await axios.get("http://localhost:8000/badge_reports/");
    console.log("GetBadgeApplications", response);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
