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
import "./RaportView"

function Generate() {
    return(
        <div class="jumbotron jumbotronStyle_3 rounded">
            <h1 class="display-4">Pole nr 3</h1>
            <p class="lead">
              Kliknij poniższy przycisk, aby wygenerować raport w formacie PDF.
            </p>
            <a class="btn btn-light btn-lg" href="/raport/raport_viev" role="button">
              Generuj raport
            </a>
        </div>
    )
}

export default Generate
