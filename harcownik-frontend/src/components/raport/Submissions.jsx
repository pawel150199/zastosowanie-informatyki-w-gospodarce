/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";

import {
  getBadgesApplications,
  getUsersData,
  updateBadgesApplications,
  addBadgeToUser,
  getBadgeRaportData,
} from "./RaportFunction";
import { tabs } from "./raportOrder";
import "./raport_style.css";

import isLogged from "../../api/isLogged";

/*
Tab provide tabel with reported submissions, user can choose which be included in raport.
*/

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
          (item) => item !== report.id
        );
        setReportedItemsToObsoleted(updatedObsoletedItems);
      } else {
        const updatedItems = selectedItemsEnded.filter(
          (item) => item.id !== report.id
        );
        setSelectedItemsEnded(updatedItems);

        const updatedObsoletedItems = endedItemsToObsoleted.filter(
          (item) => item !== report.id
        );
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
        if (selectedBadge.status === "zgłoszona") {
          setSelectedItemsReported((prevItems) => [
            ...prevItems,
            selectedBadge,
          ]);
          reportedItemsToObsoleted.push(selectedBadge.id);
        } else if (selectedBadge.status === "zakończona") {
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
      updateBadgesApplications(item, "zakończona-zaraportowana");
      addBadgesToProfile(item);
    });

    reportedItemsToObsoleted.forEach((item) => {
      updateBadgesApplications(item, "zgłoszona-zaraportowana");
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

  const rejectReportedBadges = () => {
    endedItemsToObsoleted.forEach((item) => {
      updateBadgesApplications(item, "zakończona-odrzucona");
    });

    reportedItemsToObsoleted.forEach((item) => {
      updateBadgesApplications(item, "zgłoszona-odrzucona");
    });
  };

  const addBadgesToProfile = async (item) => {
    try {
      const response = await getBadgeRaportData(item);
      const response_2 = await addBadgeToUser(
        response[0].user_id,
        response[0].badge_id
      );
      return response;
    } catch (error) {
      console.error("Error:", error);
      throw error;
    }
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
            style={{ marginLeft: "1%", marginLeft: "1%" }}
          >
            Odznacz wszystko
          </button>
        </div>
        {(selectedItemsEnded.length || selectedItemsReported.length) > 0 && (
          <button
            type="button"
            className="btn btn-dark"
            onClick={addReportedBadgesToRaport}
            style={{ marginTop: "1%", marginRight: "1%" }}
          >
            Dodaj do raportu
          </button>
        )}
        {(selectedItemsEnded.length || selectedItemsReported.length) > 0 && (
          <button
            type="button"
            className="btn btn-dark"
            onClick={() => {
              const confirmed = window.confirm(
                "Czy na pewno chcesz odrzucić zgłoszenia?"
              );
              if (confirmed) {
                rejectReportedBadges();
                window.location.reload();
              }
            }}
            style={{ marginTop: "1%", marginLeft: "1%" }}
          >
            Odrzuć zgłoszenia
          </button>
        )}
      </Container>
    </div>
  );
}

export default Submissions;
