import { Navbar, Nav, Container, Image} from 'react-bootstrap';
import React from 'react'

const MyNavbar = () => {
    return (
        <Navbar bg="light" expand="lg">
            <Container>
            <Nav.Link href="/">
                <Image src="/img/logo.jpeg"  style={{width: "3em", marginRight: "4em"}}/>
            </Nav.Link>
                <Navbar.Toggle aria-controls="basic-navbar-nav" className="mr-left"/>
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-left">
                        <Nav.Link href="/">Strona Główna</Nav.Link>
                        <Nav.Link href="/login">Logowanie</Nav.Link>
                        <Nav.Link href="/about">O nas</Nav.Link>
                        <Nav.Link href="/badges">Sprawności</Nav.Link>
                        <Nav.Link href="/user">Użytkownik</Nav.Link>
                        <Nav.Link href="/raport">Raport</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default MyNavbar;
