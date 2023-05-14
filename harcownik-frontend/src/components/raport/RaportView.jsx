/* eslint-disable */
import React from "react";
import { Container } from "react-bootstrap";
import { orderContent } from "./SelectionOfTabs";
import { RozkazL } from "./raportOrder";
function Footer() {
  function handleDownload() {
    const blob = new Blob([orderContent], {
      type: "text/plain;charset=utf-8",
    });
    saveAs(blob, "rozkaz.txt");
  }
  const jumbotronStyle = {
    backgroundColor: "#a6a2a2",
    padding: "20px",
  };

  return (
    <footer>
      <Container>
        <div className="jumbotron rounded" style={jumbotronStyle}>
          {orderContent.split("\n").map((paragraph, index) => (
            <p key={index}>{paragraph}</p>
          ))}
          <button onClick={handleDownload}>Pobierz plik </button>
        </div>
      </Container>
    </footer>
  );
}

export default Footer;
