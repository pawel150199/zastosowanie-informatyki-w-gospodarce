import axios from "axios";

// TODO: add env file
const BASE_URL = "http://172.18.0.3:8000";

export default axios.create({
    baseURL: BASE_URL
});