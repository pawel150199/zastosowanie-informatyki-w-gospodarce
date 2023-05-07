import React from "react";
import { Row, Col } from "react-bootstrap";

import ApplicationStatus from "./ApplicationStatus";
import UserEfficiency from "./UserEfficiency";
import UserRanks from "./UserRanks";
import UserRequestsHeader from "./UserRequestsHeader";

import "./UserRequests.css";

const UserRequests = () => {
  return (
    <div className="container">
      <Row>
        <UserRequestsHeader />
      </Row>
      <Row>
        {/* <Col md={4}> */}
        <ApplicationStatus />

        {/* </Col> */}
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
