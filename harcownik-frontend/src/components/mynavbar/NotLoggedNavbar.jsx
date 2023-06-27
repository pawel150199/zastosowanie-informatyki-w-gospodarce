/* eslint-disable */
import { Navbar, Nav, Container, Image, NavDropdown } from "react-bootstrap";
import React from "react";

import "./mynavbar.css";

const NotLoggedNavbar = () => {
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
                <Nav.Link className="box" href="/login">
                    Zaloguj się
                </Nav.Link>
                <Nav.Link className="box" href="/register_admin">
                    Zarejestruj Drużynę
                </Nav.Link>
              </Nav>
            </Navbar.Collapse>
          </Container>
        </Navbar>
    );
};

export default NotLoggedNavbar;