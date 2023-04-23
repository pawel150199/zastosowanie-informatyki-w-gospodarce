import React from "react";
import {
  Row,
  Col,
} from "react-bootstrap";
import "./UserRequests.css";

import ApplicationStatus from "./ApplicationStatus";
import UserEfficiency from "./UserEfficiency";
import UserRanks from "./UserRanks";
import UserRequestsHeader from "./UserRequestsHeader";


const UserRequests = () => {

  return (
    <div  className="container">
      <Row>
      <UserRequestsHeader />
      </Row>
      <Row>
        <Col md={4}>
            <ApplicationStatus />

        </Col>
        <Col md={4}>
            <UserEfficiency />
        </Col>
        <Col md={4}>
        <UserRanks />
        </Col>
      </Row>
    </div>
  );
};

export default UserRequests;
