/* eslint-disable */
import React, { useState, useEffect } from "react";
import { FaMedal } from "react-icons/fa";
import { View, Text } from "react-native";
import Badge from "react-bootstrap/Badge";
import styles from "./ProfileStyle";
import { getMeData, getMyBadge } from "./ProfileFunctions";

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
      console.log("Get me response:", response.data.name);
      setMyBadge(response.data.name);
    } catch (error) {
      setMyBadge([]);
    }
  };

  useEffect(() => {
    getMe();
  }, []);

  return (
    <View style={styles.skillsContainer}>
      <Text style={styles.heading}>
        Twoje umiejętności <FaMedal size={40} />
      </Text>
      <View style={styles.divider} />

      <View style={styles.badgeContainer}>
        <Badge containerStyle={styles.customBadge}>
          <Text style={styles.badgeText}>{myBadge}</Text>
        </Badge>
        {/* <Badge containerStyle={styles.customBadge}>
          <Text style={styles.badgeText}>Lekarz</Text>
        </Badge>
        <Badge containerStyle={styles.customBadge}>
          <Text style={styles.badgeText}>Nawigator</Text>
        </Badge>
        <Badge containerStyle={styles.customBadge}>
          <Text style={styles.badgeText}>Wojownik</Text>
        </Badge> */}
      </View>
    </View>
  );
}

export default SkillsCard;
