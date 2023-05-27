/* eslint-disable */
import axios from "axios";
import { async } from "regenerator-runtime";
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
    console.log("GRIUP ID:", groupId);
    const response = await axios.get(
      `http://localhost:8000/groups/${groupId}`,
      authHeader()
    );
    console.log("getMyGroupsResponse:", response.data);
    return response;
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};
