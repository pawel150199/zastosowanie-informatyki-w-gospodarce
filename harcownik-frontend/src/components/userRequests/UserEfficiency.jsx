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
  const [userId, setUserId] = useState();
  const [choosenGroup, setChoosenGroup] = useState("");
  const [choosenBadge, setChoosenBadge] = useState("");
  const [choosenBadgeId, setChoosenBadgeId] = useState("");

  const getId = async () => {
    if (getLoginStatus("isLogged")) {
      const response = await getMe();
      setUserId(response.id);
    }
  };

  useEffect(() => {
    getId();
    const fetchData = async () => {
      const badgesGroupData = await getBadgeGroups();
      setBadgesGroups(badgesGroupData);
    };

    fetchData();
  }, []);

  const selectGroup = (group) => {
    setChoosenGroup(group);
    console.log(group);
    getProperBadges(group);
  };
  const selectBadge = (badg) => {
    console.log("badg:", badg);
    getProperBadges;

    const badgeName = getBadgeNameById(+badg);
    setChoosenBadgeId(badg);
    console.log("Nazwa badga:", badgeName);
    setChoosenBadge(badgeName);
  };

  const getProperBadges = async (group) => {
    const badges = await getBadges(group);
    console.log("Pobrane badge z grupy:", badges);
    setBadges(badges);
  };

  function getBadgeNameById(Id) {
    const badge = badges.find((b) => b.id === Id);
    return badge ? badge.name : undefined;
  }

  return (
    <div className="jumbotron UserEfficiencyStyle rounded">
      <h1>Zakładka służąca rozpoczęcia nowej sprawności</h1>
      <DropdownButton
        alignRight
        title="Wybierz grupę"
        Id="dropdown-menu-align-right"
        onSelect={selectGroup}
      >
        {badgesGroups.map((report) => (
          <Dropdown.Item key={report.Id} eventKey={report.group}>
            {report.group}
          </Dropdown.Item>
        ))}
      </DropdownButton>
      {choosenGroup && <h4>Grupa sprawności: {choosenGroup}</h4>}
      {choosenGroup && (
        <DropdownButton
          alignRight
          title="Wybierz sprawność"
          Id="dropdown-menu-align-right"
          onSelect={selectBadge}
        >
          {badges.map((badge) => (
            <Dropdown.Item key={badge.id} eventKey={badge.id}>
              {badge.name}
            </Dropdown.Item>
          ))}
        </DropdownButton>
      )}

      {choosenBadge && <h4>Sprawność: {choosenBadge}</h4>}
      {choosenBadge && (
        <Button onClick={() => postBadge(choosenBadge, userId, choosenBadgeId)}>
          Rozpocznij sprawność
        </Button>
      )}
    </div>
  );
}

export default UserEfficiency;
