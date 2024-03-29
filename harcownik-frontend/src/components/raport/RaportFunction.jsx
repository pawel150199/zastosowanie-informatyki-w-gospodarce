/* eslint-disable */
import axios from "../../api/api";
import authHeader from "../../api/authHeader";

/*
Component providing function for communication with database. 
*/
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
      `/badge_report/${badgeId}`,
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
      `/level_report/${badgeId}`,
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

export const postPdfRaport = async (name, userId, file) => {
  try {
    const response = await axios.post(
      `/report/pdf`,
      {
        name: name,
        user_id: userId,
        file: file,
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

export const getLevelRaportData = async (levelRaportId) => {
  try {
    const response = await axios.get(
      `/level_reports/${levelRaportId}`,
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

export const addLevelToUser = async (userId, level) => {
  try {
    const response = await axios.put(
      `/user/${userId}`,
      {
        level: level,
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

export const getBadgeRaportData = async (badge_id) => {
  try {
    const response = await axios.get(
      `/badge_reports/${badge_id}`,
      authHeader()
    );
    console.log("REsponse:", response);
    return response.data;
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};

export const addBadgeToUser = async (userId, badgeId) => {
  try {
    const response = await axios.put(
      `/user/${userId}`,
      {
        badge_ids: [badgeId],
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
