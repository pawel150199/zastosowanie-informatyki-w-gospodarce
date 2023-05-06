/* eslint-disable */
import React, { useState } from "react";
import { Form, Dropdown, FormGroup, FormControl } from "react-bootstrap";
import "./raport_style.css";

const [tabs, setTabs] = useState([
  {
    id: "item1",
    label: "Wstęp",
    isChecked: false,
    patternText:
      "Druhny i Druhowie!Minęło już 50 lat od powstania naszej drużyny. Każda harcerka i harcerz powinni poszukiwać w starszcyh pokoleniach wzorów swoich postaw, które będą stanowiły drogowskazy podejmowanych wyzwań i dokonywania wyborów życiowych....",
    textValue: "",
  },
  {
    id: "item2",
    label: "Wyjątki z rozkazu",
    isChecked: false,
    patternText:
      "Druhny i Druhowie!Minęło już 50 lat od powstania naszej drużyny. Każda harcerka i harcerz powinni poszukiwać w starszcyh pokoleniach wzorów swoich postaw, które będą stanowiły drogowskazy podejmowanych wyzwań i dokonywania wyborów życiowych....",
    textValue: "",
  },
  {
    id: "item3",
    label: "Uchwały",
    isChecked: false,
    patternText:
      "Druhny i Druhowie!Minęło już 50 lat od powstania naszej drużyny. Każda harcerka i harcerz powinni poszukiwać w starszcyh pokoleniach wzorów swoich postaw, które będą stanowiły drogowskazy podejmowanych wyzwań i dokonywania wyborów życiowych....",
    textValue: "",
  },
  {
    id: "item4",
    label: "Zwolnienia",
    isChecked: false,
    patternText:
      "Druhny i Druhowie!Minęło już 50 lat od powstania naszej drużyny. Każda harcerka i harcerz powinni poszukiwać w starszcyh pokoleniach wzorów swoich postaw, które będą stanowiły drogowskazy podejmowanych wyzwań i dokonywania wyborów życiowych....",
    textValue: "",
  },
  {
    id: "item5",
    label: "Przyznanie stopni,sprawności",
    isChecked: false,
    patternText:
      "Druhny i Druhowie!Minęło już 50 lat od powstania naszej drużyny. Każda harcerka i harcerz powinni poszukiwać w starszcyh pokoleniach wzorów swoich postaw, które będą stanowiły drogowskazy podejmowanych wyzwań i dokonywania wyborów życiowych....",
    textValue: "",
  },
]);

function SelectionOfTabs() {
  const [selectedItems, setSelectedItems] = useState([]);

  // const [tabs, setTabs] = useState([
  //   {
  //     id: "item1",
  //     label: "Wstęp",
  //     isChecked: false,
  //     patternText:
  //       "Druhny i Druhowie!Minęło już 50 lat od powstania naszej drużyny. Każda harcerka i harcerz powinni poszukiwać w starszcyh pokoleniach wzorów swoich postaw, które będą stanowiły drogowskazy podejmowanych wyzwań i dokonywania wyborów życiowych....",
  //     textValue: "",
  //   },
  //   {
  //     id: "item2",
  //     label: "Wyjątki z rozkazu",
  //     isChecked: false,
  //     patternText:
  //       "Druhny i Druhowie!Minęło już 50 lat od powstania naszej drużyny. Każda harcerka i harcerz powinni poszukiwać w starszcyh pokoleniach wzorów swoich postaw, które będą stanowiły drogowskazy podejmowanych wyzwań i dokonywania wyborów życiowych....",
  //     textValue: "",
  //   },
  //   {
  //     id: "item3",
  //     label: "Uchwały",
  //     isChecked: false,
  //     patternText:
  //       "Druhny i Druhowie!Minęło już 50 lat od powstania naszej drużyny. Każda harcerka i harcerz powinni poszukiwać w starszcyh pokoleniach wzorów swoich postaw, które będą stanowiły drogowskazy podejmowanych wyzwań i dokonywania wyborów życiowych....",
  //     textValue: "",
  //   },
  //   {
  //     id: "item4",
  //     label: "Zwolnienia",
  //     isChecked: false,
  //     patternText:
  //       "Druhny i Druhowie!Minęło już 50 lat od powstania naszej drużyny. Każda harcerka i harcerz powinni poszukiwać w starszcyh pokoleniach wzorów swoich postaw, które będą stanowiły drogowskazy podejmowanych wyzwań i dokonywania wyborów życiowych....",
  //     textValue: "",
  //   },
  //   {
  //     id: "item5",
  //     label: "Przyznanie stopni,sprawności",
  //     isChecked: false,
  //     patternText:
  //       "Druhny i Druhowie!Minęło już 50 lat od powstania naszej drużyny. Każda harcerka i harcerz powinni poszukiwać w starszcyh pokoleniach wzorów swoich postaw, które będą stanowiły drogowskazy podejmowanych wyzwań i dokonywania wyborów życiowych....",
  //     textValue: "",
  //   },
  // ]);

  const handleSelect = (eventKey) => {
    if (!selectedItems.includes(eventKey)) {
      setSelectedItems([...selectedItems, eventKey]);
    }
  };

  const handleDeselect = (eventKey) => {
    setSelectedItems(selectedItems.filter((item) => item !== eventKey));
  };

  const handleTextValueChange = (event, tab) => {
    const updatedTabs = tabs.map((t) => {
      if (t.id === tab.id) {
        return { ...t, textValue: event.target.value };
      } else {
        return t;
      }
    });
    setTabs(updatedTabs);
    // console.log("Updated tab:", tab);
  };

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
              // <div className="form-group">
              //   {/* <label htmlFor="exampleInput">{tab.label}</label> */}
              //   <input
              //     type="text"
              //     className="form-control"
              //     id={tab.id}
              //     defaultValue={tab.patternText}
              //     onChange={(e) => handleTextValueChange(e, tab)}
              //   />
              //   <h1>{tab.textValue}</h1>
              // </div>
              <Form.Group controlId="exampleForm.ControlTextarea1">
                {/* <Form.Label>Przykładowy tekst</Form.Label> */}
                <Form.Control
                  as="textarea"
                  rows={3}
                  value={tab.value}
                  defaultValue={tab.patternText}
                  onChange={(e) => handleTextValueChange(e, tab)}
                />
                <h1>{tab.textValue}</h1>
              </Form.Group>
            )}
          </div>
        ))}
      </Form>
    </div>
  );
}

export default SelectionOfTabs;
