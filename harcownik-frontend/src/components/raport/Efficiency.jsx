/* eslint-disable */
import React from "react";
import { useState, useEffect } from "react";
import { Container, Table } from "react-bootstrap";
import { getLevelApplications, getUsersData } from "./RaportFunction";
import { tabs } from "./raportOrder";
import "./raport_style.css";

function Efficiency() {
  const [badgesApplications, setBadgesApplications] = useState([]);
  const [usersData, setUsersData] = useState([]);
  const [selectedItemsReported, setSelectedItemsReported] = useState([]);
  const [selectedItemsEnded, setSelectedItemsEnded] = useState([]);

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
      const selectedBadge = badgesApplications.find(
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

  const addReportedLevelToRaport = () => {
    selectedItemsReported.forEach((item) => {
      const username = usersData.find((user) => user.id === item.user_id);
      const name = username.first_name + " " + username.last_name;
      tabs[9].patternText += "- " + item.title + ": " + name + "\n";
    });

    selectedItemsEnded.forEach((item) => {
      const username = usersData.find((user) => user.id === item.user_id);
      const name = username.first_name + " " + username.last_name;
      tabs[8].patternText += "- " + item.title + ": " + name + ",\n";
    });
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
                        className={"form-check-input"}
                        type="checkbox"
                        variant="dark"
                        name="efficiency"
                        id={`flexCheckDefault_${report.id}`}
                        checked={report.checked}
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
        <div>
          <button
            type="button"
            className="btn btn-dark"
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
            onClick={addReportedLevelToRaport}
            style={{ marginTop: "1%" }}
          >
            Dodaj do raportu
          </button>
        )}
      </Container>
    </div>
  );
}

export default Efficiency;
