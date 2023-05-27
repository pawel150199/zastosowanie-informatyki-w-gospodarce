/* eslint-disable */
import React, { useState, useEffect } from "react";
import axios from "axios";
import { View, Text, TextInput, TouchableOpacity } from "react-native";
import Badge from "react-bootstrap/Badge";
import styles from "./ProfileStyle";

import authHeader from "../../api/authHeader";

function SkillsCard() {
  return (
    // console.log("dupa"),
    <View className="jumbotron" style={styles.skillsContainer}>
      <h1>Twoje umiejętności:</h1>
      <div className="d-flex flex-wrap">
        <Badge
          // variant="secondary"
          // className="mr-3 mb-3"
          style={styles.customBadge}
        >
          Buszmen
        </Badge>
        <Badge
          // variant="secondary"
          // className="mr-3 mb-3"
          style={styles.customBadge}
        >
          Lekarz
        </Badge>
        <Badge
          // variant="secondary"
          // className="mr-3 mb-3"
          style={styles.customBadge}
        >
          Nawigator
        </Badge>
        <Badge
          // variant="secondary"
          // className="mr-3 mb-3"
          style={styles.customBadge}
        >
          Wojownik
        </Badge>
      </div>
    </View>
  );
}

export default SkillsCard;
