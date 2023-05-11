import authHeader from "./authHeader";
import axios from "./api";

const getMe = async () => {
  try {
    const response = await axios.get("/me", authHeader());
    return response.data;
    // console.log("get me function:", response.data);
  } catch (error) {
    console.error(error);
  }
};

export default getMe;
