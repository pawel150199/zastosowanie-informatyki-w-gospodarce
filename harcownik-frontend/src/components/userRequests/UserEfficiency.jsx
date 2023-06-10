/* eslint-disable */
import React, { useState, useEffect } from "react";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import { Button, Container } from "react-bootstrap";

import { getBadges, getBadgeGroups, postBadge } from "./UserRequestsFunctions";
import isLogged from "../../api/isLogged";
import getMe from "../../api/getMe";

import "./UserRequests.css";

/*
Tab to create by user new Efficiency report
*/
function UserEfficiency() {
  const [badgesGroups, setBadgesGroups] = useState([]);
  const [badges, setBadges] = useState([]);
  const [userId, setUserId] = useState();
  const [choosenGroup, setChoosenGroup] = useState("");
  const [choosenBadge, setChoosenBadge] = useState("");
  const [choosenBadgeId, setChoosenBadgeId] = useState("");
  const [choosenStatus, setChoosenStatus] = useState("");
  const status = ["zgłoszona", "zakończona"];

  const getId = async () => {
    if (isLogged()) {
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
    if (isLogged()) {
      fetchData();
    }
  }, []);

  const selectGroup = (group) => {
    setChoosenGroup(group);
    getProperBadges(group);
  };
  const selectBadge = (badg) => {
    getProperBadges;

    const badgeName = getBadgeNameById(+badg);
    setChoosenBadgeId(badg);
    setChoosenBadge(badgeName);
  };

  const getProperBadges = async (group) => {
    const badges = await getBadges(group);
    setBadges(badges);
  };

  function getBadgeNameById(id) {
    const badge = badges.find((b) => b.id === id);
    return badge ? badge.name : undefined;
  }
  const selectStatus = (status) => {
    setChoosenStatus(status);
  };

  return (
    <div className="jumbotron UserEfficiencyStyle rounded">
      <h2 id="request">Rozpocznij sprawność</h2>
      <DropdownButton
        className="dark"
        alignRight
        title="Wybierz grupę"
        Id="dropdown-menu-align-right"
        variant="dark"
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
          variant="dark"
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
        <DropdownButton
          variant="dark"
          alignRight
          title="Wybierz status"
          Id="dropdown-menu-align-right"
          onSelect={selectStatus}
        >
          {status.map((status, index) => (
            <Dropdown.Item key={index} eventKey={status}>
              {status}
            </Dropdown.Item>
          ))}
        </DropdownButton>
      )}
      {choosenStatus && <h4>Zgłaszany status: {choosenStatus}</h4>}
      {choosenStatus && (
        <Button
          className="btn btn-dark"
          onClick={() =>
            postBadge(choosenBadge, userId, choosenBadgeId, choosenStatus)
          }
        >
          Rozpocznij sprawność
        </Button>
      )}
    </div>
  );
}

export default UserEfficiency;
