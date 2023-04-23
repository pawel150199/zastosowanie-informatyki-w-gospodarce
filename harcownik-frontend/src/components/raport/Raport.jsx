import React from "react";
import {
  Row,
  Col,
} from "react-bootstrap";
import "./raport_style.css";

import Raport_Headear from "./Raport_Headear";
import Submissions from "./Submissions";
import SelectionOfTabs from "./SelectionOfTabs";
import Generate from "./Generate";
import Efficiency from "./Efficiency";

const Raport = () => {

  return (
    <div  className="container">
      <Row>
        <Raport_Headear />
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
