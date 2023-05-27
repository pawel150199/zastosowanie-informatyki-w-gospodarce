/* eslint-disable */
import React, { useState, useEffect } from "react";
import axios from "axios";
import { View, Text, TextInput, TouchableOpacity, Image } from "react-native";
import styles from "./ProfileStyle";
import getMe from "./UserFunctions";

import authHeader from "../../api/authHeader";

function SkillsCard() {
  return (
    // console.log("dupa"),
    <View classname="jumbotron" style={styles.skillsContainer}>
      <h1>Skills</h1>
    </View>
  );
}

export default SkillsCard;
