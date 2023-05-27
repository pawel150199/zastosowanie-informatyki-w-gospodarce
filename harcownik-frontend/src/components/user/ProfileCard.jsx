/* eslint-disable */
import React, { useState, useEffect } from "react";
import axios from "axios";
import { View, Text, TextInput, TouchableOpacity, Image } from "react-native";
import styles from "./ProfileStyle";
import { getMeData, getMyGroupData } from "./ProfileFunctions";

// import authHeader from "../../api/authHeader";

function ProfileCard() {
  const [meData, setMeData] = useState([]);
  const [myGroup, setMyGroup] = useState([]);

  const getMyGroup = async (groupId) => {
    if (meData) {
      try {
        console.log("group id:", groupId);
        const response = await getMyGroupData(groupId);
        console.log("Get myGroup response:", response);
        setMyGroup(response.data);
      } catch (error) {
        setMyGroup([]);
      }
    } else {
      setMyGroup([]);
    }
  };

  const getMe = async () => {
    try {
      const response = await getMeData();
      console.log("Get me response:", response);
      setMeData(response.data);
      getMyGroup(response.data.group_id);
    } catch (error) {
      setMeData([]);
    }
  };

  useEffect(() => {
    getMe();
    // getMyGroup();
  }, []);

  return (
    // console.log("dupa", meData),
    <View classname="jumbotron rounded" style={styles.cardcontainer}>
      <View style={styles.imageContainer}>
        <Image source={require("./Default_pfp.png")} style={styles.image} />
      </View>
      <View style={styles.textInformation}>
        <h1>
          {meData.first_name} {meData.last_name}
        </h1>
        <h4>Poziom: {meData.level}</h4>
        <h4>Miasto: {myGroup.city}</h4>
        <h4>Szczep: {myGroup.szczep}</h4>
      </View>
    </View>
  );
}

export default ProfileCard;
