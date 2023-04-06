import { Navbar, Nav, Container, Image, NavDropdown} from 'react-bootstrap';
import React from 'react'

const MyNavbar = () => {
    return (
<<<<<<< HEAD
        <Navbar bg="light" expand="lg" className="navbar-nav  h1 fs-5" > 
            <Container>
                <Navbar.Brand href="/" className="navbar-nav mr-left">
                        <Image src="/img/logo.jpeg"  style={{width: "3em"}}/>
                </Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" className="mr-left"/>
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="navbar-nav mx-auto">
=======
        <Navbar bg="light" expand="lg" className="justify-content-center">
            <Container>
            <Nav.Link href="/">
                {/* <Image src="/img/logo.jpeg"  style={{width: "3em", marginRight: "4em"}}/> */}
            </Nav.Link>
                <Navbar.Toggle aria-controls="basic-navbar-nav" className="mr-left"/>
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="navbar-nav mx-auto">
                        <Image src="/img/logo.jpeg"  style={{width: "3em", marginRight: "3em"}}/>
>>>>>>> 7109308 (add tests and center MyNavBar)
                        <Nav.Link href="/">Strona Główna</Nav.Link>
                        <Nav.Link href="/login">Logowanie</Nav.Link>
                        <Nav.Link href="/about">O nas</Nav.Link>
                        <Nav.Link href="/badges">Sprawności</Nav.Link>
                        <Nav.Link href="/raport">Raport</Nav.Link>
                    </Nav>
                    <Nav className="navbar-nav mr-auto">
                        <NavDropdown title="Menu" id="basic-nav-dropdown">
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

