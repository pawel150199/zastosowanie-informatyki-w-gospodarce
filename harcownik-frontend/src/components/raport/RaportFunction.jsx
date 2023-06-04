/* eslint-disable */
import axios from "../../api/api";
import authHeader from "../../api/authHeader";

export const getLevelApplications = async () => {
  try {
    const response = await axios.get("/group/level_reports/", authHeader());
    return response.data;
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};

export const getBadgesApplications = async () => {
  try {
    const response = await axios.get("/group/badge_reports/", authHeader());
    return response.data;
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};

export const getUsersData = async () => {
  try {
    const response = await axios.get("/users/", authHeader());
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

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

export const getMyGroupData = async () => {
  try {
    const response = await axios.get("/me/group", authHeader());
    return response.data;
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};

export const updateBadgesApplications = async (badgeId, status) => {
  try {
    const response = await axios.put(
      `http://localhost:8000/badge_report/${badgeId}`,
      {
        status: status,
      },
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

export const updateLevelApplications = async (badgeId, status) => {
  try {
    const response = await axios.put(
      `http://localhost:8000/level_report/${badgeId}`,
      {
        status: status,
      },
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
