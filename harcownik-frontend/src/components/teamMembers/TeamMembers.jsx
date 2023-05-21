import React, { useState, useEffect } from "react";
import { Accordion, Container, Spinner, Card, Image} from "react-bootstrap";

import axios from "../../api/api";
import authHeader from "../../api/authHeader";

import "./team_member.css";

const TeamMembers = () => {
  const [members, setMembers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    axios
      .get("/users/group", authHeader())
      .then((response) => {
        setMembers(response.data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data from API: ", error);
        setIsLoading(false);
      });
  }, []);

  if (isLoading) {
    return (
      <Container className="text-center">
        <Spinner animation="border" variant="primary" />
        <div>Loading members...</div>
      </Container>
    );
  }

  return (
    <Container id="container">
      <h2 id="badges">Członkowie twojej drużyny</h2>
      <Accordion>
        {members.map((member, index) => (
          <Card key={index}>
            <Accordion.Item key={index} eventKey={index} className="mb-3">
                <Accordion.Header id="header">
                    <Image src="/img/scout.png" id="scout" className="align-left" />
                    {member.first_name} {member.last_name}
                </Accordion.Header>
            </Accordion.Item>
          </Card>
        ))}
      </Accordion>
    </Container>
  );
};

export default TeamMembers;
