import axios from 'axios';

// TODO: add env file
const BASE_URL = "http://localhost:8000"

export default axios.create({
    baseURL: BASE_URL
});

// Not sure if it is needed
export const axiosPrivate = axios.create({
    baseURL: BASE_URL,
    headers: { "Content-Type": "application/json" },
    withCredentials: true
});