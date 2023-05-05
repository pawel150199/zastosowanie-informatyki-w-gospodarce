// /* eslint-disable */
// import React from "react";
// import { Row, Col, Container } from "react-bootstrap";
// import "./raport_style.css";

// import { tabs } from "./SelectionOfTabs";

// function GenerateTextArea() {
//   tabs.forEach((tab) => {
//     if (tab.isChecked === true) {
//       const jumbotron = document.createElement("div");
//       jumbotron.classList.add("jumbotron"); //dodanie klasy 'jumbotron'

//       const heading = document.createElement("h1");
//       heading.textContent = tab.label; //dodanie etykiety jako tekst nagłówka

//       jumbotron.appendChild(heading);

//       const container = document.querySelector(`#${tab.id}`); //znalezienie kontenera o odpowiednim ID

//       container.appendChild(jumbotron); //dodanie jumbotrona do kontenera
//     }
//   });
// }
// export default GenerateTextArea;
