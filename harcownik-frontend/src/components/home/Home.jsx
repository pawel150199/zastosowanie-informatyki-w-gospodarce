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
      <div className="jumbotron jumbotron-fluid bg-dark text-light text-center rounded-4">
        <Container>
          <br></br>
          <h1>Witaj w aplikacji Harcownik</h1>
          <p className="lead">
            Jesteś jeden krok od ułatwienia zarządzania twoją drużyną
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
          drużynami. Zadaniem aplikacji jest ułatwienie zarządzania drużyną. 
          Kluczową kwestią w zarządzniu drużyną jest tworzenie rozkazów, które powoduje wiele
          problemów. Dodatkowo aplikacja udostępnia podstawowe informacje np. o
          zdobytych sprawnościach oraz o wymaganiach, które trzeba spełnić aby je
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
