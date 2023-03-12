# Aplikacja do rozliczania ze znajomymi
## Opis tematu <a name="Opis"></a>
Celem projektu jest stworzenie strony internetowej umożliwiającej zalogowanym użytkownikom na rozliczanie się za np. wspólny obiad. Użytkownik po zalogowaniu będzie mógł stworzyć wydarzenie, do którego doda innych członków a następni przypisze np. pozycje z rachunku wraz z cenami oraz informacją kto dokonał płatności. W przypadku wielu takich paragonów system wyliczy należności dla poszczególnych użytkowników w taki sposób, aby jak najbardziej zminimalizować ilość koniecznych transakcji przez użytkowników.

## Plan minimum <a name="Opis"></a>
- Tworzenie oraz logowanie się przez użytkownika,
- Tworzenie wydarzenia np. „Wyjazd do Kąsławic Dolno-Górnych”,
- Dodanie innych uczestników do wydarzenia,
- Ręczne wprowadzenie np. paragonów wraz z informacją o osobie płacącej,

## Plan rozszerzony <a name="Opis"></a>
- Tworzenie zestawień oraz podsumowań(np. w pdf) z każdego wydarzenia,
- Automatyczne rozpoznawanie pozycji z paragonu na podstawie wstawionego zdjęcia,
- Możliwość dodawania numeru konta bankowego do użytkownika,
- Generacja zestawienia z informacją, komu dany użytkownik powinien zwrócić pieniądze(np. w formie tabeli wraz z podanymi numerami kont i kwotami),

## Konkurencja <a name="Opis"></a>
Istniejące rozwiązania dostępne są w formie aplikacji mobilnych, brakuje na rynku rozwiązania w formie aplikacji webowej.

## Aspekty biznesowe <a name="Opis"></a>
Początkową formą zysku z apikacji były by dochody z wyświetlanych na niej reklamach.

## Stack technologiczny

Backend:
* Python
* fastAPI
  
Frontend:
* React
* js
* html
* css

CI/CD
* Github Actions
* bash
* Docker
  
Baza danych:
* AWS RDS

Infrastruktura:
* AWS

