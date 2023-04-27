/* eslint-disable */
import React, { useState, useEffect } from "react";
import "./UserRequests.css";
import Dropdown from "react-bootstrap/Dropdown";
import axios from "axios";
import DropdownButton from 'react-bootstrap/DropdownButton';
import { Button } from "react-bootstrap";

function UserEfficiency() {

  const [data, setData] = useState([]);

//   function GetBadgeGroups() {
//     axios.get("http://localhost:8000/badges/")
//     .then(response => {
//       setData(response.data);
//     })
//     .catch(error => {
//       console.log(error);
//     });
//   }
// };



  useEffect(() => {
    axios.get("http://localhost:8000/badges/")
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  const [value, setValue]=useState('');

  const handleSelect=(e)=>{
    setValue(e);
    console.log(e);
  }

 function PostBadge() {
  axios.post("http://localhost:8000/badge_reports/",{
  // axios.post("http://localhost:8000/badge_reports/groups/",{
    "title": value,
    "status": "zgłoszona",
    "user_id": 1,
    "badge_id": 3,
  })
  .then(function(response){
    console.log(response);
  })
  };
 


    return(
        <div className="jumbotron UserEfficiencyStyle rounded" >
          <h1>Zakładka służąca rozpoczęcia nowej sprawnośći</h1>
          <DropdownButton
        alignRight
        title="Wybierz sprawność"
        id="dropdown-menu-align-right"
        // onSelect={handleSelect}>
        //         {data.map(report => (
        //   <Dropdown.Item key={report.id} eventKey={report.name} onSelect={handleSelect}>{report.name}</Dropdown.Item>
        // ))}
        // </DropdownButton>
        onSelect={handleSelect}>
                {data.map(report => (
          <Dropdown.Item key={report.id} eventKey={report.name} onSelect={handleSelect}>{report.name}</Dropdown.Item>
        ))}
        </DropdownButton>
    <h1>Wybrałeś wartość {value}</h1>
    <Button onClick={() => PostBadge()}>Rozpocznij sprawność</Button>
    </div>
    );
  }


export default UserEfficiency;
