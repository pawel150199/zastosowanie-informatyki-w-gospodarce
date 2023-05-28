/* eslint-disable */
import React, { useEffect, useState } from "react";
import axios from "axios";

const CityInfo = ({ city }) => {
  const [country, setCountry] = useState("");
  const [flag, setFlag] = useState("");

  useEffect(() => {
    axios
      .get(
        `http://api.geonames.org/searchJSON?q=${city}&maxRows=1&username=YOUR_USERNAME`
      )
      .then((response) => {
        const data = response.data.geonames[0];
        const countryName = data.countryName;
        const countryCode = data.countryCode.toLowerCase();
        const flagUrl = `https://www.countryflags.io/${countryCode}/shiny/64.png`;

        setCountry(countryName);
        setFlag(flagUrl);
      })
      .catch((error) => {
        console.log(error);
      });
  }, [city]);

  return (
    <div>
      <h2>{city}</h2>
      {flag && <img src={flag} alt="Flag" style={{ height: "100px" }} />}
      {country && <p>Country: {country}</p>}
    </div>
  );
};

export default CityInfo;
