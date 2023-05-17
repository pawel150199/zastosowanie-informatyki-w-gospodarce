/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";

import { getBadgesApplications, getUsersData } from "./RaportFunction";
import { tabs } from "./raportOrder";
import "./raport_style.css";

function Submissions() {
  const [badgesApplications, setBadgesApplications] = useState([]);
  const [usersData, setUsersData] = useState([]);
  const [selectedItemsReported, setSelectedItemsReported] = useState([]);
  const [selectedItemsEnded, setSelectedItemsEnded] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const levelBadgesData = await getBadgesApplications();
      setBadgesApplications(levelBadgesData);

      const usersInformation = await getUsersData();
      setUsersData(usersInformation);
    };

    fetchData();
  }, []);

  const eventCheckBoxTrue = () => {
    let checkboxs = document.getElementsByName("submissions");
    for (let i = 0; i < checkboxs.length; i++) {
      if (!checkboxs[i].checked) {
        checkboxs[i].checked = true;
      }
    }
  };

  const eventCheckBoxFalse = () => {
    let checkboxs = document.getElementsByName("submissions");
    for (let i = 0; i < checkboxs.length; i++) {
      if (checkboxs[i].checked) {
        checkboxs[i].checked = false;
      }
    }
  };

  const handleCheckboxChange = (event, report) => {
    if (event.target.checked && report.status == "zgłoszona") {
      setSelectedItemsReported([...selectedItemsReported, report]);
      console.log("Selected_level_reports_reported:", [
        ...selectedItemsReported,
        report,
      ]);
    } else if (event.target.checked && report.status == "zakończona") {
      setSelectedItemsEnded([...selectedItemsEnded, report]);
      console.log("Selected_level_reports_ended:", [
        ...selectedItemsEnded,
        report,
      ]);
    } else {
      if (report.status == "zgłoszona") {
        const updatedItems = selectedItemsReported.filter(
          (item) => item.id !== report.id
        );
        setSelectedItemsReported(updatedItems);
        console.log("Selected_level_reports_reported:", updatedItems);
      } else {
        const updatedItems = selectedItemsEnded.filter(
          (item) => item.id !== report.id
        );
        setSelectedItemsEnded(updatedItems);
        console.log("Selected_level_reports_ended:", updatedItems);
      }
    }
  };

  const addReportedBadgesToRaport = () => {
    console.log("user:", usersData);

    selectedItemsReported.forEach((item) => {
      const username = usersData.find((user) => user.id === item.user_id);
      const name = username.first_name + " " + username.last_name;
      console.log("username:", name);
      tabs[11].patternText += "- " + item.title + ": " + name + "\n";
    });
    console.log(tabs[9].patternText);

    selectedItemsEnded.forEach((item) => {
      const username = usersData.find((user) => user.id === item.user_id);
      const name = username.first_name + " " + username.last_name;
      console.log("username:", name);
      tabs[10].patternText += "- " + item.title + ": " + name + ",\n";
    });
  };

  return (
    <div className="jumbotron jumbotronStyle_1 rounded ">
      <h1>Zgłoszone wnioski o nowe sprawności</h1>
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
              if (
                report.status !== "zgłoszona" &&
                report.status !== "zakończona"
              ) {
                return null;
              }
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
                        onChange={(event) =>
                          handleCheckboxChange(event, report)
                        }
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
        {/* <button
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
        </button> */}
        {(selectedItemsEnded.length || selectedItemsReported.length) > 0 && (
          <button
            type="button"
            className="btn btn-dark"
            onClick={addReportedBadgesToRaport}
            style={{ marginLeft: "4%", marginTop: "1%", marginBottom: "3%" }}
          >
            Dodaj do raportu
          </button>
        )}
      </Container>
    </div>
  );
}

export default Submissions;
