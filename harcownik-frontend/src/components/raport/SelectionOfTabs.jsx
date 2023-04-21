import React, { useState, useEffect } from "react";
import {
  Container,
  Row,
  Col,
  Jumbotron,
  Button,
  Form,
  FormControl,
  Dropdown,
} from "react-bootstrap";
import "./raport_style.css";





function SelectionOfTabs() {
  const [pdf, setPdf] = useState(null);
  const [pageNumber, setPageNumber] = useState(1);
  const [editing, setEditing] = useState(false);
  const [canvas, setCanvas] = useState(null);




  const handleEditClick = () => {
    setEditing(true);
  };


  const [selectedItems, setSelectedItems] = useState([]);

  const handleSelect = (eventKey) => {
    if (!selectedItems.includes(eventKey)) {
      setSelectedItems([...selectedItems, eventKey]);
    }
  };

  const handleDeselect = (eventKey) => {
    setSelectedItems(selectedItems.filter((item) => item !== eventKey));
  };

    
    return(
        <div class="jumbotron  jumbotronStyle_2 rounded">
        <h1>Podpunkty do rozkazu</h1>
        <Dropdown onSelect={handleSelect} onDeselect={handleDeselect}>
          <Dropdown.Toggle variant="primary" id="multi-checkbox-dropdown" style={{ width: "100%" ,backgroundColor: '#e0a158'}}>
            {selectedItems.length === 0
              ? "Wybierz kategorie"
              : `${selectedItems.length} kategorie`}
          </Dropdown.Toggle>
          <Dropdown.Menu style={{ width: "100%", backgroundColor: '#d6c0a8' }}>
            <Form>
              <Form.Check
                type="checkbox"
                label="Wstęp"
                id="item1"
                checked={selectedItems.includes("item1")}
                onChange={(e) => {
                  if (e.target.checked) {
                    handleSelect("item1");
                  } else {
                    handleDeselect("item1");
                  }
                }}
              />
              <Form.Check
                type="checkbox"
                label="Wyjątki z rozkazu"
                id="item2"
                checked={selectedItems.includes("item2")}
                onChange={(e) => {
                  if (e.target.checked) {
                    handleSelect("item2");
                  } else {
                    handleDeselect("item2");
                  }
                }}
              />
              <Form.Check
                type="checkbox"
                label="Uchwały"
                id="item3"
                checked={selectedItems.includes("item3")}
                onChange={(e) => {
                  if (e.target.checked) {
                    handleSelect("item3");
                  } else {
                    handleDeselect("item3");
                  }
                }}
              />
              <Form.Check
                type="checkbox"
                label="Zwolnienia"
                id="item4"
                checked={selectedItems.includes("item4")}
                onChange={(e) => {
                  if (e.target.checked) {
                    handleSelect("item4");
                  } else {
                    handleDeselect("item4");
                  }
                }}
              />
              <Form.Check
                type="checkbox"
                label="Przyznanie stopni,sprawności"
                id="item5"
                checked={selectedItems.includes("item5")}
                onChange={(e) => {
                  if (e.target.checked) {
                    handleSelect("item5");
                  } else {
                    handleDeselect("item5");
                  }
                }}
              />
            </Form>
          </Dropdown.Menu>
        </Dropdown>
      </div>
    )
}

export default SelectionOfTabs