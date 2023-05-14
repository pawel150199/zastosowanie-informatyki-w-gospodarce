/* eslint-disable */
import React from "react";

export let tabs = [
  {
    id: "0",
    label: "Wstęp",
    isChecked: false,
    patternText: `Wstęp okolicznościowy (Proszę uzupełnić święta państwowe, rocznice, szczególne wydarzenia w Związku).`,
    // textValue: "",
  },
  {
    id: "1",
    label: "Wyjątki z rozkazu",
    isChecked: false,
    patternText: `Wyjątki z rozkazu komendanta Hufca ZHP ......
      (Proszę uzupełnić sprawy ogólnohufcowe lub dotyczące drużyny, m.in.: pełnienie funkcji na wyższych szczeblach
      struktury, przyznanie odznaczeń lub stopni instruktorskich instruktorom danej drużyny).`,
    // textValue: "",
  },
  {
    id: "2",
    label: "Zarządzenia",
    isChecked: false,
    patternText: `Zwołuję …………………..`,
    // textValue: "",
  },
  {
    id: "3",
    label: "Informacje",
    isChecked: false,
    patternText: `Podaję do wiadomości, że ………
      Informuję o decyzji ….`,
    // textValue: "",
  },
  {
    id: "4",
    label: "Mianowania",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny mianuję ….. na …… z dniem ……..`,
    // textValue: "",
  },
  {
    id: "5",
    label: "Zwolnienia",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny zwalniam  ……… z …….z dniem ………`,
    // textValue: "",
  },
  {
    id: "6",
    label: "Utworzenie zastępu",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny powołuję zastęp  w składzie:
      •	… 
      •	…
      `,
    // textValue: "",
  },
  {
    id: "7",
    label: "Rozwiązanie zastępu",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny rozwiązuję zastęp …`,
    // textValue: "",
  },
  {
    id: "8",
    label: "Zamknięcie próby na stopień ",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny z dnia ……… zamykam próbę i przyznaję stopień ……. `,
    // textValue: "",
  },
  {
    id: "9",
    label: "Otwarcie próby na stopień",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na stopień ……:`,
    // textValue: "",
  },
  {
    id: "10",
    label: "Zamknięcie próby na sprawność",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na sprawność …..:`,
    // textValue: "",
  },
  {
    id: "11",
    label: "Otwarcie próby na sprawność",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na sprawność …..:`,
    // textValue: "",
  },
  {
    id: "12",
    label: "Otwarcia i Zamknięcia inne",
    isChecked: false,
    patternText: `...`,
    // textValue: "",
  },
  {
    id: "13",
    label: "Sprawy członkowskie",
    isChecked: false,
    patternText: `...`,
    // textValue: "",
  },
  {
    id: "14",
    label: "Kary organizacyjne",
    isChecked: false,
    patternText: `Udzielam upomnienia  *komu* *za co*`,
    // textValue: "",
  },
  {
    id: "15",
    label: "Pochwały, wyróżnienia, nagrody",
    isChecked: false,
    patternText: `Udzielam pochwały *komu* *za co*`,
    // textValue: "",
  },
];

// export const RozkazL = ({
//   numer,
//   rok,
//   swieta,
//   rocznice,
//   wydarzenia,
//   zarzadzenia,
//   informacje,
//   mianowania,
//   zwolnienia,
//   utworzenieZastepu,
//   rozwiazanieZastepu,
//   zamkniecieProbyStopnia,
//   otwarcieProbyStopnia,
//   zamkniecieProbySprawnosci,
//   otwarcieProbySprawnosci,
//   inne,
//   upomnienie,
//   pochwała,
//   czuwaj,
//   komendantHufca,
// }) => {
//   return (
//     <div>
//       <h1>
//         Rozkaz L. {numer}/{rok}
//       </h1>
//       <p>{swieta}</p>
//       <p>{rocznice}</p>
//       <p>{wydarzenia}</p>

//       <h2>
//         Wyjątki z rozkazu komendanta Hufca ZHP Bydgoszcz-Miasto L. {numer}/{rok}{" "}
//         z dnia ….
//       </h2>

//       <h3>Zarządzenia i informacje</h3>

//       <h4>Zarządzenia</h4>
//       <p>Zwołuję {zarzadzenia}</p>

//       <h4>Informacje</h4>
//       <p>Podaję do wiadomości, że {informacje}</p>
//       <p>Informuję o decyzji {informacje}</p>

//       <h3>Drużyna</h3>

//       <h4>Mianowania</h4>
//       <p>
//         Na wniosek Rady Drużyny mianuję {mianowania} na {mianowania} z dniem{" "}
//         {mianowania}
//       </p>

//       <h4>Zwolnienia</h4>
//       <p>
//         Na wniosek Rady Drużyny zwalniam {zwolnienia} z {zwolnienia} z dniem{" "}
//         {zwolnienia}
//       </p>

//       <h3>Zastępy</h3>

//       <h4>Utworzenie zastępu</h4>
//       <p>Na wniosek Rady Drużyny powołuję zastęp w składzie:</p>
//       <ul>
//         <li>{utworzenieZastepu}</li>
//         <li>{utworzenieZastepu}</li>
//       </ul>

//       <h4>Rozwiązanie zastępu</h4>
//       <p>Na wniosek Rady Drużyny rozwiązuję zastęp {rozwiazanieZastepu}</p>

//       <h3>Instrumenty metodyczne</h3>

//       <h4>Zamknięcie próby na stopień</h4>
//       <p>
//         Na wniosek Rady Drużyny z dnia {zamkniecieProbyStopnia} zamykam próbę i
//         przyznaję stopień {zamkniecieProbyStopnia} komu {komu}
//       </p>

//       <h4>Otwarcie próby na stopień</h4>
//     </div>
//   );
// };
