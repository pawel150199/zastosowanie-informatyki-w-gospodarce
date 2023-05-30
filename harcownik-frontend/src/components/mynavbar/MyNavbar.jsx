/* eslint-disable */
import { Navbar, Nav, Container, Image, NavDropdown } from "react-bootstrap";
import { useState } from "react";
import React from "react";

import getMe from "../../api/getMe";
import { removeLocalToken } from "../../api/utils";
import isLogged from "../../api/isLogged";
import { isScout, isTeamAdmin, isWebAdmin } from "../../api/isLogged";

import "./mynavbar.css";

const MyNavbar = () => {
  const [username, setUsername] = useState("");
  const [scout, setScout] = useState(false);
  const [teamAdmin, setTeamAdmin] = useState(false);
  const [webAdmin, setWebAdmin] = useState(false);

  const checkUserRole = async () => {
    setScout(await isScout());
    setTeamAdmin(await isTeamAdmin());
    setWebAdmin(await isWebAdmin());
  }

  const handleLogout = () => {
    removeLocalToken("token");
    window.location.href = "/";
  };

  const getName = async () => {
    const response = await getMe();
    setUsername(response.first_name);
  };

  if (isLogged()) {
    getName();
    checkUserRole();

  }

  return (
    <Navbar expand="lg" className="navbar-nav navbar-dark bg-dark h1 fs-4">
      <Container>
        <Navbar.Brand href="/" className="navbar-nav mr-left">
          <Image src="/img/logo.png" id="img" />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" className="mr-left" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="navbar-nav mx-auto">
            <Nav.Link className="box" href="/">
              Strona Główna
            </Nav.Link>
            <Nav.Link className="box" href="/about">
              O nas
            </Nav.Link>
            <Nav.Link className="box" href="/badges">
              Sprawności
            </Nav.Link>
            {!isLogged() ? (
              <>
                <Nav.Link className="box" href="/login">
                  Zaloguj
                </Nav.Link>
                <Nav.Link className="box" href="/register_admin">
                  Zarejestruj Drużynę
                </Nav.Link>
              </>
            ) : null}
            {scout ? (
              <Nav.Link className="box" href="/user_requests">
                Zgłoszenia użytkownika
              </Nav.Link>
            ) : null}
            {teamAdmin ? (
              <Nav.Link className="box" href="/raport">
                Raport
              </Nav.Link>
            ) : null}
            {teamAdmin ? (
              <Nav.Link className="box" href="/register_scout">
                Nowy harcerz
              </Nav.Link>
            ) : null}
          </Nav>
          <Nav className="navbar-nav navbar-dark mr-auto">
            {isLogged() ? (
              <NavDropdown title={username} id="basic-nav-dropdown">
                <NavDropdown.Item href="/user">Profil</NavDropdown.Item>
                <NavDropdown.Item href="/team_members">Twoja Drużyna</NavDropdown.Item>
                <NavDropdown.Item href="/reset_password">
                  Zmień hasło
                </NavDropdown.Item>
                <NavDropdown.Item onClick={handleLogout}>
                  Wyloguj
                </NavDropdown.Item>
              </NavDropdown>
            ) : null}
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default MyNavbar;
