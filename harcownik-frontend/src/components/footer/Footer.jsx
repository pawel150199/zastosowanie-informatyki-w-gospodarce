import React from "react";
import { Container } from "react-bootstrap";
import "./footer.css";
function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="bg-light">
      <Container>
        <p className="text-center" id="style-1">
          Today's date is: {new Date().toLocaleDateString()}
        </p>
        <p className="text-center" id="style-2">
          &copy; {year} Harcownik. All rights reserved.
        </p>
      </Container>
    </footer>
  );
}

export default Footer;
