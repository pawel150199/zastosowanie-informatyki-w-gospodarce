/* eslint-disable */
import React from "react";
import "./raport_style.css";
import {
  Container,
  Table,
} from "react-bootstrap";

function Submissions() {
  const eventCheckBoxTrue = () => {
    let checkboxs = document.getElementsByName("submissions");
    for (let i = 0; i < checkboxs.length; i++) {
      //zero-based array
      if (!checkboxs[i].checked) {
        // Zaznaczenie checkboxa
        checkboxs[i].checked = true;
      }
    }
  };

  const eventCheckBoxFalse = () => {
    let checkboxs = document.getElementsByName("submissions");
    for (let i = 0; i < checkboxs.length; i++) {
      //zero-based array
      if (checkboxs[i].checked) {
        // Zaznaczenie checkboxa
        checkboxs[i].checked = false;
      }
    }
  };

  return (
    <div className="jumbotron jumbotronStyle_1 rounded ">
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
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    value=""
                    id="flexCheckDefault"
                    name="submissions"
                  />
                  <label
                    className="form-check-label"
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
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    value=""
                    id="flexCheckDefault"
                    name="submissions"
                    // disabled
                  />
                  <label
                    className="form-check-label"
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
                <div className="form-check">
                  <input
                    className="form-check-input"
                    type="checkbox"
                    value=""
                    id="flexCheckDefault"
                    name="submissions"
                  />
                  <label
                    className="form-check-label"
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
          className="btn btn-dark"
          onClick={eventCheckBoxTrue}
          style={{ marginRight: "4%", marginTop: "1%", marginBottom: "3%" }}
        >
          Zaznacz wszystko
        </button>
        <button
          type="button"
          className="btn btn-dark"
          onClick={eventCheckBoxFalse}
          style={{ marginBottom: "3%", marginTop: "1%" }}
        >
          Odznacz wszystko
        </button>
      </Container>
    </div>
  );
}

export default Submissions;
