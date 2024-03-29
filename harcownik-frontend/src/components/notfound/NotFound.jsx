import React from "react";

/* 
Not found page which be visible if target component is not avaible
*/

const NotFound = () => {
  return (
    <div className="d-flex align-items-center justify-content-center vh-100">
      <div className="text-center">
        <h1 className="display-1 fw-bold">404</h1>
        <p className="fs-2">
          {" "}
          <span className="text-danger">Upps!</span> Strona nie została
          znaleziona.
        </p>
        <p className="lead">Strona której szukasz nie istnieje.</p>
        <a href="/" className="btn btn-primary">
          Wróć do strony głównej
        </a>
      </div>
    </div>
  );
};

export default NotFound;
