/* eslint-disable */
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Button, Container } from "react-bootstrap";
import { saveAs } from "file-saver";
import { Form, Dropdown, FormGroup, FormControl } from "react-bootstrap";
import { getLoginStatus } from "../../api/utils";
import getMe from "../../api/getMe";
import { tabs } from "./raportOrder";

import "./raport_style.css";

export let orderContent = "";

// export let tabs = [
//   {
//     id: "0",
//     label: "Wstęp",
//     isChecked: false,
//     patternText: `Wstęp okolicznościowy (Proszę uzupełnić święta państwowe, rocznice, szczególne wydarzenia w Związku).`,
//     // textValue: "",
//   },
//   {
//     id: "1",
//     label: "Wyjątki z rozkazu",
//     isChecked: false,
//     patternText: `Wyjątki z rozkazu komendanta Hufca ZHP ......
//     (Proszę uzupełnić sprawy ogólnohufcowe lub dotyczące drużyny, m.in.: pełnienie funkcji na wyższych szczeblach
//     struktury, przyznanie odznaczeń lub stopni instruktorskich instruktorom danej drużyny).`,
//     // textValue: "",
//   },
//   {
//     id: "2",
//     label: "Zarządzenia",
//     isChecked: false,
//     patternText: `Zwołuję …………………..`,
//     // textValue: "",
//   },
//   {
//     id: "3",
//     label: "Informacje",
//     isChecked: false,
//     patternText: `Podaję do wiadomości, że ………
//     Informuję o decyzji ….`,
//     // textValue: "",
//   },
//   {
//     id: "4",
//     label: "Mianowania",
//     isChecked: false,
//     patternText: `Na wniosek Rady Drużyny mianuję ….. na …… z dniem ……..`,
//     // textValue: "",
//   },
//   {
//     id: "5",
//     label: "Zwolnienia",
//     isChecked: false,
//     patternText: `Na wniosek Rady Drużyny zwalniam  ……… z …….z dniem ………`,
//     // textValue: "",
//   },
//   {
//     id: "6",
//     label: "Utworzenie zastępu",
//     isChecked: false,
//     patternText: `Na wniosek Rady Drużyny powołuję zastęp  w składzie:
//     •	…
//     •	…
//     `,
//     // textValue: "",
//   },
//   {
//     id: "7",
//     label: "Rozwiązanie zastępu",
//     isChecked: false,
//     patternText: `Na wniosek Rady Drużyny rozwiązuję zastęp …`,
//     // textValue: "",
//   },
//   {
//     id: "8",
//     label: "Zamknięcie próby na stopień ",
//     isChecked: false,
//     patternText: `Na wniosek Rady Drużyny z dnia ……… zamykam próbę i przyznaję stopień ……. `,
//     // textValue: "",
//   },
//   {
//     id: "9",
//     label: "Otwarcie próby na stopień",
//     isChecked: false,
//     patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na stopień ……:`,
//     // textValue: "",
//   },
//   {
//     id: "10",
//     label: "Zamknięcie próby na sprawność",
//     isChecked: false,
//     patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na sprawność …..:`,
//     // textValue: "",
//   },
//   {
//     id: "11",
//     label: "Otwarcie próby na sprawność",
//     isChecked: false,
//     patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na sprawność …..:`,
//     // textValue: "",
//   },
//   {
//     id: "12",
//     label: "Otwarcia i Zamknięcia inne",
//     isChecked: false,
//     patternText: `...`,
//     // textValue: "",
//   },
//   {
//     id: "13",
//     label: "Sprawy członkowskie",
//     isChecked: false,
//     patternText: `...`,
//     // textValue: "",
//   },
//   {
//     id: "14",
//     label: "Kary organizacyjne",
//     isChecked: false,
//     patternText: `Udzielam upomnienia  *komu* *za co*`,
//     // textValue: "",
//   },
//   {
//     id: "15",
//     label: "Pochwały, wyróżnienia, nagrody",
//     isChecked: false,
//     patternText: `Udzielam pochwały *komu* *za co*`,
//     // textValue: "",
//   },
// ];

