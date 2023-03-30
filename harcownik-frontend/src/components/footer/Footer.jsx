import React from 'react';
import { Container } from 'react-bootstrap';

function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className="bg-light">
      <Container>
        <p className="text-center">
          &copy; {year} Harcownik. All rights reserved.
        </p>
        <p className="text-center">
          Today's date is: {new Date().toLocaleDateString()}
        </p>
      </Container>
    </footer>
  );
}

export default Footer;
