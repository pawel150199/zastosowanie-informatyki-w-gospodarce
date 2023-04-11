# Zarządzanie migracjami bazy danych
Alembic to narzędzie do zarządzania migracjami.
Oznacza to, że przy zmianach struktury bazy danych możemy ją zupdatować odpowiednią komendą, bez usuwania jej.
<br></br>

## Tworzenie migracji
W celu stworzenia migracji należy wprowadzić komendę `alembic revision --autogenerate -m "description"`. Nowa migracja pojawi się w katalogu `versions`.
<br></br>

## Update bazy danych
W celu zmiany bazy danych zgodnie z ostatnią migracją należy wprowadzić komendę `alembic upgrade head`
<br></br>
