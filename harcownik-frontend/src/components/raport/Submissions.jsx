/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";

import { getBadgesApplications, getUsersData } from "./RaportFunction";
import { tabs } from "./raportOrder";
import "./raport_style.css";

function Submissions() {
  const [levelApplications, setlevelApplications] = useState([]);
  const [usersData, setUsersData] = useState([]);
  const [selectedItemsReported, setSelectedItemsReported] = useState([]);
  const [selectedItemsEnded, setSelectedItemsEnded] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const levelBadgesData = await getBadgesApplications();
        setlevelApplications(levelBadgesData);
      } catch (error) {
        setlevelApplications([]);
        console.log("ERROR", error);
      }

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
    } else if (event.target.checked && report.status == "zakończona") {
      setSelectedItemsEnded([...selectedItemsEnded, report]);
    } else {
      if (report.status == "zgłoszona") {
        const updatedItems = selectedItemsReported.filter(
          (item) => item.id !== report.id
        );
        setSelectedItemsReported(updatedItems);
      } else {
        const updatedItems = selectedItemsEnded.filter(
          (item) => item.id !== report.id
        );
        setSelectedItemsEnded(updatedItems);
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
        } else if (selectedBadge.status === "zakończona") {
          setSelectedItemsEnded((prevItems) => [...prevItems, selectedBadge]);
        }
      }
    });
  };

  const clearSelectedBadges = () => {
    setSelectedItemsReported([]);
    setSelectedItemsEnded([]);
  };

  const addReportedBadgesToRaport = () => {
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
        {(selectedItemsEnded.length || selectedItemsReported.length) > 0 && (
          <button
            type="button"
            className="btn btn-dark"
            onClick={addReportedBadgesToRaport}
            style={{ marginTop: "1%" }}
          >
            Dodaj do raportu
          </button>
        )}
      </Container>
    </div>
  );
}

export default Submissions;
