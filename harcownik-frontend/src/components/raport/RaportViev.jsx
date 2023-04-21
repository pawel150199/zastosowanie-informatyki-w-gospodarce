import React from "react";
import { Container } from "react-bootstrap";
// import "./footer.css";
function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer >
      <Container>
      <h1>Oto twój rozkaz bambiku</h1>
      </Container>
    </footer>
  );
}

export default Footer;
