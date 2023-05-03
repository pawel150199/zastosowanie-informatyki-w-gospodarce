import axios from "axios";

const getBadges = async (badgeGroupUrl)  => {
    try {
        const response = await axios.get(badgeGroupUrl);
        const data = response.data;
        console.log(data[0].group);
        for (let i=0; i < data.length; i++) {
            let group = data[i].group
            console.log(group)
            let url = "http://localhost:8000/badges/group/Sportowe";
            const badges = axios.get(url);  
            console.log(badges.data)
        }
    }
    catch (error){
        console.error(error);
    }
}

const handleResponse = (data) => {
    console.log(data);
}

export default getBadges;