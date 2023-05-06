export const getLocalToken = () => localStorage.getItem("token");

export const saveLocalToken = () => localStorage.setItem("token", token);

export const removeLocalToken = () => localStorage.removeItem("token");