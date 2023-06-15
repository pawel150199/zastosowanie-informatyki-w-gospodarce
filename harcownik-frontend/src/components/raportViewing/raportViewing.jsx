/* eslint-disable */
import axios from "../../api/api";
import React, { useState, useEffect } from "react";
import { Accordion, Container, Spinner } from "react-bootstrap";

const RaportViewing = () => {
  const [raports, setRaports] = useState([]);

  useEffect(() => {
    axios
      .get("/reports/2")
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
    console.log("ITEM:", item);
    try {
      console.log("ID:", id);
      const response = await axios.get(`/report/${id}/file`, {
        responseType: "arraybuffer",
      });
      console.log("PDF download successfully!", response.data);
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      console.log("Raports:", raports);
      link.setAttribute("download", item.name);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error("Error downloading PDF:", error);
    }
  };

  return (
    <Container id="container">
      <h2 id="badges">Dostępne raporty</h2>
      <Accordion>
        {raports.map((group, index) => (
          <Accordion.Item key={index} eventKey={index} className="mb-3">
            <Accordion.Header>{group.name}</Accordion.Header>
            <Accordion.Body className="d-flex justify-content-center">
              <button
                type="button"
                className="btn btn-dark "
                onClick={() => getRaportById(group.id)}
              >
                Pobierz raport
              </button>
            </Accordion.Body>
          </Accordion.Item>
        ))}
      </Accordion>
    </Container>
  );
};

export default RaportViewing;
