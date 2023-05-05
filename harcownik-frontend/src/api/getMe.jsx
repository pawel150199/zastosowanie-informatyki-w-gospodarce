import authHeader from "./authHeader";
import axios from "./api";

const getMe = async(setUsername) => {
    axios.get("/me", authHeader())
        .then((response) => {
            setUsername(response.data.first_name);
        })
        .catch((error) => {
            console.error(error);
        })
}

export default getMe;