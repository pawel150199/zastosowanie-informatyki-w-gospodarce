/* eslint-disable */
import React, { useState, useEffect } from "react";
import axios from "axios";
import { Container, Table } from "react-bootstrap";

import "./UserRequests.css";

function ApplicationStatus() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/level_reports/")
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

    return(
        <div className="jumbotron ApplicationStatusStyle rounded" >
          <Container>
            <Table responsive bordered striped style={{margintop: '50px'}} >
              <thead >
                <tr>
                  <th>Tytuł</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {data.map(report => (
                  <tr key={report.id}><td>{report.title}</td> <td>{report.status}</td></tr>
                ))}
              </tbody>
            </Table>
          </Container>
        </div>
    );
}


export default ApplicationStatus;
