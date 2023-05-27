/* eslint-disable */
import axios from "axios";
import authHeader from "../../api/authHeader";

export const getMeData = async () => {
  try {
    const response = await axios.get("http://localhost:8000/me", authHeader());
    return response;
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};

export const getMyGroupData = async (groupId) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/groups/${groupId}`,
      authHeader()
    );
    return response;
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};

export const getMyBadge = async (badgeId) => {
  try {
    console.log("BadgeId:", badgeId);
    const response = await axios.get(
      `http://localhost:8000/badges/${badgeId}`,
      authHeader()
    );
    return response;
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};
