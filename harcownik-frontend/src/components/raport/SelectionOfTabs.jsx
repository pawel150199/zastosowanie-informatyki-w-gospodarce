/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";
import { Form } from "react-bootstrap";
import { getLoginStatus } from "../../api/utils";
import getMe from "../../api/getMe";
import { scoutOrder } from "./raportOrder";
import { tabs, updateTabs } from "./raportOrder";

import "./raport_style.css";

export let orderContent = "";
export let fileContent = "";
export const userData = "";

export default function SelectionOfTabs() {
  const [selectedItems, setSelectedItems] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      if (getLoginStatus("isLogged")) {
        const response = await getMe();
        const userData = response.first_name + "  " + response.last_name;
        return userData;
      }
    };
    fetchData();
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

  function handleDownload() {
    const selectedTabs = tabs.filter((tab) => selectedItems.includes(tab.id));
    fileContent = selectedTabs.map((tab) => tab.patternText).join("\n\n");

    orderContent = scoutOrder(userData);
  }

  return (
    <div className="jumbotron jumbotronStyle_2 rounded">
      <h1>Podpunkty do rozkazu</h1>
      <Form>
        {tabs.map((tab) => (
          <div key={tab.id}>
            <Form.Check
              type="checkbox"
              label={tab.label}
              id={tab.id}
              checked={selectedItems.includes(tab.id)}
              onChange={(e) => {
                if (e.target.checked) {
                  handleSelect(tab.id);
                  tab.isChecked = true;
                  console.log("ischecked", tab.isChecked, tab.label);
                } else {
                  handleDeselect(tab.id);
                  console.log("ischecked", tab.isChecked, tab.label);
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
      <Link to="/raport/raport_view" id="raport_view">
        <Button
          variant="primary"
          className="mt-3 badge"
          onClick={handleDownload}
        >
          Przygotuj raport
        </Button>
      </Link>
    </div>
  );
}
