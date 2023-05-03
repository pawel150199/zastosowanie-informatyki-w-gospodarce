/* eslint-disable */
import React, { useState, useEffect } from "react";
import "./UserRequests.css";
import axios from "axios";
import { Container, Table } from "react-bootstrap";
import {
  getBadgeApplicationStatus,
  getLevelApplicationStatus,
} from "./ApplicationStatusFunction";

function ApplicationStatus() {
  const [badgeStatus, getBadgeStatus] = useState([]);
  const [levelStatus, getLevelStatus] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const badges = await getBadgeApplicationStatus();
      console.log("Tu pobiera status badgy!", badges);
      getBadgeStatus(badges);

      const level = await getLevelApplicationStatus();
      getLevelStatus(level);
    };
    fetchData();
  }, []);

  return (
    <div className="jumbotron ApplicationStatusStyle rounded">
      <Container>
        <h2>Zgłoszenia dotyczące sprawności</h2>
        <Table responsive bordered striped style={{ margintop: "50px" }}>
          <thead>
            <tr>
              <th>Tytuł</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {badgeStatus.map((report) => (
              <tr key={report.id}>
                <td>{report.title}</td> <td>{report.status}</td>
              </tr>
            ))}
          </tbody>
        </Table>
        <h2>Zgłoszenia dotyczące stopni</h2>
        <Table responsive bordered striped style={{ margintop: "50px" }}>
          <thead>
            <tr>
              <th>Tytuł</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {levelStatus.map((report) => (
              <tr key={report.id}>
                <td>{report.title}</td> <td>{report.status}</td>
              </tr>
            ))}
          </tbody>
        </Table>
      </Container>

      {/* <h1>{data.map(report => (
          <h2 key={report.id}>Tytuł:{report.title} Status:{report.status}</h2>
        ))}</h1> */}
    </div>
  );
}

export default ApplicationStatus;
