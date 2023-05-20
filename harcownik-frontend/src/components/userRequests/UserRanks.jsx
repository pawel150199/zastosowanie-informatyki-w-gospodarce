/* eslint-disable */
import React, { useEffect, useState } from "react";
import Dropdown from "react-bootstrap/Dropdown";
import { Button } from "react-bootstrap";
import DropdownButton from "react-bootstrap/DropdownButton";

import { getLevel, postLevelRaports } from "./UserRanksFunction";
import isLogged from "../../api/isLogged";
import getMe from "../../api/getMe";

import "./UserRequests.css";

function UserRanks() {
  const [choosenLevel, setChoosenLevel] = useState("");
  const [userId, setUserId] = useState();
  const [choosenStatus, setChoosenStatus] = useState("");
  const status = ["zgłoszona", "zakończona"];
  const levels = [
    "ochotnik-młodzik",
    "tropiciel-wywiadowca",
    "pionier-odkrywca",
    "samarytanin-ćwik",
    "harcerz orla-harcerz orli",
    "harcerz Rzeczypospolitej",
  ];

  const getId = async () => {
    if (isLogged()) {
      const response = await getMe();
      const id = response.id;
      setUserId(id);
    }
  };

  useEffect(() => {
    getId();
  }, []);

  const selectLevel = (level) => {
    setChoosenLevel(level);
  };
  const selectStatus = (status) => {
    setChoosenStatus(status);
  };

  return (
    <div className="jumbotron UserRanksStyle rounded">
      <h1>Zakładka służąca rozpoczęcia nowego stopnia</h1>
      <DropdownButton
        alignight
        title="Wybierz stopień"
        Id="dropdown-menu-align-right"
        onSelect={selectLevel}
      >
        {levels.map((level, index) => (
          <Dropdown.Item key={index} eventKey={level}>
            {level}
          </Dropdown.Item>
        ))}
      </DropdownButton>

      {choosenLevel && <h4>Sprawność: {choosenLevel}</h4>}
      {choosenLevel && (
        <DropdownButton
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
          onClick={() => postLevelRaports(choosenLevel, userId, choosenStatus)}
        >
          Rozpocznij nowy stopień
        </Button>
      )}
    </div>
  );
}

export default UserRanks;
