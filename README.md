# Szybki tutorial

## Frontend
**Na początek proponuje odpalać frontend bez kontenerów :)**

Przy użyciu środowiska node można w łatwy sposób zainstalować wszystkie zależności 
oraz odpalić cały fronten

`npm install` -> instaluje wszystkie potrzebne zależności
`npm start` -> odpala serwer

Aby zamknąć serwer wystarczy użyć kombinacji `CTRL + C`

## Kontenery
Wszystkie usługi działają w kontenerach i są odpalane przy użyciu `docker-compose up`.
Wszystkie niezbędne obrazy będą dostępne w moim dockerhubie.
W celu stworzenia najnowszego obrazu udostępnie joba Github Action, który zrobi to automatycznie.

## Dodawanie zmian na repozytorium
W związku z faktem, że nasze repozytorium powinno blokować `push` na mastera należy:
* Stworzyć swojego lokalnego brancha `git checkout -b <BRANCH_NAME>`
* Wprowadzić zmiany
* Dodać commita `git commit -a -m "comments"`
* Zpuszować na waszego brancha `git push --set-upstream origin <BRANCH_NAME>`
* Otworzyć `Pull Request`
* Czekać na review :)

