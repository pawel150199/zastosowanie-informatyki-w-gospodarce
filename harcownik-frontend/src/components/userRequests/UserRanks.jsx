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
  const [level, getLevelData] = useState([]);
  const [choosenLevel, setChoosenLevel] = useState("");
  const [userID, setUserID] = useState();

  const getId = async () => {
    if (getLoginStatus("isLogged")) {
      const response = await getMe();
      // console.log("response: ", response);
      // console.log("response: ", typeof response.id);
      const id = response.id;
      setUserID(id);
      // console.log("getMe inside userranks: ", id);
      // console.log("userID inside userranks: ", userID);
    }
  };

  const fetchData = async () => {
    const levelData = await getLevel();
    getLevelData(levelData);
  };

  useEffect(() => {
    getId();
    fetchData();
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
      <Button onClick={() => postLevelRaports(choosenLevel, userID)}>
        Rozpocznij nowy stopień
      </Button>
    </div>
  );
}

export default UserRanks;
