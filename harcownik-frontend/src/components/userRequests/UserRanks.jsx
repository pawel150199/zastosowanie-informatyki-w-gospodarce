/* eslint-disable */
import React, { useEffect, useState } from "react";
import Dropdown from "react-bootstrap/Dropdown";
import { Button } from "react-bootstrap";
import DropdownButton from "react-bootstrap/DropdownButton";

import { getLevel, postLevelRaports } from "./UserRanksFunction";
import { getLoginStatus } from "../../api/utils";
import getMe from "../../api/getMe";

import "./UserRequests.css";

function UserRanks() {
  const [choosenLevel, setChoosenLevel] = useState("");
  const [userId, setUserId] = useState();
  const levels = [
    "ochotnik-młodzik",
    "tropiciel-wywiadowca",
    "pionier-odkrywca",
    "samarytanin-ćwik",
    "harcerz orla-harcerz orli",
    "harcerz Rzeczypospolitej",
  ];

  const getId = async () => {
    if (getLoginStatus("isLogged")) {
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
    console.log("Selected Level: ", level);
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
        <Button onClick={() => postLevelRaports(choosenLevel, userId)}>
          Rozpocznij nowy stopień
        </Button>
      )}

      {/* {{ choosenLevel } && <h4>Wybrany stopień: {choosenLevel}</h4>}
      <Button onClick={() => postLevelRaports(choosenLevel, userId)}>
        Rozpocznij nowy stopień
      </Button> */}
    </div>
  );
}

export default UserRanks;
