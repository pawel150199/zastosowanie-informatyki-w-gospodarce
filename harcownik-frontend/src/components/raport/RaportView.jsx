/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Container } from "react-bootstrap";
import { orderContent } from "./SelectionOfTabs";
import { tabs } from "./raportOrder";

function Footer() {
  // const text = "";
  // const createTextFile = () => {
  //   tabs.forEach((tab) => {
  //     if (tab.isChecked) {
  //       text += `=== ${tab.label} ===\n`;
  //       text += tab.patternText;
  //       text += "\n";
  //     }
  //   });

  //   // const element = document.createElement("a");
  //   // const file = new Blob([text], { type: "text/plain" });
  //   // element.href = URL.createObjectURL(file);
  //   // element.download = "file.txt";
  //   // document.body.appendChild(element); // Required for this to work in FireFox
  //   // element.click();
  // };

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
