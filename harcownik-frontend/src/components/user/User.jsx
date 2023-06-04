/* eslint-disable */
import React, { useState } from "react";
import { Container, Row, Col, Spinner } from "react-bootstrap";

import ProfileCard from "./ProfileCard";
import SkillsCard from "./SkillsCard";

const User = () => {
  const [isLoading, setIsLoading] = useState(false);

  if (isLoading) {
    return (
      <Container className="text-center">
        <Spinner animation="border" variant="primary" />
        <div>Loading profile...</div>
      </Container>
    );
  }
  return (
    <Container>
      <Row>
        <Col md={5}>
          <ProfileCard />
        </Col>
        <Col md={7}>
          <SkillsCard />
        </Col>
      </Row>
    </Container>
  );
};

export default User;
