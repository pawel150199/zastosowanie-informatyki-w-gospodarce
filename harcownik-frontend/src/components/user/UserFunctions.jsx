/* eslint-disable */
import axios from "axios";
import { async } from "regenerator-runtime";
import authHeader from "../../api/authHeader";

export const getMeData = async () => {
  //   console.log("Data:");
  try {
    const response = await axios.get("http://localhost:8000/me", authHeader());
    // console.log("Data:", response);
    return response;
    // console.log("MEData:", response.data);
  } catch (error) {
    if (error.response.status === 404) {
      throw new Error("Data not found");
    } else {
      console.error(error);
    }
  }
};
