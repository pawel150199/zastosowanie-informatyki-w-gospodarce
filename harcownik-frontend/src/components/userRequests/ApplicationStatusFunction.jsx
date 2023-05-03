/* eslint-disable */
import "./UserRequests.css";
import axios from "axios";

export const getBadgeApplicationStatus = async () => {
  try {
    const response = await axios.get("http://localhost:8000/badge_reports/");
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getLevelApplicationStatus = async () => {
  try {
    const response = await axios.get("http://localhost:8000/level_reports/");
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
