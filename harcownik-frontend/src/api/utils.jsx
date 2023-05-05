export const getLocalToken = () => localStorage.getItem("token");

export const saveLocalToken = (token) => localStorage.setItem("token", token);

export const removeLocalToken = () => localStorage.removeItem("token");

export const getLoginStatus = () => sessionStorage.getItem("isLogged");

export const setLoginStatus = (isLogged) => sessionStorage.setItem("isLogged", isLogged);

export const removeLoginStatus = () => sessionStorage.removeItem("isLogged");
