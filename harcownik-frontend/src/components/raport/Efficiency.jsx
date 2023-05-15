/* eslint-disable */
import React from "react";
import { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";

import { getLevelApplications, getUsersData } from "./RaportFunction";
import "./raport_style.css";

function Efficiency() {
  const [badgesApplications, setBadgesApplications] = useState([]);
  const [usersData, setUsersData] = useState([]);
  const [selectedItems, setSelectedItems] = useState([]);

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

  const handleCheckboxChange = (event, report) => {
    console.log("handleCheckBox_report:", report);
    console.log("handleCheckBox_event:", event);
    if (event.target.checked) {
      console.log("uno");
      setSelectedItems([...selectedItems, report]);
      console.log("setselected:", selectedItems);
    } else {
      console.log("dos");
      const updatedItems = selectedItems.filter(
        (item) => item.id !== report.id
      );
      setSelectedItems(updatedItems);
    }
    console.log("Update:", selectedItems);
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
                        htmlFor="flexCheckDefault"
                      ></label>
                    </div>
                  </td>
                  <td>{user && `${user.first_name} ${user.last_name}`}</td>
                  <td>{report.title}</td>
                  <td>{report.status}</td>
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
