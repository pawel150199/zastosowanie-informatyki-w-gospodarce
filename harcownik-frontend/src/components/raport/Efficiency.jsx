/* eslint-disable */
import React from "react";
import { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";

import { getLevelApplications, getUsersData } from "./RaportFunction";
import "./raport_style.css";

function Efficiency() {
  const [badgesApplications, setBadgesApplications] = useState([]);
  const [usersData, setUsersData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const levelBadgesData = await getLevelApplications();
      setBadgesApplications(levelBadgesData);

      const usersInformation = await getUsersData();
      setUsersData(usersInformation);
    };
    fetchData();
  }, []);

  const eventCheckBoxTrue = () => {
    let checkboxes = document.getElementsByName("efficiency");
    for (let i = 0; i < checkboxes.length; i++) {
      if (!checkboxes[i].checked) {
        checkboxes[i].checked = true;
      }
    }
  };

  const eventCheckBoxFalse = () => {
    let checkboxes = document.getElementsByName("efficiency");
    for (let i = 0; i < checkboxes.length; i++) {
      if (checkboxes[i].checked) {
        checkboxes[i].checked = false;
      }
    }
  };

  return (
    <div className="jumbotron jumbotronStyle_4 rounded ">
      <h1>Zgłoszone wnioski o nowe poziomy harcerskie</h1>
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
            {badgesApplications.map((report) => {
              const user = usersData.find((user) => user.id === report.user_id);
              // console.log("User:", user);
              return (
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
                  <td>{user && `${user.first_name} ${user.last_name}`}</td>
                  <td>{report.title}</td> <td>{report.status}</td>
                </tr>
              );
            })}
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
