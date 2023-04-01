import React from 'react';
import { Accordion } from 'react-bootstrap';
import BadgeItem from './BadgeItem';

const Badges = () => {
  const lacznoscioweBadges = [
    {
      name: 'Goniec',
      description: [
        "Wskazała / wskazał drogę do urzędów i ważnych miejsc w swojej miejscowości",
        "Dostarczyła / dostarczył list lub ustną wiadomość do adresata w wyznaczonym terminie",
        "Nadała / nadał na poczcie: list polecony, przekaz pieniężny, paczkę",
        "Bezbłędnie przekazała / przekazał meldunek w czasie gry terenowej, posługując się wybranymi sposobami łączności"
      ],
    },
    {
      name: 'Zwiadowca',
      description: [
        "W nieznanym terenie niedostrzeżenie podeszła / podszedł wskazany obiekt",
        "Przeprowadziła / przeprowadził zwiad, sporządzając szczegółowy raport z opisem wykonanych zadań i zaobserwowanych zdarzeń",
        "Nawiązała / nawiązał łączność za pomocą radia CB, przekazała / przekazał informacje zdobyte podczas zwiadu",
        "Wie, jakie są zasady i sposoby przekazywania oraz gromadzenia poufnych informacji (np. danych osobowych), szczególnie w Internecie"
      ],
    },
    // add more badges here
  ];

  const kucharskieBadges = [
    {
      name: 'Kuchcik',
      description: [
        "Przygotował/a w terenie posiłek dla zastępu, korzystając z kuchni polowej lub kuchenki turystycznej",
        "Zadbał/a o estetyczny wygląd polowego stołu",
        "Przygotował/a sniadanie lub kolacje dla domowników"
      ],
    },
    {
      name: 'Kucharz',
      description: [
        "Prawidłowo posługiwała / posługiwał się sprzętem kuchennym (nożami, tłuczkami, maszynką do mielenia, garnkami i patelniami, cedzakiem)",
        "Ułożyła / ułożył urozmaicony jadłospis na kilkudniowy biwak lub na tydzień obozu dla całej drużyny",
        "Przygotowała / przygotował dwudaniowy obiad dla rodziny, estetycznie go podając",
        " Wybrała / wybrał na biwaku miejsce na kuchnię, urządziła / urządził ją funkcjonalnie",
      ],
    },
    // add more badges here with
  ];

  const przyrodniczeBadges = [
    {
      name: "Przyrodniczka/Przyrodnik",
      description: [
        "Harcerz rozpoznaje po sylwetkach liści dziesięć drzew",
        "Rozpoznała/rozpoznał na rysunku lub zdjęciu po pięć gatunków roślin",
        "Uczestniczył/uczestniczyła w wycieczce do lasu, ułożyła/ułożył w zastępie pięć zasad zachowania się w lesie"
      ],
    },
    {
      name: "Przyjaciel przyrody",
      description: [
        "Wskazał/a na mapie Polski parki narodowe oraz znajdujące się w okolicy rezerwaty przyrody",
        "Uczesniczył/a w wycieczce do rezerwatu przyrody",
        "Brał/a udział w pracy na rzecz parku"
      ],
    },
  ];

  const wyrobienieHarcerskieBadges = [
    {
      name: "Robinson",
      description: [
        "W dowolnej formie udokumentował/a swoje postrzezenia wobec zwierząt lub roślin",
        "Przeprowadził/a w pobliżu obozu w samotności kilkugodzinną oberwacje zycia lasu",
        "Przygotował/a dla zastępu posiłek z zebranych owoców",
      ]
    }
  ];

  return (
    <Accordion defaultActiveKey={['0']} alwaysOpen>

      <Accordion.Item eventKey="0" className="mb-3">
        <Accordion.Header>Sprawności Łącznościowe</Accordion.Header>
        <Accordion.Body>
          {lacznoscioweBadges.map((badge, index) => (
            <BadgeItem key={index} badge={badge} />
          ))}
        </Accordion.Body>
      </Accordion.Item>

      <Accordion.Item eventKey="1" className="mb-3">
        <Accordion.Header>Sprawności Kucharskie</Accordion.Header>
        <Accordion.Body>
          {kucharskieBadges.map((badge, index) => (
            <BadgeItem key={index} badge={badge} />
          ))}
        </Accordion.Body>
      </Accordion.Item>

      <Accordion.Item eventKey="2" className="mb-3">
        <Accordion.Header>Sprawności Przyrodnicze</Accordion.Header>
        <Accordion.Body>
          {przyrodniczeBadges.map((badge, index) => (
            <BadgeItem key={index} badge={badge} />
          ))}
        </Accordion.Body>
      </Accordion.Item>

      <Accordion.Item eventKey="3" className="mb-3">
        <Accordion.Header>Sprawności Wyrobienie Harcerskie</Accordion.Header>
        <Accordion.Body>
          {wyrobienieHarcerskieBadges.map((badge, index) => (
            <BadgeItem key={index} badge={badge} />
          ))}
        </Accordion.Body>
      </Accordion.Item>
      
    </Accordion>
  );
};

export default Badges;