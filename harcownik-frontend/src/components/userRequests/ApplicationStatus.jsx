/* eslint-disable */
import React, { useState, useEffect } from "react";
import "./UserRequests.css";
import axios from "axios";
import {
  Container,
  Table,
} from "react-bootstrap";






function ApplicationStatus() {

  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/level_reports/")
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.log(error);
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
              {/* <td key={report.id}>Tytuł:{report.title} Status:{report.status}</td>
              <td>Wiersz 1, Kolumna 3</td>
              <td>Wiersz 1, Kolumna 4</td> */}
            {/* </tr> */}
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
