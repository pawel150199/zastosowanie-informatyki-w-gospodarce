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
    // add more badges here with
  ]

  return (
    <Accordion defaultActiveKey={['0']} alwaysOpen>
      <Accordion.Item eventKey="0">
        <Accordion.Header>Sprawności Samerytańskie</Accordion.Header>
        <Accordion.Body>
            {samerytanskieBadges.map((badge, index) => (
              <BadgeItem key={index} badge={badge} />
            ))}
        </Accordion.Body>
      </Accordion.Item>
      <Accordion.Item eventKey="1">
        <Accordion.Header>Sprawności Sprawnościowe</Accordion.Header>
        <Accordion.Body>
            {sprawnoscioweBadges.map((badge, index) => (
              <BadgeItem key={index} badge={badge} />
            ))}
        </Accordion.Body>
      </Accordion.Item>
    </Accordion>
  );
};

export default Badges;
