/* eslint-disable */
import React, { useState, useEffect } from "react";
import { FaMedal } from "react-icons/fa";
import { View, Text } from "react-native";
import Badge from "react-bootstrap/Badge";

import { getMeData, getMyBadge } from "./ProfileFunctions";
import isLogged from "../../api/isLogged";

import styles from "./ProfileStyle";

function SkillsCard() {
  const [meData, setMeData] = useState([]);
  const [myBadge, setMyBadge] = useState([]);

  const getMe = async () => {
    try {
      const response = await getMeData();
      setMeData(response.data);
      getBadge(response.data.badge_id);
    } catch (error) {
      setMeData([]);
    }
  };

  const getBadge = async (id) => {
    try {
      const response = await getMyBadge(id);
      setMyBadge(response.data.name);
    } catch (error) {
      setMyBadge([]);
    }
  };

  useEffect(() => {
    if (isLogged()) {
      getMe();
    }
  }, []);

  return (
    <View style={styles.skillsContainer}>
      <Text style={styles.heading}>
        Twoje umiejętności <FaMedal size={40} />
      </Text>
      <View style={styles.divider} />
      {meData &&
        meData.badges &&
        meData.badges.length > 0 &&
        meData.badges
          .sort((a, b) => a.name.localeCompare(b.name))
          .map((myBadge, index) => (
            <View key={index} style={styles.badgeContainer}>
              <Badge containerStyle={styles.customBadge}>
                <Text style={styles.badgeText}>{myBadge.name}</Text>
              </Badge>
            </View>
          ))}
    </View>
  );
}

export default SkillsCard;
