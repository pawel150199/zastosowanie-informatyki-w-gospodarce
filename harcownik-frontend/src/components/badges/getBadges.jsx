/*
import axios from "axios";

const getBadges = async (badgeGroupUrl)  => {
    try {
        const response = await axios.get(badgeGroupUrl, {headers: {'Content-Type': 'application/json'}});
        console.log("RESPONSE")
        console.log(response.data);
        const data = response.data;
        console.log(data[0].group);
        let badgesData = [];
        for (let i=0; i < data.length; i++) {
            let groupData = {};
            let group = data[i].group;
            let url = "http://localhost:8000/badges/group/" + group;
            const badges = await getBadgesData(url); 
            groupData["badges"] = badges;
            groupData["group"] = group; 
            badgesData.push(groupData);
        }
        console.log(badgesData);
        return badgesData;
    }
    catch (error){
        console.error(error);
    }
}

const getBadgesData = async (url) => {
    try {
        const response = await axios.get(url);
        const data = response.data;
        return data;
    } catch (error) {
        console.error(error);
    }
}

export default getBadges;
*/


import axios from "axios";

const getBadges = async (badgeGroupUrl)  => {
    try {
        const { data } = await axios({
            method: 'get',
            url: badgeGroupUrl,
        });
        console.log(data);

        let badgesData = [];
        for (let i=0; i < data.length; i++) {
            let groupData = {};
            let group = data[i].group;
            let url = "http://localhost:8000/badges/group/" + group;
            const badges = await getBadgesData(url); 
            groupData["badges"] = badges;
            groupData["group"] = group; 
            badgesData.push(groupData);
        }
        console.log('data' + badgesData);
        return badgesData;
    }
    catch (error){
        console.error(error);
    }
}

const getBadgesData = async (url) => {
    try {
        const { data } = await axios({
            method: 'get',
            url: url,
        });
        console.log('badges data' + data);
        return data;
    } catch (error) {
        console.error(error);
    }
}

export default getBadges;
