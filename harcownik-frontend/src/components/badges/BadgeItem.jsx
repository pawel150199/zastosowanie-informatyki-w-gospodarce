import React from "react";
import { Card } from "react-bootstrap";

const BadgeItem = ({ badge }) => {
  return (
    <Card>
      <div style={{ position: "relative" }}>
        <Card.Img variant="top" src={badge.image} />
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
        {badge.description.map((text, index) => (
          <Card.Text key={index} style={{ margin: "0.5rem 0" }}> {text} </Card.Text>
        ))}
      </Card.Body>
    </Card>
  );
};

export default BadgeItem;
