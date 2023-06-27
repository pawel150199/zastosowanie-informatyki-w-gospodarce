/* eslint-disable */
import { useState } from "react";
import React from "react";

import NotLoggedNavbar from "./NotLoggedNavbar";
import ScoutNavbar from "./ScoutNavbar";
import TeamAdminNavbar from "./TeamAdminNavbar";

import getMe from "../../api/getMe";
import isLogged from "../../api/isLogged";
import { isScout, isTeamAdmin } from "../../api/isLogged";

import "./mynavbar.css";

const MyNavbar = () => {
  const [username, setUsername] = useState("");
  const [scout, setScout] = useState(false);
  const [teamAdmin, setTeamAdmin] = useState(false);

  const checkUserRole = async () => {
    getName();
    setScout(await isScout());
    setTeamAdmin(await isTeamAdmin());
  };

  const getName = async () => {
    const response = await getMe();
    setUsername(response.first_name);
};

  if (isLogged()) {
    checkUserRole();
    if (scout) {
      return (
        <ScoutNavbar username={username} />
      )
    }

    if (teamAdmin) {
      return (
        <TeamAdminNavbar username={username} />
      )
    }
  } else {
    return (
      <NotLoggedNavbar />
    )
  }
}

export default MyNavbar;
