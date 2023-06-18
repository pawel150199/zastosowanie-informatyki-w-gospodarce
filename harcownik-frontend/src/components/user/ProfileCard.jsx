/* eslint-disable */
import React, { useState, useEffect } from "react";
import { View, Image } from "react-native";
import styles from "./ProfileStyle";

import { getMeData, getMyGroupData } from "./ProfileFunctions";
import isLogged from "../../api/isLogged";

function ProfileCard() {
  const [meData, setMeData] = useState([]);
  const [myGroup, setMyGroup] = useState([]);

  const getMyGroup = async (groupId) => {
    if (meData) {
      try {
        const response = await getMyGroupData(groupId);
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
      setMeData(response.data);
      getMyGroup(response.data.group_id);
    } catch (error) {
      setMeData([]);
    }
  };

  useEffect(() => {
    if (isLogged()) {
      getMe();
    }
  }, []);

  return (
    <View classname="jumbotron rounded" style={styles.cardcontainer}>
      <View style={styles.imageContainer}>
        <Image source="/img/default.png" style={styles.image} />
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
