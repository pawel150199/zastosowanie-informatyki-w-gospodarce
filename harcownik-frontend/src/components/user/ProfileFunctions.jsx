/* eslint-disable */
import axios from "../../api/api";
import authHeader from "../../api/authHeader";

export const getMeData = async () => {
  try {
    const response = await axios.get("/me", authHeader());
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
      `/groups/${groupId}`,
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
    const response = await axios.get(
      `/badges/${badgeId}`,
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
