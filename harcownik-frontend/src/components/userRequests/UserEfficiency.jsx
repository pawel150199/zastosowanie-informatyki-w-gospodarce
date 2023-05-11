/* eslint-disable */
import React, { useState, useEffect } from "react";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import { Button } from "react-bootstrap";

import { getBadges, getBadgeGroups, postBadge } from "./getUserEfficiency";
import { getLoginStatus } from "../../api/utils";
import getMe from "../../api/getMe";

import "./UserRequests.css";

function UserEfficiency() {
  const [badgesGroups, setBadgesGroups] = useState([]);
  const [badges, setBadges] = useState([]);
  const [userID, setUserID] = useState();

  const getId = async () => {
    if (getLoginStatus("isLogged")) {
      const response = await getMe();
      const id = response.id;
      setUserID(response.id);
      console.log("getMe inside userefficiency: ", id);
      console.log("getMe type userefficiency: ", typeof id);
      console.log("userID inside userefficiency: ", typeof userID);
      console.log("userID inside userefficiency: ", userID);
    }
  };
  useEffect(() => {
    getId();
    const fetchData = async () => {
      const badges = await getBadges();
      setBadges(badges);

      const badgesGroupData = await getBadgeGroups();

      setBadgesGroups(badgesGroupData);
      console.log("Badged group:", badgesGroups);
    };

    fetchData();
  }, []);

  const [choosenGroup, setChoosenGroup] = useState("");
  const [choosenBadge, setChoosenBadge] = useState("");

  const selectGroup = (group) => {
    setChoosenGroup(group);
    console.log(group);
  };
  const selectBadge = (badg) => {
    setChoosenBadge(badg);
    console.log("Choosen Badge: ", badg);
  };

  return (
    <div className="jumbotron UserEfficiencyStyle rounded">
      <h1>Zakładka służąca rozpoczęcia nowej sprawności</h1>
      <DropdownButton
        alignRight
        title="Wybierz grupę"
        id="dropdown-menu-align-right"
        onSelect={selectGroup}
      >
        {badgesGroups.map((report) => (
          <Dropdown.Item key={report.id} eventKey={report.group}>
            {report.group}
          </Dropdown.Item>
        ))}
      </DropdownButton>
      {choosenGroup && <h4>Grupa sprawności: {choosenGroup}</h4>}
      {badges && (
        <DropdownButton
          alignRight
          title="Wybierz sprawność"
          id="dropdown-menu-align-right"
          onSelect={selectBadge}
        >
          {badges.map((badge) => (
            <Dropdown.Item key={badge.id} eventKey={badge.name}>
              {badge.name}
            </Dropdown.Item>
          ))}
        </DropdownButton>
      )}

      {choosenBadge && <h4>Sprawność: {choosenBadge}</h4>}
      {choosenBadge && (
        <Button onClick={() => postBadge(choosenBadge, userID)}>
          Rozpocznij sprawność
        </Button>
      )}
    </div>
  );
}

export default UserEfficiency;
