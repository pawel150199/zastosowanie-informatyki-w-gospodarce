/* eslint-disable */
import pdfMake from "pdfmake/build/pdfmake";
import axios from "../../api/api";
import pdfFonts from "pdfmake/build/vfs_fonts";
import {
  scoutSign,
  scoutCity,
  scoutLevel,
  scoutId,
  raportAmound,
} from "./SelectionOfTabs";
import { postPdfRaport } from "./RaportFunction";
import getMe from "../../api/getMe";

/*
Component responsible for storing the content of raport and generating it in pdf format.
*/

export let userSign = null;
export function updateTabs(updatedTabs) {
  tabs = updatedTabs;
}
export let tabs = [
  {
    id: "0",
    label: "Wstęp",
    isChecked: false,
    patternText: `Wstęp okolicznościowy (Proszę uzupełnić święta państwowe, rocznice, szczególne wydarzenia w Związku).\n`,
  },
  {
    id: "1",
    label: "Wyjątki z rozkazu",
    isChecked: false,
    patternText: `Wyjątki z rozkazu komendanta Hufca ZHP ......
      (Proszę uzupełnić sprawy ogólnohufcowe lub dotyczące drużyny, m.in.: pełnienie funkcji na wyższych szczeblach
      struktury, przyznanie odznaczeń lub stopni instruktorskich instruktorom danej drużyny).\n`,
  },
  {
    id: "2",
    label: "Zarządzenia",
    isChecked: false,
    patternText: `Zwołuję …………………..\n`,
  },
  {
    id: "3",
    label: "Informacje",
    isChecked: false,
    patternText: `Podaję do wiadomości, że ………
      Informuję o decyzji ….\n`,
  },
  {
    id: "4",
    label: "Mianowania",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny mianuję ….. na …… z dniem ……..\n`,
  },
  {
    id: "5",
    label: "Zwolnienia",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny zwalniam  ……… z …….z dniem ………\n`,
  },
  {
    id: "6",
    label: "Utworzenie zastępu",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny powołuję zastęp  w składzie:
      •	… 
      •	…
      \n`,
  },
  {
    id: "7",
    label: "Rozwiązanie zastępu",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny rozwiązuję zastęp …\n`,
  },
  {
    id: "8",
    label: "Zamknięcie próby na stopień ",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny z dnia ……… zamykam próbę i przyznaję stopień …….\n`,
  },
  {
    id: "9",
    label: "Otwarcie próby na stopień",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na stopień ……:\n`,
  },
  {
    id: "10",
    label: "Zamknięcie próby na sprawność",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na sprawność …..:\n`,
  },
  {
    id: "11",
    label: "Otwarcie próby na sprawność",
    isChecked: false,
    patternText: `Na wniosek Rady Drużyny z dnia ………. otwieram próbę na sprawność …..:\n`,
  },
  {
    id: "12",
    label: "Otwarcia i Zamknięcia inne\n",
    isChecked: false,
    patternText: `...\n`,
  },
  {
    id: "13",
    label: "Sprawy członkowskie",
    isChecked: false,
    patternText: `...\n`,
  },
  {
    id: "14",
    label: "Kary organizacyjne",
    isChecked: false,
    patternText: `Udzielam upomnienia  *komu* *za co*\n`,
  },
  {
    id: "15",
    label: "Pochwały, wyróżnienia, nagrody",
    isChecked: false,
    patternText: `Udzielam pochwały *komu* *za co*\n`,
  },
];

export const scoutOrder = ({}) => {
  pdfMake.vfs = pdfFonts.pdfMake.vfs;
  const currentDate = new Date();
  const year = currentDate.getFullYear();
  const month = currentDate.getMonth() + 1;
  const day = currentDate.getDate();

  const monthNames = [
    "stycznia",
    "lutego",
    "marca",
    "kwietnia",
    "maja",
    "czerwca",
    "lipca",
    "sierpnia",
    "września",
    "października",
    "listopada",
    "grudnia",
  ];

  const monthWord = monthNames[month - 1];
  const tittle = `Rozkaz ${month}/${year}.${raportAmound}`;
  const selectedTabs = tabs.filter((tab) => tab.isChecked);
  const patternTexts = selectedTabs.map((tab, index) => ({
    text: [
      { text: `${index + 1}. ${tab.label}\n`, fontSize: 14, bold: true },
      { text: tab.patternText.split("\n").join("\n\n") },
    ],
  }));

  const documentDefinition = {
    info: {
      title: `Rozkaz ${month}/${year}`,
      author: "Harcownik App",
    },
    content: [
      {
        text: `${scoutCity}, ${day} ${monthWord} ${year}`,
        style: "date",
        alignment: "right",
      },
      {
        text: `Rozkaz L. ${tittle}`,
        style: "title",
        alignment: "center",
      },
      ...patternTexts,
      { text: "Czuwaj!", style: "rightAlign" },
      { text: `${scoutLevel} ${scoutSign}`, style: "rightAlign" },
      {
        text: "Wygenerowane za pomocą aplikacji Harcownik",
        style: "centerAlign",
      },
    ],
    styles: {
      date: { fontSize: 12 },
      title: { fontSize: 18, bold: true, margin: [0, 20, 0, 20] },
      rightAlign: { alignment: "right", margin: [0, 10, 0, 0] },
      centerAlign: { alignment: "center", margin: [0, 10, 0, 20] },
    },

    footer: {
      text: `Wygenerowane za pomocą aplikacji Harcownik`,
      alignment: "center",
      fontSize: 8,
    },
  };

  const generatePDF = () => {
    pdfMake
      .createPdf(documentDefinition)
      .open(
        {},
        window.open("", "_blank"),
        null,
        null,
        null,
        null,
        null,
        "filename.pdf"
      );
  };

  const generatePDF_ = () => {
    return new Promise((resolve) => {
      pdfMake.createPdf(documentDefinition).getBlob((blob) => {
        const file = new File([blob], tittle, {
          type: "application/pdf",
        });
        resolve(file);
      });
    });
  };

  const uploadPDF = async () => {
    try {
      const formData = new FormData();
      formData.append("name", tittle);
      formData.append("user_id", scoutId);
      formData.append("file", await generatePDF_());

      const response = await axios.post("/report/pdf", formData, {
        headers: {
          accept: "application/json",
          "Content-Type": "multipart/form-data",
        },
      });

      console.log("PDF uploaded successfully!", response.data);
    } catch (error) {
      console.error("Error uploading PDF:", error);
    }
  };
  uploadPDF();

  return generatePDF();
};
