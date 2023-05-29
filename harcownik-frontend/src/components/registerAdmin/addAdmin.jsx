import axios from "../../api/api";
import authHeader from "../../api/authHeader";

const addAdmin = async (
  first_name,
  last_name,
  email,
  level,
  func,
  password,
  confirmPassword,
  groupId
) => {
  try {
    if (password === confirmPassword) {
      // eslint-disable-next-line
      const user = await axios.post(
        "/users/admin/",
        {
          first_name: first_name,
          last_name: last_name,
          email: email,
          level: level,
          function: func,
          password: password,
          group_id: groupId,
          is_teamadmin: true,
        },
        authHeader()
      );
      return user;
    }
  } catch (error) {
    console.error(error);
  }
};

export default addAdmin;
