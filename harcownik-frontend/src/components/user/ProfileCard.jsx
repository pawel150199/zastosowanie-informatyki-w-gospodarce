/* eslint-disable */
import React, { useState, useEffect } from "react";
import axios from "axios";
import { View, Text, TextInput, TouchableOpacity, Image } from "react-native";
import styles from "./ProfileStyle";
import { getMeData } from "./UserFunctions";
import CityInfo from "./CityInfo";

// import authHeader from "../../api/authHeader";

function ProfileCard() {
  const [meData, setMeData] = useState([]);

  const getMe = async () => {
    try {
      const response = await getMeData();
      //   console.log("Get me response:", response);
      setMeData(response.data);
    } catch (error) {
      setMeData([]);
    }
  };

  useEffect(() => {
    getMe();
  }, []);

  return (
    // console.log("dupa", meData),
    <View classname="jumbotron" style={styles.cardcontainer}>
      <View style={styles.imageContainer}>
        <Image source={require("./Default_pfp.png")} style={styles.image} />
      </View>
      <h1>
        {meData.first_name} {meData.last_name}
      </h1>
      <h4>Poziom: {meData.level}</h4>
      <CityInfo city="Warsaw" />
    </View>
  );
}

export default ProfileCard;
