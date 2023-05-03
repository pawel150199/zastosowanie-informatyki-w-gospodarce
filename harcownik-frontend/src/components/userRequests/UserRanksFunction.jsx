/* eslint-disable */
import "./UserRequests.css";
import axios from "axios";

export const getLevel = async () => {
  try {
    const response = await axios.get("http://localhost:8000/level_reports");
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const postLevelRaports = async (level) => {
  try {
    const response = await axios.post("http://localhost:8000/level_reports/", {
      title: level,
      status: "zgłoszona",
      user_id: 1,
    });
    console.error(response);
  } catch (error) {
    console.error("Error sending report:", response);
  }
};
