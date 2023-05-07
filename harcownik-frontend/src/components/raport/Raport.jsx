import React from "react";
import { Row, Col } from "react-bootstrap";

import RaportHeadear from "./RaportHeadear";
import Submissions from "./Submissions";
import SelectionOfTabs from "./SelectionOfTabs";
import Generate from "./Generate";
import Efficiency from "./Efficiency";

import "./raport_style.css";

const Raport = () => {

  return (
    <div  className="container">
      <Row>
        <RaportHeadear />
      </Row>
      <Row>
        <Col md={7}>
          <Submissions />
          <Efficiency />
        </Col>
        <Col md={5}>
          <SelectionOfTabs />
          <Generate />
        </Col>
      </Row>
    </div>
  );
};

export default Raport;
