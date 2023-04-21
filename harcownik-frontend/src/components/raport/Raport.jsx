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
import pdfjsLib from "pdfjs-dist";
import "./raport_style.css";

const Raport = () => {
  const [pdf, setPdf] = useState(null);
  const [pageNumber, setPageNumber] = useState(1);
  const [editing, setEditing] = useState(false);
  const [canvas, setCanvas] = useState(null);

  useEffect(() => {
    if (pdf) {
      renderPage();
    }
  }, [pdf, pageNumber]);

  const handleFileSelect = async (event) => {
    const file = event.target.files[0];
    const fileReader = new FileReader();
    fileReader.onload = async () => {
      const pdfData = new Uint8Array(fileReader.result);
      const pdfDoc = await pdfjsLib.getDocument({ data: pdfData }).promise;
      setPdf(pdfDoc);
      setPageNumber(1);
    };
    fileReader.readAsArrayBuffer(file);
  };

  const renderPage = async () => {
    const page = await pdf.getPage(pageNumber);
    const viewport = page.getViewport({ scale: 1.5 });
    const canvasContext = canvas.getContext("2d");
    canvas.height = viewport.height;
    canvas.width = viewport.width;
    await page.render({ canvasContext, viewport }).promise;
  };

  const handlePageChange = (delta) => {
    setPageNumber(Math.max(1, Math.min(pageNumber + delta, pdf.numPages)));
  };

  const handleEditClick = () => {
    setEditing(true);
  };

  const handleSaveClick = async () => {
    const pdfData = await pdf.getData();
    // TODO: Save the modified PDF data
    setEditing(false);
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
    <div style={{ marginTop: 0 }} class="container">
      <Row>
        <div class="jumbotron jumbotronStyle_0 rounded">
          <h1>Zakładka służąca do generowania raportu</h1>
        </div>
      </Row>
      <Row>
        <Col md={5}>
          <div class="jumbotron jumbotronStyle_1 rounded ">
            <h1>Zgłoszenia</h1>
          </div>
        </Col>
        <Col md={7}>
          <div class="jumbotron  jumbotronStyle_2 rounded">
            <h1>Podpunkty do rozkazu</h1>
            <Dropdown onSelect={handleSelect} onDeselect={handleDeselect}>
              <Dropdown.Toggle variant="primary" id="multi-checkbox-dropdown">
                {selectedItems.length === 0
                  ? "Select items"
                  : `${selectedItems.length} items selected`}
              </Dropdown.Toggle>
              <Dropdown.Menu>
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
          {/* <h1>Generuj pdf z rozkazem</h1>
                <h1>Report</h1>
                {pdf ? (
                  <div>
                    <div className="d-flex justify-content-between mb-3">
                      <Button
                        variant="primary"
                        onClick={() => handlePageChange(-1)}
                        disabled={pageNumber <= 1}
                      >
                        Previous
                      </Button>
                      <span>Page {pageNumber}</span>
                      <Button
                        variant="primary"
                        onClick={() => handlePageChange(1)}
                        disabled={pageNumber >= pdf.numPages}
                      >
                        Next
                      </Button>
                    </div>
                    <canvas
                      id="pdfCanvas"
                      ref={(el) => setCanvas(el)}
                      style={{ border: "1px solid black" }}
                    />
                    {editing ? (
                      <div>
                        {/* TODO: Add form to modify PDF contents */}
          {/* <Button variant="primary" onClick={handleSaveClick}>
                          Save
                        </Button>
                      </div>
                    ) : (
                      <div>
                        <Button variant="primary" onClick={handleEditClick}>
                          Edit
                        </Button>
                      </div>
                    )}
                    
                  </div> */}
          {/* // ) : (
                //   <div>
                //     <p>Select a PDF file to view:</p>
                //     <input type="file" accept=".pdf" onChange={handleFileSelect} />
                //   </div>
                // )} */}
          {/* </div> */}
          <div class="jumbotron jumbotronStyle_3 rounded">
            <h1 class="display-4">Pole nr 3</h1>
            <p class="lead">
              Kliknij poniższy przycisk, aby wygenerować raport w formacie PDF.
            </p>
            <Form>
              <Form.Group controlId="formBasicName" className=" form_place ">
                <FormControl type="text"  placeholder="Wprowadź tekst" className=" form_place_space" />
              </Form.Group>
            </Form>
            <a class="btn btn-light btn-lg" href="#" role="button">
              Generuj raport
            </a>
          </div>
        </Col>
      </Row>
    </div>

    // <div>
    //   <h1>Report</h1>
    //   {pdf ? (
    //     <div>
    //       <div className="d-flex justify-content-between mb-3">
    //         <Button
    //           variant="primary"
    //           onClick={() => handlePageChange(-1)}
    //           disabled={pageNumber <= 1}
    //         >
    //           Previous
    //         </Button>
    //         <span>Page {pageNumber}</span>
    //         <Button
    //           variant="primary"
    //           onClick={() => handlePageChange(1)}
    //           disabled={pageNumber >= pdf.numPages}
    //         >
    //           Next
    //         </Button>
    //       </div>
    //       <canvas
    //         id="pdfCanvas"
    //         ref={(el) => setCanvas(el)}
    //         style={{ border: '1px solid black' }}
    //       />
    //       {editing ? (
    //         <div>
    //           {/* TODO: Add form to modify PDF contents */}
    //           <Button variant="primary" onClick={handleSaveClick}>
    //             Save
    //           </Button>
    //         </div>
    //       ) : (
    //         <div>
    //           <Button variant="primary" onClick={handleEditClick}>
    //             Edit
    //           </Button>
    //         </div>
    //       )}
    //     </div>
    //   ) : (
    //     <div>
    //       <p>Select a PDF file to view:</p>
    //       <input type="file" accept=".pdf" onChange={handleFileSelect} />
    //     </div>
    //   )}
    // </div>
  );
};

export default Raport;
