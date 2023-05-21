import { getLocalToken } from "./utils";
import getMe from "./getMe";

const isLogged = () => {
  if (getLocalToken("token") === null || getLocalToken("token") === "") {
    return false;
  } else {
    return true;
  }
};

export const isScout = async () => {
  if (isLogged()) {
    const user = await getMe();
    if (user.is_teamadmin === false && user.is_webadmin === false) {
      return true;
    } else {
      return false;
    }
  }
};

export const isTeamAdmin = async () => {
  if (isLogged()) {
    const user = await getMe();
    if (user.is_teamadmin === true && user.is_webadmin === false) {
      return true;
    } else {
      return false;
    }
  }
};

export const isWebAdmin = async () => {
  if (isLogged()) {
    const user = await getMe();
    if (user.is_teamadmin === false && user.is_webadmin === true) {
      return true;
    } else {
      return false;
    }
  }
};

export default isLogged;
