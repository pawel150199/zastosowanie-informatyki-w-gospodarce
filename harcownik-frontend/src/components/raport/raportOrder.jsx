/* eslint-disable */
import React from "react";

function getCurrentYear() {
  const now = new Date();
  return now.getFullYear();
}

const currentYear = getCurrentYear();
export function updateTabs(updatedTabs) {
  tabs = updatedTabs;
}
export let tabs = [
  {
    id: "0",
    label: "Wstęp",
    isChecked: false,
    patternText: `\nWstęp okolicznościowy (Proszę uzupełnić święta państwowe, rocznice, szczególne wydarzenia w Związku).\n`,
  },
  {
    id: "1",
    label: "Wyjątki z rozkazu",
    isChecked: false,
    patternText: `\nWyjątki z rozkazu komendanta Hufca ZHP ......
      (Proszę uzupełnić sprawy ogólnohufcowe lub dotyczące drużyny, m.in.: pełnienie funkcji na wyższych szczeblach
      struktury, przyznanie odznaczeń lub stopni instruktorskich instruktorom danej drużyny).\n`,
  },
  {
    id: "2",
    label: "Zarządzenia",
    isChecked: false,
    patternText: `\nZwołuję …………………..\n`,
  },
  {
    id: "3",
    label: "Informacje",
    isChecked: false,
    patternText: `\nPodaję do wiadomości, że ………
      Informuję o decyzji ….\n`,
  },
  {
    id: "4",
    label: "Mianowania",
    isChecked: false,
    patternText: `\nNa wniosek Rady Drużyny mianuję ….. na …… z dniem ……..\n`,
  },
  {
    id: "5",
    label: "Zwolnienia",
    isChecked: false,
    patternText: `\nNa wniosek Rady Drużyny zwalniam  ……… z …….z dniem ………\n`,
  },
  {
    id: "6",
    label: "Utworzenie zastępu",
    isChecked: false,
    patternText: `\nNa wniosek Rady Drużyny powołuję zastęp  w składzie:
      •	… 
      •	…
      \n`,
  },
  {
    id: "7",
    label: "Rozwiązanie zastępu",
    isChecked: false,
    patternText: `\nNa wniosek Rady Drużyny rozwiązuję zastęp …\n`,
  },
  {
    id: "8",
    label: "Zamknięcie próby na stopień ",
    isChecked: false,
    patternText: `\nNa wniosek Rady Drużyny z dnia ……… zamykam próbę i przyznaję stopień …….\n`,
  },
  {
    id: "9",
    label: "Otwarcie próby na stopień",
    isChecked: false,
    patternText: `\nNa wniosek Rady Drużyny z dnia ………. otwieram próbę na stopień ……:\n`,
  },
  {
    id: "10",
    label: "Zamknięcie próby na sprawność",
    isChecked: false,
    patternText: `\nNa wniosek Rady Drużyny z dnia ………. otwieram próbę na sprawność …..:\n`,
  },
  {
    id: "11",
    label: "Otwarcie próby na sprawność",
    isChecked: false,
    patternText: `\nNa wniosek Rady Drużyny z dnia ………. otwieram próbę na sprawność …..:\n`,
  },
  {
    id: "12",
    label: "\nOtwarcia i Zamknięcia inne\n",
    isChecked: false,
    patternText: `...`,
  },
  {
    id: "13",
    label: "Sprawy członkowskie",
    isChecked: false,
    patternText: `\n...\n`,
  },
  {
    id: "14",
    label: "Kary organizacyjne",
    isChecked: false,
    patternText: `\nUdzielam upomnienia  *komu* *za co*\n`,
  },
  {
    id: "15",
    label: "Pochwały, wyróżnienia, nagrody",
    isChecked: false,
    patternText: `\nUdzielam pochwały *komu* *za co*\n`,
  },
];

export const scoutOrder = ({}) => {
  const selectedTabs = tabs.filter((tab) => tab.isChecked);
  const patternTexts = selectedTabs.map((tab, index) => (
    <div key={tab.id}>
      <h3>{`${index + 1}. ${tab.label}`}</h3>
      <p>{tab.patternText}</p>
    </div>
  ));

  return (
    <div>
      <h1 style={{ textAlign: "center" }}>Rozkaz L. 3/{currentYear}</h1>
      <p>{patternTexts}</p>
      <p style={{ textAlign: "right" }}>Czuwaj!</p>
      <p style={{ textAlign: "right" }}>phm. </p>
    </div>
  );
};