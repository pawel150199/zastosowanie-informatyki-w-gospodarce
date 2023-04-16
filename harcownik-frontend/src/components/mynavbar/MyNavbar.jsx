import { Navbar, Nav, Container, Image, NavDropdown} from 'react-bootstrap';
// import {React, useState} from 'react'
import {React} from 'react'
// import styles from './style.css'
import  './style.css'



const MyNavbar = () => {

    return (
        <Navbar  expand="lg" className="navbar-nav navbar-dark bg-dark h1 fs-5" > 
         {/* <Navbar className="navbar-nav navbar-dark bg-dark h1 fs-4">   */}
            <Container>
                <Navbar.Brand href="/" className="navbar-nav mr-left">
                        <Image src="/img/logo.jpeg"  style={{width: "3em"}}/>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" className="mr-left" />
                <Navbar.Collapse id="basic-navbar-nav" >
                    <Nav className="navbar-nav mx-auto" >
                        <Nav.Link className="box" href="/" >Strona Główna</Nav.Link>
                        <Nav.Link className="box" href="/login"> Logowanie</Nav.Link>
                        <Nav.Link className="box" href="/about"> O nas</Nav.Link>
                        <Nav.Link className="box" href="/badges"> Sprawności</Nav.Link>
                        <Nav.Link className="box" href="/raport"> Generuj rozkaz</Nav.Link>
                    </Nav>
                    <Nav className="navbar-nav mr-auto">
                        <NavDropdown className="box" title="Menu" id="basic-nav-dropdown">
                            <NavDropdown.Item href="/user">Profil</NavDropdown.Item>
                            <NavDropdown.Item href="#">Wyloguj</NavDropdown.Item>
                        </NavDropdown>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default MyNavbar;

