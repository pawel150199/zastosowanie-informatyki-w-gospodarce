/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";

import {
  getBadgeApplicationStatus,
  getLevelApplicationStatus,
} from "./UserRequestsFunctions";
import isLogged from "../../api/isLogged";

import "./UserRequests.css";

/*
Tab where user can check created  report and their status
*/

function ApplicationStatus() {
  const [badgeStatus, getBadgeStatus] = useState([]);
  const [levelStatus, getLevelStatus] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const badges = await getBadgeApplicationStatus();
        getBadgeStatus(badges);
      } catch (error) {
        getBadgeStatus([]);
      }
      try {
        const level = await getLevelApplicationStatus();
        getLevelStatus(level);
      } catch (error) {
        getLevelStatus([]);
      }
    };
    if (isLogged()) {
      fetchData();
    }
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
            {badgeStatus
              .filter(
                (badge) =>
                  badge.status === "zakończona" ||
                  badge.status === "zgłoszona" ||
                  badge.status === "zakończona-zaraportowana" ||
                  badge.status === "zgłoszona-zaraportowana"
              )
              .map((badge) => (
                <tr key={badge.id}>
                  <td>{badge.title}</td>
                  <td>{badge.status}</td>
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
            {levelStatus
              .filter(
                (badge) =>
                  badge.status === "zakończona" ||
                  badge.status === "zgłoszona" ||
                  badge.status === "zakończona-zaraportowana" ||
                  badge.status === "zgłoszona-zaraportowana"
              )
              .map((level) => (
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
