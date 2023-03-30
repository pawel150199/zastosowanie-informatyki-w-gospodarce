import React from 'react';
import { Card, Button } from 'react-bootstrap';

const BadgeItem = ({ badge }) => {
  return (
    <Card>
      <Card.Img variant="top" src={badge.image} />
      <Card.Body>
        <Card.Title>{badge.name}</Card.Title>
        <Card.Text>{badge.description}</Card.Text>
        <Button variant="primary">Learn More</Button>
      </Card.Body>
    </Card>
  );
};

export default BadgeItem;