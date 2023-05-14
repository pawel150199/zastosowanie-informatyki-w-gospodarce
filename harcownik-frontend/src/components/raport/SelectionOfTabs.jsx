/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Button, Container } from "react-bootstrap";
import { Form, Dropdown, FormGroup, FormControl } from "react-bootstrap";
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
  const [raportContent, setRaportContent] = useState();

  useEffect(() => {
    const fetchData = async () => {
      if (getLoginStatus("isLogged")) {
        const response = await getMe();
        const userData = response.first_name + "  " + response.last_name;
        console.log("UserData przypisanie:", userData);
        return userData;
        // console.log("response_user_name:", userData);
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
    // console.log("event", event);
    // console.log("tab", tab.patternText);
    let updatedTabs = tabs.map((t) => {
      if (t.id === tab.id) {
        return { ...t, patternText: event.target.value };
      } else {
        return t;
      }
    });
    // console.log("Tabs przed:", tabs);
    updateTabs(updatedTabs);
    // console.log("Tabs:", tabs);
  };

  function handleDownload() {
    const selectedTabs = tabs.filter((tab) => selectedItems.includes(tab.id));
    // console.log("selectedTabs:", selectedTabs);
    fileContent = selectedTabs.map((tab) => tab.patternText).join("\n\n");
    // console.log("fileContent:", fileContent);

    // const orderPattern = {
    //   heading: "ROZKAZ HARCERSKI",
    //   addressee: "Druchny i druchowie",
    //   contents: `\n\n${fileContent}`,
    //   signature: "Komendant drużyny",
    //   date: "Warszawa, 13 maja 2023 r.",
    // };

    // orderContent = `Związek Harcerstwa Polskiego                       Kg, dnia 22.22.222
    // Hufiec Wąchock
    // Drużynowy 17 DH „Pioruny”
    // im. Zeusa Gromowładnego
    //                                         Rozkaz L.3/2019

    //   \n\n${fileContent}\n\n

    //                                                              Czuwaj !
    //                                                              phm. ${userData}

    // `;

    // orderContent = `${orderPattern.heading}\n\n${orderPattern.addressee}\n\n${orderPattern.contents}\n\n${orderPattern.signature}\n\n${orderPattern.date}`;
    orderContent = scoutOrder(userData);
    console.log("orderContent:", orderContent);

    const blob = new Blob([orderContent], {
      type: "text/plain;charset=utf-8",
    });
    // saveAs(blob, "rozkaz.txt");
    // console.log("orderContent:", orderContent);

    setRaportContent(orderContent);
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
