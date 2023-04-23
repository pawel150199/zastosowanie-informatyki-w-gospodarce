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

// import Jumbotron1 from "./Jumbotron0";
// import Jumbotron2 from "./Jumbotron1";
// import "./Jumbotron0"
// import "./Jumbotron1"
import Raport_Headear from "./Raport_Headear";
import Submissions from "./Submissions";
import SelectionOfTabs from "./SelectionOfTabs";
import Generate from "./Generate";
import Efficiency from "./Efficiency";

const Raport = () => {
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

  return (
    <div  class="container">
      <Row>
        <Raport_Headear />
      </Row>
      <Row>
        <Col md={7}>
          <Submissions />
          <Efficiency />
        </Col>
        <Col md={5}>
          <SelectionOfTabs />
          <Generate />
        </Col>
      </Row>
    </div>
  );
};

export default Raport;
