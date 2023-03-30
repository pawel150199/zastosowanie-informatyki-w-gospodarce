import React from 'react';
import { Accordion, Card, Button } from 'react-bootstrap';
import BadgeItem from './BadgeItem';

const Badges = () => {
  const samerytanskieBadges = [
    {
      name: 'Kręgielnia',
      description: 'Zdobądź minimum 50 punktów w grze w kręgle',
      image: 'https://via.placeholder.com/150',
    },
    {
      name: 'Malarstwo',
      description: 'Namaluj obraz olejny o wymiarach 60x40 cm',
      image: 'https://via.placeholder.com/150',
    },
    // add more badges here
  ];

  const sprawnoscioweBadges = [
    {
      name: 'Pływanie',
      description: 'Przebyj dystans 500 metrów stylem dowolnym',
      image: 'https://via.placeholder.com/150',
    },
    {
      name: 'Ratownictwo',
      description: 'Udziel pierwszej pomocy w przypadku udaru cieplnego',
      image: 'https://via.placeholder.com/150',
    },
    // add more badges here
  ];

  return (
    <Accordion defaultActiveKey="0">
      <Card>
        <Card.Header>
          <Accordion.Toggle as={Button} variant="link" eventKey="0">
            Sprawności Samerytańskie
          </Accordion.Toggle>
        </Card.Header>
        <Accordion.Collapse eventKey="0">
          <Card.Body>
            {samerytanskieBadges.map((badge, index) => (
              <BadgeItem key={index} badge={badge} />
            ))}
          </Card.Body>
        </Accordion.Collapse>
      </Card>
      <Card>
        <Card.Header>
          <Accordion.Toggle as={Button} variant="link" eventKey="1">
            Sprawnościowe
          </Accordion.Toggle>
        </Card.Header>
        <Accordion.Collapse eventKey="1">
          <Card.Body>
            {sprawnoscioweBadges.map((badge, index) => (
              <BadgeItem key={index} badge={badge} />
            ))}
          </Card.Body>
        </Accordion.Collapse>
      </Card>
    </Accordion>
  );
};

export default Badges;
