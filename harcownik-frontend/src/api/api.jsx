import axios from 'axios';

// TODO: add env file
const BASE_URL = "http://localhost:8000"

export default axios.create({
    baseURL: BASE_URL
});