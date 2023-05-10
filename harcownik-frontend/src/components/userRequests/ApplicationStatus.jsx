/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";

import {
  getBadgeApplicationStatus,
  getLevelApplicationStatus,
} from "./ApplicationStatusFunction";
import { getMe_2 } from "../../api/getMe";
import getMe from "../../api/getMe";
// import authHeader from "../../authHeader";
import { getLoginStatus } from "../../api/utils";
import "./UserRequests.css";

// import getMe from "../../api/getMe";

function ApplicationStatus() {
  const [badgeStatus, getBadgeStatus] = useState([]);
  const [levelStatus, getLevelStatus] = useState([]);
  const [userID, setUserID] = useState("");

  if (getLoginStatus("isLogged")) {
    const id = getMe(setUserID, "id");
    console.log("getloginstatus: ", id);
  }

  // getMe(setUserID, "id");
  // console.log("getMe inside jumbotron:", userID);

  useEffect(() => {
    // getMe(setUserID, "id");
    // const fetchMe = async () => {
    //   const userID = await getMe_2("id");
    //   setUserID(userID);
    //   console.log("getMe inside jumbotron:", userID);
    //   fetchData();
    // };
    // fetchMe();

    const fetchData = async () => {
      console.log("userID przekazany do funkcji get: ", userID);
      const badges = await getBadgeApplicationStatus(userID);
      console.log("Badges are downloaded: ", badges);
      getBadgeStatus(badges);

      const level = await getLevelApplicationStatus(userID);
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
