import React from "react";
import { Row, Col } from "react-bootstrap";

import ApplicationStatus from "./ApplicationStatus";
import UserEfficiency from "./UserEfficiency";
import UserRanks from "./UserRanks";
import UserRequestsHeader from "./UserRequestsHeader";

import "./UserRequests.css";

/*
Page on which user can create new level or badge status report. 
User can also check reports which will be add to raport. 
*/

const UserRequests = () => {
  return (
    <div className="container">
      <Row>
        <UserRequestsHeader />
      </Row>
      <Row>
        <ApplicationStatus />
      </Row>
      <Row>
        <Col md={6}>
          <UserEfficiency />
        </Col>
        <Col md={6}>
          <UserRanks />
        </Col>
      </Row>
    </div>
  );
};

export default UserRequests;
