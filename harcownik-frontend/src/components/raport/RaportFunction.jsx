/* eslint-disable */
import axios from "axios";
import { async } from "regenerator-runtime";
import authHeader from "../../api/authHeader";

export const getLevelApplications = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/level_reports/",
      authHeader()
    );
    // console.log("GetLevelApplications: ", response);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getBadgesApplications = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/badge_reports/",
      authHeader()
    );
    // console.log("GetBadgeApplications: ", response);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getUsersData = async () => {
  try {
    const response = await axios.get(
      "http://localhost:8000/users/",
      authHeader()
    );
    // console.log("GetBadgeApplications: ", response);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
