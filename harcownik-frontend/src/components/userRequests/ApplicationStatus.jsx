/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";

import {
  getBadgeApplicationStatus,
  getLevelApplicationStatus,
} from "./ApplicationStatusFunction";
import isLogged from "../../api/isLogged";

import "./UserRequests.css";

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
        <h2 id="request">Zgłoszenia dotyczące sprawności</h2>
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
                  badge.status === "zakończona" || badge.status === "zgłoszona"
              )
              .map((badge) => (
                <tr key={badge.id}>
                  <td>{badge.title}</td>
                  <td>{badge.status}</td>
                </tr>
              ))}
          </tbody>
        </Table>
        <h2 id="request">Zgłoszenia dotyczące stopni</h2>
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
                (level) =>
                  level.status === "zakończona" || level.status === "zgłoszona"
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
