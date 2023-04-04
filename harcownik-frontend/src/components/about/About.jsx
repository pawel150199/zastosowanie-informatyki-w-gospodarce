import React from 'react';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';


const About = () => {
  return (
    <div>
      <div className="jumbotron">
        <h1 className="display-4 text-center">Harcownik</h1>
        <br></br>
        <p className="lead text-center">Harcownik to aplikacja webowa skierowana do organizacji harcerskich. Ma ona za zadanie usprawnić zarządzanie harcerzykami.</p>
      </div>
      <br></br>
      <br></br>
      <Card className="text-center justify-content-md-center">
        <br></br>
        <Card.Title>Nasz zespół</Card.Title>
        <br></br>
        <Container>
        <Row>
          <Col>
            <Card className="h-100">
              <Card.Img variant="top" src="/img/pawel.jpg" />
              <Card.Body className="d-flex flex-column">
                <Card.Title>Paweł Polski</Card.Title>
                <Card.Text>
                  Odpowiada za rozwój aplikacji, utrzymanie jej oraz kwestie związane z infrastrukturą.
                </Card.Text>
                <div className="mt-auto">
                <Button data-testid="Learn More Paweł" variant="primary" className="mt-auto" href="https://pl-pl.facebook.com/people/Pawe%C5%82-Polski/pfbid0c17y1CUAhTfbuT7w9hnkAGRMtFWYS7eRURVCxBqZrezy11E1eX7nu5SxWGhCS1yel/">Learn More</Button>
                </div>
              </Card.Body>
            </Card>
          </Col>
          <Col>
            <Card className="h-100">
              <Card.Img variant="top" src="/img/michas.jpg" />
              <Card.Body className="d-flex flex-column">
                <Card.Title>Michał Włosek</Card.Title>
                <Card.Text>
                  Odpowiada za rozwój aplikacji oraz za jej jakość.
                </Card.Text>
                <div className="mt-auto">
                <Button data-testid="Learn More Michał" variant="primary" className="align-bottom" href="https://pl-pl.facebook.com/michal.wlo.7">Learn More</Button>
                </div>
              </Card.Body>
            </Card>
          </Col>
          <Col>
            <Card className="h-100">
              <Card.Img variant="top" src="/img/kasia.jpg" />
              <Card.Body className="d-flex flex-column">
                <Card.Title>Katarzyna Duszyńska</Card.Title>
                <Card.Text>
                  Odpowiada za rozwój aplikacji oraz kwestie związane z organizacją zespołą (Scrum Master) oraz za finalny wygląd aplikacji.
                </Card.Text>
                <div className="mt-auto">
                <Button data-testid="Learn More Kasia" variant="primary" className="align-bottom" href="https://www.facebook.com/kasia.duszynska.52">Learn More</Button>
                </div>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
      </Card>
      
    </div>
  );
}

export default About;