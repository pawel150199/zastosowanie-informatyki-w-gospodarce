import { getLocalToken } from "./utils";

const authHeader = () => {
    const token = getLocalToken();
    return {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    };
}

const loginHeader = () => {
    return {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
}

export { loginHeader };
export default authHeader;