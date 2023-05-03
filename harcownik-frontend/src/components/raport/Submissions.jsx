/* eslint-disable */
import React, { useState, useEffect } from "react";
import { getBadgesApplications, getLevelApplications } from "./RaportFunction";
import "./raport_style.css";
import { Container, Table } from "react-bootstrap";

function Submissions() {
  // const [levelApplications, setLevelApplications] = useState([]);
  const [badgesApplications, setBadgesApplications] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      // const levelApplicationsData = await getLevelApplications();
      // setLevelApplications(levelApplicationsData);
      const levelBadgesData = await getBadgesApplications();
      setBadgesApplications(levelBadgesData);
    };
    fetchData();
  }, []);
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

export default Submissions;
