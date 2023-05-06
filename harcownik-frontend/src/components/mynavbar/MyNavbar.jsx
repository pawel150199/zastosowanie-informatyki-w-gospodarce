import { Navbar, Nav, Container, Image, NavDropdown} from "react-bootstrap";
import { useState } from "react"; 
import React from "react";

import getMe from "../../api/getMe";
import { getLoginStatus, removeLocalToken, removeLoginStatus } from "../../api/utils";

import  "./mynavbar.css";

const MyNavbar = () => {
    const [username, setUsername] = useState("");
    
    const handleLogout = () => {
        removeLoginStatus("isLogged");
        removeLocalToken("token");
        window.location.reload()
    }

    if (getLoginStatus("isLogged")) {
        getMe(setUsername);
    }

    return (
        <Navbar  expand="lg" className="navbar-nav navbar-dark bg-dark h1 fs-4"> 
            <Container>
                <Navbar.Brand href="/" className="navbar-nav mr-left">
                        <Image src="/img/logo.png" id="img" style={{width: "1.8em"}}/>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" className="mr-left" />
                <Navbar.Collapse id="basic-navbar-nav" >
                    <Nav className="navbar-nav mx-auto" >
                        <Nav.Link className="box" href="/" >Strona Główna</Nav.Link>
                        <Nav.Link className="box" href="/login"> Logowanie</Nav.Link>
                        <Nav.Link className="box" href="/about"> O nas</Nav.Link>
                        <Nav.Link className="box" href="/badges"> Sprawności</Nav.Link>
                        <Nav.Link className="box" href="/raport"> Raport</Nav.Link>
                    </Nav>
                    <Nav className="navbar-nav navbar-dark mr-auto">
                    {getLoginStatus("isLogged") ? (
                        <NavDropdown title={username} id="basic-nav-dropdown">
                          <NavDropdown.Item href="/user">Profil</NavDropdown.Item>
                          <NavDropdown.Item href="/reset_password">Zmień hasło</NavDropdown.Item>
                          <NavDropdown.Item onClick={handleLogout}>Wyloguj</NavDropdown.Item>
                        </NavDropdown>
                    ) : null}
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
};

export default MyNavbar;
