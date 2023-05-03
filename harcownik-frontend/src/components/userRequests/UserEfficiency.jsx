/* eslint-disable */
import React, { useState, useEffect } from "react";
import "./UserRequests.css";
import Dropdown from "react-bootstrap/Dropdown";
import axios from "axios";
import DropdownButton from "react-bootstrap/DropdownButton";
import { Button } from "react-bootstrap";
import { getBadges, getBadgeGroups, postBadge } from "./getUserEfficiency";

function UserEfficiency() {
  const [badgesGroups, setBadgesGroups] = useState([]);
  const [badges, setBadges] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const badges = await getBadges();
      setBadges(badges);

      const badgesGroupData = await getBadgeGroups();
      setBadgesGroups(badgesGroupData);
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
    console.log("Wybrany badge", badg);
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
          <Dropdown.Item key={report.id} eventKey={report.title}>
            {report.title}
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
        <Button onClick={() => postBadge(choosenBadge)}>
          Rozpocznij sprawność
        </Button>
      )}
    </div>
  );
}

export default UserEfficiency;
