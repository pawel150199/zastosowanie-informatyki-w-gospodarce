/* eslint-disable */
import axios from "axios";
import React, { useState, useEffect } from "react";
import { Accordion, Container, Spinner } from "react-bootstrap";
import BadgeItem from "./BadgeItem";
import "./badges.css";

const Badges = () => {
  const [badges, setBadges] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    axios
      .get("http://localhost:8000/badges/grouped")
      .then((response) => {
        setBadges(response.data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data from API: " + error);
        setIsLoading(false);
      });
  }, []);

  if (isLoading) {
    return (
      <Container className="text-center">
        <Spinner animation="border" variant="primary" />
        <div>Loading badges...</div>
      </Container>
    );
  }

  return (
    <Container id="container">
      <h2 id="badges">Sprawności harcerzy polskich</h2>
      <Accordion>
        {badges.map((group, index) => (
          <Accordion.Item key={index} eventKey={index} className="mb-3">
            <Accordion.Header className="text-center">
              {group.group}
            </Accordion.Header>
            <Accordion.Body>
              {group.badges.map((badge, index) => (
                <BadgeItem key={index} badge={badge} />
              ))}
            </Accordion.Body>
          </Accordion.Item>
        ))}
      </Accordion>
    </Container>
  );
};

export default Badges;
