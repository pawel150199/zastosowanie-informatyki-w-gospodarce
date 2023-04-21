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

function Submissions() {
  return (
    <div class="jumbotron jumbotronStyle_1 rounded ">
      <h1>Zgłoszenia</h1>
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
                    class="form-check-input"
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
              <td>Wiersz 1, Kolumna 2</td>
              <td>Wiersz 1, Kolumna 3</td>
              <td>Wiersz 1, Kolumna 4</td>
            </tr>
            <tr>
              <td>
                <div class="form-check">
                  <input
                    class="form-check-input"
                    type="checkbox"
                    value=""
                    id="flexCheckDefault"
                    disabled
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
                    id="flexCheckDefault"
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
      </Container>
    </div>
  );
}

export default Submissions;
