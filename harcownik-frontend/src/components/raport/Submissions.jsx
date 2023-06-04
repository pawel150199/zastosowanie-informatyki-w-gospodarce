/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";

import {
  getBadgesApplications,
  getUsersData,
  updateBadgesApplications,
} from "./RaportFunction";
import { tabs } from "./raportOrder";
import "./raport_style.css";

import isLogged from "../../api/isLogged";

function Submissions() {
  const [levelApplications, setlevelApplications] = useState([]);
  const [usersData, setUsersData] = useState([]);
  const [selectedItemsReported, setSelectedItemsReported] = useState([]);
  const [selectedItemsEnded, setSelectedItemsEnded] = useState([]);
  const [endedItemsToObsoleted, setEndedItemsToObsoleted] = useState([]);
  const [reportedItemsToObsoleted, setReportedItemsToObsoleted] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      if (isLogged()) {
        try {
          const levelBadgesData = await getBadgesApplications();
          setlevelApplications(levelBadgesData);
        } catch (error) {
          setlevelApplications([]);
        }

        const usersInformation = await getUsersData();
        setUsersData(usersInformation);
      }
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
      reportedItemsToObsoleted.push(report.id);
    } else if (event.target.checked && report.status == "zakończona") {
      setSelectedItemsEnded([...selectedItemsEnded, report]);
      endedItemsToObsoleted.push(report.id);
    } else {
      if (report.status == "zgłoszona") {
        const updatedItems = selectedItemsReported.filter(
          (item) => item.id !== report.id
        );
        setSelectedItemsReported(updatedItems);
        const updatedObsoletedItems = reportedItemsToObsoleted.filter(
          (item) => item.id !== report.id
        );
        console.log("UpdateItems", updatedObsoletedItems);
        setReportedItemsToObsoleted(updatedObsoletedItems);
      } else {
        const updatedItems = selectedItemsEnded.filter(
          (item) => item.id !== report.id
        );
        setSelectedItemsEnded(updatedItems);
        // console.log("Report.id:", report);
        // console.log("zawartość listy:", endedItemsToObsoleted);

        const updatedObsoletedItems = endedItemsToObsoleted.filter(
          (item) => item.id !== report.id
        );
        // console.log("UpdateItems", updatedObsoletedItems);
        setEndedItemsToObsoleted(updatedObsoletedItems);
      }
    }
  };

  const handleAllCheckboxChange = (checkedIds) => {
    checkedIds.forEach((id) => {
      const numericId = parseInt(id);
      const selectedBadge = levelApplications.find(
        (badge) => badge.id === numericId
      );
      if (selectedBadge) {
        // endedItemsToObsoleted.push(selectedBadge.id);
        // console.log("Selected badge:", selectedBadge.id);
        if (selectedBadge.status === "zgłoszona") {
          setSelectedItemsReported((prevItems) => [
            ...prevItems,
            selectedBadge,
          ]);
          reportedItemsToObsoleted.push(selectedBadge.id);
        } else if (selectedBadge.status === "zakończona") {
          console.log("Selected badge_2:", selectedBadge.id);
          setSelectedItemsEnded((prevItems) => [...prevItems, selectedBadge]);
          endedItemsToObsoleted.push(selectedBadge.id);
        }
      }
    });
  };

  const clearSelectedBadges = () => {
    setSelectedItemsReported([]);
    setSelectedItemsEnded([]);
    setEndedItemsToObsoleted([]);
    setReportedItemsToObsoleted([]);
  };

  const addReportedBadgesToRaport = () => {
    endedItemsToObsoleted.forEach((item) => {
      console.log("Item:", item);
      updateBadgesApplications(item, "zgłoszona/wykorzystana");
    });

    reportedItemsToObsoleted.forEach((item) => {
      console.log("Item:", item);
      updateBadgesApplications(item, "zgłoszona/wykorzystana");
    });

    selectedItemsReported.forEach((item) => {
      const username = usersData.find((user) => user.id === item.user_id);
      const name = username.first_name + " " + username.last_name;
      tabs[11].patternText += "- " + item.title + ": " + name + "\n";
    });

    selectedItemsEnded.forEach((item) => {
      const username = usersData.find((user) => user.id === item.user_id);
      const name = username.first_name + " " + username.last_name;
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
            {levelApplications.map((report) => {
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
                        name="submissions"
                        id={`flexCheckDefault_${report.id}`}
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
        <div>
          <button
            type="button"
            className="btn btn-dark"
            variant="dark"
            onClick={() => {
              eventCheckBoxTrue();
              const checkedCheckboxes = Array.from(
                document.querySelectorAll('input[type="checkbox"]:checked')
              );
              const checkedIds = checkedCheckboxes.map((checkbox) =>
                checkbox.id.replace("flexCheckDefault_", "")
              );
              handleAllCheckboxChange(checkedIds);
            }}
            style={{ marginRight: "1%" }}
          >
            Zaznacz wszystko
          </button>
          <button
            type="button"
            className="btn btn-dark"
            variant="dark"
            onClick={() => {
              clearSelectedBadges();
              eventCheckBoxFalse();
            }}
            style={{ marginLeft: "1%" }}
          >
            Odznacz wszystko
          </button>
        </div>
        {(selectedItemsEnded.length || selectedItemsReported.length) > 0 &&
          (console.log("Tablica zakończone:", endedItemsToObsoleted),
          console.log("Tablica rozpoczęte:", reportedItemsToObsoleted),
          (
            <button
              type="button"
              className="btn btn-dark"
              onClick={addReportedBadgesToRaport}
              style={{ marginTop: "1%" }}
            >
              Dodaj do raportu
            </button>
          ))}
      </Container>
    </div>
  );
}

export default Submissions;
