/* eslint-disable */
import React from "react";
import { Card } from "react-bootstrap";

const BadgeItem = ({ badge }) => {
  return (
    <Card>
      <div style={{ position: "relative" }}>
        <div style={{
          position: "absolute",
          bottom: 0,
          left: 0,
          right: 0,
          backgroundColor: "rgba(0, 0, 0, 0.5)",
          padding: "0.5rem",
        }}>
          <Card.Title style={{ color: "white" }}>{badge.name}</Card.Title>
        </div>
      </div>
      <Card.Body>
          <Card.Text key={badge.index} style={{ margin: "0.5rem 0" }}> {badge.description} </Card.Text>
      </Card.Body>
    </Card>
  );
};

export default BadgeItem;
