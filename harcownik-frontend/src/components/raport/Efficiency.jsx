/* eslint-disable */
import React from "react";
import { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";

import { getBadgesApplications, getLevelApplications } from "./RaportFunction";
import "./raport_style.css";

function Efficiency() {
  const [badgesApplications, setBadgesApplications] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      if (getLoginStatus("isLogged")) {
        const response = await getMe();
        // setUserID(response.id);
        const levelBadgesData = await getBadgesApplications(response.id);
        setBadgesApplications(levelBadgesData);
      }
    };
    fetchData();
  }, []);

  const eventCheckBoxTrue = () => {
    let checkboxes = document.getElementsByName("efficiency");
    for (let i = 0; i < checkboxes.length; i++) {
      // zero-based array
      if (!checkboxes[i].checked) {
        // mark checkbox
        checkboxes[i].checked = true;
      }
    }
  };

  const eventCheckBoxFalse = () => {
    let checkboxes = document.getElementsByName("efficiency");
    for (let i = 0; i < checkboxes.length; i++) {
      // zero-based array
      if (checkboxes[i].checked) {
        // mark checkbox
        checkboxes[i].checked = false;
      }
    }
  };

  return (
    <div className="jumbotron jumbotronStyle_4 rounded ">
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
            {badgesApplications.map((report) => (
              <tr key={report.id}>
                <td>
                  <div className="form-check">
                    <input
                      className="form-check-input ef"
                      type="checkbox"
                      value=""
                      name="efficiency"
                      id="flexCheckDefault"
                    />
                    <label
                      className="form-check-label"
                      for="flexCheckDefault"
                    ></label>
                  </div>
                </td>
                <td>Imie i nazwisko</td>
                <td>{report.title}</td> <td>{report.status}</td>
              </tr>
            ))}
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

export default Efficiency;
