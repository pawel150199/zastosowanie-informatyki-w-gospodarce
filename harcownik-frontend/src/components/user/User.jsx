/* eslint-disable */
import React from "react";
import { Container, Row, Col } from "react-bootstrap";

import ProfileCard from "./ProfileCard";
import SkillsCard from "./SkillsCard";

const User = () => {
  return (
    <Container>
      <Row>
        <Col md={7}>
          <ProfileCard />
        </Col>
        <Col md={5}>
          <SkillsCard />
        </Col>
      </Row>
    </Container>
  );
};

export default User;
