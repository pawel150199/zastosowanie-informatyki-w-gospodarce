/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";

import {
  getBadgeApplicationStatus,
  getLevelApplicationStatus,
} from "./ApplicationStatusFunction";
import getMe from "../../api/getMe";
import { getLoginStatus } from "../../api/utils";
import "./UserRequests.css";

function ApplicationStatus() {
  const [badgeStatus, getBadgeStatus] = useState([]);
  const [levelStatus, getLevelStatus] = useState([]);
  const [userID, setUserID] = useState();

  useEffect(() => {
    const fetchData = async () => {
      if (getLoginStatus("isLogged")) {
        const response = await getMe();
        const id = response.id;
        const badges = await getBadgeApplicationStatus(id);
        getBadgeStatus(badges);
        const level = await getLevelApplicationStatus(id);
        getLevelStatus(level);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="jumbotron ApplicationStatusStyle rounded">
      <Container>
        <h2>Zgłoszenia dotyczące sprawności</h2>
        <Table responsive bordered striped style={{ marginTop: "50px" }}>
          <thead>
            <tr>
              <th>Tytuł</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {badgeStatus.map((Status) => (
              <tr key={Status.id}>
                <td>{Status.title}</td>
                <td>{Status.status}</td>
              </tr>
            ))}
          </tbody>
        </Table>
        <h2>Zgłoszenia dotyczące stopni</h2>
        <Table responsive bordered striped style={{ marginTop: "50px" }}>
          <thead>
            <tr>
              <th>Tytuł</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {levelStatus.map((level) => (
              <tr key={level.id}>
                <td>{level.title}</td>
                <td>{level.status}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Container>
    </div>
  );
}

export default ApplicationStatus;
