import React, { useState, useEffect } from "react";
import "./raport_style.css";
import {
  Container,
  Row,
  Col,
  Jumbotron,
  Button,
  Form,
  FormControl,
  Dropdown,
  Table,
} from "react-bootstrap";

function Efficiency() {
  const eventCheckBoxTrue = () => {
    let checkboxs = document.getElementsByName("efficiency");
    for (let i = 0; i < checkboxs.length; i++) {
      //zero-based array
      if (!checkboxs[i].checked) {
        // Zaznaczenie checkboxa
        checkboxs[i].checked = true;
      }
    }
  };

  const eventCheckBoxFalse = () => {
    let checkboxs = document.getElementsByName("efficiency");
    for (let i = 0; i < checkboxs.length; i++) {
      //zero-based array
      if (checkboxs[i].checked) {
        // Zaznaczenie checkboxa
        checkboxs[i].checked = false;
      }
    }
  };

  return (
    <div class="jumbotron jumbotronStyle_4 rounded ">
      <h1>Sprawności</h1>
      <Container>
        <Table responsive striped bordered>
          <thead>
            <tr>
              <th></th>
              <th>Imię i Nazwisko</th>
              <th>Zgłoszenie</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>
                <div class="form-check">
                  <input
                    class="form-check-input ef"
                    type="checkbox"
                    value=""
                    name="efficiency"
                    id="flexCheckDefault"
                    // checked onClick={eventCheckBox()}
                  />
                  <label
                    class="form-check-label"
                    for="flexCheckDefault"
                  ></label>
                </div>
              </td>
              <td>Wiersz 1, Kolumna 2</td>
              <td>Wiersz 1, Kolumna 3</td>
              <td>Wiersz 1, Kolumna 4</td>
            </tr>
            <tr>
              <td>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    name="efficiency"
                    type="checkbox"
                    value=""
                    id="flexCheckDefault"
                  />
                  <label
                    class="form-check-label"
                    for="flexCheckDefault"
                  ></label>
                </div>
              </td>
              <td>Wiersz 2, Kolumna 2</td>
              <td>Wiersz 2, Kolumna 3</td>
              <td>Wiersz 2, Kolumna 4</td>
            </tr>
            <tr>
              <td>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value=""
                    name="efficiency"
                    id="flexCheckDefault"
                    // checked onClick={eventCheckBox()}
                  />
                  <label
                    class="form-check-label"
                    for="flexCheckDefault"
                  ></label>
                </div>
              </td>
              <td>Wiersz 3, Kolumna 2</td>
              <td>Wiersz 3, Kolumna 3</td>
              <td>Wiersz 3, Kolumna 4</td>
            </tr>
          </tbody>
        </Table>
        <button
          type="button"
          class="btn btn-dark"
          onClick={eventCheckBoxTrue}
          style={{ marginRight: "4%", marginTop: "1%", marginBottom: "3%" }}
        >
          Zaznacz wszystko
        </button>
        <button
          type="button"
          class="btn btn-dark"
          onClick={eventCheckBoxFalse}
          style={{ marginBottom: "3%", marginTop: "1%" }}
        >
          Odznacz wszystko
        </button>
      </Container>
    </div>
  );
}

export default Efficiency;
