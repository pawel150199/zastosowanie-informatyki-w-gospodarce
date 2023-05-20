export const getLocalToken = () => sessionStorage.getItem("token");

export const saveLocalToken = (token) => sessionStorage.setItem("token", token);

export const removeLocalToken = () => sessionStorage.removeItem("token");
