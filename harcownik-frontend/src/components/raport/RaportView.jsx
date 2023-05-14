/* eslint-disable */
import React from "react";
import { Container } from "react-bootstrap";
import { orderContent } from "./SelectionOfTabs";
import ReactDOMServer from "react-dom/server";
// import fs from "fs";
import { saveAs } from "file-saver";
function Footer() {
  // function handleDownload() {
  //   const blob = new Blob([JSON.stringify(orderContent)], {
  //     type: "text/plain;charset=utf-8",
  //   });
  //   saveAs(blob, "plik.txt");
  // }

  function downloadTxtFile() {
    const scoutOrderText = ReactDOMServer.renderToString(orderContent);

    fs.writeFile("scoutOrder.txt", scoutOrderText, (err) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log("Scout order saved to file!");
    });
  }

  const jumbotronStyle = {
    backgroundColor: "#a6a2a2",
    padding: "20px",
  };

  return (
    <footer>
      <Container>
        <div className="jumbotron rounded" style={jumbotronStyle}>
          {orderContent}
          <button onClick={downloadTxtFile}>Pobierz plik </button>
        </div>
      </Container>
    </footer>
  );
}

export default Footer;
