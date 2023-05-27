/* eslint-disable */
import React from "react";
import { Container, Row, Col, Badge, Image } from "react-bootstrap";
import { FaMedal } from "react-icons/fa";
import ProfileCard from "./ProfileCard";
import SkillsCard from "./SkillsCard";
import TeamMembers from "../teamMembers/TeamMembers";

const UserPage = () => {
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
      {/* <Row>
        <TeamMembers />
      </Row> */}
    </Container>
  );
};

export default UserPage;
