# Harcownik API (WIP)

## Użyte technologie
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Alpine Linux](https://img.shields.io/badge/Alpine_Linux-%230D597F.svg?style=for-the-badge&logo=alpine-linux&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
<br></br>

## Instalacja aplikacji
W celu instalacji należy zainstalować pythona w wersji 3.9 i doinstalować paczkę poetry.
Po tym kroku można zainstalować wszystkie wymagane paczki komendą `poetry install`
## Jak uruchomić?
W celu uruchomienia API należy użyć komendy `uvicorn src.main:app --reload`
<br></br>

## Dokumentacja API
W ramach API dostępna jest dokumentacja w oparciu na narzędzie jakim jest swagger. Umozliwia on przeglądanie wszystkich dostępnych endpointów oraz testowanie ich. Dokumentacja dostępna jest pod adresem `http://<SERVER>:<PORT>/docs`
<br></br>
