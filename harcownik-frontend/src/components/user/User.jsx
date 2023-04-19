import React from "react";
import { Container, Row, Col, Badge, Image } from "react-bootstrap";
import { FaMedal } from "react-icons/fa";

const UserPage = () => {
  // User data mockup
  const user = {
    name: "Katarzyna Duszyńska",
    email: "dus.kas@wp.pl",
    role: "Harcmistrzyni",
    lastLogin: "2023-03-25 15:30:00",
  };

  // Function to format the last login date and time
  const formatLastLogin = (dateTimeString) => {
    const dateTime = new Date(dateTimeString);
    return dateTime.toLocaleString();
  };

  return (
    <Container className="my-5">
      <Row>
        <Col md={4}>
          <div className="text-center mb-3">
            <Image 
              src="/img/kasia.jpg"
              alt="Profile"
              roundedCircle
              style={{ width: "150px", height: "150px" }}
            />
          </div>
          <div className="text-center">
            <h3>{user.name}</h3>
            <p>{user.email}</p>
            <Badge variant="info">{user.role}</Badge>
          </div>
        </Col>
        <Col md={8}>
          <div className="d-flex justify-content-between align-items-center">
            <h3>Odznaki</h3>
            <FaMedal size={30} />
          </div>
          <hr />
          <div className="d-flex flex-wrap">
            <Badge variant="success" className="mr-2 mb-2">Buszmen</Badge>
            <Badge variant="success" className="mr-2 mb-2">Lekarz</Badge>
            <Badge variant="success" className="mr-2 mb-2">Nawigator</Badge>
            <Badge variant="success" className="mr-2 mb-2">Wojownik</Badge>
          </div>
          <hr />
          <div>
            <h3>Informacje</h3>
            <ul>
              <li>
                <strong>Data ostatniego logowania:</strong>{" "}
                {formatLastLogin(user.lastLogin)}
              </li>
              <li>Konto zostało założone 2022-01-01</li>
            </ul>
          </div>
        </Col>
      </Row>
    </Container>
  );
};

export default UserPage;