export default function SelectionOfTabs() {
  // const [tabs, setTabs] = useState([
  //   // {
  //   //   id: "20",
  //   //   label: "Hufiec",
  //   //   isChecked: true,
  //   //   patternText: `Związek Harcerstwa Polskiego
  //   //   Hufiec Wąchock
  //   //   Drużynowy 17 DH „Pioruny”
  //   //   im. Zeusa Gromowładnego`,
  //   //   // textValue: "",
  //   // },
  //   {
  //     id: "0",
  //     label: "Wstęp",
  //     isChecked: false,
  //     patternText: `Wstęp okolicznościowy (Proszę uzupełnić święta państwowe, rocznice, szczególne wydarzenia w Związku).`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "1",
  //     label: "Wyjątki z rozkazu",
  //     isChecked: false,
  //     patternText: `Wyjątki z rozkazu komendanta Hufca ZHP ......
  //     (Proszę uzupełnić sprawy ogólnohufcowe lub dotyczące drużyny, m.in.: pełnienie funkcji na wyższych szczeblach
  //     struktury, przyznanie odznaczeń lub stopni instruktorskich instruktorom danej drużyny).`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "2",
  //     label: "Zarządzenia",
  //     isChecked: false,
  //     patternText: `Zwołuję …………………..`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "3",
  //     label: "Informacje",
  //     isChecked: false,
  //     patternText: `Podaję do wiadomości, że ………
  //     Informuję o decyzji ….`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "4",
  //     label: "Mianowania",
  //     isChecked: false,
  //     patternText: `Na wniosek Rady Drużyny mianuję ….. na …… z dniem ……..`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "5",
  //     label: "Zwolnienia",
  //     isChecked: false,
  //     patternText: `Na wniosek Rady Drużyny zwalniam  ……… z …….z dniem ………`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "6",
  //     label: "Utworzenie zastępu",
  //     isChecked: false,
  //     patternText: `Na wniosek Rady Drużyny powołuję zastęp  w składzie:
  //     •	…
  //     •	…
  //     `,
  //     // textValue: "",
  //   },
  //   {
  //     id: "7",
  //     label: "Rozwiązanie zastępu",
  //     isChecked: false,
  //     patternText: `Na wniosek Rady Drużyny rozwiązuję zastęp …`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "8",
  //     label: "Zamknięcie próby na stopień ",
  //     isChecked: false,
  //     patternText: `Na wniosek Rady Drużyny z dnia ……… zamykam próbę i przyznaję stopień ……. `,
  //     // textValue: "",
  //   },
  //   {
  //     id: "9",
  //     label: "Otwarcie próby na stopień",
  //     isChecked: false,
  //     patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na stopień ……:`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "10",
  //     label: "Zamknięcie próby na sprawność",
  //     isChecked: false,
  //     patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na sprawność …..:`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "11",
  //     label: "Otwarcie próby na sprawność",
  //     isChecked: false,
  //     patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na sprawność …..:`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "12",
  //     label: "Otwarcia i Zamknięcia inne",
  //     isChecked: false,
  //     patternText: `...`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "13",
  //     label: "Sprawy członkowskie",
  //     isChecked: false,
  //     patternText: `...`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "14",
  //     label: "Kary organizacyjne",
  //     isChecked: false,
  //     patternText: `Udzielam upomnienia  *komu* *za co*`,
  //     // textValue: "",
  //   },
  //   {
  //     id: "15",
  //     label: "Pochwały, wyróżnienia, nagrody",
  //     isChecked: false,
  //     patternText: `Udzielam pochwały *komu* *za co*`,
  //     // textValue: "",
  //   },
  // ]);
  const [selectedItems, setSelectedItems] = useState([]);
  const [raportContent, setRaportContent] = useState();
  const [userData, setUserData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      if (getLoginStatus("isLogged")) {
        const response = await getMe();
        const user = response.first_name + "  " + response.last_name;
        setUserData(user);
        console.log("response_user_name:", userData);
      }
    };
    fetchData();
  }, []);

  const handleSelect = (eventKey) => {
    if (!selectedItems.includes(eventKey)) {
      setSelectedItems([...selectedItems, eventKey]);
    }
  };

  const handleDeselect = (eventKey) => {
    setSelectedItems(selectedItems.filter((item) => item !== eventKey));
  };

  const handleTextValueChange = (event, tab) => {
    console.log("event", event);
    console.log("tab", tab.patternText);
    const updatedTabs = tabs.map((t) => {
      if (t.id === tab.id) {
        return { ...t, patternText: event.target.value };
      } else {
        return t;
      }
    });
    tabs = updatedTabs;
    // setTabs(updatedTabs);
  };

  function handleDownload() {
    const selectedTabs = tabs.filter((tab) => selectedItems.includes(tab.id));
    console.log("selectedTabs:", selectedTabs);
    const fileContent = selectedTabs.map((tab) => tab.patternText).join("\n\n");
    console.log("fileContent:", fileContent);

    // const orderPattern = {
    //   heading: "ROZKAZ HARCERSKI",
    //   addressee: "Druchny i druchowie",
    //   contents: `\n\n${fileContent}`,
    //   signature: "Komendant drużyny",
    //   date: "Warszawa, 13 maja 2023 r.",
    // };

    orderContent = `Związek Harcerstwa Polskiego                       Kg, dnia 22.22.222
    Hufiec Wąchock
    Drużynowy 17 DH „Pioruny”
    im. Zeusa Gromowładnego
                                            Rozkaz L.3/2019

      \n\n${fileContent}\n\n

                                                                 Czuwaj !
                                                                 phm. ${userData}

    `;

    // orderContent = `${orderPattern.heading}\n\n${orderPattern.addressee}\n\n${orderPattern.contents}\n\n${orderPattern.signature}\n\n${orderPattern.date}`;
    console.log("orderContent:", orderContent);

    const blob = new Blob([orderContent], {
      type: "text/plain;charset=utf-8",
    });
    // saveAs(blob, "rozkaz.txt");
    console.log("orderContent:", orderContent);

    setRaportContent(orderContent);
  }

  return (
    <div className="jumbotron jumbotronStyle_2 rounded">
      <h1>Podpunkty do rozkazu</h1>
      <Form>
        {tabs.map((tab) => (
          <div key={tab.id}>
            <Form.Check
              type="checkbox"
              label={tab.label}
              id={tab.id}
              checked={selectedItems.includes(tab.id)}
              onChange={(e) => {
                if (e.target.checked) {
                  handleSelect(tab.id);
                  tab.isChecked = true;
                  console.log("ischecked", tab.isChecked, tab.label);
                } else {
                  handleDeselect(tab.id);
                  console.log("ischecked", tab.isChecked, tab.label);
                }
              }}
            />
            {selectedItems.includes(tab.id) && (
              <Form.Group controlId="exampleForm.ControlTextarea1">
                <Form.Control
                  as="textarea"
                  rows={3}
                  value={tab.value}
                  defaultValue={tab.patternText}
                  onChange={(e) => handleTextValueChange(e, tab)}
                />
              </Form.Group>
            )}
          </div>
        ))}
      </Form>
      <Link to="/raport/raport_view" id="raport_view">
        <Button
          variant="primary"
          className="mt-3 badge"
          onClick={handleDownload}
        >
          Przygotuj raport
        </Button>
      </Link>
    </div>
  );
}
