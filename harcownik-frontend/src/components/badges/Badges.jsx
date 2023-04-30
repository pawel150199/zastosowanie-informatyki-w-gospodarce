import axios from "axios";
import React from "react";
import { useState, useEffect } from "react";
import { Accordion } from "react-bootstrap";

import BadgeItem from "./BadgeItem";


const Badges = () => {
/*
  const [badges, setBadges] = useState();

  useEffect(() => {
    const fetchData = async() => {
      const response = await axios.get("http://localhost:8000/badges/all");
      setBadges(response.data);
    }
    fetchData();
  }, []);

  console.log("XDDD" + badges)
*/

  const badges = [
    {
      group: "Sprawności Łącznościowe",
      badges: [
        {
          name: "Goniec",
          description: [
            "Wskazała / wskazał drogę do urzędów i ważnych miejsc w swojej miejscowości",
            "Dostarczyła / dostarczył list lub ustną wiadomość do adresata w wyznaczonym terminie",
            "Nadała / nadał na poczcie: list polecony, przekaz pieniężny, paczkę",
            "Bezbłędnie przekazała / przekazał meldunek w czasie gry terenowej, posługując się wybranymi sposobami łączności"
          ],
        },
        {
          name: "Zwiadowca",
          description: [
            "W nieznanym terenie niedostrzeżenie podeszła / podszedł wskazany obiekt",
            "Przeprowadziła / przeprowadził zwiad, sporządzając szczegółowy raport z opisem wykonanych zadań i zaobserwowanych zdarzeń",
            "Nawiązała / nawiązał łączność za pomocą radia CB, przekazała / przekazał informacje zdobyte podczas zwiadu",
            "Wie, jakie są zasady i sposoby przekazywania oraz gromadzenia poufnych informacji (np. danych osobowych), szczególnie w Internecie"
          ],
        },
        // add more badges here
      ],
    },
    {
      group: "Sprawności Inne",
      badges: [
        {
          name: "Goniec",
          description: [
            "Wskazała / wskazał drogę do urzędów i ważnych miejsc w swojej miejscowości",
            "Dostarczyła / dostarczył list lub ustną wiadomość do adresata w wyznaczonym terminie",
            "Nadała / nadał na poczcie: list polecony, przekaz pieniężny, paczkę",
            "Bezbłędnie przekazała / przekazał meldunek w czasie gry terenowej, posługując się wybranymi sposobami łączności"
          ],
        },
        {
          name: "Zwiadowca",
          description: [
            "W nieznanym terenie niedostrzeżenie podeszła / podszedł wskazany obiekt",
            "Przeprowadziła / przeprowadził zwiad, sporządzając szczegółowy raport z opisem wykonanych zadań i zaobserwowanych zdarzeń",
            "Nawiązała / nawiązał łączność za pomocą radia CB, przekazała / przekazał informacje zdobyte podczas zwiadu",
          ],
        },
        // add more badges here
      ]
    },
    // add more groups here
  ];
  

  return (
    <Accordion defaultActiveKey={["0"]}>
      {badges.map((group, index) => (
        <Accordion.Item key={index} eventKey={index} className="mb-3">
          <Accordion.Header>{group.group}</Accordion.Header>
          <Accordion.Body>
            {group.badges.map((badge, index) => (
              <BadgeItem key={index} badge={badge} />
            ))}
          </Accordion.Body>
        </Accordion.Item>
      ))}
    </Accordion>
  );
};

export default Badges;