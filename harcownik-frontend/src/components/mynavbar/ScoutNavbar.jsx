/* eslint-disable */
import { Navbar, Nav, Container, Image, NavDropdown } from "react-bootstrap";
import React from "react";

import { removeLocalToken } from "../../api/utils";

import "./mynavbar.css";

const ScoutNavbar = ({ username }) => {

    const handleLogout = () => {
        removeLocalToken("token");
        window.location.href = "/";
    };

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
                    <Nav.Link className="box" href="/user_requests">
                        Zgłoszenia użytkownika
                    </Nav.Link>
                </Nav>
                <Nav className="navbar-nav navbar-dark mr-auto">
                    <NavDropdown title={username} id="basic-nav-dropdown">
                        <NavDropdown.Item href="/user">Profil</NavDropdown.Item>
                        <NavDropdown.Item href="/team_members">
                            Twoja Drużyna
                        </NavDropdown.Item>
                        <NavDropdown.Item href="/reset_password">
                            Zmień hasło
                        </NavDropdown.Item>
                        <NavDropdown.Item onClick={handleLogout}>
                            Wyloguj się
                        </NavDropdown.Item>
                    </NavDropdown>
                </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default ScoutNavbar;