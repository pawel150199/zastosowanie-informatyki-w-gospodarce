/* eslint-disable */
import React, { useState, useEffect } from "react";
import {
  Accordion,
  Container,
  Spinner,
  Card,
  Image,
  Button,
} from "react-bootstrap";

import axios from "../../api/api";
import authHeader from "../../api/authHeader";
import isLogged, { isTeamAdmin } from "../../api/isLogged";

import "./team_member.css";

const TeamMembers = () => {
  const [members, setMembers] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [teamAdmin, setTeamAdmin] = useState(false);

  const checkUserRole = async () => {
    setTeamAdmin(await isTeamAdmin());
  };

  const handleDeleteMember = async (user_id) => {
    axios
      .delete(`/user/group/delete/${user_id}`, authHeader())
      .then(() => {
        window.location.reload();
      })
      .catch((error) => {
        console.error("Wystąpił bład", error);
        setIsLoading(false);
      });
  };
  if (isLogged()) {
    checkUserRole();
  }

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
      }, []);
  });

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
              {teamAdmin ? (
                <Accordion.Body className="text-center">
                  <Button
                    variant="danger"
                    onClick={() => handleDeleteMember(member.id)}
                  >
                    Usuń
                  </Button>
                </Accordion.Body>
              ) : null}
            </Accordion.Item>
          </Card>
        ))}
      </Accordion>
    </Container>
  );
};

export default TeamMembers;
