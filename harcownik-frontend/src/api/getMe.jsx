import authHeader from "./authHeader";
import axios from "./api";

const getMe = async (setUsername, field) => {
  // axios
  //   .get("/me", authHeader())
  //   .then((response) => {
  //     console.log("REsponse:", response);
  //     setUsername(response.data[field]);
  //   })
  //   .catch((error) => {
  //     console.error(error);
  //   });
  try {
    const response = await axios.get("/me", authHeader());
    console.log("New get me:", response.data);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export default getMe;
