/* eslint-disable */
import React, { useState } from "react";
import { Link } from "react-router-dom";
import { Button, Container } from "react-bootstrap";
import { saveAs } from "file-saver";
import { Form, Dropdown, FormGroup, FormControl } from "react-bootstrap";

import "./raport_style.css";

export let orderContent = "";

export default function SelectionOfTabs() {
  const [tabs, setTabs] = useState([
    {
      id: "0",
      label: "Wstęp",
      isChecked: false,
      patternText: `Wstęp okolicznościowy (święta państwowe, rocznice, szczególne wydarzenia w Związku, tematom tym może być poświęcony rozkaz specjalny drużynowego).
        Wyjątki z rozkazu komendanta Hufca ZHP Wąchock L. …/… z dnia ….. 2013 r.
        (sprawy ogólnohufcowe lub dotyczące drużyny, m.in.: pełnienie funkcji na wyższych szczeblach
          struktury, przyznanie odznaczeń lub stopni instruktorskich instruktorom danej drużyny).`,
      textValue: "",
    },
    {
      id: "1",
      label: "Wyjątki z rozkazu",
      isChecked: false,
      patternText: "Wyjątki z rozkazu",
      textValue: "",
    },
    {
      id: "2",
      label: "Uchwały",
      isChecked: false,
      patternText: "Uchwały",
      textValue: "",
    },
    {
      id: "3",
      label: "Zwolnienia",
      isChecked: false,
      patternText: "Zwolnienia",
      textValue: "",
    },
    {
      id: "4",
      label: "Przyznanie stopni,sprawności",
      isChecked: false,
      patternText: "Przyznanie stopni,sprawności",
      textValue: "",
    },
  ]);
  const [selectedItems, setSelectedItems] = useState([]);
  const [raportContent, setRaportContent] = useState();

  const handleSelect = (eventKey) => {
    if (!selectedItems.includes(eventKey)) {
      setSelectedItems([...selectedItems, eventKey]);
    }
  };

  const handleDeselect = (eventKey) => {
    setSelectedItems(selectedItems.filter((item) => item !== eventKey));
  };

  // const handleTextValueChange = (event, tab) => {
  //   console.log("event", event);
  //   console.log("tab", tab.patternText);
  //   const updatedTabs = tabs.map((t) => {
  //     if (t.id === tab.id) {
  //       return { ...t, textValue: event.target.value };
  //     } else {
  //       return t;
  //     }
  //   });
  //   setTabs(updatedTabs);
  // };

  const handleTextValueChange = (event, tab) => {
    console.log("event", event);
    console.log("tab", tab.patternText);
    const updatedTabs = tabs.map((t) => {
      if (t.id === tab.id) {
        return { ...t, patternText: event.target.value };
      } else {
        return t;
      }
    });
    setTabs(updatedTabs);
  };

  function handleDownload() {
    const selectedTabs = tabs.filter((tab) => selectedItems.includes(tab.id));
    console.log("selectedTabs:", selectedTabs);
    const fileContent = selectedTabs.map((tab) => tab.patternText).join("\n\n");
    console.log("fileContent:", fileContent);

    const orderPattern = {
      heading: "ROZKAZ HARCERSKI",
      addressee: "Druchny i druchowie",
      contents: `\n\n${fileContent}`,
      signature: "Komendant drużyny",
      date: "Warszawa, 13 maja 2023 r.",
    };

    orderContent = `Związek Harcerstwa Polskiego                       Kg, dnia 22.22.222
    Hufiec Wąchock
    Drużynowy 17 DH „Pioruny”
    im. Zeusa Gromowładnego
                                            Rozkaz L.3/2019

      \n\n${orderPattern.contents}\n\n

                                                                 Czuwaj !
                                                                 phm. Jan Nowak

    `;

    // orderContent = `${orderPattern.heading}\n\n${orderPattern.addressee}\n\n${orderPattern.contents}\n\n${orderPattern.signature}\n\n${orderPattern.date}`;
    console.log("orderContent:", orderContent);

    const blob = new Blob([orderContent], {
      type: "text/plain;charset=utf-8",
    });
    // saveAs(blob, "rozkaz.txt");
    console.log("orderContent:", orderContent);

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
