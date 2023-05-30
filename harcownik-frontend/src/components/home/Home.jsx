import React, { useState } from "react";
import { Link } from "react-router-dom";
import { Button, Container } from "react-bootstrap";
import Image from "react-bootstrap/Image";

import "./home.css";

function Home() {
  const features = [
    "Generowanie raportu do rozkazu",
    "Przeglądanie wszystkich sprawności",
    "Bezpieczeństwo danych użytkowników",
    "Akceptacja raportu przez drużynowego",
  ];
  const [index, setIndex] = useState(0);

  const handleSlide = () => {
    setIndex(index + 1 === features.length ? 0 : index + 1);
  };

  const images = [
    "/img/home1.jpeg",
    "/img/home2.jpeg",
    "/img/home3.jpeg",
    "/img/home4.jpeg",
  ];

  return (
    <div>
      <center>
        <Container>
          <Image src="/img/logo_with_name.png" id="img_name" />
        </Container>
      </center>
      <div className="jumbotron jumbotron-fluid bg-dark text-light text-center rounded-4">
        <Container>
          <br></br>
          <h1>Witaj w aplikacji</h1>
          <p className="lead">
            Jesteś jeden krok od ułatwienia zarządzania grupą harcerzyków
          </p>
          <Link to="/login" className="text-center">
            <Button variant="primary" className="mt-3 badge">
              Zaloguj się
            </Button>
          </Link>
        </Container>
        <br></br>
      </div>
      <Container>
        <br></br>
        <h2 className="text-center" id="info">
          Czym jest Harcownik?
        </h2>
        <p className="text-center">
          Jest to aplikacja przeznaczona dla podgrup harcerskich zwanych
          drużyną. Zadaniem aplikacji jest ułatwienie zarządzanie drużyną w tym
          kluczowa jest kwestia generowania rozkazu, który powoduje wiele
          problemów. Dodatkowo aplikacja udostępnia podstawowe informacje np. o
          zdobytych zdolnościach oraz o wymaganiach, które trzeba spełnić aby je
          zdobyć. Aplikacja wysyła powiadomienia przypominające o składkach.
        </p>
        <br></br>
        <div className="text-center p-3 mb-5 bg-white rounded" id="features">
          <h2 className="text-center">Założenia</h2>
          <Image src={images[index]} alt="home1" id="img" />
          <p>{features[index]}</p>
          <p>
            Slide {index + 1} of {features.length}
          </p>
          <Button variant="primary" className="mt-3" onClick={handleSlide}>
            Następny
          </Button>
        </div>
      </Container>
    </div>
  );
}

export default Home;
