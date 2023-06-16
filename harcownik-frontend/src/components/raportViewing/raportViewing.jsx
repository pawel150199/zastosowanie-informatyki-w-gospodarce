/* eslint-disable */
import axios from "../../api/api";
import React, { useState, useEffect } from "react";
import { Accordion, Container, Spinner } from "react-bootstrap";

const RaportViewing = () => {
  const [raports, setRaports] = useState([]);
  //   const [raportsAmount, setRaportsAmount] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    axios
      .get("/reports")
      .then((response) => {
        setRaports(response.data);
        setIsLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data from API: ", error);
        setIsLoading(false);
      });
  }, []);

  const getRaportById = async (id) => {
    const item = raports.find((item) => item.id === id);
    try {
      const response = await axios.get(`/report/${id}/file`, {
        responseType: "arraybuffer",
      });
      console.log("PDF download successfully!", response.data);
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", item.name + ".pdf");
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error("Error downloading PDF:", error);
    }
  };

  const deleteRaportById = async (id) => {
    const item = raports.find((item) => item.id === id);
    console.log("ITEM:", item);
    try {
      console.log("ID:", id);
      const response = await axios.delete(`reports/delete/${id}`, {
        responseType: "arraybuffer",
      });
      console.log("PDF delete successfully!", response.data);
      window.location.reload();
    } catch (error) {
      console.error("Error downloading PDF:", error);
    }
  };

  const fetchAndDisplayPDF = async (id) => {
    try {
      const response = await axios.get(`/report/${id}/file`, {
        responseType: "arraybuffer", // Ustawienie typu odpowiedzi na arraybuffer
      });

      const blob = new Blob([response.data], { type: "application/pdf" }); // Tworzenie Blob z danych odpowiedzi
      const url = URL.createObjectURL(blob); // Tworzenie URL dla Blob

      // Otwarcie nowego okna przeglądarki ze wskazanym adresem URL
      window.open(url, "_blank");
    } catch (error) {
      console.error("Błąd podczas pobierania pliku PDF: ", error);
    }
  };

  return (
    <Container id="container">
      <h2 id="badges">Dostępne raporty</h2>
      <Accordion>
        {raports
          .sort((a, b) => a.name.localeCompare(b.name))
          .map((raport, index) => (
            <Accordion.Item key={index} eventKey={index} className="mb-3">
              <Accordion.Header>{raport.name}</Accordion.Header>
              <Accordion.Body className="d-flex justify-content-center">
                <button
                  type="button"
                  className="btn btn-dark "
                  style={{ marginRight: "10px" }}
                  onClick={() => getRaportById(raport.id)}
                >
                  Pobierz raport
                </button>
                <button
                  type="button"
                  className="btn btn-dark "
                  style={{ marginLeft: "10px" }}
                  onClick={() => deleteRaportById(raport.id)}
                >
                  Usuń raport
                </button>
                <button
                  type="button"
                  className="btn btn-dark "
                  style={{ marginLeft: "10px" }}
                  onClick={() => fetchAndDisplayPDF(raport.id)}
                >
                  Podgląd
                </button>
              </Accordion.Body>
            </Accordion.Item>
          ))}
      </Accordion>
    </Container>
  );
};

export default RaportViewing;
