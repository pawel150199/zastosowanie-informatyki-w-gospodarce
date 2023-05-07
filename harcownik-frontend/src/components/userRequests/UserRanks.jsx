/* eslint-disable */
import React, { useEffect, useState } from "react";
import Dropdown from "react-bootstrap/Dropdown";
import { Button } from "react-bootstrap";
import DropdownButton from "react-bootstrap/DropdownButton";

import { getLevel, postLevelRaports } from "./UserRanksFunction";

import "./UserRequests.css";

function UserRanks() {
  const [level, getLevelData] = useState([]);
  const [choosenLevel, setChoosenLevel] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      const levelData = await getLevel();
      getLevelData(levelData);
    };
    fetchData();
  });

  const selectLevel = (level) => {
    setChoosenLevel(level);
    console.log("Selected Level: ", level);
  };

  return (
    <div className="jumbotron UserRanksStyle rounded">
      <h1>Zakładka służąca rozpoczęcia nowego stopnia</h1>
      <DropdownButton
        alignRight
        title="Wybierz stopień"
        id="dropdown-menu-align-right"
        onSelect={selectLevel}
      >
        {level.map((level) => (
          <Dropdown.Item key={level.id} eventKey={level.title}>
            {level.title}
          </Dropdown.Item>
        ))}
      </DropdownButton>
      <h4>Wybrany stopień: {choosenLevel}</h4>
      <Button onClick={() => postLevelRaports(choosenLevel)}>
        Rozpocznij nowy stopień
      </Button>
    </div>
  );
}

export default UserRanks;
