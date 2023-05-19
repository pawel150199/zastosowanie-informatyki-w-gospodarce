/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Container } from "react-bootstrap";
import { orderContent } from "./SelectionOfTabs";

function Footer() {
  const jumbotronStyle = {
    backgroundColor: "#a6a2a2",
    padding: "20px",
  };

  return (
    <footer>
      <Container>
        <div className="jumbotron rounded" style={jumbotronStyle}>
          {orderContent}
        </div>
      </Container>
    </footer>
  );
}

export default Footer;
