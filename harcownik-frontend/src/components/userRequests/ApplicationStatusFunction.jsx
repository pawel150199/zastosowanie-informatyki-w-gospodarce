/* eslint-disable */
import axios from "axios";

import getMe from "../../api/getMe";

import "./UserRequests.css";

export const getBadgeApplicationStatus = async (userID) => {
  try {
    console.log("userID inside status function:", userID);
    const myURL_ = `http://localhost:8000/badge_reports/user/${userID}`;
    const response = await axios.get(myURL_);
    console.log("url: ", myURL_);

    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const getLevelApplicationStatus = async (userID) => {
  try {
    // const myURL = `http://localhost:8000/level_reports/user/${userID}`;
    const myURL_ = `http://localhost:8000/level_reports/user/${userID}`;
    const response = await axios.get(myURL_);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
