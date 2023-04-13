import React from 'react'

const NotFound = () => {
    return (
                <div>
                  <meta charSet="UTF-8" />
                  <meta httpEquiv="X-UA-Compatible" content="IE=edge" />
                  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                  <title>Bootstrap 5 404 Error Page</title>
                  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" />
                  <div className="d-flex align-items-center justify-content-center vh-100">
                    <div className="text-center">
                      <h1 className="display-1 fw-bold">404</h1>
                      <p className="fs-2"> <span className="text-danger">Opps!</span> Strona nie została znaleziona.</p>
                      <p className="lead">
                        Strona której szukasz nie istnieje.
                      </p>
                      <a href="/" className="btn btn-primary">Wróć do strony głównej</a>
                    </div>
                  </div>
                </div>
              
    );
}

export default NotFound;