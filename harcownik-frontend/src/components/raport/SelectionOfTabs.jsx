/* eslint-disable */
import axios from "../../api/api";
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";
import { Form } from "react-bootstrap";
import { authHeader } from "../../api/authHeader";
import getMe from "../../api/getMe";
import { scoutOrder } from "./raportOrder";
import { tabs, updateTabs } from "./raportOrder";
import isLogged from "../../api/isLogged";
import { getMyGroupData } from "./RaportFunction";

import "./raport_style.css";

/*
Tab where user decide which paragraph of raport will be included to final version. User can also modify text.
*/

export let orderContent = "";
export let fileContent = "";
export let userData = "";
export let scoutSign = "";
export let scoutCity = "";
export let scoutLevel = "";
export let scoutId = "";
export let raportAmound = "";

export default function SelectionOfTabs() {
  const [selectedItems, setSelectedItems] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      if (isLogged()) {
        const response = await getMe();

        scoutSign = response.first_name + " " + response.last_name;
        scoutLevel = response.level;
        scoutId = response.id;

        const responseData = await getMyGroupData();
        scoutCity = responseData.city;
      }
    };
    const fetchDataAmount = async () => {
      if (isLogged()) {
        axios
          .get("/report/amount", authHeader())
          .then((response) => {
            raportAmound = parseInt(response.data[0]) + 1;
          })
          .catch((error) => {
            console.error("Error fetching data from API: ", error);
          });
      }
    };
    fetchData();
    fetchDataAmount();
  }, []);

  const handleSelect = (eventKey) => {
    if (!selectedItems.includes(eventKey)) {
      setSelectedItems([...selectedItems, eventKey]);
    }
  };

  const handleDeselect = (eventKey) => {
    setSelectedItems(selectedItems.filter((item) => item !== eventKey));
  };

  const handleTextValueChange = (event, tab) => {
    let updatedTabs = tabs.map((t) => {
      if (t.id === tab.id) {
        return { ...t, patternText: event.target.value };
      } else {
        return t;
      }
    });
    updateTabs(updatedTabs);
  };
  const handleSelectAll = () => {
    const allTabIds = tabs.map((tab) => tab.id);
    setSelectedItems(allTabIds);
  };
  function handleDownload() {
    const selectedTabs = tabs.filter((tab) => selectedItems.includes(tab.id));
    fileContent = selectedTabs.map((tab) => tab.patternText).join("\n\n");
    orderContent = scoutOrder(userData);
    window.location.href = "/raport_viewing";
  }

  const chooseAllTabs = () => {
    tabs.forEach((tab) => {
      tab.isChecked = true;
      handleSelect(tab.id);
    });
  };

  return (
    <div className="jumbotron jumbotronStyle_2 rounded">
      <h1>Podpunkty do rozkazu</h1>
      <Form>
        {tabs.map((tab) => (
          <div key={tab.id}>
            <Form.Check
              type="checkbox"
              className={selectedItems.includes(tab.id) ? "black-checkbox" : ""}
              label={tab.label}
              id={tab.id}
              checked={selectedItems.includes(tab.id)}
              onChange={(e) => {
                if (e.target.checked) {
                  handleSelect(tab.id);
                  tab.isChecked = true;
                } else {
                  handleDeselect(tab.id);
                }
              }}
            />
            {selectedItems.includes(tab.id) && (
              <Form.Group controlId="exampleForm.ControlTextarea1">
                <Form.Control
                  as="textarea"
                  rows={3}
                  value={tab.value}
                  defaultValue={tab.patternText}
                  onChange={(e) => handleTextValueChange(e, tab)}
                />
              </Form.Group>
            )}
          </div>
        ))}
      </Form>
      <Button
        type="button"
        className="btn btn-dark"
        onClick={() => {
          chooseAllTabs();
          handleSelectAll();
        }}
        style={{ marginRight: "1%", marginTop: "1%" }}
      >
        Zaznacz wszystko
      </Button>
      <Button
        type="button"
        className="btn btn-dark"
        onClick={handleDownload}
        style={{ marginLeft: "1%", marginTop: "1%" }}
      >
        Przygotuj raport
      </Button>
    </div>
  );
}
