from sqlalchemy.orm import Session
from src import crud, schemas
from src.core.settings import settings


def init_badges(db: Session) -> None:

    badges = [
        # SPRAWNOŚCI SAMARYTAŃSKIE
        schemas.CreateBadge(
            name="HIGIENISTKA / HIGIENISTA *",
            description=[
                "1. Założyła /założył opatrunek, nakleiła /nakleił plaster z opatrunkiem, zabandażowała /zabandażował kończynę, wykorzystała /wykorzystał do założenia opatrunku chustę trójkątną.",
                "2. Zabezpieczyła / zabezpieczył się przed przeziębieniem, odmrożeniem.",
                "3. Potrafi prawidłowo postąpić w przypadku skaleczenia, otarcia nogi, niewielkiego oparzenia, krwotoku z nosa, użądlenia przez pszczołę lub osę.",
                "4. Zmierzyła / zmierzył temperaturę. Wie, jaka jest prawidłowa temperatura ciała.",
                "5. Poznała / poznał alarmowe numery telefonów. Wie, kiedy i w jaki sposób należy z nich korzystać.",
            ],
            group="Samarytańskie",
        ),
        schemas.CreateBadge(
            name="SANITARIUSZKA / SANITARIUSZ **",
            description=[
                "1. Poznała/poznał zasady kompletowania apteczki. Skompletowała/skompletował apteczkę osobistą.",
                "2. Potrafi prawidłowo postąpić w przypadku: krwotoku (np. z kończyny), stłuczenia, zaprószenia oka, omdlenia, konieczności unieruchomienia kończyny, konieczności udrożnienia górnych dróg oddechowych.",
                "3. Pełniła / pełnił służbę samarytańską na wycieczce, biwaku lub obozie.",
                "4. Prawidłowo sprawdziła /sprawdził tętno.",
            ],
            group="Samarytańskie",
        ),
        schemas.CreateBadge(
            name="RATOWNICZKA / RATOWNIK ***",
            description=[
                "1. Skompletowała / skompletował torbę pierwszej pomocy dla drużyny na rajd, wycieczkę lub biwak.",
                "2. Wie, jak postąpić w przypadku zatrucia pokarmowego (substancjami chemicznymi, grzybami, zepsutą żywnością).",
                "3. Potrafi udzielić pomocy w przypadku utraty przytomności. Ułożyła / ułożył poszkodowanego w pozycji bocznej bezpiecznej.",
                "4. Umie zorganizować transport chorego. Zastosowała/zastosował różne sposoby przenoszenia rannych. Kierując patrolem noszowym, pokonała/pokonał kilka przeszkód (zejście do dołu, podejście pod górę, pokonanie ogrodzenia).",
                "5. Brała / brał udział w zawodach w ratownictwie lub ratowniczej grze terenowej. Pełniła / pełnił służbę w ambulatorium obozowym lub podczas dużej imprezy, opiekowała/opiekował się chorym.",
            ],
            group="Samarytańskie",
        ),
        schemas.CreateBadge(
            name="LIDER ZDROWIA ***",
            description=[
                "1. Włączyła / włączył do swojego postępowania jak najwięcej elementów zdrowego stylu życia (np. zdrowe odżywianie, higiena nauki i pracy, zwalczanie stresu, uprawianie sportu).",
                "2. Wskazała / wskazał rówieśnikom korzyści płynące ze zdrowego trybu życia.",
                "3. Zorganizowała / zorganizował i przeprowadziła / przeprowadził z drużyną akcję promującą zdrowy tryb życia.",
                "4. Potrafi wymienić metody i ośrodki leczenia uzależnienia od nikotyny, alkoholu i narkotyków.",
                "5. Wykorzystuje posiadaną wiedzę na temat uzależnień − od nikotyny, alkoholu i narkotyków − w codziennym postępowaniu i kontaktach z innymi ludźmi.",
            ],
            group="Samarytańskie",
        ),
        # SPRAWNOŚCI PRZYRODNICZE
        schemas.CreateBadge(
            name="PRZYRODNICZKA / PRZYRODNIK *",
            description=[
                "1. Rozpoznała / rozpoznał po sylwetkach i liściach dziesięć drzew (np. dąb, brzozę, klon, leszczynę, wierzbę, topolę, lipę, sosnę, świerk, jodłę, modrzew).",
                "2. Rozpoznała / rozpoznał na rysunku lub zdjęciu po pięć gatunków roślin i zwierząt chronionych występujących w Polsce.",
                "3. Uczestniczyła / uczestniczył w wycieczce do lasu, ułożyła / ułożył i przedstawiła / przedstawił w zastępie pięć zasad zachowania się w lesie.",
                "4. Samodzielnie lub z zastępem zasadziła/zasadził drzewko w pobliżu swojego domu, na działce lub przy szkole.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="PRZYJACIEL PRZYRODY **",
            description=[
                "1. Wskazała / wskazał na mapie Polski parki narodowe oraz znajdujące się w okolicy (np. w gminie lub powiecie) rezerwaty przyrody, parki krajobrazowe i wybrane pomniki przyrody. Wyjaśniła / wyjaśnił cele, dla których je utworzono.",
                "2. Uczestniczyła / uczestniczył w wycieczce do rezerwatu przyrody lub parku narodowego. Zachowywała / zachowywał się zgodnie z obowiązującym tam regulaminem.",
                "3. Brała /brał udział w pracy na rzecz środowiska naturalnego, np. w parku, na szlaku turystycznym, podczas imprezy ekologicznej.",
                "4. W swoim domu oszczędza wodę i energię elektryczną, dba o wykorzystanie surowców wtórnych.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="ZNAWCA PRZYRODY ***",
            description=[
                "1. Skompletowała / skompletował biblioteczkę (książki, artykuły, foldery, adresy stron internetowych) o tematyce ekologicznej.",
                "2. Poznała / poznał zasady ekologicznego obozowania. Zastosowała / zastosował je w praktyce.",
                "3. Wzięła / wziął udział w akcji na rzecz ratowania lub ochrony środowiska naturalnego.",
                "4. Przygotowała / przygotował i przeprowadziła / przeprowadził zbiórkę na temat znaczenia przyrody dla zdrowia człowieka oraz potrzeby jej ochrony przed zagrożeniami cywilizacyjnymi.",
                "5. Zapoznała / zapoznał się z celami i działaniami kilku wybranych organizacji ekologicznych",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="EKOLOG (mistrzowska)",
            description=[
                "1. Poznała / poznał systematykę roślin i zwierząt. Poznała / poznał rośliny i zwierzęta chronione w Polsce.",
                "2. Przedstawiła / przedstawił w interesującej formie bogactwo polskich lasów oraz znaczenie lasów dla przyszłości człowieka na Ziemi.",
                "3. Wskazała / wskazał występujące w polskich lasach zagrożenia dotyczące drzew, ptaków i zwierząt.",
                "4. Poznała / poznał zasady ekologicznego obozowania. Zastosowała / zastosował je w praktyce.",
                "5. Wyznaczyła / wyznaczył sobie dodatkowe zadania mistrzowskie.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="PRZYJACIEL ROŚLIN *",
            description=[
                "1. Opiekowała / opiekował się roślinami w domu, w harcówce, w szkolnej pracowni lub na działce przez cały okres próby na sprawność.",
                "2. Odwiedziła / odwiedził ogród botaniczny (była / był na łące, w lesie, w polu itp.) i opowiedziała / opowiedział na zbiórce o swoich obserwacjach dotyczących występującej tam roślinności.",
                "3. Rozpoznała / rozpoznał na zdjęciach i w naturze po pięć roślin trujących, leczniczych, chwastów i zbóż.",
                "4. Zna rośliny i owoce jadalne występujące w lesie. Przygotowała / przygotował z nich posiłek, np. podwieczorek dla zastępu.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="ZIELARKA / ZIELARZ **",
            description=[
                "1. Prowadziła / prowadził zbiór roślin (zna kalendarz ich zbierania i wie, jakie części roślin należy zbierać). Zbiera, suszy i przechowuje rośliny tak, aby nie straciły swoich właściwości.",
                "2. Przygotowała / przygotował do apteczki drużyny zestaw ziół oraz krótki opis sposobu ich stosowania.",
                "3. Przygotowała / przygotował informację o wybranych 15 roślinach chronionych występujących w Polsce i przedstawiła/przedstawił ją na zbiórce zastępu, drużyny lub w klasie.",
                "4. Przyrządziła / przyrządził ziołowy środek przydatny w leczeniu, kosmetyce lub gospodarstwie domowym.",
                "5. Rozpoznała / rozpoznał grzyby jadalne i trujące.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="BOTANIK ***",
            description=[
                "1. Przedstawiła / przedstawił na zbiórce drużyny wybrane gatunki występujących na świecie roślin zagrożonych wyginięciem („czerwona księga”).",
                "2. Opowiedziała / opowiedział w drużynie o interesujących roślinach, występujących w rezerwacie lub parku narodowym w swojej okolicy.",
                "3. Przedstawiła/przedstawił zastępowi lub drużynie swoje zbiory: albumy, atlasy i inne publikacje na temat roślin, zaprezentowała/zaprezentował ich zawartość.",
                "4. Zorganizowała / zorganizował i poprowadziła / poprowadził wyprawę drużyny (lub klasy) w celu poznania środowiska roślinnego (np. lasu, łąki) lub wyprawę do ogrodu botanicznego albo muzeum przyrodniczego.",
                "5. Wykonała / wykonał projekt przydomowego, działkowego lub przyszkolnego ogródka.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="KWIACIARKA / KWIACIARZ *",
            description=[
                "1. W bukiecie 15 kwiatów rozpoznała / rozpoznał kwiaty ogrodowe, doniczkowe, polne i chwasty.",
                "2. Wie, w jakich miesiącach i porach roku kwitną w Polsce poszczególne kwiaty.",
                "3. Założyła / założył w czasie próby własny ogródek kwiatowy, np. na klombie, w doniczkach, na działce.",
                "4. Ułożyła / ułożył bukiet z kwiatów lub przedstawiła / przedstawił na zbiórce foldery, zdjęcia i rysunki najciekawszych okazów.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="MIŁOŚNICZKA KWIATÓW / MIŁOŚNIK KWIATÓW **",
            description=[
                "1. Ułożyła / ułożył bukiety ze świeżych kwiatów na różne okazje.",
                "2. Wie, co to jest ikebana. Wykonała / wykonał kwiatową dekorację na wybraną uroczystość w rodzinie, szkole lub drużynie.",
                "3. Zastosowała / zastosował suszone rośliny do wykonania różnych ozdób.",
                "4. Pielęgnowała / pielęgnował w czasie próby rzadki lub trudny w uprawie okaz rośliny. Swoje doświadczenia z uprawy przedstawiła / przedstawił w zastępie.",
                "5. Wie, jakie kwiaty można uprawiać w Polsce i jakie sprowadza się z zagranicy.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="LEŚNIK ***",
            description=[
                "1. Śledziła/śledził życie lasu o różnych porach dnia i nocy, w tym tropiła/tropił zwierzęta, rozpoznawała/rozpoznawał ich legowiska i znała/znal jego zwyczaje.",
                "2. Wykazywała/wykazywał znajomość drzew i umiejętność ich rozpoznawania, np. podczas odbycia obchodu lasu z leśniczym.",
                "3. Zorganizowała/zorganizował zwiad lub wycieczkę do lasu dla młodszych członków zastępu lub drużyny, pokazując bogactwo lasu.",
                "4. Uczestniczyła/uczestniczył w pracach leśnych, takich jak prace w szkółce, oczyszczanie pasów przeciwpożarowych lub sadzenie drzew.",
                "5. Przedstawiła/przedstawił na zbiórce drużyny bogactwo polskich lasów oraz ich znaczenie dla człowieka na Ziemi, wskazując zagrożenia dla drzew, ptaków i zwierząt występujące w lasach.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="OGRODNICZKA / OGRODNIK ***",
            description=[
                "1. Na zbiórce zastępu przedstawiła / przedstawił znaczenie gleby i nawożenia dla uprawy warzyw.",
                "2. Rozpoznała / rozpoznał nasiona marchwi, pietruszki, sałaty, ogórków i buraczków. Wyhodowała/wyhodował własne rośliny z nasion i rozsady.",
                "3. Przygotowała / przygotował kompost z odpadów ogrodniczych.",
                "4. Zaplanowała / zaplanował siew i zbieranie plonów na działce lub w ogrodzie.",
                "5. Przygotowała / przygotował wybrane warzywa do przechowania podczas zimy.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="SADOWNICZKA / SADOWNIK * * *",
            description=[
                "1. Rozpoznała / rozpoznał po pniach i liściach popularne drzewa owocowe: jabłonie, grusze, śliwy, wiśnie, czereśnie.",
                "2. Zerwała / zerwał i ułożyła/ułożył w skrzynce owoce, przygotowując je do trans-portu.",
                "3. Przygotowała / przygotował owoce do składowania przez zimę.",
                "4. Brała / brał udział w pielęgnacji sadu, szczepieniu drzewek i zabezpieczeniu go przed szkodnikami.",
                "5. Przedstawiła/przedstawił na zbiórce zastępu lub drużyny zebrane przez siebie artykuły i poradniki dotyczące sadownictwa.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="PRZYJACIEL ZWIERZĄT *",
            description=[
                "1. Wzięła / wziął udział w zimowym dokarmianiu dzikich zwierząt w najbliższych lasach oraz dowiedziała / dowiedział się, jakie zwierzęta należy pomagać.",
                "2. Rozpoznała / rozpoznał tropy dzikich zwierząt, takich jak dzik, sarna, zając.",
                "3. Poznała / poznał głosy pięciu różnych zwierząt, nagrywając je i odtwarzając na zbiórce drużyny po wycieczce do lasu, pola lub łąki.",
                "4. Obserwowała / obserwował życie zwierząt domowych przez miesiąc, zapisując najciekawsze spostrzeżenia i opowiadając o nich na zbiórce zastępu.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="ZNAWCA ZWIERZĄT * *",
            description=[
                "1. Rozpoznała / rozpoznał na zdjęciach i rysunkach 15 gatunków zwierząt.",
                "2. Przygotowała /przygotował informację o zwierzętach chronionych w Polsce oraz o zwierzętach niebezpiecznych zamieszkujących w Polsce i przedstawiła / przed-stawił ją na zbiórce zastępu lub drużyny.",
                "3. Pomogła / pomógł w przetrwaniu zimy potrzebującym zwierzętom (ptakom, zwierzętom w lesie, bezdomnym psom).",
                "4. Wie, jakie niebezpieczne zwierzęta żyją w Polsce. Opowiedziała / opowiedział koleżankom/kolegom, jak należy postępować w przypadku spotkania z nimi.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="ZOOLOG ***",
            description=[
                "1.Przedstawiła / przedstawił wybrane gatunki zwierząt żyjących na całym świecie, zagrożonych wyginięciem („czerwona księga”).",
                "2. Zna systematykę zwierząt. Przedstawiła / przedstawił na zbiórce lub na lekcji życie wybranego gatunku.",
                "3. Zaprezentowała / zaprezentował zastępowi lub drużynie swoje zbiory: albumy, atlasy i inne publikacje na temat zwierząt, opowiedziała / opowiedział o ich zawartości.",
                "4. Zorganizowała / zorganizował dla zastępu wyprawę do zoo, muzeum przyrodniczego lub lasu, opowiedziała / opowiedział o wybranych gatunkach zwierząt. Nauczyła / nauczył zastęp sposobów obserwacji zwierząt.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="PSZCZELARZ ***",
            description=[
                "1. Od wiosny do jesieni pracowała / pracował w pasiece i prowadziła / prowadził notatnik swoich czynności.",
                "2. Nauczyła / nauczył się zabezpieczać pszczoły przed zimą.",
                "3. Potrafi postępować w przypadku użądlenia przez owady.",
                "4. Opowiedziała / opowiedział na zbiórce o właściwościach leczniczych produktów wytwarzanych przez pszczoły.",
                "5. Urządziła / urządził w harcówce, szkole lub w gminie wystawę wydawnictw dotyczących pszczelarstwa i produktów wytworzonych przez pszczoły.",
            ],
            group="Przyrodnicze",
        ),
        schemas.CreateBadge(
            name="HODOWCA (GOŁĘBI, KRÓLIKÓW, RYBEK) **",
            description=[
                "1. Przeczytała / przeczytał literaturę dotyczącą hodowli wybranych zwierząt.",
                "2. Przygotowała / przygotował dla swoich zwierząt pomieszczenia i utrzymuje je w stałej czystości.",
                "3. Zaprezentowała/zaprezentował na zbiórce zastępu wyhodowane przez siebie zwierzęta, opowiedziała/opowiedział o ich zwyczajach, sposobach żywienia i zapobiegania chorobom.",
                "4. Zwraca uwagę osobom, które źle odnoszą się do zwierząt i ptaków.",
            ],
            group="Przyrodnicze",
        ),
        # WYROBIENIE HARCERSKIE
        schemas.CreateBadge(
            name="ROBINSON **",
            description=[
                "1. Przeprowadziła / przeprowadził w pobliżu obozu w samotności kilkugodzinną obserwację życia lasu o wschodzie Słońca.",
                "2. W dowolnej formie udokumentowała / udokumentował swoje spostrzeżenia (zauważone zwierzęta i ich tropy, zjawiska przyrody, występujące rośliny chronione, jadalne itp.), zaprezentowała / zaprezentował je na zbiórce zastępu.",
                "3. Przygotowała / przygotował dla zastępu posiłek, korzystając z zebranych owoców lasu.",
                "4. Wraz z kolegą / koleżanką biwakowała / biwakował w pobliżu obozu przez 24 godziny.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="LEŚNY CZŁOWIEK ***",
            description=[
                "1. Odbyła / odbył samotną wędrówkę po lesie (od świtu do zmroku), zdobyła / zdobył pożywienie z dziko rosnących roślin.",
                "2. Przeprowadziła / przeprowadził obserwacje i poznała / poznał różnorodność ekosystemów leśnych w Polsce.",
                "3. Przygotowała / przygotował prezentację multimedialną lub gawędę o ekologii lasu i przedstawiła / przedstawił ją na zbiórce zastępu, drużyny lub w klasie.",
                "4. Znajdując się w lesie, zbudowała / zbudował schronienie i zaprezentowała / zaprezentował swój sposób na przetrwanie w warunkach naturalnych.",
                "5. Poprowadziła / poprowadził wyprawę drużyny (lub klasy) po lesie, zwracając uwagę na najważniejsze cechy i zasady zachowania się w lesie.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="TRZY PIÓRA (mistrzowska)",
            description=[
                "Przeszła / przeszedł pomyślnie trzy próby − milczenia, głodu i samotności − przez kolejne trzy doby: w czasie pierwszej doby powstrzymała / powstrzymał się od spożywania jakich-kolwiek pokarmów i napojów (z wyjątkiem czystej wody), uczestnicząc we wszystkich zajęciach obozowych, w czasie drugiej doby zachowała / zachował całkowite milczenie, trzecią dobę spędziła / spędził w lesie, niezauważona / niezauważony przez ludzi, żywiąc się pokarmem leśnym."
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="HARCOWNIK *",
            description=[
                "1. Uczestniczyła / uczestniczył w pięciu grach terenowych, przestrzegała / przestrzegał obowiązujących w nich zasad.",
                "2. Poznała / poznał 10 ćwiczeń rozwijających spostrzegawczość, refleks, pamięć.",
                "3. Uczestniczyła / uczestniczył razem z zastępem w zawodach, turnieju, meczu lub innej formie współzawodnictwa między zastępami.",
                "4. Brała / brał udział w INO, grze ekologicznej lub biegu patrolowym.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="ORGANIZATORKA HARCÓW / ORGANIZATOR HARCÓW **",
            description=[
                "1. Przeprowadziła / przeprowadził dziesięć gier terenowych i sportowych, ucząc kolegów zasad w nich obowiązujących.",
                "2. Zorganizowała / zorganizował dla zastępu (drużyny) ćwiczenia typu „kim” w harcówce i w terenie.",
                "3. Zorganizowała / zorganizował mecz, olimpiadę lub inne zawody między zastępami.",
                "4. Prowadzi własny notatnik zawierający zbiór gier i ćwiczeń do wykorzystania w pomieszczeniu i w terenie.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="MISTRZYNI HARCÓW / MISTRZ HARCÓW ***",
            description=[
                "1. Przedstawiła / przedstawił zestaw gier i ćwiczeń, zebranych w czasie próby.",
                "2. Przeprowadziła / przeprowadził po kilkanaście gier terenowych i świetlicowych w drużynie (szczepie) lub dla dzieci spoza ZHP.",
                "3. Przygotowała / przygotował trasę i program harcerskiego biegu terenowego, sprawdzającego znajomość technik harcerskich.",
                "4. Nauczyła / nauczył młodszych kilku gier i ćwiczeń do wykorzystania na zbiórkach i w szkole.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="ZNAWCA OBRZĘDÓW I ZWYCZAJÓW DRUŻYNY *",
            description=[
                "1. Poznała / poznał znaczenie słów „zwyczaje” i „obrzędy”.",
                "2. Poznała / poznał historię swojej drużyny.",
                "3. Dotarła / dotarł do kroniki lub kronik drużyny, przeczytała / przeczytał je.",
                "4. Pozyskane informacje dotyczące zwyczajów swojej drużyny przedstawiła / przedstawił na zbiórce zastępu.",
                "5. Poznała / poznał harcerskie piosenki śpiewane w drużynie, nauczyła / nauczył się ich.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="ZNAWCA ZWYCZAJÓW I TRADYCJI HARCERSTWA **",
            description=[
                "1. Wie, jak powstała pieśń „Wszystko, co nasze”.",
                "2. Wie, skąd wywodzi się tradycja pozdrowienia „czuwaj” i co ono oznacza. Przygotowała / przygotował krótką gawędę dla zastępu na ten temat.",
                "3. Poznała / poznał harcerskie zwyczaje związane z ogniskiem, napisała/ napisał artykuł do gazetki hufca (drużyny, szkoły) o tych zwyczajach.",
                "4. Zna pieśni obrzędowe, np. „Bratnie słowo”, „Płonie ognisko”. Nauczyła / nauczył młodszą harcerkę/młodszego harcerza tych pieśni.",
                "5. Zorganizowała / zorganizował przedsięwzięcie dotyczące historii lub tradycji harcerstwa (dla harcerzy,społeczności lokalnej, koleżanek i kolegów w szkole).",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="BI-PI *",
            description=[
                "1. Wie, co oznacza zwyczaj zawiązywania węzełka na chuście. Przestrzega tego zwyczaju.",
                "2. Wie, do jakich organizacji skautowych należy ZHP oraz jakie są ich symbole (lilia i koniczyna). Zaprezentowała / zaprezentował je drużynie (np. w postaci prezentacji multimedialnej lub planszy do harcówki).",
                "3. Poznała / poznał życiorys twórcy skautingu gen. Roberta Baden-Powella. Podczas zbiórki zastępu przedstawiła / przedstawił w dowolnej formie jedną z jego przy- gód.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="LILIA I KONICZYNA **",
            description=[
                "1. Zna symbolikę skautowej lilijki i koniczynki, wie, jak wyglądają oraz jaka jest ich historia.",
                "2. Wie, kiedy powstał skauting i kto go założył.",
                "3. Wie, co oznaczają skróty WOSM i WAGGGS (nauczyła/nauczył się pełnej nazwy obu organizacji w języku angielskim).",
                "4. Zdobyła / zdobył informacje o organizacji skautowej w wybranym kraju. Wybrane informacje przedstawiła / przedstawił na zbiórce drużyny",
                "5. Wzięła / wziął udział w przygotowaniu zbiórki z okazji Dnia Myśli Braterskiej. Wysłała / wysłał kartkę z życzeniami do wybranej organizacji skautowej, drużyny lub skauta.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="ZNAWCA SKAUTINGU ***",
            description=[
                "1. Zna historię skautingu − wie, jak powstał skauting i jak rozwinął się w ruch ogólnoświatowy.",
                "2. Wie, na czym polega działanie światowych organizacji skautowych (WOSM i WAGGGS).",
                "3. Zna najważniejsze organizacje skautowe działające w krajach europejskich.",
                "4. Dobrze poznała / poznał wybraną organizację skautową − zna jej historię i współczesną działalność, nawiązała / nawiązał kontakt ze skautami tej organizacji.",
                "5. Samodzielnie przygotowała / przygotował zbiórkę na temat skautingu.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="RZECZNICZKA DRUŻYNY / RZECZNIK DRUŻYNY ***",
            description=[
                "1. Zdobyła / zdobył podstawową wiedzę dotyczącą przekazu informacji, dowiedziała / dowiedział się, jak należy formułować informacje.",
                "2. Zredagowała / zredagował kilka ogłoszeń lub informacji związanych z działalnością drużyny, wywiesił je w szkole, w hufcu lub zamieścił na stronie internetowej drużyny.",
                "3. Napisała / napisał artykuł o drużynie do lokalnego pisma (wychodzącego w mieście, gminie lub powiecie).",
                "4. Systematycznie pisze artykuły o drużynie do gazetki hufca (gazetki szkolnej) lub zamieszcza teksty na stronie internetowej drużyny.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="RZECZNIK HARCERSTWA (mistrzowska)",
            description=[
                "1. Przeczytała / przeczytał trzy pozycje książkowe dotyczące przekazywania informacji.",
                "2. Poznała / poznał specyfikę strony internetowej ZHP, śledziła / śledził na bieżąco informacje dotyczące ZHP.",
                "3. Napisała / napisał artykuł do lokalnej gazety o przebiegu dowolnego przedsięwzięcia hufca, chorągwi.",
                "4. Zaprosiła / zaprosił lokalnych dziennikarzy i opiekowała / opiekował się nimi w czasie imprezy hufca.",
                "5. Ukończyła / ukończył warsztaty dziennikarskie. Uczestniczy w pracach zespołu promocji i informacji w hufcu lub w chorągwi.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="ZNAWCA MUSZTRY **",
            description=[
                "1. Zapoznała / zapoznał się z zasadami musztry.",
                "2. Nienagannie wydaje i wykonuje komendy.",
                "3. Przeprowadziła / przeprowadził zajęcia z musztry z zastępem lub drużyną.",
                "4. Brała / brał udział w pokazie musztry zastępu, drużyny lub obozu.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="MISTRZYNI MUSZTRY / MISTRZ MUSZTRY ***",
            description=[
                "1. Poznała / poznał regulamin musztry i ceremoniału harcerskiego, przestrzega go.",
                "2. Przygotowała / przygotował drużynę do uroczystości na placu, ucząc musztry i dopilnowując regulaminowego umundurowania.",
                "3. Przeprowadziła / przeprowadził pokaz musztry drużyny.",
                "4. Przeprowadziła / przeprowadził szkolenie zastępowych z zakresu musztry.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="WARTOWNICZKA / WARTOWNIK **",
            description=[
                "1. Zna i stosuje zasady służby wartowniczej ZHP.",
                "2. Pełniła/pełnił bez zarzutu służbę wartowniczą łącznie przez 12 godzin w nocy i 8 godzin w dzień.",
                "3. Pełniła / pełnił wartę na posterunku honorowym podczas trwania uroczystości.",
                "4. Wie, jakie znaczenie ma służba wartownicza dla bezpieczeństwa osób i mienia znajdującego się na terenie obozu (biwaku).",
                "5. Brała / brał udział w przynajmniej pięciu grach doskonalących czujność, spostrzegawczość itp.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="DOWÓDCA WARTY ***",
            description=[
                "1. Zdobyła / zdobył sprawność „wartownika”.",
                "2. Pełniła / pełnił funkcję dowódcy warty (instruktora służbowego na obozie, biwaku). Pokierowała / pokierował budową wartowni obozowej.",
                "3. Potrafi rozstawić wartowników, dokonać zmiany warty. Dokonała / dokonał zmiany wartowników na posterunku honorowym podczas trwania uroczystości.",
                "4. Zorganizowała / zorganizował co najmniej pięć gier doskonalących czujność oraz spostrzegawczość.",
                "5. Opiekowała/opiekował się harcerką/harcerzem zdobywającą/zdobywającym sprawność „wartownika”.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="OGNIK *",
            description=[
                "1. Zapoznała / zapoznał się ze znaczeniem odkrycia i poskromienia ognia.",
                "2. Pod opieką zastępowej / zastępowego ułożyła / ułożył ognisko i rozpaliła / rozpalił je.",
                "3. Pełniła / pełnił funkcję strażnika ognia.",
                "4. Zna gatunki drewna odpowiedniego do budowania ognisk harcerskich.",
                "5. Zatarła / zatarł ślady ogniska po jego wygaszeniu, zabezpieczyła / zabezpieczył zapałki przed zamoknięciem.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="STRAŻNICZKA OGNIA / STRAŻNIK OGNIA **",
            description=[
                "1. Pełniła / pełnił trzy służby przy ognisku, umiejętnie podkładając drwa lub gałęzie, regulując wysokość płomienia i ograniczając iskrzenie.",
                "2. Poznała / poznał przepisy przeciwpożarowe na obozach i biwakach. Dowiedziała / dowiedział się, jak ugasić na człowieku płonące ubranie. Nauczyła / nauczył się posługiwać podstawowym sprzętem gaśniczym.",
                "3. Poprawnie zbudowała / zbudował podstawowe stosy ogniskowe.",
                "4. Poznała / poznał obrzędowość związaną z harcerskim ogniskiem.",
                "5. Rozróżnia trzy podstawowe stopnie oparzenia i potrafi udzielić pierwszej pomocy w przypadku oparzenia.",
            ],
            group="Wyrobienie Harcerskie",
        ),
        schemas.CreateBadge(
            name="MISTRZYNI OGNISK / MISTRZ OGNISK ***",
            description=[
                "1. Rozpoznaje różne gatunki drewna. Wie, czym się charakteryzują i jak się palą.",
                "2. Wygłosiła/wygłosił gawędę na temat ognia i zasad zachowania się przy ognisku harcerskim.",
                "3. Przygotowała / przygotował strażników ognia do pełnienia obowiązków przy ognisku.",
                "4. Poznała / poznał różne rodzaje stosów ogniskowych, nauczyła / nauczył się je układać.",
                "5. Nauczyła / nauczył się rozpalać ognisko w trudnych warunkach atmosferycznych (wiatr, deszcz, śnieg).",
            ],
            group="Wyrobienie Harcerskie",
        ),
        #Kucharskie
        schemas.CreateBadge(
            name="KUCHCIK *",
            description=[
                "1. Przygotowała / przygotował w terenie posiłek dla zastępu, korzystając z kuchni polowej lub kuchenki turystycznej.",
                "2. Zadbała / zadbał o estetyczny wygląd polowego „stołu”.",
                "3. Przestrzegała / przestrzegał zasad higieny przy sporządzaniu posiłków i zapoznała / zapoznał z nimi zastęp.",
                "4. Przygotowała / przygotował śniadanie lub kolację dla domowników.",
                "5. Przygotowała / przygotował podwieczorek według własnego pomysłu.",
            ],
            group="Kucharskie",
        ),
        schemas.CreateBadge(
            name="KUCHARZ **",
            description=[
                "1. Prawidłowo posługiwała / posługiwał się sprzętem kuchennym (nożami, tłuczkami, maszynką do mielenia, garnkami i patelniami, cedzakiem).",
                "2. Ułożyła / ułożył urozmaicony jadłospis na kilkudniowy biwak lub na tydzień obozu dla całej drużyny.",
                "3. Przygotowała / przygotował dwudaniowy obiad dla rodziny, estetycznie go podając.",
                "4. Wybrała / wybrał na biwaku miejsce na kuchnię, urządziła / urządził ją funkcjonalnie.",
            ],
            group="Kucharskie",
        ),
        schemas.CreateBadge(
            name="KUCHMISTRZYNI / KUCHMISTRZ ***",
            description=[
                "1. Rozplanowała / rozplanował i urządziła / urządził blok kuchenny na obozie drużyny lub kilkudniowym biwaku.",
                "2. Kierowała / kierował co najmniej przez trzy dni służbą kuchenną na obozie lub na biwaku: układała / układał jadłospisy, gotowała / gotował każdego dnia inną zupę, przygotowywała / przygotowywał dania mięsne i jarskie.",
                "3. Poznała / poznał zasady racjonalnego żywienia dzieci i dorosłych.",
                "4. Ułożyła / ułożył wybraną dietę (np. niskokaloryczną, dla cukrzyków) oraz wyliczyła/wyliczył podstawowe wartości odżywcze w stosunku do tej diety.",
                "5. Przygotowała / przygotował młodszych do próby na sprawność „kuchcika”.",
            ],
            group="Kucharskie",
        ),
        #FINANSOWO-EKONOMICZNE
        schemas.CreateBadge(
            name="OSZCZĘDNA / OSZCZĘDNY *",
            description=[
                "1. Wie, jakie są podstawowe miesięczne opłaty domowe.",
                "2. Zaoszczędziła / zaoszczędził pieniądze na wybrany przez siebie cel.",
                "3. Współuczestniczyła / współuczestniczył w organizowaniu akcji zarobkowej.",
                "4. Wymieniła / wymienił surowce wtórne, które zbierała / zbierał i segregowała / segregował.",
                "5. Oszczędnie gospodaruje wszelkimi materiałami.",
            ],
            group="Finansowo-ekonomiczne",
        ),
        schemas.CreateBadge(
            name="SKARBNICZKA / SKARBNIK **",
            description=[
                "1. Poznała / poznał przepisy finansowe ZHP obowiązujące drużynę.",
                "2. Opracowała / opracował preliminarz finansowy imprezy drużyny.",
                "3. Zorganizowała / zorganizował akcję zarobkową zastępu.",
                "4. Przyjęła / przyjął składki członkowskie zastępu i prawidłowo je wpisała / wpisał do książki finansowej drużyny.",
                "5. Nauczyła / nauczył się prawidłowo wypełniać książkę finansową drużyny.",
            ],
            group="Finansowo-ekonomiczne",
        ),
        schemas.CreateBadge(
            name="FINANSISTA ***",
            description=[
                "1. Opracowała / opracował plan finansowy drużyny na rok harcerski i przedstawiła / przedstawił swoją koncepcję radzie drużyny.",
                "2. Przygotowała / przygotował i zrealizowała / zrealizował projekt mający na celu zachęcenie do oszczędzania.",
                "3. Zarządzała / zarządzał finansami biwaku drużyny: przygotowała / przygotował preliminarz, prawidłowo rozliczyła / rozliczył wydatki.",
                "4. Przedstawiła / przedstawił koleżankom i kolegom sposoby oszczędzania i gospodarowania własnymi środkami finansowymi.",
            ],
            group="Finansowo-ekonomiczne",
        ),
        schemas.CreateBadge(
            name="BANKIER *",
            description=[
                "1. Wie,zjakiegobankukorzystająrodzice,gdziesięznajdujeijakieusługioferuje.",
                "2. Opłaciła / opłacił w banku lub na poczcie rachunki domowe.",
                "3. Poznała/poznał dostępne dla siebie sposoby oszczędzania pieniędzy i przedstawiła / przedstawił je na zbiórce zastępu.",
                "4. Zaoszczędziła / zaoszczędził wyznaczoną kwotę pieniędzy, przeznaczając ją na wybrany przez siebie cel.",
            ],
            group="Finansowo-ekonomiczne",
        ),
        schemas.CreateBadge(
            name="BANKOWIEC **",
            description=[
                "1. Zebrała / zebrał informacje o ofertach różnych banków. Wie, jakie usługi oferują i na jakich warunkach, oraz które z nich mają oferty skierowane do młodzieży.",
                "2. Wie, co to jest: kredyt, pożyczka, lokata, przelew, konto bankowe.",
                "3. Potrafi wypłacić pieniądze z bankomatu. Potrafi, korzystając z Internetu, dokonać przelewu bankowego.",
                "4. Potrafi wypełnić druk przekazu i przelewu pocztowego, wie, jaka jest różnica między nimi.",
                "5. Przez okres dwóch miesięcy zbierała / zbierał systematycznie składki w zastępie / drużynie i właściwie rozliczyła / rozliczył je ze skarbnikiem drużyny.",
            ],
            group="Finansowo-ekonomiczne",
        ),
        schemas.CreateBadge(
            name="ZNAWCA BANKOWOŚCI *** ",
            description=[
                "1. Zna historię pieniądza i zaprezentowała / zaprezentował ją w ciekawej formie drużynie.",
                "2. Wie, co to jest: ROR, prowizja, stopa procentowa, kapitalizacja odsetek.",
                "3. Na podstawie zebranych informacji na temat ofert banków (w tym internetowych) wybrała / wybrał propozycję najdogodniejszą dla siebie oraz zaprezentowała / zaprezentował swój wybór drużynie i uzasadniła / uzasadnił go.",
                "4. Założyła / założył konto w banku i dokonała / dokonał na nim podstawowych operacji. Systematycznie planuje i rozlicza swoje wydatki.",
            ],
            group="Finansowo-ekonomiczne",
        ),
        schemas.CreateBadge(
            name="MŁODY PRACOWNIK ***",
            description=[
                "1. Zna różne techniki określania predyspozycji zawodowych. Dokonała / dokonał samooceny i określiła / okreśił swoje predyspozycje zawodowe.",
                "2. Zapoznała / zapoznał się z ofertami rynku pracy w wybranej przez siebie dziedzi- nie. Wie, jakie są oczekiwania potencjalnego pracodawcy.",
                "3. Przedstawiła / przedstawił drużynie techniki autoprezentacji przydatne w roz- mowach z pracodawcą.",
                "4. Zorganizowała / zorganizował szkolenie dla członków zastępu z zakresu pisania CV i listów motywacyjnych.",
                "5. Zorganizowała / zorganizował w drużynie „harcerskie pośrednictwo pracy”.",
            ],
            group="Finansowo-ekonomiczne",
        ),
        schemas.CreateBadge(
            name="PRZEWODNIK PO RYNKU PRACY (mistrzowska)",
            description=[
                "1. Systematycznie prowadzi szkolenia dla swojego środowiska harcerskiego / klasy na temat przygotowania do podjęcia pierwszej pracy.",
                "2. Współpracuje z lokalnym Urzędem Pracy w celu aktualizowania bazy ofert pracy i systematycznego przedstawiania jej w hufcu (np. gazetka, tablica ogłoszeń).",
                "3. Opracowała / opracował młodzieżowy poradnik, dotyczący przygotowania do podjęcia pierwszej pracy.",
                "4. Zapoznała / zapoznał się z możliwościami podejmowania przez młodzież pracy za granicą, wie, jakie firmy tym się zajmują. Przedstawiła / przedstawił propozycje w hufcu.",
            ],
            group="Finansowo-ekonomiczne",
        ),
        schemas.CreateBadge(
            name="MŁODYMAKLER ***",
            description=[
                "1. Wie, co oznaczają następujące pojęcia: akcja, dywidenda, obligacja. Zna rodzaje obligacji i wie, które są notowane na giełdzie.",
                "2. Wie, co to jest system WARSET.",
                "3. Zna podstawowe indeksy na giełdzie warszawskiej, ich specyfikę i potrafi podać nazwy pięciu kolejnych spółek z największym udziałem w dwóch podstawowych indeksach (WIG 20, TECHWIG).",
                "4. Potrafi krótko przedstawić rodzaje portfeli inwestycyjnych zarządzania aktywami, ich budowę oraz stopy zwrotu od początku roku podane przez trzy najlepsze w tej dziedzinie domy maklerskie.",
                "5. Przez miesiąc śledziła / śledził notowania na giełdzie wybranej spółki, oceniła / ocenił szanse opłacalności inwestycji w jej akcje i przedstawiła / przedstawił je na zbiórce drużyny.",
                "6. Przeprowadziła / przeprowadził w drużynie grę „Giełda”.",
            ],
            group="Finansowo-ekonomiczne",
        ),
        schemas.CreateBadge(
            name="MAKLER (mistrzowska)",
            description=[
                "1. Wie, co oznaczają pojęcia: futures, warrant, opcja.",
                "2. Systematycznie czyta informacje prasowe oraz korzysta z informacji w Internecie na tematy giełdowe.",
                "3. Poznała / poznał techniki gry na giełdzie, wybrała / wybrał najlepszą dla siebie.",
                "4. Zna wszystkie typy zleceń oraz ich dodatkowe warunki, potrafi dokładnie wyja- śnić specyfikę zleceń z limitem aktywacji.",
                "5. Zna wszystkie instrumenty finansowe notowane na giełdzie warszawskiej.",
                "6. Potrafi podać nazwy głównych indeksów giełd światowych.",
                "7. Otworzyła / otworzył własne konto w domu maklerskim, złożyła / złożył zlecenie. Doświadczenia przedstawiła / przedstawił na zbiórce drużyny.",
            ],
            group="Finansowo-ekonomiczne",
        ),
        #KWATERMISTRZOWSKIE
        schemas.CreateBadge(
            name="SOBIERADEK OBOZOWY *",
            description=[
                "1. Rozbiła / rozbił samodzielnie mały namiot.",
                "2. Uczestniczyła / uczestniczył w budowie urządzeń namiotowych, posługując się sprzętem pionierskim.",
                "3. Samodzielnie wykonała/wykonał przedmiot przydatny na obozie, np. kosz na śmieci, wieszak, tablicę rozkazów.",
                "4. Rozpaliła / rozpalił ogień w bezpiecznym miejscu i zatarła / zatarł dokładnie ślady po zakończeniu ogniska.",
            ],
            group="Kwatermistrzowskie",
        ),
        schemas.CreateBadge(
            name="TECHNIK OBOZOWY **",
            description=[
                "1. Umiejętnie posługiwała / posługiwał się zakonserwowanym przez siebie sprzętem pionierskim przy budowie urządzeń namiotowych.",
                "2. Zbudowała / zbudował urządzenie obozowe własnego pomysłu, stosując węzły i gwoździe odpowiedniej wielkości.",
                "3. Wraz z zastępem rozstawiała / rozstawiał namioty różnego typu i wielkości.",
                "4. Po zakończeniu obozu wraz z zastępem składała / składał namioty, przygotowując je do przechowywania w magazynie (suszyła / suszył, naprawiała / naprawiał,talkowała / talkował).",
                "",
            ],
            group="Kwatermistrzowskie",
        ),
        schemas.CreateBadge(
            name="WYGA OBOZOWY ***",
            description=[
                "1. Uczestniczyła / uczestniczył w zwiadzie kwatermistrzowskim przed obozem drużyny.",
                "2. Kierowała / kierował rozstawieniem obozu, właściwie dobierając miejsca na namioty mieszkalne, kuchnie i sanitariaty.",
                "3. Zapoznała / zapoznał się z możliwościami zastosowania różnego rodzaju drewna do budowy urządzeń obozowych.",
                "4. Budowała / budował urządzenia obozowe ogólnego użytkowania, np. kuchnię, pomosty, stołówkę.",
                "5. Brała / brał udział w kwaterce obozowej.",
            ],
            group="Kwatermistrzowskie",
        ),
        schemas.CreateBadge(
            name="MAJSTERKLEPKA *",
            description=[
                "1. Skompletowała / skompletował zestaw podstawowych narzędzi do majsterkowania i umie się nimi bezpiecznie posługiwać.",
                "2. Oczyściła / oczyścił przedmioty z drewna, metalu i tworzyw sztucznych, nie niszcząc ich.",
                "3. Skleiła / skleił rozbitą porcelanę, plastik, metal. Przedstawiła / przedstawił swoje sposoby drobnych napraw na zbiórce zastępu.",
                "4. Wykonała / wykonał proste prace, jak np. ostrzenie noży, wymiana baterii w latarce, kalkulatorze, radiu, wymiana uszczelki w kranie, naoliwienie zamka.",
            ],
            group="Kwatermistrzowskie",
        ),
        schemas.CreateBadge(
            name="GOSPODARZ **",
            description=[
                "1. Opiekowała / opiekował się harcówką przez okres próby: dokonała / dokonał w niej drobnych napraw lub zaproponowała / zaproponował nowe funkcjonalne i estetyczne rozmieszczenie wyposażenia.",
                "2. Konserwowała / konserwował sprzęt pionierski, sportowy lub obozowy.",
                "3. Skompletowała / skompletował sprzęt potrzebny na obozie drużyny lub szczepu.",
                "4. Wie, na czym polega inwentaryzacja, brała / brał udział w spisie z natury.",
                "5. Prowadziła / prowadził magazyn sprzętu na obozie drużyny lub w ciągu roku wraz z dokumentacją.",
            ],
            group="Kwatermistrzowskie",
        ),
        schemas.CreateBadge(
            name="KWATERMISTRZYNI / KWATERMISTRZ ***",
            description=[
                "1. Stosuje zasady logistyki w życiu codziennym − korzysta z tej wiedzy przy planowaniu prac drużyny.",
                "2. Uczestniczyła / uczestniczył w organizowaniu obozu drużyny pod względem kwatermistrzowskim, zadbała/zadbał o zaplecze dla obozu.",
                "3. Była odpowiedzialna / był odpowiedzialny za organizacyjną stronę biwaku lub rajdu szczepu.",
                "4. Przez okres co najmniej sześciu miesięcy pełniła / pełnił funkcję kwatermistrzyni/kwatermistrza drużyny lub szczepu.",
                "5. Nauczyła / nauczył młodszych konserwować sprzęt pionierski i porządkować magazyn sprzętu oraz posługiwać się narzędziami zgodnie z podstawowymi zasadami bezpieczeństwa.",
            ],
            group="Kwatermistrzowskie",
        ),
        schemas.CreateBadge(
            name="LOGISTYK (mistrzowska)",
            description=[
                "1. Odpowiadała / odpowiadał za logistyczne przygotowanie obozu, przeprowadzając zwiad i organizując zaplecze dla obozu, przygotowała / przygotował niezbędne dokumenty.",
                "2. Pełniła / pełnił funkcję kwatermistrzyni / kwatermistrza lub zaopatrzeniowca na obozie.",
                "3. Przygotowała / przygotował preliminarz i współuczestniczyła / współuczestniczył w rozliczeniu obozu.",
                "4. Podsumowała / podsumował roczną działalność drużyny / szczepu pod względem organizacyjnym: przeprowadziła / przeprowadził inwentaryzację, oceniła / ocenił ilościowo i jakościowo zaplecze sprzętowe, skontrolowała / skontrolował i uzupełniła / uzupełnił dokumentację. Wnioski i propozycje przedstawiła / przedstawił radzie drużyny /szczepu.",
                "5. Wyznaczyła / wyznaczył sobie dodatkowe zadania mistrzowskie.",
            ],
            group="Kwatermistrzowskie",
        ),
        #TERENOZNAWCZE, KRAJOZNAWCZE I TURYSTYCZNE
        schemas.CreateBadge(
            name="OBSERWATORKA / OBSERWATOR *",
            description=[
                "1. Wyznaczyła / wyznaczył strony świata za pomocą busoli, słońca, gwiazd i drzew.",
                "2. Poruszała / poruszał się bezszelestnie po pomieszczeniu zamkniętym i w terenie, czołgając się i maskując swoją obecność. Rozpoznała / rozpoznał w lesie ślady ludzi, zwierząt i pojazdów.",
                "3. Uczestniczyła/uczestniczył w biegu terenowym poruszając się według znaków patrolowych.",
                "4. Zapamiętała / zapamiętał przebytą drogę w terenie leśnym i w mieście, wróciła / wrócił nią samodzielnie bez błądzenia.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="TERENOZNAWCA **",
            description=[
                "1. Oceniła / ocenił prawidłowo odległość od wyznaczonego punktu, wykorzystując zasady określania odległości w terenie.",
                "2. Dokonała / dokonał pomiaru niedostępnych obiektów w terenie: wysokości drzewa, szerokości rzeki.",
                "3. Trafiła / trafił do wyznaczonego miejsca w nieznanym terenie na podstawie szkicu lub mapy.",
                "4. Poprowadziła / przeprowadził patrol w terenie, posługując się busolą i bezbłędnie docierając do miejsca oznaczonego na mapie.",
                "5. Wytypowała / wytypował w nowym terenie miejsce na biwak drużyny, rozplanowując jego rozbicie.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="TOPOGRAF ***",
            description=[
                "1. Wyznaczyła / wyznaczył strony świata według przedmiotów terenowych w nocy i w dzień oraz według słońca i zegarka.",
                "2. Trafiła / trafił według mapy do odległego o kilka kilometrów obiektu, wykonując w czasie marszu szkic drogi z zastosowaniem właściwej skali.",
                "3. Naniosła / naniósł na powiększony przez siebie wycinek mapy lub planu miasta uzyskane w czasie zwiadu terenowego informacje o znajdujących się tam ważnych obiektach.",
                "4. Uzyskała / uzyskał informacje o ważnych obiektach w nieznanym terenie, korzystając z Internetu i naniósł / naniosła je na przygotowywany dla potrzeb drużyny fragment planu miasta.",
                "5. Przeszkoliła / przeszkolił młodszych w zakresie znajomości znaków patrolowych i topograficznych.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="KARTOGRAF (mistrzowska)",
            description=[
                "1. Wykonała / wykonał z pamięci szkic sytuacyjny terenu.",
                "2. Dokonała / dokonał pomiaru terenu nadającego się na urządzenie obozu lub dziecięcego placu zabaw. Wykonała / wykonał dokładny plan.",
                "3. Wykreśliła / wykreślił mapę wybranego terenu (zaktualizowała / zaktualizował starą mapę) na potrzeby obozu, gry terenowej, rajdu itp.",
                "4. Przygotowała/przygotował trasę imprezy na orientację i biegu terenowego z przeszkodami.",
                "5. Przeprowadziła / przeprowadził w drużynie (szczepie) szkolenie z terenoznawstwa.",
                "6. Wyznaczyła / wyznaczył sobie dodatkowe zadania mistrzowskie.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="WSKAZIDROGA *",
            description=[
                "1. W czasie gry lub zwiadu terenowego poprowadziła / poprowadził zastęp do określonego miejsca odległego o 2−3 km, odszukała/odszukał wyznaczony obiekt.",
                "2. Na planie zaznaczyła / zaznaczył nazwy ulic i placów oraz ważne obiekty − ośrodek zdrowia, aptekę, pocztę, straż pożarną, posterunek policji itp.",
                "3. Poznała / poznał najbliższy obiekt godny zwiedzenia (zabytek, muzeum, osobliwość przyrodniczą itp.) i opowiedziała / opowiedział o nim na zbiórce zastępu.",
                "4. Wyszukała / wyszukał interesujące informacje o swojej miejscowości w przewodniku, encyklopedii, Internecie oraz przedstawiła/przedstawił je zastępowi.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="PRZEWODNICZKA / PRZEWODNIK PO... **",
            description=[
                "mieście, okolicy, miejscach pamięci narodowej, muzeach itp. Kanon wymagań sprawności:",
                "1. Poznała / poznał historię swojego regionu. W sposób szczególny interesuje się wybranym okresem lub miejscem.",
                "2. Opracowała / opracował trasę kilkugodzinnej wycieczki i wykonała / wykonał projekt folderu turystycznego o niej.",
                "3. Nawiązała / nawiązał niezbędne kontakty z gospodarzem terenu oraz obiektów i placówek ujętych w opracowaniu propozycji trasy wycieczkowej.",
                "4. Przeprowadziła / prowadził dla kolegów / koleżanek ze swojego środowiska lub przyjezdnych wycieczkę opracowaną przez siebie trasą.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="KRAJOZNAWCA ***",
            description=[
                "1. Oprowadziła / oprowadził trzy wycieczki po swoim mieście (okolicy), wykazując się znajomością jego historii, zabytków i ciekawych obiektów.",
                "2. Pokierowała / pokierował sporządzeniem informacji o walorach turystycznych okolicy na podstawie zajęć terenowych i literatury (geografia i historia okolicy, system połączeń komunikacyjnych, przemysł i rolnictwo, obiekty historyczne i przyrodnicze, sztuka, zwyczaje ludowe itp.).",
                "3. Zaplanowała/zaplanował cykl wycieczek do miejsc ciekawych pod względem historycznym, przyrodniczym lub geograficznym, posługując się mapami i przewodnikami.",
                "4. Zorganizowała / zorganizował dla młodszych zwiad etnograficzny lub konkursy, np. znajomości stylów architektonicznych, z zakresu historii ruchu krajoznawczego, historii sztuki regionu.",
                "5. Uczestniczyła / uczestniczył w trzech wycieczkach krajoznawczych w różnych regionach Polski.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="ŁAZIK *",
            description=[
                "1. Skompletowała/skompletował ekwipunek turystyczny.",
                "2. Uczestniczyła / uczestniczył w kilku wycieczkach, ubierając się stosownie do warunków terenowych i pogodowych, zabezpieczając się przed przegrzaniem,przemoczeniem oraz otarciem stóp.",
                "3. Poprawnie spakowała / spakował plecak, zabierając tylko rzeczy przydatne na wyprawie.",
                "4. Poznała / poznał zasady poruszania się po drogach.",
                "5. Uczestnicząc w wycieczkach i rajdach, zawsze zachowuje pogodę ducha, mimo trudów wędrowania.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="TRAMP **",
            description=[
                "1. Odbyła / odbył co najmniej pięć samodzielnych wypraw w promieniu kilku kilometrów od miejsca zamieszkania.",
                "2. Poznała / poznał zasady bezpiecznego marszu (tempo, odpoczynek, obciążenie, przepisy ruchu drogowego).",
                "3. Nocowała / nocował w lesie bez namiotu, a także w nieznanej miejscowości, korzystając np. ze schroniska PTSM.",
                "4. Zorganizowała / zorganizował biwak zastępu (drużyny), rozbijając go, a następ- nie likwidując bez pozostawienia śladów.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="WĘDROWIEC ***",
            description=[
                "1. Przedstawiła / przedstawił na zbiórce drużyny najpiękniejsze regiony turystyczne w Polsce.",
                "2. Zorganizowała / zorganizował dla drużyny wycieczki o różnej tematyce, m.in. krajoznawcze, przyrodnicze, historyczne.",
                "3. W czasie obozów wędrownych zainteresowała / zainteresował się historią poznawanych miejsc i żyjących tam ludzi.",
                "4. Zorganizowała / zorganizował rajd według opracowanego przez siebie programu i trasy.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="WŁÓCZĘGA NIZINNY **",
            description=[
                "1. Spędziła / spędził dziesięć dni na wycieczkach, przemierzając pieszo szlaki nizinne.",
                "2. Wskazała / wskazał na mapie trasy trzech ostatnich wędrówek przebytych z drużyną.",
                "3. Zapoznała / zapoznał się z publikacjami dotyczącymi atrakcji turystycznych swojego regionu (np. przewodniki, strony internetowe). Najciekawsze przedstawiła / przedstawił na zbiórce zastępu.",
                "4. Uczestniczyła / uczestniczył w dwóch kilkudniowych wycieczkach pieszych w terenie nizinnym.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="WYGA ***",
            description=[
                "1. Poprowadziła / przeprowadził dwie przynajmniej trzydniowe wędrówki grupy po zaplanowanym przez siebie szlaku, pod opieką pełnoletniego opiekuna.",
                "2. Zdobyła / zdobył srebrną Odznakę Turystyki Pieszej.",
                "3. W charakterze wyczynu odbyła/odbył w terenie nizinnym wielogodzinną, nieprzerwaną wędrówkę.",
                "4. Ukończyła / ukończył kurs pierwszej pomocy.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="WŁÓCZĘGA GÓRSKI **",
            description=[
                "1. Zdobyła / zdobył pięć szczytów wybranego pasma górskiego.",
                "2. Spędziła / spędził dziesięć dni na całodniowych wycieczkach górskich.",
                "3. Prawidłowo wypełniła / wypełnił książeczkę Górskiej Odznaki Turystycznej.",
                "4. Zapoznała / zapoznał się z publikacjami dotyczącymi atrakcji turystycznych swojego regionu (np. przewodniki, strony internetowe). Zachęciła / zachęcił harcer- ki / harcerzy z drużyny do zwiedzania proponowanych atrakcji.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="WYGA GÓRSKI ***",
            description=[
                "1. Zdobyła / zdobył trzy szczyty wybranych dwóch pasm górskich.",
                "2. Ukończyła/ukończył kurs pierwszej pomocy. Stosuje zasady racjonalnego uprawiania turystyki górskiej, umie obliczyć czas marszu, zna niebezpieczeństwa gór.",
                "3. Ma ekwipunek turystyczny niezbędny do wędrówki po górach i odpowiednio go konserwuje.",
                "4. Wykonała / wykonał kronikę kilkudniowej wędrówki w wybranym paśmie górskim, uzupełniła / uzupełnił ją o informacje z fachowej literatury i przedstawiła / przedstawił ją na forum drużyny.",
                "5. Była / był na dwóch obozach wędrownych w górach.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="WSPINACZ **",
            description=[
                "1. Zna terminologię wspinaczkową (nazwy sprzętu, komendy, slang wspinaczkowy).",
                "2. Poznała / poznał biografię wybitnego alpinisty i przedstawiła / przedstawił jego sylwetkę na zbiórce zastępu.",
                "3. Regularnie uczestniczy w zajęciach na ściance wspinaczkowej.",
                "4. Pod opieką instruktora pogłębia swoje umiejętności, pokonując coraz trudniejsze trasy.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="WSPINACZ DOSKONAŁY ***",
            description=[
                "1. Skompletowała/skompletował podstawowy sprzęt wspinaczkowy (uprząż, przyrząd asekuracyjny, karabinek, buty wspinaczkowe, karabinek, ewentualnie lina).",
                "2. Przeczytała / przeczytał wybraną pozycję dotyczącą wspinaczki skałkowej.",
                "3. Przeprowadziła / przeprowadził zbiórkę zastępu lub drużyny przybliżającą techniki wspinaczki oraz asekuracji.",
                "4. Systematycznie podnosi swoją sprawność fizyczną, uprawiając wybraną dyscyplinę sportu. Regularnie trenuje na ściance wspinaczkowej.",
                "5. Pod opieką doświadczonego instruktora wspinaczki pokonała / pokonał trasę skalną o trudności minimum VI.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="GEOLOG ***",
            description=[
                "1. Na podstawie swoich obserwacji i wiedzy zdobytej w podróżach i wycieczkach scharakteryzowała / scharakteryzował podstawowe typy krajobrazu Polski: wysokogórski, górski, wyżynny, nadmorski, pojezierza i nizinny.",
                "2. Odwiedziła / odwiedził teren wydmowy (nadmorski lub sandrowy), oglądając meandry rzeczne i pradolinę rzeki.",
                "3. Zwiedziła / zwiedził jaskinię. Wie, jakie procesy ją kształtowały. Potrafi nazwać podstawowe formy naciekowe.",
                "4. Rozróżniła / rozróżnił kilka rodzajów skał, prezentując kolegom swoje zbiory kamieni.",
                "5. Przygotowała / przygotował prezentację dla zastępu / drużyny na temat wybranego zagadnienia geologicznego.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="TURYSTKA ROWEROWA / TURYSTA ROWEROWY *",
            description=[
                "1. Zna zasady bezpiecznego poruszania się pojazdu jednośladowego po drodze.",
                "2. Potrafi rozróżnić części roweru, konserwować je i wykonać drobne naprawy.",
                "3. Wzięła / wziął udział w rajdach rowerowych, zdobywając co najmniej 30 punktów na Kolarską Odznakę Turystyczną.",
                "4. Poznała / poznał szlaki i ścieżki rowerowe w pobliżu miejsca swojego zamieszkania, opisała/opisał je w dzienniczku turysty rowerowego do własnego użytku.",
                "5. Przygotowała / przygotował rower i ekwipunek do wyprawy (światła, koła, apteczka, mapa).",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="KOLARZ **",
            description=[
                "1. Zdobyła / zdobył kartę rowerową lub motorowerową. Umie czytać mapę i posługiwać się busolą.",
                "2. Zdobyła / zdobył małą brązową Kolarską Odznakę Turystyczną.",
                "3. Zorganizowała/zorganizował dla zastępu/drużyny zbiórkę popularyzującą turystykę rowerową, przedstawiła / przedstawił na niej sprzęt rowerowy i pamiątki ze swoich wypraw.",
                "4. Opracowała / opracował plan i przeprowadziła / przeprowadził ciekawą wycieczkę z biwakowaniem, uwzględniając różnice wzniesień i nawierzchni oraz przygotowanie turystyczne uczestników wyprawy rowerowej.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="KOLARZ TURYSTA ***",
            description=[
                "1. Zdobyła / zdobył małą srebrną Kolarską Odznakę Turystyczną. Wzięła / wziął udział w rowerowym obozie wędrownym.",
                "2. Przedstawiła / przedstawił dziennik swoich wypraw lub inne materiały (fotografie, szkice, rysunki, itp.) dotyczące historii, osobliwości przyrodniczych oraz geologicznych zwiedzanych miejscowości.",
                "3. Zorganizowała / zorganizował rajd rowerowy dla drużyny.",
                "4. Poznała / poznał zasady konserwacji sprzętu rowerowego i propaguje tę wiedzę w swojej drużynie.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="NARCIARKA KLASYCZNA / NARCIARZ KLASYCZNY *",
            description=[
                "1. Poznała / poznał dwa kroki biegowe na nartach.",
                "2. Wykonała / wykonał zjazd pod bramkami z kijów, zmieniając kierunek jazdy przestępowaniem i hamując pługiem.",
                "3. Rozróżniła / rozróżnił trzy gatunki śniegu i umie przygotować narty do różnych warunków śniegowych.",
                "4. Potrafi wymienić olimpijskie dyscypliny narciarskie.",
                "5. Uczestniczyła / uczestniczył w wycieczkach narciarskich, przebywając jednorazowo co najmniej 5 km, a w sumie minimum 30 km.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="NARCIARKA BIEGOWA / NARCIARZ BIEGOWY **",
            description=[
                "1. Uczestniczyła / uczestniczył w co najmniej pięciu wycieczkach narciarskich, podczas których przebyła / przebył jednorazowo minimum 10 km.",
                "2. Opracowała / opracował trasę wycieczki narciarskiej na podstawie mapy topograficznej, zaplanowała/zaplanował ekwipunek indywidualny i zbiorowy na trasę.",
                "3. Potrafi udzielić pierwszej pomocy w wypadku narciarskim.",
                "4. Zna zasady bezpiecznego poruszania się na nartach w terenie.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="NARCIARKA TURYSTKA / NARCIARZ TURYSTA ***",
            description=[
                "1. Zjeżdżała / zjeżdżał w skos i na wprost stoku,zmieniając kierunek jazdy przestępowaniem.",
                "2. Zjeżdżała / zjeżdżał pługiem, wykonując łuki z pługu, cristianię do stoku i od stoku oraz „w tył zwrot” na stoku.",
                "3. Scharakteryzowała / scharakteryzował kombinację klasyczną i alpejską.",
                "4. Zaplanowała / zaplanował wycieczkę narciarską, biorąc pod uwagę możliwości uczestników. Podczas wycieczek przebyła/przebył w sumie 75 km.",
                "5. Ukończyła / ukończył kurs pierwszej pomocy, przestrzega zasad poruszania się w terenie górskim w czasie zimy. Zna rejony działania GOPR i TOPR oraz ich telefony alarmowe, wie, jak wezwać pomoc w inny sposób (Międzynarodowy Kod Górski, race, flary).",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="WIOŚLARKA / WIOŚLARZ *",
            description=[
                "1. Scharakteryzowała / scharakteryzował zasady bezpieczeństwa na wodzie i komendy żeglarskie oraz zasady pokonywania przeszkód wodnych.",
                "2. Wykonała / wykonał następujące czynności: przygotowanie kajaka, kanadyjki lub łodzi wiosłowej do rejsu, rozlokowanie niezbędnego ładunku, wodowanie, wsiadanie i wysiadanie.",
                "3. Wiosłowała / wiosłował na kajaku.",
                "4. Wiosłowała / wiosłował jednym i dwoma wiosłami w dulkach.",
                "5. Umie wiosłować „na śrubkę” i „na pych”.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="KAJAKARKA / KAJAKARZ **",
            description=[
                "1. Zdobyła / zdobył kartę pływacką.",
                "2. Płynęła / płynął 200 m kajakiem, utrzymując kurs.",
                "3. Uczestniczyła / uczestniczył w całodniowej wycieczce kajakowej, przygotowując wcześniej kajak i wyposażenie do wyprawy.",
                "4. Poznała / poznał przepisy bezpieczeństwa na wodzie, sposoby zachowania się w przypadku przewrócenia kajaka i udzielania pierwszej pomocy poszkodowanym (postępowanie z tonącym, pierwsza pomoc w przypadku udaru słonecznego i cieplnego, oparzenia, wychłodzenia organizmu).",
                "5. Konserwowała / konserwował kajak przed sezonem i po nim, wykonując przy tym drobne naprawy.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        schemas.CreateBadge(
            name="KAJAKARKA TURYSTKA / KAJAKARZ TURYSTA ***",
            description=[
                "1. Przebyła / przebył co najmniej trzy szlaki kajakowe, stosując się do śródlądowego prawa drogi.",
                "2. Zna kryteria oceny oraz umiejętnie ocenił stan wody, nurt, mieliznę i głębię. Do wniosków płynących z oceny sytuacji dostosował swoje zachowanie na wodzie.",
                "3. Zorganizowała / zorganizował wycieczkę wodną, przygotowując apteczkę, ekwipunek i wyposażenie kajaka lub łodzi, planując zaprowiantowanie stosownie do warunków zaopatrzenia na trasie.",
                "4. Potrafi zachować się w przypadku przewrócenia kajaka, w razie potrzeby udzielić pierwszej pomocy.",
                "5. Wiosłowała / wiosłował w kajaku, szalupie lub łodzi, na jedno i dwa wiosła, „na pych” i „na śrubę”.",
            ],
            group="Terenoznawcze, krajoznawcze i turystyczne",
        ),
        #ŁĄCZNOŚCIOWE
        schemas.CreateBadge(
            name="GONIEC *",
            description=[
                "1. Wskazała / wskazał drogę do urzędów i ważnych miejsc w swojej miejscowości.",
                "2. Dostarczyła / dostarczył list lub ustną wiadomość do adresata w wyznaczonym terminie.",
                "3. Nadała / nadał na poczcie: list polecony, przekaz pieniężny, paczkę.",
                "4. Bezbłędnie przekazała / przekazał meldunek w czasie gry terenowej, posługując się wybranymi sposobami łączności.",
                "5. Odebrała / odebrał i wysłała / wysłał wiadomość pocztą internetową.",
            ],
            group="Łącznościowe",
        ),
        schemas.CreateBadge(
            name="ŁĄCZNICZKA / ŁĄCZNIK **",
            description=[
                "1. Znalazła / znalazł w książce telefonicznej lub w Internecie adresy i numery telefonów dowolnych instytucji, dysponując tylko ich nazwą.",
                "2. Obsługując centralkę telefoniczną, utrzymała / utrzymał łączność w terenie.",
                "3. Wykonała / wykonał przyrząd do sygnalizacji w terenie, nadając i odbierając za jego pomocą depeszę napisaną alfabetem Morse’a.",
                "4. Opracowała / opracował szyfr dla zastępu (drużyny).",
            ],
            group="Łącznościowe",
        ),
        schemas.CreateBadge(
            name="ZWIADOWCA ***",
            description=[
                "1. W nieznanym terenie niedostrzeżenie podeszła / podszedł wskazany obiekt.",
                "2. Przeprowadziła / przeprowadził zwiad, sporządzając szczegółowy raport z opisem wykonanych zadań i zaobserwowanych zdarzeń.",
                "3. Nawiązała / nawiązał łączność za pomocą radia CB, przekazała / przekazał informacje zdobyte podczas zwiadu.",
                "4. Wie, jakie są zasady i sposoby przekazywania oraz gromadzenia poufnych informacji (np. danych osobowych), szczególnie w Internecie.",
                "5. Przeprowadziła / przeprowadził w zastępie (drużynie) szkolenie z łączności.",
            ],
            group="Łącznościowe",
        ),
        schemas.CreateBadge(
            name="SYGNALISTKA / SYGNALISTA *",
            description=[
                "1. Sprawnie nadała / nadał i odebrała / odebrał telegram alfabetem Morse’a za pomocą chorągiewek i latarki.",
                "2. Podała / podał treść informacji w zwięzłej formie.",
                "3. Poznała / poznał zasady szyfrowania i rozszyfrowywania, posługując się szyfrem w grach harcerskich.",
                "4. Pełniła / pełnił służbę łączności na wycieczce lub w grze polowej.",
                "5. Przeprowadziła/przeprowadził zajęcia z sygnalizacji dla zastępu lub drużyny.",
            ],
            group="Łącznościowe",
        ),
    ]

    for badge in badges:
        crud.create_badge(db, badge=badge)


def init_groups(db: Session) -> None:
    groups = [
        schemas.CreateGroup(
            name="Forward", number=7, szczep="Zielona Siódemka", city="Bydgoszcz"
        )
    ]

    for group in groups:
        crud.create_group(db, group=group)


def init_users(db: Session) -> None:
    users = [
        schemas.CreateUser(
            first_name="admin",
            last_name="admin",
            email="admin@harcownik.com",
            is_webadmin=True,
            level="admin",
            function="admin",
            password="zaq12wsx",
        )
    ]

    for user in users:
        crud.create_user(db, user=user)
