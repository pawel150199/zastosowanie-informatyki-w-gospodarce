/* eslint-disable */
import React from "react";
import { Row } from "react-bootstrap";
import "./raport_style.css";

import RaportHeadear from "./RaportHeadear";
import Submissions from "./Submissions";
import SelectionOfTabs from "./SelectionOfTabs";
import Efficiency from "./Efficiency";

/*
Page responsible for providing all needed tabs to prepare scout raport. User will choose reported levels and badges. 
Then define which tab will be included in final report. 
*/

const Raport = () => {
  return (
    <div className="container">
      <Row>
        <RaportHeadear />
      </Row>
      <Row>
        <Submissions />
      </Row>
      <Row>
        <Efficiency />
      </Row>
      <Row>
        <SelectionOfTabs />
      </Row>
    </div>
  );
};

export default Raport;
