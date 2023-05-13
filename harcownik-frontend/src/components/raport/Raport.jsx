/* eslint-disable */
import React from "react";
import { Row, Col, Container } from "react-bootstrap";
import "./raport_style.css";

import RaportHeadear from "./RaportHeadear";
import Submissions from "./Submissions";
import SelectionOfTabs from "./SelectionOfTabs";
import Generate from "./Generate";
import Efficiency from "./Efficiency";
import { tabs } from "./SelectionOfTabs";

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
