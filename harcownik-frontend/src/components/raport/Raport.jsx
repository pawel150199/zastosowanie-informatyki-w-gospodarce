import React, { useState, useEffect } from "react";
import { Container, Row, Col, Jumbotron, Button } from "react-bootstrap";
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

  return (
    <div class="container">
      <Row>
        <div class="jumbotron jumbotronStyle_0 rounded">
          <h1 >Zakładka służąca do generowania raportu</h1>
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
            <h1>Generuj pdf z rozkazem</h1>
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
                    <Button variant="primary" onClick={handleSaveClick}>
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
              </div>
            ) : (
              <div>
                <p>Select a PDF file to view:</p>
                <input type="file" accept=".pdf" onChange={handleFileSelect} />
              </div>
            )}
          </div>
          <div class="jumbotron jumbotronStyle_3 rounded">
            <h1 class="display-4">Pole nr 3</h1>
            <p class="lead">
              Kliknij poniższy przycisk, aby wygenerować raport w formacie PDF.
            </p>
            <hr class="my-4"></hr>
            {/* <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p> */}
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
