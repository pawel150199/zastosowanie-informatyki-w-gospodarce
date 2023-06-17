/* eslint-disable */
import axios from "../../api/api";
import React, { useState, useEffect } from "react";
import { Accordion, Container, Spinner } from "react-bootstrap";
import authHeader from "../../api/authHeader";

const RaportViewing = () => {
  const [raports, setRaports] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    axios
      .get("/me/reports", authHeader())
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
        ...authHeader(),
        responseType: "arraybuffer",
      });
      console.log("PDF download successfully!");
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
    try {
      const response = await axios.delete(
        `reports/delete/${id}`,
        authHeader(),
        {
          responseType: "arraybuffer",
        }
      );
      console.log("PDF delete successfully!");
      window.location.reload();
    } catch (error) {
      console.error("Error downloading PDF:", error);
    }
  };

  const fetchAndDisplayPDF = async (id) => {
    try {
      const response = await axios.get(`/report/${id}/file`, {
        ...authHeader(),
        responseType: "arraybuffer",
      });
      const blob = new Blob([response.data], { type: "application/pdf" });
      const url = URL.createObjectURL(blob);
  
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
                  style={{ marginLeft: "10px", marginRight: "10px" }}
                  onClick={() => {
                    const shouldDelete = window.confirm(
                      "Czy na pewno chcesz usunąć ten raport?"
                    );
                    if (shouldDelete) {
                      deleteRaportById(raport.id);
                    }
                  }}
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
