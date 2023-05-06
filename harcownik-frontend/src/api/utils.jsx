export const getLocalToken = () => sessionStorage.getItem("token");

export const saveLocalToken = (token) => sessionStorage.setItem("token", token);

export const removeLocalToken = () => sessionStorage.removeItem("token");

export const getLoginStatus = () => sessionStorage.getItem("isLogged");

export const setLoginStatus = (isLogged) => sessionStorage.setItem("isLogged", isLogged);

export const removeLoginStatus = () => sessionStorage.removeItem("isLogged");
