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

export const getBadges = async () => {
  try {
    // console.log("http://localhost:8000/badges");
    const response = await axios.get(
      "http://localhost:8000/badges",
      authHeader()
    );
    return response.data;
  } catch (error) {
    console.error("http://localhost:8000/badges", error);
  }
};

export const postBadge = async (data, userID) => {
  try {
    // console.log("otrzymany user id do post:");
    const response = await axios.post(
      "http://localhost:8000/badge_reports/",
      {
        title: data,
        status: "zgłoszona",
        user_id: userID,
        badge_id: 3,
      },
      authHeader()
    );
    console.error(response);
  } catch (error) {
    console.error("Error sending report: ", response);
  }
};
