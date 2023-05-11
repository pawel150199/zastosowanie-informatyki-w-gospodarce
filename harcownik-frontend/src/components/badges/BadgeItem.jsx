import React from "react";
import { Card } from "react-bootstrap";

const BadgeItem = ({ badge }) => {
  return (
    <Card key={badge.id} style={{ marginBottom: "1rem" }}>
      <div id="item-1">
        <div id="item-2">
          <Card.Title style={{ color: "white" }}>{badge.name}</Card.Title>
        </div>
      </div>
      <Card.Body className="text-center">
        {badge.description.map((description, index) => (
          <Card.Text key={index} style={{ margin: "0.5rem 0" }}>{description}</Card.Text>
        ))}
      </Card.Body>
    </Card>
  );
};

export default BadgeItem;
