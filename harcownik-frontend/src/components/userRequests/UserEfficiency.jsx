/* eslint-disable */
import React, { useState, useEffect } from "react";
import Dropdown from "react-bootstrap/Dropdown";
import axios from "axios";
import DropdownButton from "react-bootstrap/DropdownButton";
import { Button } from "react-bootstrap";

import "./UserRequests.css";

function UserEfficiency() {
  const [badgesGroups, setBadgesGroups] = useState([]);
  const [badges, setBadges] = useState([]);

  useEffect(() => {
    axios
      .all([
        axios.get("http://localhost:8000/badges/"),
        axios.get("http://localhost:8000/level_reports/"),
      ])
      .then(
        axios.spread((badgesGroupsResponse, badgesResponse) => {
          setBadgesGroups(badgesGroupsResponse.data);
          setBadges(badgesResponse.data);
        })
      )
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const [choosenGroup, setChoosenGroup] = useState("");
  const [choosenBadge, setChoosenBadge] = useState("");

  const handleSelect = (group) => {
    setChoosenGroup(group);
    //TODO: delete debugging logs
    console.log("Choosen Group: " + group);
  };
  const handleSelect1 = (badg) => {
    setChoosenBadge(badg);
    console.log("Choosen Badge: " + badg);
  };

  function PostBadge() {
    axios
      .post("http://localhost:8000/badge_reports/", {
        title: choosenGroup,
        status: "zgłoszona",
        user_id: 1,
        badge_id: 3,
      })
      .then(function (response) {
        console.log("Response Data: " + response);
      });
  }

  return (
    <div className="jumbotron UserEfficiencyStyle rounded">
      <h1>Zgłoszenie Sprawności</h1>
      <DropdownButton
        alignRight
        title="Wybierz sprawność"
        id="dropdown-menu-align-right"
        onSelect={handleSelect}
      >
        {badgesGroups.map((report) => (
          <Dropdown.Item key={report.id} eventKey={report.name}>
            {report.name}
          </Dropdown.Item>
        ))}
      </DropdownButton>
      <DropdownButton
        alignRight
        title="Wybierz sprawność"
        id="dropdown-menu-align-right"
        onSelect={handleSelect1}
      >
        {badges.map((badge) => (
          <Dropdown.Item
            key={badge.id}
            eventKey={badge.title}
            // onClick={badgeSelect}
          >
            {badge.title}
          </Dropdown.Item>
        ))}
      </DropdownButton>
      <h4>Grupa sprawności: {choosenGroup}</h4>
      <h4>Sprawność: {choosenBadge}</h4>
      <Button onClick={() => PostBadge()}>Rozpocznij sprawność</Button>
    </div>
  );
}

export default UserEfficiency;
