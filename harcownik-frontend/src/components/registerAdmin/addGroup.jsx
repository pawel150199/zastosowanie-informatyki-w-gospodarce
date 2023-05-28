import axios from "../../api/api";
import authHeader from "../../api/authHeader";

const addGroup = async (name, number, szczep, city) => {
    try {
        // eslint-disable-next-line
        const group = await axios.post(
          "/groups",
          {
            name: name,
            number: number,
            szczep: szczep,
            city: city,
          },
          authHeader()
        );
        return group;
    } catch (error) {
        console.error(error);
    }
}

export default addGroup;