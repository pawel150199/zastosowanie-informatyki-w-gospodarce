import React from "react";

import "./RaportView";

import "./raport_style.css";

function Generate() {
  return (
    <div className="jumbotron jumbotronStyle_3 rounded">
      <h1 className="display-4">Pole nr 3</h1>
      <p className="lead">
        Kliknij poniższy przycisk, aby wygenerować raport w formacie PDF.
      </p>
      <a
        className="btn btn-light btn-lg"
        href="/raport/raport_viev"
        role="button"
      >
        Generuj raport
      </a>
    </div>
  );
}

export default Generate;
