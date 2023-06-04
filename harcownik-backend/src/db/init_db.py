from sqlalchemy.orm import Session
from src import crud, schemas


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
        # Kucharskie
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
        # FINANSOWO-EKONOMICZNE
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
        # KWATERMISTRZOWSKIE
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
        # TERENOZNAWCZE, KRAJOZNAWCZE I TURYSTYCZNE
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
        # ŁĄCZNOŚCIOWE
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
        # JĘZYKOWE
        schemas.CreateBadge(
            name="JĘZYKOZNAWCA *",
            description=[
                "1. Wyraża się poprawnie, nauczyła / nauczył się umiejętnie korzystać ze słowników języka polskiego i poprawnej polszczyzny.",
                "2. Nauczyła / nauczył się podstawowych zwrotów grzecznościowych w językach: angielskim, francuskim, niemieckim, rosyjskim.",
                "3. W wybranym przez siebie języku obcym nauczyła / nauczył się podstawowego słownictwa związanego z harcerstwem (co najmniej 20 słówek).",
                "4. Uczy się systematycznie wybranego języka obcego.",
            ],
            group="Językowe",
        ),
        schemas.CreateBadge(
            name="TŁUMACZKA / TŁUMACZ **",
            description=[
                "1. Pogłębiła / pogłębił w czasie próby znajomość języka obcego.",
                "2. Przetłumaczyła / przetłumaczył na język polski kilka gier skautowych.",
                "3. Napisała / napisał słowniczek o tematyce harcerskiej, zawierający ok. 100 słówek w języku, którego się uczy.",
                "4. Uczestnicząc w spotkaniu skautowym, pomagała / pomagał innym porozumieć się w języku, którego się uczy.",
            ],
            group="Językowe",
        ),
        schemas.CreateBadge(
            name="POLIGLOTKA / POLIGLOTA ***",
            description=[
                "1. Potrafi porozumieć się w podstawowych sprawach w co najmniej dwóch językach obcych i tłumaczyć rozmowę z wybranego języka.",
                "2. Przetłumaczyła / przetłumaczył artykuły o tematyce skautowej, upowszechniając ich treść w swoim środowisku.",
                "3. Zaoferowała / zaoferował swoją służbę jako tłumacz podczas spotkania skautowego organizowanego przez szczep, hufiec lub chorągiew.",
                "4. Nauczyła / nauczył młodszych kilku zwrotów obcojęzycznych.",
            ],
            group="Językowe",
        ),
        # NAUKOWE
        schemas.CreateBadge(
            name="SZPERACZ *",
            description=[
                "1. Przygotowując żądaną informację, umiejętnie posłużyła / posłużył się przewodnikiem, encyklopedią, Internetem.",
                "2. Zlokalizowała / zlokalizował wybrany obiekt w nieznanym terenie, wykorzystując dostępne źródła informacji.",
                "3. Przeprowadziła / przeprowadził wywiad dotyczący ciekawostek wybranej miejscowości i zaprezentowała / zaprezentował go na zbiórce zastępu.",
                "4. W czasie obozu, biwaku lub rajdu zebrała/zebrał ciekawostki na temat odwiedzanych miejsc i ludzi, prezentując je potem kolegom.",
            ],
            group="Naukowe",
        ),
        schemas.CreateBadge(
            name="POSZUKIWACZ **",
            description=[
                "1. Wybrała / wybrał dziedzinę swoich zainteresowań i stale pogłębia swą wiedzę, odwiedzając miejsca związane z tym tematem.",
                "2. Zorganizowała / zorganizował wycieczkę zastępu (drużyny) do miejsc, w których znajdują się eksponaty z dziedziny jej/jego zainteresowań.",
                "3. Przeprowadziła / przeprowadził zwiad społeczny w czasie obozu lub biwaku,zdobywając wiedzę na temat historii i ważnych spraw mieszkańców regionu.",
                "4. Wykazała / wykazał się znajomością krain geograficznych i okresów dziejowych Polski.",
            ],
            group="Naukowe",
        ),
        schemas.CreateBadge(
            name="BADACZKA / BADACZ ***",
            description=[
                "1. Wykazała / wykazał się zainteresowaniami w wybranej dziedzinie (doświadczenia fizyczne, chemiczne, biologiczne, badania etnograficzne, archeologiczne, historyczne, religioznawcze, geologiczne itp.).",
                "2. Interesująco przedstawiła / przedstawił dziedzinę swoich zainteresowań.",
                "3. Spopularyzowała / spopularyzował w drużynie (w szkole) wybrane odkrycie naukowe lub wydarzenie historyczne (społeczne), wyjątkowo ważne dla dziejów ludzkości.",
                "4. Zorganizowała/zorganizował młodzieżową debatę naukową na wybrany przez siebie temat.",
            ],
            group="Naukowe",
        ),
        # SPORTOWE
        schemas.CreateBadge(
            name="SPORTOWIEC *",
            description=[
                "1. Interesuje się wybraną dyscypliną sportu i popularyzuje ją, wymieniła / wymienił nazwiska swoich ulubionych sportowców.",
                "2. Codziennie wykonuje poranną gimnastykę.",
                "3. Zademonstrowała / zademonstrował swój zestaw ćwiczeń treningowych.",
                "4. Zorganizowała / zorganizował spotkanie z zawodnikiem lub trenerem wybranej dyscypliny albo zaprezentowała / zaprezentował film o życiu sportowców.",
            ],
            group="Sportowe",
        ),
        schemas.CreateBadge(
            name="[NAZWA DYSCYPLINY] np. PIŁKARZ, NARCIARZ **",
            description=[
                "1. Uprawia wybraną dyscyplinę sportu.",
                "2. Zademonstrowała / zademonstrował swoje umiejętności w tej dyscyplinie.",
                "3. Zorganizowała / zorganizował dla harcerzy zajęcia zapoznające z uprawianą dyscypliną sportu (pokazy, zawody, naukę zasad i techniki itd.).",
                "4. Uczestniczyła / uczestniczył kilkakrotnie w zawodach sportowych, zawsze przestrzegając zasady fair play.",
                "5. Stara się systematycznie poprawiać swoje wyniki.",
            ],
            group="Sportowe",
        ),
        schemas.CreateBadge(
            name="OLIMPIJCZYK ***",
            description=[
                "1. Uprawia wybraną dyscyplinę sportu pod fachowym kierunkiem.",
                "2. Uczestniczyła / uczestniczył w olimpiadzie sportowej (np. szkolnej, obozowej,międzyszkolnej), poprawiając swoje wyniki.",
                "3. Spopularyzowała / spopularyzował ideę olimpijską w swoim środowisku: w szkole, w drużynie (szczepie).",
                "4. Reprezentowała / reprezentował szkołę na zawodach sportowych, starając się przyczynić do sukcesów swojej drużyny.",
            ],
            group="Sportowe",
        ),
        schemas.CreateBadge(
            name="GIMNASTYCZKA / GIMNASTYK *",
            description=[
                "1. Opracowała / opracował własne zestawy ćwiczeń w domu i na powietrzu.",
                "2. Poznała / poznał sławne gimnastyczki i gimnastyków i ich kariery sportowe.",
                "3. Prowadziła / prowadził gimnastykę zastępu, drużyny, grupy dzieci.",
                "4. Brała / brał udział w zawodach sportowych w drużynie, starając się osiągać najlepsze wyniki.",
            ],
            group="Sportowe",
        ),
        schemas.CreateBadge(
            name="MISTRZYNI GIMNASTYKI / MISTRZ GIMNASTYKI **",
            description=[
                "1. Nauczyła / nauczył się poprawnie wykonywać ćwiczenia z wybranego rodzaju gimnastyki.",
                "2. Zrozumiała / zrozumiał rolę ćwiczeń gimnastycznych dla organizmu.",
                "3. Uczestniczy regularnie w zajęciach wybranej gimnastyki prowadzonych przez fachowca.",
                "4. Dobrała / dobrał muzykę do uprawianych przez siebie codziennie ćwiczeń.",
                "5. Przeprowadziła / przeprowadził gimnastykę zastępu lub drużyny na obozie lub biwaku, zwracając uwagę na dokładność wykonywania ćwiczeń.",
            ],
            group="Sportowe",
        ),
        schemas.CreateBadge(
            name="MŁODA PŁYWACZKA / MŁODY PŁYWAK *",
            description=[
                "1. Przepłynęła / przepłynął 100 m, w tym połowę na plecach.",
                "2. Wytrzymała / wytrzymał pod wodą 20 sekund.",
                "3. Nauczyła / nauczył się prawidłowo zakładać kamizelkę ratunkową.",
                "4. Poznała / poznał zasady bezpieczeństwa i higieny kąpieli.",
            ],
            group="Sportowe",
        ),
        schemas.CreateBadge(
            name="PŁYWACZKA / PŁYWAK **",
            description=[
                "1. Przepłynęła / przepłynął 200 m, w tym połowę na plecach.",
                "2. Skoczyła / skoczył do wody z wysokości co najmniej 1 m i przepłynęła / przepłynął pod lustrem wody 10 m.",
                "3. Wyciągnęła / wyciągnął przedmiot znajdujący się 1,5 m pod wodą.",
                "4. Nauczyła / nauczył młodszych zakładania kamizelki ratunkowej i podawania koła ratunkowego.",
                "5. Poznała / poznał zasady bezpieczeństwa kąpieli oraz ratowania tonącego.",
            ],
            group="Sportowe",
        ),
        schemas.CreateBadge(
            name="PŁYWACZKA DOSKONAŁA / PŁYWAK DOSKONAŁY ***",
            description=[
                "1. Przepłynęła / przepłynął 400 m (dziewczęta) i 600 m (chłopcy) w wodzie stojącej lub 800 m (dziewczęta) i 1000 m (chłopcy) z prądem co najmniej dwoma stylami.",
                "2. Przepłynęła / przepłynął pod wodą 15 metrów.",
                "3. Uczestniczyła / uczestniczył w wyznaczaniu kąpieliska zgodnie z przepisami.",
                "4. Zademonstrowała / zademonstrował w wodzie sposób ratowania tonącego.",
            ],
            group="Sportowe",
        ),
        # ARTYSTYCZNE
        schemas.CreateBadge(
            name="ŚPIEWACZKA / ŚPIEWAK *",
            description=[
                "1. Rozpoczęła / rozpoczął śpiew kilku piosenek na zbiórce zastępu.",
                "2. Nauczyła / nauczył zastęp jednej piosenki.",
                "3. Zaśpiewała / zaśpiewał z pamięci dziesięć piosenek (np. harcerskich lub żołnierskich).",
                "4. Występowała / występował z zastępem, śpiewając kilka piosenek oraz brała / brał udział w inscenizacji piosenki.",
                "5. Prowadzi na bieżąco swój śpiewnik harcerski, ma w nim zapisanych co najmniej 20 piosenek.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="PIEŚNIARKA / PIEŚNIARZ **",
            description=[
                "1. Przedstawiła / przedstawił prowadzony przez siebie śpiewnik lub swoją płytotekę.",
                "2. Śpiewała / śpiewał na uroczystościach harcerskich, szkolnych lub kościelnych.",
                "3. Nauczyła / nauczył zastęp lub drużynę kilku tradycyjnych i współczesnych piosenek harcerskich oraz turystycznych.",
                "4. Wymieniła / wymienił swoich ulubionych piosenkarzy, śpiewaków i zespoły, uzasadniając wybór w sposób przekonujący.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="WODZIREJKA / WODZIREJ ***",
            description=[
                "1. Przygotowała / przygotował program i przeprowadził pięć ognisk harcerskich dla szczepu lub kilku drużyn, w tym co najmniej dwa ogniska tematyczne.",
                "2. Zorganizowała / zorganizował bal harcerski, tematyczną zabawę taneczną lub dyskotekę, zapewniając w przerwach konkursy, zabawy i pląsy.",
                "3. Przedstawiła / przedstawił prowadzony przez siebie notatnik, w którym zapisuje pomysły pląsów, zabaw i okrzyków.",
                "4. Przygotowała / przygotował młodszych do próby na sprawności „tancerza”, „muzyka” lub „piosenkarza”.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="GRAJEK **",
            description=[
                "1. Nauczyła / nauczył się grać przynajmniej na jednym instrumencie, zagrała / zagał na nim melodię.",
                "2. Brała / brał udział w przygotowaniu uroczystości harcerskiej, organizując orkiestrę.",
                "3. Nauczyła / nauczył zastęp lub drużynę piosenki na podstawie zapisu nutowego.",
                "4. Zorganizowała / zorganizował w drużynie naukę piosenek, akompaniując na instrumencie.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="MUZYCZKA / MUZYK ***",
            description=[
                "1. Zagrała / zagrał kilka melodii na wybranym instrumencie.",
                "2. Scharakteryzowała / scharakteryzował okresy w dziejach polskiej muzyki, wymieniając najsłynniejszych kompozytorów i ich utwory.",
                "3. Zorganizowała / zorganizował wyjście drużyny na koncert do filharmonii lub opery.",
                "4. Akompaniowała / akompaniował na ognisku, dobierając wcześniej związany z tematem zestaw piosenek.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="ARTYSTKA / ARTYSTA (mistrzowska)",
            description=[
                "1. Doskonale orientuje się w życiu artystycznym i kulturalnym swojego regionu i Polski.",
                "2. Animuje działalność artystyczną w swoim środowisku harcerskim.",
                "3. Brała / brał udział w warsztatach specjalistycznych, doskonalących umiejętności w wybranej przez siebie dziedzinie artystycznej.",
                "4. Odniosła / odniósł sukces na festiwalu, przeglądzie, konkursie, wystawie itp.",
                "5. Wyznaczyła / wyznaczył sobie dodatkowe zadania mistrzowskie.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="PLASTYCZKA / PLASTYK *",
            description=[
                "1. Nauczyła / nauczył się wykonywać różnymi technikami rysunki, plakaty i obrazy, loga, napisy (co najmniej pięć rodzajów)",
                "2. Wykonała / wykonał ilustrację do kroniki i plakat reklamowy.",
                "3. Rozpoznała / rozpoznał wskazane dzieła rzeźby i malarstwa polskiego.",
                "4. Wykonała / wykonał ozdobę do harcówki lub totem obozowy.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="DEKORATORKA / DEKORATOR **",
            description=[
                "1. Nauczyła / nauczył się wykonywać różnymi technikami rysunki, plakaty i obrazy, loga, napisy (co najmniej dziesięć rodzajów technik plastycznych).",
                "2. Rozpoznała / rozpoznał różne style w malarstwie.",
                "3. Przygotowała / przygotował dekorację wybranej sali według projektu.",
                "4. Wymieniła/wymienił filmy, które mają najciekawszą jej/jego zdaniem scenografię.",
                "5. Przedstawiła / przedstawił zaprojektowane przez siebie urządzenie pokoju, harcówki, namiotu, świetlicy obozowej",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="SCENOGRAFKA / SCENOGRAF ***",
            description=[
                "1. Poznała / poznał zasady projektowania kostiumów i dekoracji.",
                "2. Opracowała / opracował scenografię do przedstawienia w sali i w plenerze, opra- cowała/opracował rzuty do scenografii.",
                "3. Zorganizowała / zorganizował wykonanie oraz pokierowała / pokierował zespoła- mi wykonującymi dekorację wystawy lub innej imprezy kulturalnej.",
                "4. Wykonała / wykonał detal scenograficzny, wykorzystując różne materiały.",
                "5. Przygotowała / przygotował młodszych do zdobycia sprawności „plastyka” lub „dekoratora”.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="RECYTATORKA / RECYTATOR *",
            description=[
                "1. Uczestniczyła / uczestniczył w pracach koła żywego słowa lub konkursie recytatorskim.",
                "2. Zaprezentowała / zaprezentował utwory swoich ulubionych autorów na zbiórce zastępu.",
                "3. Umiejętnie zinterpretowała / zinterpretował nieznany sobie utwór poetycki lub prozatorski, dobierając barwę głosu, modulację, tempo i rytm.",
                "4. Uczestniczyła / uczestniczył w przygotowaniu wieczoru poezji, prezentując na nim swoje ulubione utwory.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="AKTORKA / AKTOR **",
            description=[
                "1. Opowiedziała / opowiedział na zbiórce o swoich ulubionych aktorach i ich największych rolach.",
                "2. Przygotowała / przygotował kostium i rekwizyty, charakteryzując się do wybranej roli i zagrała/zagrał ją w trakcie przedstawienia w szkole lub drużynie.",
                "3. Uczęszcza na kółko teatralne lub wzięła / wziął udział w przedstawieniu przygotowanym przez drużynę.",
                "4. Zaprezentowała / zaprezentował się w różnych formach na scenie, np. monolog,dialog, pantomima.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="REŻYSER ***",
            description=[
                "1. Skompletowała / skompletował literaturę, materiały repertuarowe i recenzje na temat widowisk scenicznych.",
                "2. Opracowała / opracował reżyserię wybranej przez siebie sztuki lub programu, planując wykorzystanie sceny, zagospodarowanie planu, ruch sceniczny, miejsce muzyki i tańca w przedstawieniu i oczekiwania wobec scenografa oraz ustalając próby.",
                "3. Przygotowała / przygotował do wystawienia sztukę lalkową, program kabaretowy lub montaż literacki.",
                "4. Zna nazwiska słynnych reżyserów polskich i światowych. Zaprezentowała / zaprezentował sylwetkę jednego z nich na zbiórce zastępu lub drużyny.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="LALKARKA / LALKARZ **",
            description=[
                "1. Wykonała / wykonał różne lalki, np. pacynki, marionetki, kukiełki.",
                "2. Urządziła / urządził scenę i dekoracje dla teatru lalek.",
                "3. Zorganizowała / zorganizował z zastępem przedstawienie kukiełkowe.",
                "4. Zagrała / zagrał rolę w teatrzyku kukiełkowym, poruszając lalką, lub w teatrzyku cieni.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="GAWĘDZIARKA / GAWĘDZIARZ **",
            description=[
                "1. Poznała / poznał legendy, opowieści ludowe i wykorzystała / wykorzystał je w swoich gawędach.",
                "2. Opowiedziała / opowiedział jedną z przeczytanych w czasie próby książek, zainteresowując słuchaczy losami bohaterów.",
                "3. Opowiadając na ogniskach i kominkach, każdą historię wzbogaciła / wzbogacił o morał, przysłowie.",
                "4. Opowiedziała / opowiedział „na zamówienie” trzy gawędy: jedną na wskazany temat, drugą na podstawie zaobserwowanego wydarzenia i trzecią dostosowaną do sytuacji, w której się aktualnie znalazła / znalazł.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="TANCERKA / TANCERZ *",
            description=[
                "1. Poprowadziła / przeprowadził kilka pląsów i zabaw z muzyką na zbiórce zastępu.",
                "2. Zatańczyła / zatańczył publicznie wybrany taniec narodowy, ludowy, towarzyski,dyskotekowy.",
                "3. Nauczyła / nauczył tańczyć wybrany taniec koleżanki lub kolegów w zastępie / drużynie.",
                "4. Zaimprowizowała / zaimprowizował ruchy taneczne do melodii.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="MISTRZYNI TAŃCA / MISTRZ TAŃCA **",
            description=[
                "1. Rozróżniła / rozróżnił melodię i kroki dziesięciu tańców.",
                "2. Uczestniczyła / uczestniczył w zajęciach klubu lub zespołu tanecznego.",
                "3. Wzięła / wziął udział w konkursie tanecznym, starając się uzyskać najlepszą ocenę.",
                "4. Przeprowadziła / przeprowadził kurs tańca w drużynie lub klasie.",
                "5. Zna nazwiska słynnych tancerek i tancerzy. Przedstawiła / przeprowadził sylwetkę jednego z nich na zbiórce zastępu.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="FOTOAMATORKA / FOTOAMATOR *",
            description=[
                "1. Poznała / poznał budowę aparatu fotograficznego, rodzaje aparatów fotograficznych oraz zasady wykonywania zdjęć.",
                "2. Wykonała / wykonał zdjęcie tematyczne, odpowiednio ustawiając aparat.",
                "3. Na biwaku lub obozie robiła / robił zdjęcia drużynie, a następnie wybierała / wybrał najlepsze na wystawę.",
                "4. Przygotowała / przygotował na konkurs lub wystawę w szkole lub w szczepie własny serwis zdjęciowy.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="FOTOGRAF **",
            description=[
                "1. Przedstawiła / przedstawił album zdjęć przez siebie wykonanych.",
                "2. Fotografując, stosowała/stosował prawidłowe ustawienie aparatu i oświetlenia.",
                "3. Wykonała / wykonał portret osoby lub zjawiska przyrody.",
                "4. Zorganizowała / zorganizował wystawę fotograficzną w drużynie (szkole, szczepie), prezentując na niej również swoje prace.",
            ],
            group="Artystyczne",
        ),
        schemas.CreateBadge(
            name="MISTRZYNI OBIEKTYWU / MISTRZ OBIEKTYWU ***",
            description=[
                "1. Poznała / poznał zasady działania kamery, wykonując na niej film, dokumentujący wydarzenie w drużynie, szkole lub rodzinie.",
                "2. Rozróżniła / rozróżnił zaprezentowane gatunki filmowe, potrafi zareklamować film stosownie do oczekiwań odbiorcy.",
                "3. Nakręciła/nakręcił film (telefonem komórkowym, kamerą cyfrową) według własnego scenariusza i przygotowała / przygotował go samodzielnie do prezentacji.",
                "4. Zorganizowała/zorganizował w drużynie lub szczepie wieczór filmowy, prezentujący filmy nakręcone w trakcie różnych przedsięwzięć harcerskich lub szkolnych. Zachęciła/zachęcił innych do dokumentowania wydarzeń za pomocą filmów.",
            ],
            group="Artystyczne",
        ),
        # Społeczne i obywatelskie
        schemas.CreateBadge(
            name="MŁODA OBYWATELKA / MŁODY OBYWATEL *",
            description=[
                "1. Poznała / poznał historię godła i barw narodowych. Wie, co oznaczają i potrafi się wobec nich zachować.",
                "2. Potrafi zaśpiewać hymn państwowy.",
                "3. Odszukała / odszukał na mapie Polski miejsca, które dotąd odwiedziła / odwie- dził lub chciałaby / chciałby odwiedzić.",
                "4. Zapoznała / zapoznał się z częścią statutu szkoły, zawierającą prawa i obowiązki ucznia. Angażuje się w życie swojej klasy.",
                "5. Poznała/poznał daty polskich świąt narodowych. Wie, na pamiątkę jakich wydarzeń zostały ustanowione. Przygotowała/przygotował z zastępem zbiórkę z okazji jednego z nich.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="OBYWATELKA / OBYWATEL **",
            description=[
                "1. Współpracuje z samorządem szkolnym. Przygotowała / przygotował kampanię promującą prawa i obowiązki uczniowskie.",
                "2. Angażuje się w życie szkoły.",
                "3. Poznała / poznał najważniejsze fakty z historii najnowszej Polski.",
                "4. Dowiedziała / dowiedział się, gdzie znajdują się najważniejsze urzędy w jej / jego miejscowości i gminie. Przygotowała/przygotował mapę miasta przedstawiającą ich lokalizację oraz główne sprawy, jakimi się zajmują.",
                "5. Zorganizowała / zorganizował dla drużyny wycieczkę do urzędu gminy lub miasta.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="OBYWATELKA / OBYWATEL RZECZYPOSPOLITEJ ***",
            description=[
                "1. Zapoznała / zapoznał się z najważniejszymi prawami i obowiązkami obywateli Rzeczypospolitej Polskiej.",
                "2. Wie, na czym polega demokracja. Brała / brał udział w demokratycznym podejmowaniu decyzji.",
                "3. Zgromadziła / zgromadził własną biblioteczkę książek o historii najnowszej Polski. W drużynie, zastępie, klasie przygotowała / przygotował i przeprowadziła / przeprowadził grę o historii najnowszej kraju.",
                "4. Orientuje się w bieżących wydarzeniach politycznych, gospodarczych i kulturalnych kraju. Zapoznała / zapoznał się z podziałem polskiej sceny politycznej. Dowiedziała / dowiedział się, kto sprawuje najważniejsze funkcje państwowe.",
                "5. Angażuje się w pracę parlamentu młodzieży lub jednej z młodzieżowych organizacji. W swojej działalności godnie reprezentuje ZHP.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="ZNAWCA WŁASNEJ MIEJSCOWOŚCI **",
            description=[
                "1. Na podstawie wywiadów z mieszkańcami ustaliła / ustalił najważniejsze wydarzenia w swojej miejscowości w XX wieku.",
                "2. Dowiedziała / dowiedział się, czy istnieje w jej / jego miejscowości lista honorowych mieszkańców. Wie, kto jest na tej liście i dlaczego.",
                "3. Przedstawiła / przedstawił historię swojej miejscowości w formie pisanej (artykuł w gazecie) lub ustnej (gawęda na zbiórce).",
                "4. Zorganizowała / zorganizował wraz z zastępem grę miejską dla drużyny.",
                "5. Dowiedziała / dowiedział się, jak przedstawia się aktualna sytuacja mieszkańców (gdzie pracują, jak spędzają czas wolny, co robią najmłodsi mieszkańcy itd.).",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="PRZEWODNICZKA PO REGIONIE / PRZEWODNIK PO REGIONIE **",
            description=[
                "1. Wzięła / wziął udział w zwiadzie etnograficznym zastępu w wybranej okolicy. Zwróciła / zwrócił uwagę na styl budownictwa, elementy sztuki ludowej, język mieszkańców.",
                "2. Zaprezentowała / zaprezentował drużynie swoje spostrzeżenia, zdjęcia, szkice oraz co najmniej jeden przedmiot będący wyrobem rzemiosła ludowego z wybranej okolicy.",
                "3. Skompletowała / skompletował biblioteczkę zawierającą pozycje opisujące interesujący ją / jego region.",
                "4. Poznała / poznał co najmniej jeden taniec, piosenkę lub przyśpiewkę ludową z wybranego regionu.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="ZNAWCA REGIONU ***",
            description=[
                "1. Zwiedziła / zwiedził z zastępem muzeum regionalne lub skansen.",
                "2. Wskazała / wskazał atuty kulturowe regionu i zagrożenia dla jego rozwoju.",
                "3. Poznała / poznał główne problemy ochrony środowiska swojego regionu. Zainicjowała / zainicjował w drużynie działania zmierzające do ich rozwiązania.",
                "4. Odwiedza strony internetowe własnego województwa. Śledzi na bieżąco ukazujące się tam informacje.",
                "5. Nawiązała / nawiązał kontakt z redakcją lokalnego radia lub gazety, pomogła / pomógł w przygotowaniu cyklu artykułów o ciekawostkach regionu lub zamieściła/zamieścił artykuł o regionie na portalu dziennikarstwa obywatelskiego.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="ETNOGRAFKA / ETNOGRAF ***",
            description=[
                "1. Poznała/poznał gwarę regionu, w którym mieszka, lub język mniejszości zamieszkującej na tym terenie i inne charakterystyczne elementy kultury regionu.",
                "2. Przedstawiła / przedstawił swoje zbiory opowieści i pieśni ludowych oraz publikacji o działalności twórców ludowych, zespołów folklorystycznych.",
                "3. Na wycieczce drużyny pełniła / pełnił rolę przewodnika po obiektach kultury ludowej.",
                "4. Zaznaczyła/zaznaczył na mapie Polski regiony etnograficzne oraz scharakteryzowała/scharakteryzował je.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="MŁODA EUROPEJKA / MŁODY EUROPEJCZYK *",
            description=[
                "1. Dowiedziała / dowiedział się, kim był Robert Schuman i czym jest Unia Europejska.",
                "2. Przygotowała / przygotował do harcówki mapę Polski z zaznaczonymi sąsiadami naszego kraju.",
                "3. Przygotowała / przygotował dla zastępu / drużyny / szkoły konkurs na najlepszy plakat o Europie.",
                "4. Zna symbole jednoczącej się Europy. Wykonała / wykonał flagę europejską do harcówki.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="EUROPEJKA / EUROPEJCZYK **",
            description=[
                "1. Dowiedziała / dowiedział się, czym była Deklaracja Schumana i jakie miała znaczenie w pokojowym jednoczeniu kontynentu.",
                "2. Umie wymienić kraje należące do Unii Europejskiej.",
                "3. Przygotowała / przygotował dla drużyny kwiz o Europie, którego pytania dotyczyły krajów, stolic, głównych rzek i najbardziej znanych zabytków.",
                "4. Poznała / poznał hymn Unii Europejskiej. Na zbiórce nauczyła / nauczył innych go śpiewać.",
                "5. Poznała / poznał główne instytucje zjednoczonej Europy.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="OBYWATELKA EUROPY / OBYWATEL EUROPY ***",
            description=[
                "1. Poznała / poznał główne etapy tworzenia się Unii Europejskiej. Potrafiła / potrafił wymienić założycieli zjednoczonej Europy. Dowiedziała / dowiedział się, jaki mieli wkład w integrowanie Europy.",
                "2. Poznała / poznał instytucje europejskie oraz ich kompetencje. Przygotowała / przygotował do harcówki planszę przedstawiającą te instytucje.",
                "3. Dowiedziała / dowiedzał się, czym jest obywatelstwo europejskiej i jakie płyną z niego korzyści.",
                "4. Rozumie proces integracji Polski z instytucjami europejskimi.",
                "5. Przygotowała / przygotował dla drużyny debatę nad przyszłością Europy.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="ZNAWCA EUROPY (mistrzowska)",
            description=[
                "1. Poznała / poznał wkład polskich myślicieli w proces jednoczenia Europy.",
                "2. Poznała / poznał historię integracji europejskiej. Rozumie różne podejścia do przyszłości Europy.",
                "3. Dowiedziała / dowiedział się, jaka jest procedura podejmowania decyzji w Unii Europejskiej oraz jaka jest waga polskiego głosu.",
                "4. Przygotowała / przygotował warsztaty na temat integracji europejskiej lub zagadnienia szczegółowego dla wybranej grupy.",
                "5. Dowiedziała / dowiedział się, jakie instytucje oraz organizacje w Polsce zajmują się tematyką integracji europejskiej. Zgłosiła / zgłosił się do współpracy z Regionalnym Centrum Integracji Europejskiej lub inną instytucją.",
                "6. Poznała / poznał sposoby pozyskiwania funduszy europejskich, np. program „Młodzież”, programy dla studentów.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="ZNAWCA PRAW CZŁOWIEKA **",
            description=[
                "1. Wie, czym są prawa i wolności człowieka. Rozumie pojęcie godności.",
                "2. Wie, jakie dokumenty międzynarodowe ustanawiają podstawowe prawa i wolności człowieka. Przygotowała / przygotował do harcówki / klasy plakat z katalogiem podstawowych praw i wolności człowieka.",
                "3. Wie, jakie organizacje pozarządowe w Polsce podejmują tematykę praw człowieka.",
                "4. Wie, w których krajach prawa człowieka nadal są łamane. Przygotowała / przygotował wraz z drużyną akcję propagującą prawa człowieka. W tym celu nawiązała / nawiązał współpracę z organizacją zajmującą się tą problematyką.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="OBROŃCA PRAW CZŁOWIEKA ***",
            description=[
                "1. Wie, skąd pochodzi idea praw człowieka oraz jakie wydarzenia miały największy wpływ na ich rozwój. Rozumie, czym są kolejne generacje praw człowieka.",
                "2. Zna najważniejsze dokumenty międzynarodowe dotyczące praw człowieka. Wie, które organizacje międzynarodowe odpowiadają za przestrzeganie praw człowieka.",
                ".3. Wybrała / wybrał jedną dziedzinę praw człowieka, którą poznała /poznał szczególnie dokładnie (np. prawa kobiet, prawa dzieci, prawa uchodźców).",
                "4. Przygotowała/przygotował zbiórkę drużyny na temat wybranej grupy i jej praw oraz akcję (w szczepie, hufcu, szkole) na rzecz ochrony tej grupy. W tym celu nawiązała/nawiązał współpracę z Amnesty International lub inną organizacją.",
                "5. Wie, w jakich krajach prawa człowieka są nadal łamane. Przygotowała / przygo/tował w dowolnej formie prezentację na ten temat, przedstawiła / przedstawił ją na zbiórce drużyny.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="MŁODY WYBORCA ***",
            description=[
                "1. Wyraziła / wyraził i uzasadniła / uzasadnił swoje zdanie na temat udziału harcerzy i harcerek w samorządzie szkolnym.",
                "2. Określiła / określił, w jaki sposób jej / jego zastęp i zastępowa / zastępowy uczestniczą w samorządnym realizowaniu zadań w drużynie.",
                "3. Wzięła / wziął udział w tworzeniu programu wyborczego do samorządu szkolnego.",
                "4. Zapoznała / zapoznał się z podstawowymi zasadami wyborczymi w Polsce. Wie, jakie wybory odbywają się w naszym kraju i co to jest referendum.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="WYBORCA (mistrzowska)",
            description=[
                "1. Wyraziła / wyraził i uzasadniła / uzasadnił swoje zdanie na temat udziału obywateli w formach demokratycznego sprawowania władzy samorządowej i państwowej. Zna istotę społeczeństwa obywatelskiego.",
                "2. Potrafi wskazać, na czym polega samorządność drużyny w realizacji zadań.",
                "3. Prześledziła / prześledził programy partii politycznych w Polsce, zwracając uwa- gę na główne problemy społeczne, na które one odpowiadają. Zapoznała / zapoznał się z układami sił partyjnych w Niemczech, Anglii i Francji oraz w innych krajach.",
                "4. Wzięła / wziął udział w wyborach do samorządu uczniowskiego lub władz samorządowych i państwowych.",
                "5. Rozumie mechanizmy sprawowania władzy w państwie demokratycznym, rolę wyborów i zasadę pomocniczości państwa.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="NEGOCJATORKA / NEGOCJATOR ***",
            description=[
                "1. Przeprowadziła / przeprowadził ćwiczenie, dyskusję lub debatę, podczas której skuteczne negocjowała / negocjował między dorosłymi a dziećmi.",
                "2. Przedstawiła / przedstawił zastępowi podstawowe zasady negocjacji.",
                "3. Przeprowadziła / przeprowadził dla zastępu warsztaty z komunikacji.",
                "4. Doprowadziła / doprowadził do porozumienia między stronami konfliktu.",
                "5. Łagodziła / łagodził konflikty w zastępie, klasie lub drużynie różnymi sposobami.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="ORGANIZATORKA NAUKI / ORGANIZATOR NAUKI *",
            description=[
                "1. Opracowała / opracował tygodniowy rozkład zajęć, w którym uwzględniła / uwzględnił wszystkie swoje zajęcia (lekcje, zajęcia pozalekcyjne, obowiązki domowe, czas odpoczynku).",
                "2. Zorganizowała / zorganizował sobie miejsce do nauki w domu (oświetlenie, ustawienie krzesła itp.).",
                "3. Przedstawiła/przedstawił kolegom zestaw ćwiczeń odprężających, stosowanych podczas przerw w nauce.",
                "4. Dowiedziała / dowiedział się, w jakich zajęciach pozalekcyjnych i na jakich zasa- dach można brać udział w szkole, okolicznych klubach lub domach kultury. Wyniki zwiadu przedstawiła / przedstawił na zbiórce zastępu. Zrobiła / zrobił mapkę okolicy, z informacjami, gdzie odbywają się zajęcia pozalekcyjne.",
                "5. Dowiedziała / dowiedział się, jakie czasopisma popularnonaukowe są dostępne na rynku, zastanowiła / zastanowił się, które są przeznaczone dla niej / niego, przeczytała / przeczytał jeden wybrany numer i zaprezentowała / zaprezentował zastępowi najciekawszy artykuł w dowolnej formie, zwracając uwagę na różne możliwości poszerzania wiedzy.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="ORGANIZATORKA CZASU / ORGANIZATOR CZASU **",
            description=[
                "1. Planując swój czas, korzysta z kalendarza i terminarza.",
                "2. Przedstawiła / przedstawił zastępowi różne propozycje aktywnego spędzenia wolnego czasu i zorganizowała / zorganizował wybraną przez zastęp propozycję wspólnego spędzenia czasu.",
                "3. Przeprowadziła / przeprowadził sondę wśród uczniów klasy lub szkoły na temat spędzania wolnego czasu, z wynikami sondy zapoznała / zapoznał drużynę.",
                "4. Zna zasady gospodarowania czasem.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="PLANISTA ***",
            description=[
                "1. Zorganizowała/zorganizował dla drużyny udział w wybranym przedsięwzięciu pozaharcerskim.",
                "2. Współorganizowała / współorganizował biwak drużyny, brała/brał udział w podziale zadań, była/był odpowiedzialna/odpowiedzialny za wybrane zadania (np. lista zakupów, dojazdy, zamówienie autokaru).",
                "3. Sporządziła / sporządził plan, program i preliminarz wybranego przedsięwzięcia drużyny.",
                "4. Zaplanowała / zaplanował kilka ciekawych propozycji do planu pracy drużyny, propozycje przedstawiła/przedstawił radzie drużyny, a po zatwierdzeniu uczestniczyła / uczestniczył w ich realizacji.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="",
            description=[
                "",
                "",
                "",
                "",
                "",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="STARSZA SIOSTRA / STARSZY BRAT *",
            description=[
                "1. Opiekowała / opiekował się młodszym dzieckiem przez kilka godzin, umiejętnie je zabawiając.",
                "2. Pod opieką rodziców zadbała / zadbał o powierzone dziecko: przestrzegała / przestrzegał godzin karmienia, przygotowała / przygotował do wyjścia na spacer w odpowiednim ubraniu, towarzyszyła / towarzyszył przy toalecie porannej i wieczornej, ułożyła / ułożył do snu.",
                "3. Potrafi zapewnić bezpieczeństwo zabawy w domu i na spacerze.",
                "4. Przygotowała / przygotował i przeprowadziła / przeprowadził grę lub zabawę dla dzieci w wieku przedszkolnym.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="PIASTUNKA / PIASTUN **",
            description=[
                "1. Systematycznie opiekowała / opiekował się młodszym dzieckiem (rodzeństwem, dzieckiem sąsiadów itp.) przez dłuższy okres (miesiąc, wakacje): przygotowywała / przygotowywał odpowiednie posiłki, wyprowadzała / wyprowadzał na spacer w odpowiednim ubraniu, myła / mył i kładła / kładł do snu, zapewniała / zapewniał bezpieczną zabawę, pomagała / pomagał w nauce (w przypadku opieki nad dzieckiem w wieku szkolnym).",
                "2. Własnoręcznie przygotowała / przygotował niespodziankę dla dziecka (zabawka, ubranko, ulubiony podwieczorek).",
                "3. Opracowała / opracował krótki wykaz książek, dotyczących opieki nad dzieckiem. Zapoznała / zapoznał zastęp z jedną z nich.",
                "4. Opracowała / opracował kilka interesujących zabaw i gier dla dzieci.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="POMOCNA DŁOŃ *",
            description=[
                "1. Opiekowała / opiekował się młodszym rodzeństwem lub innym dzieckiem pod nieobecność rodziców, zapewniając bezpieczeństwo i przygotowując posiłki.",
                "2. Pomagała / pomagał rodzicom w organizacji dużego rodzinnego wydarzenia (remont, uroczystość, przeprowadzka).",
                "3. Opiekowała / opiekował się chorym domownikiem lub sąsiadem, podając posiłki i lekarstwa oraz umilając czas.",
                "4. Wyręczyła / wyręczył inną osobę w wykonaniu jakiegoś jej obowiązku.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="UCZYNNA / UCZYNNY **",
            description=[
                "1. Samodzielnie lub razem z zastępem dotarła / dotarł do osób potrzebujących pomocy w okolicy (osoby starsze, niepełnosprawne, samotne), przedstawiła / przedstawił wykaz takich osób radzie drużyny.",
                "2. Sprawdziła / sprawdził, jakiej pomocy potrzebują od niego członkowie rodziny (rodzice, dziadkowie, rodzeństwo), przyjęła / przyjął na siebie kolejny, nowy obowiązek rodzinny (np. pomoc w nauce rodzeństwu, pomoc w ogrodzie dziad- kom, mycie samochodu rodziców) i wypełniała / wypełniał go rzetelnie przez co najmniej miesiąc.",
                "3. Przez dłuższy okres, np. zimą, w wakacje, pomagała / pomagał osobie starszej, niepełnosprawnej, samotnej, potrzebującej opieki.",
                "4. Pełniła / pełnił służbę w szkolnej stołówce, świetlicy lub bibliotece, pomagając młodszym.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="DOMOWNICZKA / DOMOWNIK *",
            description=[
                "1. Estetycznie nakryła / nakrył stół do codziennego posiłku i uroczystego obiadu rodzinnego.",
                "2. Posprzątała / posprzątał kuchnię, umieszczając wszystko na właściwym miejscu.",
                "3. Zabezpieczyła / zabezpieczył przed zepsuciem wędliny, masło, pieczywo, mleko.",
                "4. Odkurzyła / odkurzył mieszkanie, stosując właściwy sprzęt i środki do podłóg, mebli, dywanów.",
                "5. Przygotowała / przygotował podwieczorek dla członków rodziny, zadbała / zadbał o właściwy wystrój miejsca spożywania posiłku.",
                "6. Pielęgnowała / pielęgnował kwiaty domowe (podlewanie, przesadzanie).",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="GOSPODYNI / GOSPODARZ * *",
            description=[
                "1. Zrobiła / zrobił pranie, prawidłowo segregując rzeczy do prania, stosując odpowiednie proszki i płyny.",
                "2. Pod opieką osoby dorosłej umyła / umył okna",
                "3. Zna środki czystości używane do utrzymania porządku w domu, wie, jak się je stosuje. Zna domowe sposoby i środki stosowane do czyszczenia, mycia różnych urządzeń domowych, zabezpieczania przed owadami itp.",
                "4. Nauczyła / nauczył się posługiwać sprzętem gospodarstwa domowego.",
                "5. Zrobiła / zrobił listę zakupów oraz zakupy potrzebne do całodziennego wyżywienia rodziny. Samodzielnie przygotowała/przygotował posiłek dla domowników.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="PANI DOMU / PAN DOMU ***",
            description=[
                "1. Przez kilka dni zajmowała / zajmował się prowadzeniem domu: utrzymywała / utrzymywał czystość i porządek w mieszkaniu, przyrządzała / przyrządzał wszystkie posiłki zgodnie z opracowanym przez siebie tygodniowym jadłospisem, zorganizowała / zorganizował tygodniowe zakupy według wcześniej przygotowanej listy.",
                "2. Zorganizowała / zorganizował uroczystość rodzinną dla kilku osób, przygotowała / przygotował potrawy. Zadbała / zadał o odpowiednią oprawę przyjęcia (muzyka, eleganckie nakrycie, wystrój pokoju).",
                "3. Skompletowała / skompletował lub przejrzała / przejrzał apteczką domową. Po uzgodnieniu z rodzicami uzupełniła / uzupełnił ewentualne braki.",
                "4. Dokonała / dokonał miesięcznych opłat za mieszkanie, telefon, gaz.",
                "5. Odczytała / odczytał liczniki na wodę i gaz, przygotowała / przygotował dom do dłuższej nieobecności (wyłączenie wody, gazu, zabezpieczenie mieszkania przed kradzieżą, zalaniem).",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="OPIEKUNKA CHORYCH / OPIEKUN CHORYCH **",
            description=[
                "1. Opiekowała / opiekował się chorym w domu lub na obozie. Wykonywała / wykonywał następujące czynności: sprzątała / sprzątał w pomieszczeniu, w którym przebywał chory, ścieliła / ścielił łóżko i zmieniała / zmieniał pościel, podawała / podawał posiłki i lekarstwa według zaleceń lekarza.",
                "2. Przygotowała / przygotował dietetyczny posiłek odpowiedni do rodzaju choroby osoby, którą się opiekowała / opiekował",
                "3. Pomogła / pomógł chorej osobie w załatwieniu spraw osobistych, np. przekazując wiadomości do szkoły lub pracy, robiąc zakupy.",
                "4. Zorganizowała / zorganizował choremu rozrywkę, starając się ulżyć jego dolegliwościom.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="HISTORYK RODZINNY **",
            description=[
                "1. Poznała / poznał historię swojej rodziny, wykonała / wykonał wykaz ważnych rodzinnych wydarzeń.",
                "2. Uporządkowała / uporządkował album rodzinny, opisała /opisał zdjęcia, ułożyła / ułożył je chronologicznie",
                "3. Odtworzyła / odtworzył drzewo genealogiczne swojej rodziny przynajmniej trzy pokolenia wstecz, korzystając np. z ksiąg kościelnych lub dokumentów rodzinnych. Uporządkowała / uporządkował dokumentację i pamiątki rodzinne (świadectwa, dyplomy, listy, pamiątki).",
                "4. Prowadziła / prowadził kronikę rodziny, zapisała / zapisał w niej np. kilka ciekawych przygód rodziny, wywiady przeprowadzone ze starszymi członkami rodziny, słowniczek pierwszych słów młodszego rodzeństwa.",
                "5. Współorganizowała / współorganizował i uczestniczyła / współuczestniczył w rodzinnej wycieczce do miejsc ważnych dla rodziny (np. miejscowość, z której pochodzą dziadkowie, kościół, w którym brali ślub, miejsce, gdzie poznali się rodzice, miejsce walki, w której uczestniczył ktoś z rodziny).",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="POSZUKIWACZ NIEZNANEGO ŚWIATA **",
            description=[
                "1. Dowiedziała / dowiedział się, gdzie w najbliższej okolicy mieszkają osoby niepełnosprawne.",
                "2. Nawiązała / nawiązał kontakt z dzieckiem (rówieśnikiem) niepełnosprawnym, dowiedziała/dowiedział się, na czym polega jego niepełnosprawność.",
                "3. Zaprosiła / zaprosił niepełnosprawnego kolegę na zbiórkę.",
                "4. W dowolnej formie pomagała / pomagał niepełnosprawnej koleżance lub niepełnosprawnemu koledze.",
                "5. Poznała / poznał kilka zwrotów grzecznościowych w języku migowym.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="ODKRYWCA NIEZNANEGO ŚWIATA ***",
            description=[
                "1. Poznała / poznał system pomocy społecznej w swojej gminie, odnalazła / odnalazł instytucje wspomagające osoby niepełnosprawne.",
                "2. Wraz z zastępem przeprowadziła / przeprowadził zwiad po swojej miejscowości, odnalazła / odnalazł miejsca trudne do pokonania przez osoby niepełnosprawne ruchowo. Przedstawiła / przedstawił projekt ich likwidacji.",
                "3. Przygotowała / przygotował oraz przeprowadziła /przeprowadził kilka gier i zabaw na zbiórce zastępu, w której uczestniczyły też dzieci niepełnosprawne.",
                "4. Przeprowadziła / przeprowadził krótką rozmowę w języku migowym, poznała / poznał technikę posługiwania się alfabetem Braille’a.",
                "5. Brała / brał udział w kweście ulicznej, sprzedaży cegiełek lub innej akcji zbierania pieniędzy na cele społeczne.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="ZNAWCA KRWIODAWSTWA **",
            description=[
                "1. Wie, co to jest krew i zna jej rolę w organizmie człowieka.",
                "2. Wie, kto może zostać honorowym dawcą krwi i gdzie w najbliższej okolicy można oddać krew.",
                "3. Zaprosiła /zaprosił na zbiórkę zastępu lub drużyny zasłużonego honorowego dawcę krwi.",
                "4. Przygotowała/przygotował program na uroczystość lub apel z okazji Dni Honorowego Krwiodawstwa PCK albo wykonał plakat zachęcający do honorowego oddawania krwi.",
                "5. Namówił co najmniej dwie osoby do oddania krwi.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="POPULARYZATOR KRWIODAWSTWA ***",
            description=[
                "1. Wie, jakie znaczenie mają poszczególne składniki krwi dla prawidłowego funkcjonowania organizmu człowieka oraz jakie choroby leczone są z wykorzystaniem leków krwiopochodnych i w jakich sytuacjach wykorzystywania jest krew dla ratowania zdrowia i życia człowieka.",
                "2. Wie, jakie organizacje i instytucje zajmują się promocją krwiodawstwa i pobieraniem krwi.",
                "3. Wraz z zastępem lub drużyną odwiedził regionalne centrum krwiodawstwa i krwiolecznictwa (punkt krwiodawstwa) lub wziął udział w otwartej akcji poboru krwi. Poznał procedury związane z pobieraniem krwi.",
                "4. Przygotował prezentację multimedialną promującą honorowe krwiodawstwo, którą zaprezentował na zbiórce drużyny lub przed swoją klasą. Prezentację zamieścił na stronie internetowej.",
                "5. Do oddania krwi namówił co najmniej trzy osoby.",
            ],
            group="Społeczne i obywatelskie",
        ),
        schemas.CreateBadge(
            name="AMBASADOR KRWIODAWSTWA (mistrzowska)",
            description=[
                "1. Zna budowę tkanki krwi i rolę składników krwi dla prawidłowego funkcjonowania organizmu człowieka. Wie, jakie jest wykorzystanie poszczególnych składników krwi dla ratowania zdrowia i życia człowieka.",
                "2. Potrafi omówić historię leczenia z wykorzystaniem krwi ludzkiej, w tym rozwój krwiodawstwa w Polsce. Zna zadania organizacji i instytucji zajmujących się organizacją i promocją krwiodawstwa w Polsce.",
                "3. Odnalazł w swoim otoczeniu osobę, która otrzymała krew lub preparaty krwiopochodne. Przeprowadził z nią wywiad, który zaprezentował swojej drużynie.",
                "4. Nawiązał kontakt z Klubem Honorowych Dawców Krwi PCK lub placówką publicznej służby krwi. Poznał drogę krwi od dawcy do biorcy, potrafi omówić etapy pobierania krwi i jej przygotowania dla celów leczniczych.",
                "5. Zorganizował w środowisku szkolnym lub lokalnym akcję promującą honorowe krwiodawstwo. Do oddania krwi namówił co najmniej cztery osoby.",
                "6. Do wyboru: chce oddać honorowo krew, prowadzi zdrowy styl życia, zapoznał się z kwestionariuszem dla krwiodawcy i sprawdził, czy spełnia wymagania dla dawcy (oprócz wieku) – dla osób poniżej 18 roku życia, oddał honorowo krew – dla osób, które ukończyły 18 lat (nie dotyczy osób, który z powodów zdrowotnych nie zostały zakwalifikowane do oddania krwi).",
            ],
            group="Społeczne i obywatelskie",
        ),
        # KOMPUTEROWE
        schemas.CreateBadge(
            name="KOMPUTEROWIEC *",
            description=[
                "1. Wykonała / wykonał podstawowe czynności na komputerze: napisała / napisał tekst w edytorze tekstu, korzystając z arkusza kalkulacyjnego, wykonała / wykonał prostą operację, np. ▪ sumowanie komórek, założyła / założył własną skrzynkę e-mail, napisała / napisał i wysłała / wysłał wiadomość pocztą elektroniczną.",
                "2. Zebrała / zebrał biblioteczkę informatyczną i przygotowała /przygotował do wykorzystania w drużynie.",
                "3. Znalazła / znalazł w Internecie informacje z dziedziny, którą się interesuje.",
                "4. Zainstalowała / zainstalował nowy program komputerowy i skonfigurowała / skonfigurował go do własnych potrzeb.",
                "5. Obsługując komputer, przestrzega zasad higieny pracy.",
            ],
            group="Komputerowe",
        ),
        schemas.CreateBadge(
            name="ZNAWCA KOMPUTERÓW **",
            description=[
                "1. Wskazała / wskazał najlepsze modele monitorów, skanerów, drukarek, modemów oraz innych podzespołów komputerowych w zależności od potrzeb i możliwości użytkownika, uzasadniła / uzasadnił swój wybór. Systematycznie czyta prasę komputerową.",
                "2. Zainstalowała / zainstalował w komputerze i właściwie skonfigurowała / skonfigurował dodatkowy sprzęt: kartę muzyczną, twardy dysk, CD-ROM, skaner.",
                "3. Zaradziła / zaradził w kilku przypadkach awarii sprzętu komputerowego.",
                "4. Zaprezentowała / zaprezentował młodszym harcerzom budowę i zasadę działania komputera oraz innych urządzeń, np. drukarki, skanera.",
                "5. Poznaje dowolny język programowania, wykorzystując nabyte umiejętności napisała / napisał prostą aplikację.",
            ],
            group="Komputerowe",
        ),
        schemas.CreateBadge(
            name="INFORMATYK ***",
            description=[
                "1. Przedstawiła / przedstawił młodszym harcerzom rolę i perspektywy rozwoju informatyki we współczesnym świecie. Zorganizowała / zorganizował w drużynie (szczepie) zajęcia z obsługi wybranego programu użytkowego.",
                "2. Poznała / poznał co najmniej jeden język programowania, uczy się następnego, opracowała / opracował aplikację na użytek drużyny, szczepu, hufca.",
                "3. Poznała / poznał podstawowe rodzaje licencji na oprogramowanie komputerowe, promuje stosowanie legalnych programów.",
                "4. Samodzielnie złożyła / złożył komputer i właściwie go skonfigurowała / skonfigurował (na poziomie BIOS-u i systemu operacyjnego).",
                "5. Pełni stałą służbę opartą na wiedzy informatycznej, np. administrator stronwww (hufca, szczepu, drużyny), serwisant sprzętu komputerowego w komendzie hufca, administrator elektronicznej bazy danych.",
            ],
            group="Komputerowe",
        ),
        schemas.CreateBadge(
            name="INTERNAUTKA / INTERNAUTA **",
            description=[
                "1. Wskazała / wskazał najciekawsze jej / jego zdaniem strony w Internecie i uzasadniła / uzasadnił swój wybór. Odszukała / odszukał strony zaprzyjaźnionych środowisk harcerskich.",
                "2. Znalazła / znalazł w Internecie potrzebne mu informacje, wykorzystała / wykorzystał je na zbiórce.",
                "3. Skonfigurowała / skonfigurował konto w programie pocztowym, przesłała / przesłał i odebrała / odebrał informacje za pomocą poczty elektronicznej, subskrybuje minimum jedną grupę dyskusyjną.",
                "4. Zapoznała / zapoznał się z popularnymi nazwami związanymi z Internetem.",
                "5. Umie znaleźć w sieci potrzebne oprogramowanie, zna rodzaje licencji i stosuje się do nich.",
            ],
            group="Komputerowe",
        ),
        schemas.CreateBadge(
            name="MISTRZYNI INTERNETU / MISTRZ INTERNETU ***",
            description=[
                "1 Nawiązała / nawiązał współpracę z zespołem GK ZHP zajmującym się Internetem, uczestniczyła / uczestniczył w zadaniu realizowanym przez ten zespół.",
                "2. Zna zasady budowania ośrodków www z zakresu wizualizacji projektu, zagadnień PR i oprogramowania.",
                "3. Skompletowała / skompletował zespół do realizacji projektu internetowego (serwisu www), rozdzieliła / rozdzielił zadania w zespole: przygotowanie i korekta tekstów, przygotowanie grafiki, kodowanie serwisu, promocja itp., gotowy serwis opublikowała / opublikował w Internecie.",
                "4. Stale rozwija swoje umiejętności w zakresie języków programowania stosowanych w budowaniu ośrodków www, zna co najmniej dwa, w tym jeden z grupy języków server-side, przygotowała / przygotował layout strony stosując optymalizację grafiki.",
                "5. Przeprowadziła / przeprowadził formę kształceniową dotyczącą tematyki Internetu.",
            ],
            group="Komputerowe",
        ),
        schemas.CreateBadge(
            name="DTP-owiec ***",
            description=[
                "1. Sprawnie posługuje się fachową terminologią: bękart, interlinia, szeryf, kerning, punktura, tekstura itp.",
                "2. Zna zasady składu komputerowego i wykorzystuje je w wykonywanych pracach.",
                "3. Wykonała / wykonał zaawansowane prace DTP i zaprezentowała / zaprezentował je na zbiórce lub w szkole.",
                "4. Swoje umiejętności wykorzystała / wykorzystał, przygotowując śpiewnik, poradnik lub inne wydawnictwo dla drużyny, szczepu, hufca.",
                "5. Na zbiórce wytłumaczyła / wytłumaczył młodszym, jakie zagrożenia wynikają z piractwa komputerowego.",
            ],
            group="Komputerowe",
        ),
        schemas.CreateBadge(
            name="GRAFIK KOMPUTEROWY (mistrzowska)",
            description=[
                "1. Samodzielnie wykonała / wykonał zaawansowane prace graficzne na komputerze i zaprezentowała / zaprezentował je na zbiórce lub w szkole.",
                "2. Swoje umiejętności wykorzystała / wykorzystał, wykonując prace graficzne dla drużyny, szczepu, hufca.",
                "3. Potrafi sprawnie wykonać zaawansowane operacje: skanować i obrabiać grafikę, importować do i eksportować z innych programów, przygotować dokument do druku, wykonywać retusze itp.",
                "4. Nauczyła / nauczył młodszych harcerzy podstaw obsługi programu graficznego.",
                "5. Na zbiórce wytłumaczyła / wytłumaczył zagrożenia wynikające z piractwa komputerowego, zna zasady dotyczące ochrony praw autorskich do grafiki komputerowej.",
            ],
            group="Komputerowe",
        ),
        schemas.CreateBadge(
            name="",
            description=[
                "",
                "",
                "",
                "",
                "",
            ],
            group="Komputerowe",
        ),
        schemas.CreateBadge(
            name="ZNAWCA.... *** (nazwa programu komputerowego)",
            description=[
                "1. Zainstalowała / zainstalował wybrany program, poznała / poznał jego tajniki, skonfigurowała / skonfigurował program odpowiednio do swoich potrzeb.",
                "2. Zgromadziła / zgromadził biblioteczkę informatyczną związaną z wybranym programem.",
                "3. Wykonała / wykonał w wybranym programie materiały i pomoce potrzebne drużynie, szczepowi, hufcowi.",
                "4. Nauczyła / nauczył młodszych harcerzy podstawowej obsługi wybranego programu, zaprezentowała / zaprezentował efekty swojej pracy z programem.",
                "5. Na zbiórce wytłumaczyła / wytłumaczył istotę i zagrożenia wynikające z piractwa komputerowego.",
            ],
            group="Komputerowe",
        ),
        schemas.CreateBadge(
            name="PROGRAMISTKA / PROGRAMISTA... (nazwa języka programowania) (mistrzowska)",
            description=[
                "1. Poznała / poznał genezę i historię wybranego języka programowania, wskazała / wskazał najważniejsze udoskonalenia w jego ostatnich wersjach.",
                "2. Zgromadziła / zgromadził biblioteczkę informatyczną związaną z wybranym językiem programowania.",
                "3. Samodzielnie napisała / napisał dużą aplikację i zaprezentowała / zaprezentował ją w szkole, na studiach lub w drużynie.",
                "4. Napisała / napisał program pomocny w pracy drużyny, szczepu, hufca.",
                "5. Zna wymagania dotyczące praw autorskich do programów komputerowych i kodów źródłowych.",
            ],
            group="Komputerowe",
        ),
        # WSPIERAJĄCE WYCHOWANIE DUCHOWE I RELIGIJNE
        schemas.CreateBadge(
            name="BETLEJEMSKIE ŚWIATŁO POKOJU *",
            description=[
                "1. Poznała / poznał Dobra Nowinę związaną z narodzinami Jezusa oraz przesłanie Betlejemskiego Światła Pokoju. Wie, jaką drogą dociera ono do Polski.",
                "2. Poznała / poznał tradycje bożonarodzeniowe oraz uczestniczyła / uczestniczył w wigilii harcerskiej.",
                "3. Pomogła / pomógł w zorganizowaniu w swoim domu świąt Bożego Narodzenia.",
                "4. Uczestniczyła/uczestniczył w uroczystości przekazania Betlejemskiego Światła Pokoju (np. w hufcu, w instytucjach miejskich, w szkole, na harcerskiej mszy).",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="OPIEKUNKA / OPIEKUN BETLEJEMSKIEGO ŚWIATŁA POKOJU **",
            description=[
                "1. Zapoznała / zapoznał drużynę z przesłaniem Betlejemskiego Światła Pokoju.",
                "2. Samodzielnie lub z zastępem odwiedziła / odwiedził samotną osobę mieszkającą w sąsiedztwie, przekazując jej Światło.",
                "3. Przyniosła/przyniósł Betlejemskie Światło Pokoju do swego domu i zapoznała/zapoznał rodzinę z jego ideą. Wysłała/wysłał kartki z życzeniami bożonarodzeniowymi rodzinie lub przyjaciołom.",
                "4. Zorganizowała / zorganizował wspólnie z zastępem wigilię dla zaprzyjaźnionego środowiska harcerskiego, przekazując mu Światło.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="STRAŻNICZKA / STRAŻNIK BETLEJEMSKIEGO ŚWIATŁA POKOJU ***",
            description=[
                "1. Wspólnie z drużyną co roku organizuje zbiórkę, na której zapoznaje zaprzyjaźnioną drużynę z przesłaniem i tradycjami Betlejemskiego Światła Pokoju.",
                "2. Zorganizowała / zorganizował udział drużyny w przekazaniu Betlejemskiego Światła Pokoju do kościołów, urzędów i innych instytucji oraz mieszkańcom.",
                "3. Wspólnie z drużyną pomogła / pomógł w zorganizowaniu wigilii dla osób samotnych, podczas której przekazano im Betlejemskie Światło Pokoju.",
                "4. W porozumieniu z rodziną lub drużyną zaprosiła / zaprosił na kolację wigilijną do domu lub na zbiórkę wigilijną samotną osobę z sąsiedztwa, przekazując jej Betlejemskie Światło Pokoju.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="PRZEWODNIK DUCHOWY ***",
            description=[
                "1. Brała / brał udział jako przedstawiciel drużyny lub hufca w służbach (medycznej, porządkowej itp.) w swojej parafii lub diecezji. Zaangażowała / zaangażował do tej służby chętnych harcerzy ze swojego środowiska.",
                "2. Zadbała/zadbał, by wszyscy przygotowali się do tych wydarzeń od strony duchowej (sakrament pokuty, czynny udział w nabożeństwach, przyjęcie komunii św.)",
                "3. Przeczytała / przeczytał Dzieje Apostolskie. W gawędzie przedstawiła / przedstawił drużynie losy jednego z apostołów, np. podróże misyjne św. Pawła.",
                "4. Wspólnie z chętnymi osobami z drużyny nawiązała / nawiązał kontakt z duszpasterzami w swojej parafii, zaoferowała / zaoferował pomoc i współpracę (np. organizowanie spotkań modlitewnych, wieczorów skupienia, służby liturgicznej, znalezienie kapelana dla hufca).",
                "5. Zadbała / zadbał o zorganizowanie rekolekcji dla harcerzy ze swego środowiska.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="MŁODY PIELGRZYM **",
            description=[
                "1.Potrafi wyjaśnić, jaki jest cel pielgrzymowania.",
                "2. Uczestniczyła / uczestniczył w dwóch pielgrzymkach harcerskich (pieszych lub autokarowych), zrealizowanych od chwili otwarcia próby.",
                "3. W czasie pielgrzymki brała / brał czynny udział w rekolekcjach (zaangażowanie w życie grupy, przygotowanie duchowe, przyjęcie sakramentów).",
                "4. Opisała / opisał swoje doświadczenia pielgrzymkowe i przedstawiła / przedstawił na zbiórce zastępu.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="PIELGRZYM ***",
            description=[
                "1. Zapoznała / zapoznał się z historią pielgrzymowania. Przedstawiła / przedstawił ją w formie gawędy na zbiórce drużyny.",
                "2. Zorganizowała/zorganizowałwyjazddrużynynapielgrzymkęharcerską(pieszą lub autokarową).",
                "3. Zorganizowała / zorganizował wyjazdowe rekolekcje dla harcerzy ze swojego środowiska.",
                "4. Opracowała / opracował mapę ciekawych miejsc w Polsce, do których pielgrzymują wierni. Przedstawiła / przedstawił ją w drużynie (w szczepie, w hufcu itp.) i opowiedziała / opowiedział o swoich doświadczeniach pielgrzymowania.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="PRZYJACIEL LITURGII (DO WYBORU, np.KATOLICKIEJ, PRAWOSŁAWNEJ, PROTESTANCKIEJ) **",
            description=[
                "1. Pobożnie i aktywnie uczestniczy w nabożeństwie / mszy św, stanowiąc wzór dla innych.",
                "2. Potrafi posługiwać się kalendarzem liturgicznym. Wie, kiedy obchodzi się podstawowe święta i jakie nabożeństwa są odprawiane w ciągu roku liturgicznego.",
                "3. Pomagała / pomagał w przygotowaniu nabożeństwa mszy św., tzn. komentarze do czytań, procesję z darami, dobrać odpowiednie pieśni, ułożyć modlitwę wiernych itp.",
                "4. Nauczyła / nauczył chętnych harcerzy z drużyny odpowiedniego zachowania na nabożeństwie mszy.",
                "5. Uczestniczyła / uczestniczył w budowaniu ołtarza polowego na obozie drużyny. Zadbała / zadbał o urządzenie miejsca wokół niego, tak by atmosfera sprzyjała wyciszeniu i modlitwie.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="ZNAWCA LITURGII (DO WYBORU, np. KATOLICKIEJ, PRAWOSŁAWNEJ, PROTESTANCKIEJ) ***",
            description=[
                "1. Zna strukturę mszy św. (np. nabożeństwa protestanckiego, mszy prawosławnej), poprawnie odmawia modlitwy i wykonuje gesty podczas uczestnictwa w takiej mszy.",
                "2. Zna podstawowe paramenty liturgiczne i umie wyjaśnić ich znaczenie (np. lichtarz, krzyż procesyjny, trybularz, cyborium). Umie przygotować ołtarz do nabożeństwa mszy św. (odpowiednio do wybranej religii).",
                "3. Zna ceremoniał sztandarowy stosowany podczas uroczystości religijnych (odpowiednio do wybranej religii). Potrafi wydawać odpowiednie komendy pocztom sztandarowym.",
                "4. Nauczyła / nauczył chętnych harcerzy z drużyny odpowiedniego zachowania na mszy / nabożeństwie, z uwzględnieniem również tych, którzy nie są bezpośrednio zaangażowani religijnie w liturgię.",
                "5. Zadbała/zadbał wspólnie z chętnymi osobami o urządzenie na obozie lub biwaku miejsca modlitwy (skupienia, wyciszenia), w którym każdy może realizować swoje potrzeby duchowe (np. ołtarza polowego, kapliczki obozowej, namiotu skupienia, gdzie można udostępnić odpowiednie lektury ku pokrzepieniu ducha, polany, na której można pobyć sam na sam z sobą i z naturą).",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="MŁODY RELIGIOZNAWCA * *",
            description=[
                "1. Wie, jak nazywa się pięć głównych religii świata. Opowiedział o nich zainteresowanym osobom z drużyny (zastępu).",
                "2. Wie, gdzie w okolicy znajdują się świątynie lub miejsca modlitwy różnych wyznań. Zorganizował wycieczkę zastępu do jednego z tych miejsc i przedstawił w interesujący sposób podstawowe informacje z nim związane.",
                "3. Zapoznała / zapoznał się z życiorysem założyciela wybranej religii i przedstawił jego osobę na zbiórce drużyny.",
                "4. Nawiązała / nawiązał kontakt z osobą z kręgów skautowych lub harcerskich, która wyznaje inną religię.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="RELIGIOZNAWCA ***",
            description=[
                "1. Potrafi wymienić pięć głównych religii świata i ich założycieli. Umie wyjaśnić ich główne dogmaty wiary. Wskaże w Polsce miejsca głównych skupisk wyznawców różnych religii.",
                "2. Zorganizowała/zorganizował wyjście zastępu lub drużyny do świątyni wyznawców wybranej religii (meczet, synagoga itp.) i przedstawiła/przedstawił kilka informacji z nią związanych.",
                "3. Przeprowadziła / przeprowadził w zastępie lub w drużynie dyskusję na temat tolerancji religijnej (na czym ona polega, jakie są skutki nietolerancji w społeczeństwie itp.).",
                "4. Zapoznała / zapoznał się z najważniejszymi dokumentami na temat dialogu międzyreligijnego (np. Deklaracja o stosunku Kościoła katolickiego do religii niechrześcijańskich, Deklaracja o wolności religijnej).",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="MŁODY EKUMENISTA ***",
            description=[
                "1. Umie wyjaśnić, czym jest ekumenizm.",
                "2. Zapoznała / zapoznał zastęp z ideą Tygodnia Modlitw o Jedność Chrześcijan.",
                "3. Poznała / poznał zwyczaje świąteczne wybranych wyznań chrześcijańskich, np. Boże Narodzenie u katolików i prawosławnych lub obchody świąt maryjnych w różnych rejonach Polski i zapoznała/zapoznał z nimi zainteresowane osoby z drużyny.",
                "4. Zapoznała / zapozał się z treścią jednego z dokumentów kościelnych autorstwa Jana Pawła II na temat ekumenizmu i w przystępny sposób przedstawi swoje przemyślenia na ten temat na zbiórce drużyny.",
                "5. Nauczyła / nauczył się modlitwy „Ojcze nasz” w obcym języku.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="EKUMENISTA (mistrzowska)",
            description=[
                "1. Umie wyjaśnić, czym jest ekumenizm. Zna istotne różnice między najważniej- szymi wyznaniami chrześcijańskimi (katolicyzm, prawosławie, protestantyzm).",
                "2. Zorganizowała / zorganizował w zastępie lub w drużynie dyskusję z udziałem przedstawicieli różnych wyznań chrześcijańskich.",
                "3. Wzięła/wziął udział w spotkaniu ekumenicznym (np. w Taizè) lub w obchodach Tygodnia Modlitw o Jedność Chrześcijan. Nauczyła / nauczył się trzech kanonów śpiewanych przez braci z Taizè.",
                "4. Zapoznała / zapoznał się z nauczaniem Jana Pawła II na temat dialogu ekumenicznego.",
                "5. Umie przygotować modlitwę ekumeniczną dla zastępu (drużyny, obozu, na biwaku), np. na zakończenie dnia.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="POSZUKUJĄCA WARTOŚCI / POSZUKUJĄCY WARTOŚCI **",
            description=[
                "1. Umie opowiedzieć, czym jest rozwój duchowy i religijny, potrafi wyjaśnić różnicę między pojęciami „duchowość” i „religijność”.",
                "2. Prowadzi dzienniczek, w którym dokumentuje swoje przemyślenia i doświadczenia duchowe.",
                "3. Nauczyła / nauczył się wybierać wartościową lekturę, filmy, spektakle teatralne i opowiedział o swoich przeżyciach z tym związanych.",
                "4. Wie, jak nazywa się pięć głównych religii świata. Potrafi wyjaśnić, dlaczego na świecie jest wiele tradycji religijnych i duchowych.",
                "5. Zorganizowała / zorganizował dla zastępu /drużyny zbiórkę, w czasie której harcerze mogli porozmawiać o swoim światopoglądzie i nauczyć się tolerowania różnic w tym względzie.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="POSZUKUJĄCA AUTORYTETU / POSZUKUJĄCY AUTORYTETU ***",
            description=[
                "1. Zapoznała / zapoznał się z biografią osoby znanej z etycznego postępowania, której życiowe dokonania inspirują do podążania tą samą drogą, np. świętego, mędrca, autorytetu moralnego.",
                "2. Zapoznała / zapoznał się z filozofią życia, poglądami tej osoby oraz z metodami pracy nad sobą, które stosowała ona w swoim życiu.",
                "3. Opracowała / opracował na tej podstawie plan osobistego rozwoju duchowego i zastosowała / zastosował ten program w swoim życiu.",
                "4. Zorganizowała / zorganizował kominek, na którym interesująco przedstawiła / przedstawił biografię wybranej osoby harcerzom swojej drużyny.",
                "5. Przeczytała / przeczytał lekturę z zakresu duchowości, np. A. Glassa Podstawy duchowości instruktora harcerskiego, Dzienniki św. Tereski od Dzieciątka Jezus, pisma R. Cantalamessa, opowiadania B. Ferrero.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="SZARA LILIJKA **",
            description=[
                "1. Na 24 godziny oderwała / oderwał się od codziennych spraw, nie kontaktowała / kontaktował się z nikim (polecana samotna wycieczka na cały dzień do lasu). W tym czasie przemyślała / przemyślał Prawo Harcerskie i swój dotychczasowy do niego stosunek, oceniła / ocenił swoją wolę wypełniania Przyrzeczenia i Prawa Harcer- skiego całym życiem (w każdej chwili, w każdym miejscu, każdym swoim czynem).",
                "2. Zastanowiła/zastanowił się też nad swoimi wadami i pomyślała/pomyślał nad tym, jak skuteczniej z nimi walczyć. Zdobywający przyznają sobie sprawność sami, jeżeli szczerze potwierdzą w swoim sumieniu, że chcą żyć zgodnie z zasadami harcerskimi zawartymi w Przyrzeczeniu i Prawie Harcerskim.",
                "3. Obrzędowe przyznanie sprawności można połączyć z odnowieniem Przyrzeczenia. Sprawność tę trzeba zdobywać co roku od nowa. Po upływie terminu jej „ważności” wymagana jest powtórna próba lub przystąpienie do zdobywania sprawności „mężnego” lub „chwata”.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="MĘŻNY **",
            description=[
                "Przez siedem dni od chwili przystąpienia do próby (po otrzymaniu od opiekuna lub drużynowego listu otwierającego próbę) w tajemnicy przed osoba zdobywająca tę sprawność prowadzi walkę z wadą, słabością, kompleksem, który w szczególny sposób komplikuje jej współżycie z innymi ludźmi (np. kłótliwość, zarozumiałość, nietolerancja, nieśmiałość, spóźnianie się, nierzetelność).",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        schemas.CreateBadge(
            name="CHWAT ***",
            description=[
                "Słowo „chwat” tworzą pierwsze litery następujących nazw cech charakteru: C − cnota (postępowanie zgodne z zasadami moralnymi),H − hart (wytrwałość wobec przeciwności losu), W − wola (siła woli, umiejętność konsekwentnego dążenia do celu), A − altruizm (poświęcanie swoich talentów na rzecz innych), T − tężyzna (ćwiczenie sprawnego i wytrzymałego ciała i ducha).Aby zdobyć tę sprawność, harcerka / harcerz musi się zastanowić, brak których z wymienionych cech jest jej/jego wadą. Następnie opracowuje zadania (dla każdej litery po jednym), które mogą pomóc w walce z tymi słabościami. Powinny to być zadania realizowane specjalnie na potrzeby tej sprawności, niepowtarzające się np. przy zdobywaniu stopnia. Kiedy już harcerka/harcerz wymyśli zadania, wy- biera opiekuna próby (przyjaciela, kogoś zaufanego), którego zapoznaje z wybrany- mi zadaniami. Bardzo ważne jest, by opiekunem została osoba, która będzie umiała wspierać i motywować podopiecznego w walce ze słabością.",
            ],
            group="Wspierające wychowanie duchowe i religijne",
        ),
        # HOBBYSTYCZNE (23)
        schemas.CreateBadge(
            name="PRZYJACIEL KSIĄŻKI *",
            description=[
                "1. Systematycznie czyta książki. Zgromadziła / zgromadził własną biblioteczkę ulubionych pozycji.",
                "2. Samodzielnie wykonała / wykonał kilka zakładek do swoich książek.",
                "3. Brała / brał udział w konkursie czytelniczym organizowanym np. w szkole, drużynie, przez redakcję czasopisma lub portalu internetowego.",
                "4. Wykonała / wykonał drobne naprawy introligatorskie kilku książek, pełniła / pełnił dyżur w bibliotece szkolnej lub publicznej.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="BIBLIOTEKARKA / BIBLIOTEKARZ **",
            description=[
                "1. Prowadziła / prowadził w czasie próby na sprawność bibliotekę drużyny (szczepu) lub obozu.",
                "2. W czasie dyżurów w bibliotece szkolnej lub publicznej sprawnie posługiwała / posługiwał się katalogiem książek. Przygotowała / przygotował dla osoby prowadzącej zajęcia materiały na określony temat.",
                "3. Zorganizowała / zorganizował wieczór literacki w drużynie, szkole, domu kultury.",
                "4. Zorganizowała / zorganizował w szczepie lub szkole kiermasz książek.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="BIBLIOFIL ***",
            description=[
                "1. Zgromadziła / zgromadził własny księgozbiór i prowadzi jego katalog.",
                "2. Wykonała / wykonał ekslibris do biblioteki domowej, szkolnej lub publicznej.",
                "3. Urządziła / urządził w drużynie wystawę ciekawych książek, prezentując na niej także własne zbiory.",
                "4. Urządziła / urządził w szkole lub szczepie wieczór wspólnego czytania wybranej książki, spotkanie z autorem lub podobną imprezę.",
                "5. Nawiązała / nawiązał kontakt z antykwariatem, poznał sposoby gromadzenia wydawnictw antykwarycznych i przechowywania oraz zabezpieczania starodruków.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="KRONIKARKA / KRONIKARZ *",
            description=[
                "1. Prowadziła / prowadził w okresie próby kronikę zastępu (drużyny), posługując się kilkoma rodzajami pisma.",
                "2. Sporządziła / sporządził notatki z wydarzeń na podstawie relacji świadków.",
                "3. Dopilnowała / dopilnował przez co najmniej jeden rok, aby kronika była zawsze tam, gdzie drużyna.",
                "4. Zapoznała/zapoznał się z twórczością najbardziej znanych polskich kronikarzy.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="REPORTERKA / REPORTER **",
            description=[
                "1. Przygotowała / przygotował rzeczowe relacje z biwaku lub obozu drużyny, z uroczystości szkolnej, z wydarzeń mających miejsce w okolicy.",
                "2. Posługiwała / posługiwał się sprzętem reporterskim (dyktafon, aparat fotograficzny, kamera), przygotowując materiały dla szkolnego (lokalnego) radia, telewizji, gazety.",
                "3. Napisała / napisał dwa reportaże: na wybrany i na zadany temat. Dobrała / dobrał ilustrujące je rysunki lub zdjęcia. Przedstawiła/ przedstawił je w drużynie.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="DZIENNIKARKA / DZIENNIKARZ ***",
            description=[
                "1. Poznała / poznał cechy, jakimi powinni charakteryzować się dziennikarze oraz zasady, jakie obowiązują w ich zawodzie.",
                "2. Przeprowadziła / przeprowadził wywiad na określony temat.",
                "3. Przez okres próby brała / brał udział w pracy redakcji harcerskiej, pisząc do wybranego działu.",
                "4. Nawiązała / nawiązał stały kontakt z gazetą młodzieżową lub dla dzieci i systematycznie dostarcza jej swoje artykuły.",
                "5. Przekazała / przekazał napisany przez siebie reportaż z imprezy harcerskiej do lokalnej gazety.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="WYDAWCA (mistrzowska)",
            description=[
                "1. Poznała / poznał pracę redakcji gazety lub wydawnictwa książkowego.",
                "2. Rozróżniła / rozróżnił rodzaje czcionek drukarskich i typy edytorów komputerowych, stosując je w swojej gazecie lub publikacjach książkowych.",
                "3. Złożyła / złożył na komputerze gazetę lub inną publikację.",
                "4. Rozprowadzała / rozprowadzał wydawnictwa przygotowane przez drużynę, hufiec, szkołę, dom kultury itp."
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="MIŁOŚNICZKA ARCHITEKTURY / MIŁOŚNIK ARCHITEKTURY **",
            description=[
                "1. Rozpoznaje sześć podstawowych nowożytnych stylów w architekturze. Odwiedziła / odwiedził znajdujące się w okolicy budowle charakterystyczne dla tych stylów. Wyniki zwiadu zaprezentowała / zaprezentował na zbiórce zastępu.",
                "2. Zorganizowała / zorganizował wyprawę do ciekawego obiektu, opowiedziała / opowiedział o cechach charakterystycznych tej budowli, jej stylu i historii.",
                "3. Zorganizowała / zorganizował zbiórkę poświęconą znanym polskim architektom.",
                "4. Zaprojektowała / zaprojektował rozmieszczenie mebli i wystrój swego pokoju.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="ARCHITEKT ***",
            description=[
                "1. Umie opowiedzieć o prekursorach poszczególnych stylów w architekturze.",
                "2. Wykonała / wykonał rejestr lub przewodnik po ciekawych budynkach nowoczesnych i zabytkowych w swojej miejscowości lub gminie.",
                "3. Zorganizowała / zorganizował wyprawę (zastępu lub drużyny) do innej miejscowości w celu zwiedzenia ciekawych budowli. Przygotowała / przygotował wystawę fotograficzną lub inną formę prezentacji ciekawych rozwiązań architektonicznych, które mogłyby być zastosowane na tym terenie.",
                "4. Pomogła / pomógł innym harcerkom/harcerzom w zaprojektowaniu urządzenia ich pokoi.",
                "5. Zaprojektowała / zaprojektował wygląd i rozmieszczenie namiotów oraz urządzeń na obozie drużyny. Swój projekt przedstawiła / przedstawił radzie drużyny.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="IGIEŁKA *",
            description=[
                "1. Wykonała / wykonał drobne prace: przyszyła/przyszył guziki do koszuli, obrębiła / obrębił chusteczkę, naszyła / naszył łatę na spodnie, zacerowała / zacerował dziurę w swetrze.",
                "2. Uszyła / uszył ręcznie lub na maszynie drobny przedmiot, np. łapki do garnków, kieszeń na grzebienie w łazience, fartuszek kuchenny, worek na kapcie.",
                "3. Wyszyła / wyszył swój monogram lub znaczek sprawności na rękawie munduru.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="KRAWCOWA / KRAWIEC **",
            description=[
                "1. Rozróżniła / rozróżnił podstawowe rodzaje tkanin: bawełna, wełna, jedwab, sztuczne tworzywa.",
                "2. Nauczyła / nauczył się szyć na maszynie. Uszyła/uszył według gotowego wykroju spódnicę lub szorty, obrębiła / obrębił obrus, wszyła / wszył suwak, uszyła / uszył poszewkę na poduszkę.",
                "3. Nauczyła / nauczył się konserwować maszynę do szycia.",
                "4. Uszyła / uszył chusty dla drużyny lub zastępu.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="MISTRZYNI IGŁY / MISTRZ IGŁY ***",
            description=[
                "1. Zaprezentowała / zaprezentował własny styl ubierania się, szyjąc samodzielnie lub adaptując gotowe ubrania do własnych potrzeb.",
                "2. Uszyła / uszył samodzielnie bluzkę, mundur, szorty lub spodnie, pobierając uprzednio miarę i przygotowując wykrój.",
                "3. Zorganizowała / zorganizował pokaz mody na zbiórce, wykorzystując ubrania członków zastępu i posługując się aktualnymi żurnalami.",
                "4. Przeprowadziła / przeprowadził w drużynie naukę podstaw szycia.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="MISTRZYNI / MISTRZ RĘCZNYCH ROBÓTEK **",
            description=[
                "1. Wykonała / wykonał różne prace: na drutach lub na maszynie dziewiarskiej lub splotła/splótł makramę według własnego wzoru.",
                "2. Przedstawiła / przedstawił na zbiórce zastępu lub drużyny własnoręcznie wykonane prace.",
                "3. Zorganizowała / zorganizował w drużynie (szczepie lub w szkole) wystawę robótek ręcznych, zapraszając na nią znanych w okolicy mistrzów i mistrzynie.",
                "4. Nauczyła / nauczył młodszych wykonania prostych  makram.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="PROJEKTANTKA MODY / PROJEKTANT MODY **",
            description=[
                "1. Wymieniła / wymienił kilku polskich i zagranicznych projektantów mody.",
                "2. Czyta systematycznie w czasopismach i w Internecie artykuły prezentujące aktualne trendy w modzie.",
                "3. Przedstawiła / przedstawił swoje zbiory projektów ubrań i wykrojów.",
                "4. Przedstawiła/przedstawił zaprojektowany samodzielnie strój na zbiórce zastępu lub drużyny.",
                "5. Zaprezentowała / zaprezentował cztery stylizacje,np.:doszkoły(pracy), na dyskotekę, na wycieczkę, na ważne spotkanie. Wyjaśniła/wyjaśnił w zastępie lub drużynie zasady doboru stroju odpowiedniego do okazji, typu urody, sylwetki.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="KOLEKCJONERKA / KOLEKCJONER ***",
            description=[
                "1. Posiada własne zbiory.",
                "2. Opracowała / opracował system katalogowania własnych zbiorów i posługuje się nim, uzupełniając swoją kolekcję.",
                "3. Skompletowała / skompletował specjalistyczną biblioteczkę i utrzymuje kontakty z innymi kolekcjonerami o podobnym hobby.",
                "4. Zorganizowała / zorganizował wystawę swoich eksponatów.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="ROWERZYSTKA / ROWERZYSTA *",
            description=[
                "1. Potrafi jeździć na rowerze.",
                "2. Zdobyła / zdobył kartę rowerową.",
                "3. Konserwowała / konserwował rower przed wycieczką i po niej.",
                "4. Uczestniczyła / uczestniczył w trzech całodniowych wycieczkach rowerowych.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="CYKLISTA **",
            description=[
                "1. Zna zasady bezpiecznego poruszania się pieszych i rowerzystów po drogach.",
                "2. Zna budowę i potrafi konserwować rower. Potrafi zmienić dętkę.",
                "3. Brała / brał udział w kilku wycieczkach rowerowych.",
                "4. Wie, jaka jest różnica pomiędzy wymijaniem, omijaniem i wyprzedzaniem oraz zna zasady pierwszeństwa przejazdu (m.in. na skrzyżowaniach). Poznała / poznał dziesięć znaków poziomych (na jezdni) i pokazała / pokazał je zastępowi podczas wycieczki po mieście.",
                "5. Wykonała / wykonał planszę ze znakami drogowymi, obejmującą: 10 znaków ostrzegawczych, 10 znaków zakazu, 12 znaków nakazu oraz 10 znaków informacyjnych. Wytłumaczyła / wytłumaczył ich znaczenie na zbiórce zastępu.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="ZNAWCA RUCHU DROGOWEGO ***",
            description=[
                "1. W okresie próby systematycznie pełniła / pełniił służbę ruchu w miejscach i przy okazjach tego wymagających.",
                "2. Uczestniczyła / uczestniczył w spotkaniu z policjantem na temat bezpieczeństwa na drogach i obowiązujących przepisów.",
                "3. Zorganizowała / zorganizował wraz z zastępem zawody na rowerowym torze przeszkód lub w miasteczku ruchu drogowego, popularyzując w ten sposób obowiązujące przepisy w drużynie, szczepie lub szkole.",
                "4. Zorganizowała / zorganizował dla młodszych kolegów pokaz prawidłowego poruszania się po drogach, połączony z konkursem.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="STRAŻNICZKA BEZPIECZEŃSTWA / STRAŻNIK BEZPIECZEŃSTWA **",
            description=[
                "1. Zapoznała / zapoznał się, wspólnie z osobą dorosłą, ze stanem technicznym maszyn używanych w gospodarstwie.",
                "2. Spisała / spisał, jakich napraw należy dokonać, aby wszystkie urządzenia były bezpieczne. Wnioski przedstawiła / przedstawił osobie dorosłej.",
                "3. Zapoznała / zapoznał się ze znakami oznaczającymi niebezpieczne narzędzia, miejsca oraz czynności.",
                "4. Przygotowała / przygotował i przedstawiła / przedstawił na zbiórce drużyny zasady bezpiecznego posługiwania się sprzętem w gospodarstwie.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="MŁODY STRATEG *",
            description=[
                "1. Zagrał co najmniej w trzy różne gry planszowe lub karciane, w tym przynajmniej jedną o tematyce harcerskiej lub historycznej, dobrze zna zasady tych gier.",
                "2. Wziął udział w turnieju gier planszowych lub karcianych.",
                "3. Wie, na czym polega system szwajcarski.",
                "4. Zaprezentował i zagrał z zastępem lub drużyną w wybraną przez siebie grę planszową lub karcianą.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="STRATEG **",
            description=[
                "1. Zagrał w pięć różnych gier planszowych lub karcianych, w tym w co najmniej dwie gry o tematyce historycznej lub harcerskiej. Potrafi wytłumaczyć ich zasady.",
                "2. Na zbiórce drużyny zaprezentował historię, twórców oraz rodzaje gier planszowych i karcianych.",
                "3. Zorganizował w swoim środowisku (drużyna, szkoła, kółko zainteresowań) akcję promującą gry planszowe i karciane.",
                "4. Wziął udział w konkursie organizowanym przez wydawnictwo gier planszowych lub karcianych.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="TRZY KOŚCI ***",
            description=[
                "1. Zorganizował warsztaty dla co najmniej ośmiu osób na temat gier planszowych i karcianych, przeprowadził podczas nich turniej w wybraną grę.",
                "2. Opracował grę planszową lub karcianą z dziedziny swoich zainteresowań lub za- adaptował już istniejącą grę. Upowszechnił grę w swoim środowisku (szczepie, hufcu, szkole).",
                "3. Wziął udział w konwencie lub festiwalu, którego tematów były gry planszowe lub karciane.",
                "4. Zorganizował wraz z zastępem lub drużyną akcję zarobkową, z której dochód przeznaczył na zakup gry planszowej lub karcianej dla drużyny lub zastępu.",
            ],
            group="Hobbystyczne",
        ),
        schemas.CreateBadge(
            name="MISTRZ GRY (mistrzowska)",
            description=[
                "1. Zorganizował turniej gier planszowych lub karcianych na poziomie hufca, szkoły, domu kultury.",
                "2. Samodzielnie lub wraz z zespołem stworzył grę planszową lub karcianą o tematyce harcerskiej i upowszechnił ją w środowisku harcerskim.",
                "3. Zdobył fundusze na zakup pięciu gier lub pozyskał pięć gier dla swojego środowiska. Regularnie powiększa zbiór gier drużyny (szczepu, hufca).",
                "4. Stworzył grupę lub uczestniczy w grupie miłośników gier planszowych, z którą regularnie prowadził otwarte spotkania i warsztaty gier.",
            ],
            group="Hobbystyczne",
        ),
        # DLA HARCEREK I HARCERZY NIEDOWIDZĄCYCH (2)
        schemas.CreateBadge(
            name="UWAŻNY PIESZY",
            description=[
                "1 Poznała / poznał zasady ruchu drogowego w mieście, uczestnicząc w zajęciach organizowanych w miasteczku ruchu drogowego.",
                "2. Samodzielnie, pod okiem drużynowego, przeprowadziła/przeprowadził zastęp przez dwa ruchliwe skrzyżowania oznakowane sygnalizacją świetlną.",
                "3. Poznała / poznał zasady poruszania się w terenie niezabudowanym i zastosowała / zastosował je w praktyce, np. prowadząc zastęp na wędrówce.",
                "4. Spopularyzowała / spopularyzował wśród kolegów w interesującej formie podstawowe zasady bezpiecznego poruszania się po ulicach i drogach.",
            ],
            group="Dla harcerek i harcerzy niedowidzących",
        ),
        schemas.CreateBadge(
            name="MAŁY OPTYK",
            description=[
                "1. Poznała / poznał zasady higieny wzroku i przestrzega ich podczas pracy, nauki, w domu, na wycieczce itp., a także propaguje je wśród kolegów.",
                "2. Poznała / poznał rodzaje szkieł optycznych i zrealizowała / zrealizował co najmniej trzy recepty okulistyczne.",
                "3. Dokonała / dokonał drobnych napraw okularów swoich i kolegów.",
                "4. Wyczyściła / wyczyścił za pomocą odpowiednich środków szkła korekcyjne, utrzymuje je w czystości.",
            ],
            group="Dla harcerek i harcerzy niedowidzących",
        ),
        # DLA HARCEREK I HARCERZY NIEWIDOMYCH (3)
        schemas.CreateBadge(
            name="KUCHARKA DOMOWA / KUCHARZ DOMOWY",
            description=[
                "1. Poznała / poznał cechy podstawowych produktów żywnościowych i potrafi zakupić ich potrzebną ilość.",
                "2. Potrafi obsługiwać urządzenia grzejne (kuchnie gazowe, elektryczne, grzałkę).",
                "3. Potrafi samodzielnie przygotować śniadanie i kolację: pokroiła / pokroił chleb, przygotowała / przygotował kanapki (kroiła / kroił wędlinę, ser itp.), parzyła / parzył herbatę, ugotowała / ugotował jajka, przygotowała / przygotował jajecznicę.",
                "4. Nakryła / nakrył do stołu prawidłowo i estetycznie.",
                "5. Przestrzegała / przestrzegał zasad higieny przy przygotowaniu posiłków.",
            ],
            group="Dla harcerek i harcerzy niewidomych",
        ),
        schemas.CreateBadge(
            name="WIOŚLARKA / WIOŚLARZ",
            description=[
                "1. Poznała / poznał co najmniej dwa typy jednostek wiosłowych (kajak, ponton, łódź), potrafi przygotować jednostkę do pływania, prawidłowo wiosłować, wykonywać podstawowe manewry za pomocą steru i bez steru.",
                "2. Poznała / poznał i prawidłowo stosuje podstawowy sprzęt ratowniczy (potrafi prawidłowo założyć kamizelkę ratunkową). Poznała / poznał zasady bezpieczeń- stwa na wodzie.",
                "3. Poznała / poznał zasady prawidłowego biwakowania nad wodą i spędziła / spędził co najmniej siedem dni nad wodą.",
                "4. Potrafi zaśpiewać trzy piosenki wodniackie, upowszechniła / upowszechnił w swoim środowisku sporty wodniackie.",
                "5. Wie, co to jest PTTK. Zna zasady zdobywania turystycznej odznaki kajakowej.",
            ],
            group="Dla harcerek i harcerzy niewidomych",
        ),
        schemas.CreateBadge(
            name="CHODZĘ SAMA / CHODZĘ SAM",
            description=[
                "1. Potrafi dojść do wyznaczonych punktów na terenie ośrodka, pomagała / pomagał słabszym w trafieniu do wyznaczonego miejsca.",
                "2. Przestrzega przepisów bezpiecznego poruszania się na terenie ośrodka.",
                "3. Potrafi rozróżnić rodzaje podłoża.",
                "4. Umie korzystać z pomocy przewodnika.",
                "5. Umie określić słuchowo na ulicy (drodze) kierunek i rodzaj jadącego pojazdu, potrafi np. za pomocą węchu określić mijane obiekty.",
                "6. Poznała / poznał zasady poruszania się w ruchu ulicznym.",
            ],
            group="Dla harcerek i harcerzy niewidomych",
        ),
        # DLA HARCEREK I HARCERZY GŁUCHYCH (2)
        schemas.CreateBadge(
            name="MÓWIĘ I MIGAM",
            description=[
                "1. Opanowała / opanował język migowy polski w stopniu wystarczającym do porozumiewania się w życiu codziennym.",
                "2. Stale pogłębia znajomość zunifikowanego języka migowego.",
                "3. Potrafi swobodnie porozumieć się językiem polskim w sprawach życia codziennego. Rozumie, co do niej/niego mówią i jest rozumiana/rozumiany przez słyszących.",
                "4. Wywiązała / wywiązał się z roli tłumacza „na żywo” podczas spotkania grupy osób głuchych i grupy osób słyszących.",
                "5. Pomogła / pomógł osobie głuchej, słabo mówiącej, załatwić sprawy np. w urzędzie lub dziecku głuchemu porozumieć się z osobą dorosłą nieznającą „migów”.",
            ],
            group="Dla harcerek i harcerzy głuchych",
        ),
        schemas.CreateBadge(
            name="TŁUMACZ NA MIGI",
            description=[
                "1. Opanowała / opanował język migowy polski i wybrany język migowy obcy w stopniu wystarczającym do porozumiewania się w życiu codziennym.",
                "2. Była / była tłumaczem „na migi” w czasie spotkania grupy głuchych polskich z wycieczką głuchych obcokrajowców.",
                "3. Opowiedziała / opowiedział „na migi” wycieczce głuchych obcokrajowców o pracy drużyny, do której należy.",
                "4. Stale pogłębia znajomość zunifikowanego języka migowego.",
            ],
            group="Dla harcerek i harcerzy głuchych",
        ),
        # JEŹDZIECKIE I KAWALERYJSKIE (23)
        schemas.CreateBadge(
            name="SANITARIUSZKA WETERYNARYJNA / SANITARIUSZ WETERYNARYJNY **",
            description=[
                "1. Poznała / poznał ogólną budowę kostnoszkieletową konia i położenie najważniejszych narządów wewnętrznych.",
                "2. Potrafi zmierzyć temperaturę, tętno i liczbę oddechów konia, zna ich prawidłowe wartości.",
                "3. Udzieliła / udzielił pierwszej pomocy w przypadku zranienia konia, ochwatu, morzyska (kolki).",
                "4. Zna skład apteczki weterynaryjnej. Wie, jak się stosuje podstawowe leki i maście.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="WETERYNARZ ***",
            description=[
                "1. Zna dokładną budowę konia (szkielet, położenie narządów).",
                "2. Udzieliła /udzielił pierwszej pomocy przy zranieniu, ochwacie, kolce, zmierzyć temperaturę, tętno i liczbę oddechów.",
                "3. Przygotowała / przygotował pacjenta i środki potrzebne do zabiegu przed przybyciem lekarza.",
                "4. Pełniła / pełnił służbę weterynaryjną na obozie.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="SZERMIERZ *",
            description=[
                "1. Dobrze jeździ konno.",
                "2. Poznała / poznał rodzaje białej broni i techniki władania nią, zademonstrowała / zademonstrował podstawowe pchnięcia (pieszo).",
                "3. Poznała / poznał zasady bezpieczeństwa i przepisy sportowe dotyczace władania białą bronią.",
                "4. Swoje umiejętności zaprezentowała / zaprezentował zastępowi / drużynie.",
                "5. W ciekawej formie przedstawiła / przedstawił klasie, drużynie lub zastępowi historię wybranego pułku kawalerii II RP.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="LANSJER **",
            description=[
                "1. Bardzo dobrze jeździ konno.",
                "2. Poznała / poznał budowę i zastosowanie lancy. Zna kilka wzorów szabel.",
                "3. Przygotowała / przygotował pokaz władania lancą dla swojego środowiska (drużyny, szczepu), prezentując prawidłowe pchnięcia i zasłony, pomagała / pomagał w szkoleniu jeździeckim i nauczyła / nauczył władania lancą swój zastęp.",
                "4. Rozróżniła / rozróżnił proporczyki pułków kawalerii 20-lecia.",
                "5. Przedstawiła / przedstawił w ciekawy sposób na szerszym forum (np. w formie strony www, spotkania w domu kultury) historię wybranego pułku kawalerii, uzasadniając swój wybór i korzystając ze źródeł.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="SZWOLEŻER ***",
            description=[
                "1. Opanowała / opanował podstawowe ćwiczenia woltyżerskie.",
                "2. Poznała / poznał budowę szabli i zasady walki z konia: cięcie łóz w cwale, cięcie glinianej gomóły, cięcie z góry w prawo, w prawo od ucha, z dołu i z góry w lewo. Opanowała / opanował pchnięcia i zasłony.",
                "3. Złożyła / złożył egzamin składający się z pokazu władania szablą konno i woltyżerki.",
                "4. Przygotowała / przygotował młodszych kolegów do zdobycia sprawności „szermierza” lub „lansjera”. Nauczyła / nauczył ich musztry z szablą pieszo.",
                "5. Potrafi prawidłowo stroczyć i założyć na konia rząd wojskowy (szeregowego) wz. 36.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="POMOCNIK PODKUWACZA *",
            description=[
                "1. Poznała / poznał zasady postępowania w przypadku gnicia strzałki i obluzowania podków.",
                "2. Poznała / poznał rodzaje podków i ich przeznaczenie oraz zasady prawidłowego podkuwania koni.",
                "3. Pomagała / pomagał podczas rozczyszczania kopyta konia, wykonując polecenia podkuwacza (kowala). Umie prawidłowo trzymać nogi konia.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="PODKUWACZ **",
            description=[
                "1. Poznała / poznał budowę anatomiczną końskiego kopyta i występujące w nim nieprawidłowości oraz zasadę narastania rogu kopytnego.",
                "2. Uczestniczyła / uczestniczył w podkuwaniu koni, zdejmując stare podkowy, prawidłowo rozczyszczając kopyto.",
                "3. Nauczyła / nauczył młodszych kolegów zasady trzymania nóg do podkuwania i pielęgnacji kopyt.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="KOWAL ***",
            description=[
                "1. Zna budowę anatomiczną końskiego kopyta.",
                "2. Poznała / poznał narzędzia kowalskie i nauczyła / nauczył się nimi posługiwać.",
                "3. Nauczyła / nauczył młodszych harcerzy zasad obchodzenia się z końskimi kopytami podczas podkuwania (rozczyszczanie, zdejmowanie starych podków).",
                "4. Podkuła / podkuł samodzielnie dwie nogi konia (pod okiem fachowca!), prawidłowo dobierając rozmiar podkowy.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="STAJENNA / STAJENNY *",
            description=[
                "1. Poznała / poznał podstawowe zasady bezpieczeństwa pracy przy koniach.",
                "2. Rozróżniła / rozróżnił stanowisko i boks, omawiając ich wady i zalety, potrafi je prawidłowo pościelić.",
                "3. Poznała / poznał zasady żywienia koni.",
                "4. Pielęgnowała / pielęgnował konia, czyszcząc i siodłając go, zadając paszę i pojąc według przyjętej kolejności, ścieląc stanowisko, sprzątając stajnię.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="MASZTALERZ **",
            description=[
                "1. Poznała / poznał pasze stosowane w żywieniu koni i potrafi prawidłowo zaplanować dzienną dawkę pokarmową w zależności od pracy wykonanej przez konia.",
                "2. Poznała / poznał zagadnienia z zakresu hodowli koni: najważniejsze rasy hodowlane w Polsce i na świecie, okres trwania ciąży u konia, termin przeprowadzania stanówki i odsadzania źrebiąt.",
                "3. Zna podstawowe narowy i nałogi u koni i potrafi im zapobiegać.",
                "4. Współopiekowała / współopiekował się koniem przez wyznaczony czas (czyszczenie, siodłanie, karmienie, pojenie, ścielenie boksu/stanowiska), zachowując zasady bezpieczeństwa.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="KONIUSZY ***",
            description=[
                "1. Kierowała / kierował pracą wachty stajennej na obozie lub w klubie.",
                "2. Kierowała / kierował żywieniem koni, stosując zasady zmian pasz (pod nadzore instruktora).",
                "3. Opiekowała / opiekował się jednym lub kilkoma końmi.",
                "4. Brała / brał udział w ujeżdżaniu młodych koni pod siodłem lub w zaprzęgu.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="ADEPTKA JEŹDZIECKA / ADEPT JEŹDZIECKI *",
            description=[
                "1. Poznała / poznał budowę zewnętrzną, maści i odmiany koni. Wiedzę tę przekazała / przekazał swojemu zastępowi podczas zbiórki.",
                "2. Zna zasady bezpieczeństwa podczas jazdy konnej i przebywania z końmi, stosuje je w praktyce.",
                "3. Poznała / poznał budowę siodła ogólnoużytkowego i rozróżnia typy nachrapników: polski, hanowerski i meksykański.",
                "4. Czyściła / czyścił konia i prawidłowo zakładała / zakładał rząd jeździecki (siodło i ogłowie). Wie, jak zapobiec zapoprężeniu i grudzie.",
                "5. Jeżdżąc konno, prawidłowo trzymała / trzymał się w stępie i kłusie, potrafi anglezować na prawidłową nogę.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="AMAZONKA / JEŹDZIEC **",
            description=[
                "1. Poznała / poznał sposoby użytkowania, typy i rasy koni w Polsce.",
                "2. Rozróżnia typy i rodzaje siodeł.",
                "3. Pielęgnowała / pielęgnował konia czyszcząc go przed i po jeździe.",
                "4. Poznała / poznał zasady poruszania się konno w terenie.",
                "5. Kreśliła / kreślił figury na ujeżdżalni w każdym chodzie konia.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="AMAZONKA DOSKONAŁA / JEŹDZIEC DOSKONAŁY ***",
            description=[
                "1. Potrafi udzielić pierwszej pomocy.",
                "2. Wymieniła / wymienił główne regiony hodowli koni na świecie, poznała / poznał zwyczaje, tradycje i piosenki jeździeckie.",
                "3. Wykonywała / wykonywał wszelkie prace stajenne, pomagając przy żniwach lub zwózce siana, konserwując sprzęt jeździecki, zadając paszę i sprzątając sta- nowiska lub boksy koni. Nauczyła / nauczył zastęp podstawowych umiejętności w zakresie obsługi koni.",
                "4. Poznała / poznał ważniejsze schorzenia koni, potrafi im zapobiec i udzielić pierwszej pomocy weterynaryjnej.",
                "5. Wykonała / wykonał zwroty na przodzie i na zadzie, ustępowanie od łydki, branie przeszkody (do 100 cm), potrafi prowadzić konia kontrgalopem.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="SKÓRNIK *",
            description=[
                "1. Wyczyściła / wyczyścił, zmiękczyła / zmiękczył, zakonserwowała / zakonserwował skórzane elementy ekwipunku jeździeckiego.",
                "2. Poznała / poznał podstawowe narzędzia pracy rymarskiej (igły rymarskie, szydło,koń rymarski, nóż, dratwa, dziurkacz), posłużyła / posłużył się nimi.",
                "3. Prawidłowo przygotowała / przygotował dratwę do szycia, szyła / szył na dwie igły.",
                "4. Wszyła / wszył oderwaną sprzączkę, wycięła / wyciął nową dziurkę w skórze.",
                "5. Poznała / poznał ogólną budowę siodła ogólnoużytkowego i rozróżniła / rozróżnił typy nachrapników: polski, hanowerski, meksykański.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="CZELADNIK RYMARSKI **",
            description=[
                "1. Połączyła / połączył skórę różnymi sposobami.",
                "2. Zszyła / zszył rozerwany kantar lub uzdę, puśliska lub przystuły.",
                "3. Poznała / poznał różne rodzaje rzędów jeździeckich, rozróżnia różne rodzaje uprzęży.",
                "4. Wykonała / wykonał najprostszy kantar dla konia (np. z taśmy, ze sznurka).",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="RYMARZ ***",
            description=[
                "1. Rozróżniła / rozróżnił różne rodzaje skóry, poznała / poznał ich cechy i przeznaczenie.",
                "2. Posługując się sprawnie narzędziami rymarskimi, połączyła / połączył skórę nitami, zastosowała / zastosował jedną z technik zdobienia skóry.",
                "3. Wykonała / wykonał kantar ze skóry, ozdobiła / ozdobił go według własnego pomysłu.",
                "4. Nauczyła / nauczył harcerzy prostych prac rymarskich.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="POMOCNIK LUZAKA *",
            description=[
                "1. Potrafi rozpoznać trzy różne rodzaje kiełzna, zna ich działanie.",
                "2. Wie, czym różnią się szory od chomąta.",
                "3. Opiekowała / opiekował się koniem podczas zawodów lub pokazu, czyszcząc go, zaplatając grzywę i ogon, pojąc, karmiąc i ścieląc boks.",
                "4. Pomagała / pomagał przy zaprzęganiu konia, zapoznając się z budową użytkowanej uprzęży.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="LUZAK **",
            description=[
                "1. Wymieniła / wymienił rodzaje uprzęży i typy pojazdów, rozpoznając je na rysunkach lub zdjęciach.",
                "2. Poznała / poznał zasady zaprzęgania koni w pojedynkę i w parze, powożąc w łatwym terenie.",
                "3. Ubierała / ubierał konia w szory i chomąto, rozróżniając prawidłowo poszczególne części uprzęży.",
                "4. Brała / brał udział w przygotowaniach do zawodów zaprzęgów, pełniąc funkcję luzaka.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="WOŹNICA ***",
            description=[
                "1. Poznała / poznał budowę uprzęży. Wie, co to jest munsztuk zaprzęgowy, pehlam liverpool, fasculce itp.",
                "2. Rozróżniła / rozróżnił style zaprzęgów: angielski, węgierski, bałagulski i inne.",
                "3. Jeździła / jeździł parokonnym zaprzęgiem w różnorodnym terenie",
                "4. Prowadziła / prowadził wóz taborowy podczas rajdu konnego.",
                "5. Potrafi opisać zasady zawodów w powożeniu. W ciekawy sposób przedstawiła / przedstawił je na forum drużyny.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="ADEPTKA WOLTYŻERKI / ADEPT WOLTYŻERKI *",
            description=[
                "1. Bez problemu wsiada i zsiada z konia zarówno z lewej, jak i prawej strony.",
                "2. Prawidłowo wykonuje następujące ćwiczenia: na koniu gimnastycznym: nożyce, wskok, sztandar, stanie na siodle, na stojącym koniu: 4 strony świata, martwy Indianin, rybka w przód i w tył, na koniu chodzącym na lonży: ćwiczenia na równowagę, jazda bokiem i tyłem.",
                "3. Potrafi nazwać ćwiczenia woltyżerskie (wykonywane przez kogoś innego, na filmie itp.).",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="WOLTYŻERKA / WOLTYŻER **",
            description=[
                "1. Regularnie jeździ konno (stęp, kłus, galop).",
                "2. Zna zasady bezpieczeństwa podczas jazdy konnej i stosuje się do nich.",
                "3. ▪Wykonała / wykonał następujące ćwiczenia: na koniu stojącym: stanie na siodle, nożyce, wskok, sztandar, na koniu chodzącym na lonży (stęp, kłus, galop): 4 strony świata, martwy Indianin, rybka w przód i w tył.",
                "4. Zna budowę rzędu woltyżerskiego.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        schemas.CreateBadge(
            name="WOLTYŻERKA DOSKONAŁA / WOLTYŻER DOSKONAŁY ***",
            description=[
                "1. Ukończyła / ukończył podstawowy kurs jazdy konnej i regularnie jeŹdzi konno.",
                "2. Poznała / poznał przepisy dotyczące bezpieczeństwa ćwiczeń woltyżerskich i stosuje je w praktyce.",
                "3. Wykonała / wykonał następujące ćwiczenia: na konia stojącego: wskok trzema sposobami, na konia chodzącego na lonży w stępie, kłusie i galopie: wskok, zeskok, zeskok-wyskok, rybka, nożyce, stanie na siodle, sztandar, przeskok przez konia, na konia biegnącego luzem: wskok.",
                "4. Prawidłowo założyła / założył rząd woltyżerski.",
                "5. Nauczyła / nauczył młodszych podstawowych ćwiczeń na koniu gimnastycznym.",
            ],
            group="Jeździeckie i kawaleryjskie",
        ),
        # POCZTOWE (3)
        schemas.CreateBadge(
            name="POCZTOWIEC **",
            description=[
                "1. Poznała / poznał zasady działania poczt harcerskich oraz ich historię.",
                "2. Poznała / poznał zasady kolekcjonowania zbiorów filatelistycznych.",
                "3. Wykonała / wykonał projekt wydawnictwa poczty harcerskiej do druku.",
                "4. Przygotowała / przygotował własne zbiory wydawnictw poczty harcerskiej do wystawy.",
                "5. Brała / brał czynny udział w przygotowaniu wystawy.",
            ],
            group="Pocztowe",
        ),
        schemas.CreateBadge(
            name="POCZTYLION ***",
            description=[
                "1. Poznała / poznał zasady prowadzenia dokumentacji poczty harcerskiej i różnemtechniki powielania (drukowania).",
                "2. Wykonała / wykonał samodzielnie klisze lub pieczątkę dla poczty harcerskiej (np. linoryt).",
                "3. Zorganizowała / zorganizował sieć obsługi pocztowej na obozie lub złazie.",
                "4. Nawiązała / nawiązał współpracę z inną pocztą harcerską.",
                "5. Poznała / poznał zakres zadań, jakimi zajmuje się współcześnie Poczta Polska.",
            ],
            group="Pocztowe",
        ),
        schemas.CreateBadge(
            name="POCZTMISTRZ (mistrzowska)",
            description=[
                "1. Kierowała / kierował co najmniej kilkoma projektami tematycznymi poczty.",
                "2. Współpracowała / współpracował z Pocztą Polską, Polskim Związkiem Filatelistycznym lub odpowiednią organizacją/firmą spedycyjną lub logistyczną.",
                "3. Nadesłała / nadesłał wydawnictwa swojej poczty do Centralnego Archiwum Poczt Harcerskich.",
                "4. Wyznaczyła / wyznaczył sobie dodatkowe zadanie mistrzowskie w porozumieniu z naczelnikiem macierzystej PH.",
            ],
            group="Pocztowe",
        ),
        # WODNE I ŻEGLARSKIE (9)
        schemas.CreateBadge(
            name="ZAŁOGANT *",
            description=[
                "1. Nazwała / nazwał części jachtu mieczowego.",
                "2. Zna zasady bezpiecznego zachowania się na pokładzie jachtu.",
                "3. Potrafi określić kurs względem wiatru,wyjaśnić zasady działania miecza i steru.",
                "4. W czasie żeglugi obsługiwała / obsługiwał ster, trzymała / trzymał żagle i balastowała / balastował przy przechyłach łodzi.",
            ],
            group="Wodne i żeglarskie",
        ),
        schemas.CreateBadge(
            name="JUNGA **",
            description=[
                "1. Poznała / poznał regulamin i zasady służby jachtowej oraz komendy żeglarskie.",
                "2. Pełniła / pełnił wachtę w czasie rejsu zatokowego.",
                "3. Wykonywała / wykonywał manewry proste i złożone jachtem dwumasztowym.",
                "4. Klarowała / klarował jacht przed i po pływaniu.",
            ],
            group="Wodne i żeglarskie",
        ),
        schemas.CreateBadge(
            name="SZYPER ***",
            description=[
                "1. Zna teorię manewrowania jachtem mieczowym o powierzchni żagla do 20 m2 i komendy żeglarskie.",
                "2. Wykonała / wykonał proste i złożone manewry jachtem mieczowym.",
                "3. Pełniła / pełnił funkcje załogi na wszystkich stanowiskach manewrowych.",
                "4. Brała / brał udział w kilku wielodniowych rejsach żeglarskich.",
                "5. Zna zasady bezpieczeństwa podczas rejsu, potrafi udzielić pomocy tonącemu, przy udarze słonecznym i cieplnym oraz przy wychłodzeniu organizmu. Potrafi wezwać pomoc, znajdując się na wodzie, zna numer telefonu alarmowego WOPR.",
            ],
            group="Wodne i żeglarskie",
        ),
        schemas.CreateBadge(
            name="SZKUTNIK *",
            description=[
                "1. Poznała / poznał zasady budowy jachtów, konstrukcję łodzi i nazewnictwo jej części oraz rodzaje poszycia, drzewca, osprzętu, olinowania i ożaglowania.",
                "2. Zna konstrukcję pięciu najczęściej używanych łodzi żaglowych.",
                "3. Brała / brał udział w zabezpieczaniu sprzętu wodnego przed zimą.",
                "4. Wykonała / wykonał sploty lin miękkich, zeszlifowała / zeszlifował na równo laminowany element.",
                "5. Malowała / malował elementy jachtu farbami rozpuszczalnikowymi, zadbała / zadbał o narzędzia po zakończeniu malowania.",
            ],
            group="Wodne i żeglarskie",
        ),
        schemas.CreateBadge(
            name="BOSMAN **",
            description=[
                "1. Poznała / poznał zasady bezpieczeństwa podczas prac bosmańskich w porcie oraz w czasie pływania.",
                "2. Zna konstrukcję i budowę najpopularniejszych typów łodzi żaglowych i wiosłowych.",
                "3. Remontowała / remontował sprzęt żeglarski naprawiając również uszkodzenia żagli.",
                "4. Zacumowała / zacumował jacht w różnych warunkach, stosując podstawowe węzły.",
            ],
            group="Wodne i żeglarskie",
        ),
        schemas.CreateBadge(
            name="SYGNALISTA MORSKI *",
            description=[
                "1. Rozpoznała / rozpoznał polskie bandery i flagi: marynarki wojennej i handlowej, PZŻ, klubowe jednostki pływającej.",
                "2. Poznała / poznał zasady ceremoniału morskiego i etykiety jachtowej.",
                "3. Poznała / poznał zasady wywieszania banderek odwiedzanych państw oraz flag kodu MKS przy wejściu do obcego portu.",
                "4. Umie wezwać pomoc według MPZZM.",
            ],
            group="Wodne i żeglarskie",
        ),
        schemas.CreateBadge(
            name="MŁODY NAWIGATOR *",
            description=[
                "1. Zna instrumenty nawigacyjne.",
                "2. Umie odczytać głębokość na mapie, wysokość latarni.",
                "3. Zna zasadę podziału kuli ziemskiej z siatką geograficzną.",
                "4. Potrafi zmierzyć szybkość jachtu i głębokość wody.",
                "5. Potrafi porównać wskazanie kompasu jachtowego oraz kompasu wniesionego i trzymanego w różnych miejscach.",
            ],
            group="Wodne i żeglarskie",
        ),
        schemas.CreateBadge(
            name="NAWIGATOR **",
            description=[
                "1. Potrafi odczytać z mapy długość i szerokość geograficzną wskazanego punktu oraz zaznaczyć punkt o podanych współrzędnych.",
                "2. Potrafi odczytać z mapy morskiej odległość między dwoma wskazanymi punktami",
                "3. Potrafi wyznaczyć pozycję obserwowaną z dwóch namiarów (rzeczywistych) jednoczesnych.",
                "4. Potrafi prowadzić nawigację zliczeniową i przenieść pozycję zliczoną na określoną pozycję obserwowaną.",
                "5. Potrafi prawidłowo opisać na mapie czynności z pkt. 3−4.",
            ],
            group="Wodne i żeglarskie",
        ),
        schemas.CreateBadge(
            name="NAWIGATOR MORSKI ***",
            description=[
                "1. Odczytała / odczytał z mapy morskiej: przebieg farwaterów, występujące przeszkody nawigacyjne i wartość deklinacji w roku.",
                "2. Zmierzyła / zmierzył szybkość logiem burtowym i głębokość sondą ręczną.",
                "3. Posługiwała / posługiwał się polskimi locjami i spisem świateł. W nocy na podstawie widocznych świateł określiła / określił swą pozycję.",
                "4. Wykreśliła / wykreślił na mapie namiary, zaznaczając pozycję obserwowaną oraz kursy, odkładając przebytą drogę i zaznaczając pozycję zliczoną Przeliczyła / przeliczył kursy i namiary kompasowe na rzeczywiste, dokonała / dokonał zapisów w dzienniku jachtowym.",
                "5. Prowadziła / prowadził zliczeniówkę podczas rejsu; po określeniu różnicy pozycji obserwowanej i zliczonej (np. po nocy) potrafiła/potrafił ją wytłumaczyć.",
            ],
            group="Wodne i żeglarskie",
        ),
        # METEOROLOGICZNE (4)
        schemas.CreateBadge(
            name="ASPIRANT METEOROLOGICZNY *",
            description=[
                "1. Potrafi zauważyć nadchodzący szkwał (burzę).",
                "2. Potrafi wyjaśnić zjawisko rosy naturalnej i na okularach po wejściu zimą do ciepłego pomieszczenia.",
                "3. Potrafi rozpoznać i nazwać chmury deszczowe.",
            ],
            group="Meterologiczne",
        ),
        schemas.CreateBadge(
            name="METEOROLOG **",
            description=[
                "1. Potrafi ocenić siłę wiatru w skali Bouforta (lub m/s).",
                "2. Na planie akwenu szkoleniowego (lub strefy pilotażowej) zaznaczyła / zaznaczył lokalne, specyficzne obszary wiatrowe (oraz prądy wstępujące).",
                "3. Potrafi nazwać widoczne na niebie chmury i powiedzieć, skąd się wzięły (jak powstały) i co zwiastują.",
                "4. Rozpoznała / rozpoznał różne rodzaje chmur i określiła / określił ich wysokość. Rozróżnia rodzaje mas powietrza.",
            ],
            group="Meterologiczne",
        ),
        schemas.CreateBadge(
            name="MŁODY SYNOPTYK ***",
            description=[
                "1. Potrafi na podstawie układu chmur i innych zjawisk określić sytuację baryczną (np. nadejście ciepłego frontu).",
                "2. Potrafi rozpoznać moment przejścia frontu i podać przewidywany rozwój sytuacji meteorologicznej.",
                "3. Potrafi odebrać i wyjaśnić specjalistyczną (morską, lotniczą) prognozę pogody. Wie, gdzie ją można znaleźć.",
                "4. Przyjmie i zapisze telefoniczną prognozę pogody.",
                "5. Przeprowadziła / przeprowadził obserwacje meteorologiczne i zapisywała / zapisywał wyniki pomiarów co najmniej przez dwa tygodnie.",
            ],
            group="Meterologiczne",
        ),
        schemas.CreateBadge(
            name="SYNOPTYK (mistrzowskie)",
            description=[
                "1. Na podstawie mapki synoptycznej sporządził krótkoterminową prognozę.",
                "2. Zna typowe trasy niżów i statystyczny rozkład kierunków wiatru na terenie Polski w różnych porach roku.",
                "3. Potrafi odebrać i zrozumieć prognozę meteo w języku obcym.",
                "4. Potrafi odczytać i zinterpretować prognozę NAVTEX lub ATIS.",
                "5. Zinterpretował zarejestrowany przez siebie barogram w odniesieniu do panujących warunków meteorologicznych.",
            ],
            group="Meterologiczne",
        ),
        # LOTNICZE (16)
        schemas.CreateBadge(
            name="MODELARKA KARTONOWA / MODELARZ KARTONOWY *",
            description=[
                "1. Wyjaśnił, jakie siły działają na szybowiec w locie.",
                "2. Wyważyła / wyważył i wyregulowała / wyregulował latający kartonowy model szybowca, aby wykonał lot prosty.",
                "3. Na modelu zademonstrowała / zademonstrował działanie sterów i lotek.",
                "4. Wykonała / wykonał z papieru strzałę i gołębia oraz model latający szybowca z kartonu bez użycia kleju.",
                "5. Brała / brał udział w zawodach kartonówek.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="MODELARKA REDUKCYJNA / MODELARZ REDUKCYJNY **",
            description=[
                "1. Rozpoznaje pięć najważniejszych typów polskich szybowców i dziesięć typów używanych w Polsce samolotów.",
                "2. Wykazała / wykazał się znajomością nazw części samolotu, wyjaśniła / wyjaśnił działanie sterów.",
                "3. Zbudowała / zbudował latający model sylwetkowy (tj. o sylwetce istniejącego samolotu lub szybowca) z kartonu lub styropianu na procę lub na wędkę oraz brała / brał udział w zawodach akrobacji modeli.",
                "4. Skleiła / skleił estetycznie plastikowy model z gotowego zestawu oraz prawidłowo umieściła / umieścił na nim znaki i numery.",
                "5. Wzięła / wziął udział w konkursie modeli samolotów z tworzyw sztucznych lub zademonstrowała / zademonstrował swoje modele w zastępie.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="MODELARKA KONSTRUKTORKA / MODELARZ KONSTRUKTOR ***",
            description=[
                "1. Rozpoznaje typy współczesnych szybowców, samolotów i śmigłowców polskiej konstrukcji i używanych w Polsce oraz najważniejsze zagraniczne.",
                "2. Rozpoznaje rodzaje drewna i tworzyw sztucznych (styropian, polistyren, szkło organiczne), potrafi je kleić i obrabiać.",
                "3. Zbudowała / zbudował trzy modele z drewna lub kartonu wiernie oddające wygląd samolotów lub skleiła / skleił pięć modeli plastikowych, estetycznie i prawidłowo je malując.",
                "4. Wykazując się znajomością zasad rysunku technicznego, narysowała / narysował plan samolotu, którego model zbudowała / zbudował, uzupełniając go o szczegóły konstrukcji i malowanie według fotografii.",
                "5. Opowiedziała / opowiedział o dziejach, konstrukcji i osiągnięciach samolotów, śmigłowców, szybowców, których modele zbudowała / zbudował.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="KONSTRUKTORKA LATAWCÓW / KONSTRUKTOR LATAWCÓW *",
            description=[
                "1. Rozpoznaje różne rodzaje latawców. Wie, jaka jest konstrukcja każdego z nich i zna ich zastosowania dawniej i dziś.",
                "2. Wyjaśniła / wyjaśnił, jakie siły działają na latawce w locie i od czego zależy prawidłowy lot.",
                "3. Potrafi wyregulować latawiec, aby prawidłowo wzbijał się w powietrze i latał.",
                "4. Zbudowała / zbudował dwa latawce − płaski i skrzynkowy. Zbudowała / zbudował wyciąg do latawca i zastosowała / zastosował go.",
                "5. Uczestniczyła / uczestniczył ze swym latawcem w zawodach latawcowych, np. z okazji Święta Latawca.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="RADIOMODELARKA / RADIOMODELARZ **",
            description=[
                "1. Zna przynajmniej dwa systemy zdalnego sterowania. Wie, czym się charakteryzują. Wie, jaką rolę w urządzeniu zdalnie sterowanym spełniają przekaźniki elektromechaniczne, czujniki i silniki elektryczne.",
                "2. Wyjaśniła / wyjaśnił, gdzie i na jakich warunkach można uzyskać zezwolenie na budowę urządzeń nadawczo-odbiorczych do sterowania radiomodelarskiego.",
                "3. Narysowała / narysował i objaśniła / objaśnił schemat blokowy jednokanałowego nadajnika i odbiornika sterowania falami radiowymi.",
                "4. Zademonstrowała / zademonstrował na zbiórce zastępu lub drużyny funkcjonowanie zestawu zdalnego sterowania modeli, wyjaśniła / wyjaśnił kolegom, na czym ono polega.",
                "5. Przeprowadziła / przeprowadził pokaz akrobacji lotniczej z wykorzystaniem zestawu zdalnego sterowania.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="KONSTRUKTORKA LOTNICZA / KONSTRUKTOR LOTNICZY ***",
            description=[
                "1. Opowiedziała / opowiedział o kilku najnowszych osiągnięciach techniki lotniczej, rodzajach doświadczalnych samolotów i różnych układach aerodynamicznych samolotów. Objaśniła / objaśnił zasady lotu różnych rodzajów statków latających.",
                "2. Wyjaśniła / wyjaśnił, jaką rolę spełniają poszczególne elementy konstrukcyjne i urządzenia aerodynamiczne samolotów.",
                "3. Objaśniła / objaśnił, do czego służy wirnik ogonowy śmigłowca oraz jak się steruje śmigłowcem. Wyważyła / wyważył i wyregulowała / wyregulował model o układzie nietypowym: kaczki lub bezogonowca.",
                "4. Zbudowała / zbudował model latający o układzie nietypowym: kaczki lub bezogonowca.",
                "5. Zbudowała / zbudował model doświadczalny własnego pomysłu dowolnego statku powietrznego (np. śmigłowiec, pionowzlot, samolot skróconego startu, poduszkowiec) lub ze specjalnymi urządzeniami aerodynamicznymi (sploty, zaburzacze, hamulce aerodynamiczne, interceptory zamiast lotek itp.) i zademonstrowała / zademonstrował jego działanie.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="MŁODY BALONIARZ *",
            description=[
                "1. Wyjaśniła / wyjaśnił zasady unoszenia się balonu w powietrzu oraz budowę balonu sportowego.",
                "2. Rozpoznaje rodzaje balonów i zna ich zastosowanie.",
                "3. Stosuje przepisy bezpiecznego wypuszczania balonów na ogrzane powietrze.",
                "4. Zbudowała / zbudował razem z kolegami balon z bibułki na ogrzane powietrze.",
                "5. Brała / brał udział w pokazie wypuszczania balonu na ogrzane powietrze lub w zawodach balonów.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="TECHNIK BALONOWY **",
            description=[
                "1. Opowiedziała / opowiedział o dziejach baloniarstwa w Polsce i na świecie.",
                "2. Rozpoznała / rozpoznał różne rodzaje balonów oraz wykazał się znajomością ich budowy, teorii lotu oraz sposobów kierowania nimi.",
                "3. Wykazała / wykazał się umiejętnością obsługi balonu na ogrzane powietrze przy starcie.",
                "4. Brała / brał czynny udział w przygotowaniach do wzlotu balonu.",
                "5. Jako pasażer brała / brał udział w locie balonem na ogrzane powietrze.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="ASPIRANT SZYBOWCOWY *",
            description=[
                "1. Zna najważniejsze fakty z historii sportu szybowcowego i największe osiągnięcia w tej dziedzinie.",
                "2. Wie, w jakich konkurencjach odbywają się szybowcowe loty wyczynowe, zna nazwiska polskich szybowników, zdobywców Medalu Lilienthala.",
                "3. Wyjaśniła / wyjaśnił,jakie wymagania podwzględem zdrowia, cech psychicznych i cech charakteru stawiane są pilotowi. Zna i stosuje zasady higieny lotniczej.",
                "4. Wie, jak wyglądają odznaki szybowcowe i jakie wymagania trzeba na nie spełnić.",
                "5. Rozpoznaje rodzaje i typy szybowców produkowanych w Polsce. Prawidłowo nazwała / nazwał poszczególne elementy konstrukcji szybowca i potrafi określić ich rolę w czasie lotu szybowca lub modelu.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="MŁODA SZYBOWNICZKA / MŁODY SZYBOWNIK **",
            description=[
                "1. Wie, jakie siły działają na szybowiec w locie i jakie warunki sprzyjają lotom szybowcowym. W terenie lub na mapie wskaże, gdzie powstają prądy wznoszące.",
                "2. Zna zasady bezpieczeństwa obowiązujące na starcie szybowcowym. Pełniła / pełnił funkcję dyżurnego i chronometrażysty na starcie.",
                "3. Uczestniczyła / uczestniczył w wykładaniu, wyhangarowywaniu i transporcie szybowca, wykładaniu znaków startowych i przygotowywaniu szybowca do lotu − samodzielnie podpinała / podpinał linę holowniczą i wypuszczała / wypuszczał szybowiec przy starcie.",
                "4. Zapoznała / zapoznał się z co najmniej jedną książką o tematyce szybowcowej.",
                "5. Wykonała / wykonał lot pasażerski szybowcem.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="ASPIRANT LOTNICZY *",
            description=[
                "1. Wymieniła / wymienił wymagania zdrowotne i psychiczne stawiane lotnikom. Zna warunki przyjęcia na szkolenia lotnicze (wiek, wykształcenie) i główne rodzaje pracy w lotnictwie.",
                "2. Zna nazwy głównych części samolotu.",
                "3. Rozpoznaje polskie cywilne i wojskowe odznaki lotnicze.",
                "4. Potrafi poruszać się po lotnisku zgodnie z obowiązującymi zasadami i rozpoznaje znaki startowe.",
                "5. Odbyła / odbył lot pasażerski samolotem sportowym lub turystycznym.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="MŁODY LOTNIK **",
            description=[
                "1. Określiła / określił nawigacyjną prędkość, meteorologiczny kierunek i prędkość wiatru oraz możliwości latania w danych warunkach.",
                "2. Zna przeznaczenie dźwigara, kesonu, wręgi, żebra, okucia i pokrycia.",
                "3. Scharakteryzuje różnice w konstrukcji kratownicowej i półskorupowej.",
                "4. Zademonstruje ruchy sterami samolotu oraz opisze główne przyrządy pokładowe.",
                "5. Wskaże podstawowe typy silników lotniczych i najpopularniejszych producentów.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="OBSERWATORKA LOTNICZA / OBSERWATOR LOTNICZY *",
            description=[
                "1. Rozpoznaje podstawowe rodzaje statków powietrznych, zna ich prawidłowe nazwy oraz podział samolotów według ich przeznaczenia i budowy.",
                "2. Zna meteorologiczne warunki odbywania lotów dziennych i nocnych, zasady obserwacji nieba oraz zasadę działania urządzeń radiolokacyjnych.",
                "3. Zna sygnały alarmowe obrony cywilnej i wie, jak się zachować po ich usłyszeniu.",
                "4. Zmierzyła / zmierzył wysokość lotu samolotu za pomocą lornetki polowej oraz oceniła / ocenił „na oko” w przybliżeniu wysokość, na jakiej leci samolot, jego prędkość i kierunek lotu.",
                "5. Potrafi rozpoznać najważniejsze polskie i zagraniczne samoloty (co najmniej piętnaście typów) cywilne i wojskowe oraz rozróżnić znaki rozpoznawcze i rejestracyjne samolotów przynajmniej dziesięciu państw.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="ASPIRANT LOTNIARZ *",
            description=[
                "1. Wyjaśniła / wyjaśnił zasady lotu i pilotażu lotni.",
                "2. Wykazała / wykazał,że zna siły działające na lotnię w locie oraz wie, w jakich warunkach można wykonywać loty. Zna podstawowe zasady wykonywania lotów.",
                "3. Rozróżniła / rozróżnił przynajmniej trzy rodzaje uprzęży dla pilotów lotniowych i ich zastosowanie.",
                "4. Opowiedziała / opowiedział o najważniejszych faktach z historii lotniarstwa i sportu lotniarskiego.",
                "5. Wymieniła / wymienił najważniejsze zawody lotniowe organizowane w Polsce.",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="MŁODA LOTNIARKA / MŁODY LOTNIARZ **",
            description=[
                "1. Określiła / określił kierunek i prędkość wiatru względem zbocza oraz możliwości latania w danych warunkach.",
                "2. Zademonstrowała / zademonstrował i wyjaśniła / wyjaśnił kolegom zasady sterowania lotnią.",
                "3. Brała / brał udział w składaniu i rozkładaniu lotni i przygotowaniu jej do lotów. Prawidłowo założyła / założył i przypięła / przypiął uprząż do lotni.",
                "4. Wykonała / wykonał ćwiczenia przygotowawcze do wstępnego szkolenia w pilotażu lotni (rozbieg i dobieg z lotnią, utrzymanie lotni w łożu wiatru, lot latawcowy na uwięzi).",
            ],
            group="Lotnicze",
        ),
        schemas.CreateBadge(
            name="DYŻURNY STARTU SPADOCHRONOWEGO **",
            description=[
                "1. Zna przepisy organizacji skoków spadochronowych w zakresie obowiązującym skoczków uczniów.",
                "2. Zna obowiązki dyżurnego startu spadochronowego i zrzutowiska, a także obowiązki i zakres uprawnień osób funkcjonujących na starcie spadochronowym.",
                "3. Zna wszystkie obowiązujące znaki i sygnały używane podczas prowadzenia skoków spadochronowych.",
                "4. Potrafi w terenie i na podstawie mapy dokonać wyboru lądowiska i zrzutowiska oraz określić, jakim powinno odpowiadać warunkom.",
                "5. Pełniła / pełnił obowiązki dyżurnego lub pomocnika dyżurnego na starcie spadochronowym lub zrzutowisku, wykładała / wykładał znaki, dokonywała / dokonywał pomiaru wiatru anemometrem, określała / określał jego kierunek meteorologiczny i nawigacyjny.",
            ],
            group="Lotnicze",
        ),
        # STRAŻACKIE (3)
        schemas.CreateBadge(
            name="STRAŻAK *",
            description=[
                "1. Zna stopnie Państwowej Straży Pożarnej oraz stopnie funkcyjnych Ochotniczej Straży Pożarnej.",
                "2. Potrafi wymienić podstawowe przyczyny powstawania pożarów.",
                "3. Potrafi szybko ubrać się w osobiste uzbrojenie strażaka.",
                "4. Zna rodzaje i wyposażenie węży oraz sprzęt do ich obsługi i zasady konserwacji.",
                "5. Wspólnie z zastępem budowała/budował linię wężową.",
            ],
            group="Strażckie",
        ),
        schemas.CreateBadge(
            name="MECHANIK SPRZĘTU POŻARNICZEGO **",
            description=[
                "1. Zna zasady działania, budowę i obsługę motopompy.",
                "2. Sprawnie posługuje się gaśnicą, hydronetką, kocem gaśniczym, bosakiem, sprzętem burzącym i tłumicą.",
                "3. Potrafi wymienić środki transportowe używane przez straże pożarne.",
                "4. Potrafi rozwinąć skróty określeń samochodów strażackich.",
                "5. Potrafi udzielić pierwszej pomocy w przypadku oparzenia i porażenia prądem.",
            ],
            group="Strażckie",
        ),
        schemas.CreateBadge(
            name="STRAŻAK RATOWNIK ***",
            description=[
                "1. Potrafi zebrać informacje o stanie zaopatrzenia miejscowości w wodę oraz ustalić najdogodniejsze miejsce na ustawienie motopompy.",
                "2. Zna rodzaje prądów gaśniczych wodnych.",
                "3. Kierowała / kierował budową linii wężowej oraz gaszeniem przez zastęp ognia podczas ćwiczeń.",
                "4. Ukończyła / ukończył kurs pierwszej pomocy.",
                "5. Prowadziła / prowadził służbową korespondencję radiową używając kryptonimów.",
            ],
            group="Strażckie",
        ),
        # HARCERSKA SŁUŻBA GRANICZNA (3)
        schemas.CreateBadge(
            name="STRAŻNICZKA GRANICY / STRAŻNIK GRANICY *",
            description=[
                "1. Zna podstawowe zadania Straży Granicznej i jej strukturę.",
                "2. Zna numer telefonu najbliższej jednostki Straży Granicznej.",
                "3. Zna przebieg linii granicy w rejonie zamieszkania i potrafi wskazać jej charakterystyczne punkty.",
                "4. Potrafi skrycie obserwować innych (samemu nie będąc widzianym). Sporządzła/ sporządził meldunek z zaobserwowanych zdarzeń.",
                "5. Potrafi wymienić nazwy kilku miejscowości na terytorium państwa sąsiedniego w pobliżu swojego miejsca zamieszkania.",   
            ],
            group="Harcerska służba graniczna",
        ),
        schemas.CreateBadge(
            name="TROPICIEL ŚLADÓW **",
            description=[
                "1. Umie rozpoznawać ślady ludzi, określając przy tym: ich wiek, kierunek marszu, długość kroku i sposób poruszania się.",
                "2. Przeprowadziła / przeprowadził wywiad z funkcjonariuszem Straży Granicznej na temat rozpoznawania i zabezpieczania śladów.",
                "3. Przeprowadziła / przeprowadził w terenie zajęcia dla zastępu z rozpoznawania śladów.",
                "4. Samotnie spędziła / spędził w terenie 8 godzin, opisując ślady ujawnione na drogach dojazdu do linii granicy.",
                "5. Sporządziła / sporządził odlew gipsowy śladu człowieka.",   
            ],
            group="Harcerska służba graniczna",
        ),
        schemas.CreateBadge(
            name="POGRANICZNIK ***",
            description=[
                "1. Zna podział pogranicza (pas drogi granicznej, strefa nadgraniczna).",
                "2. Umie wymienić elementy służby granicznej.",
                "3. Zna strukturę Straży Granicznej.",
                "4. Potrafi wymienić nazwy przejść granicznych w swoim województwie.",
                "5. Zna podstawowe fakty z historii polskich formacji granicznych.",   
            ],
            group="Harcerska służba graniczna",
        ),
        # ŁĄCZNOŚCIOWE (6)
        schemas.CreateBadge(
            name="NASŁUCHOWIEC *",
            description=[
                "1. Scharakteryzowała / scharakteryzował międzynarodowy podział pasm radiowych i służby je użytkujące.",
                "2. Poznała / poznał zakresy amatorskich pasm KF i ich wewnętrzny podział oraz podstawowe wyrazy Q-kodu i podstawowe skróty służbowe.",
                "3. Poznała / poznał zasady budowy znaków rozpoznawczych i prefiksy minimum pięciu państw.",
                "4. Obsługiwała / obsługiwał odbiornik komunikacyjny, pełniła / pełnił dyżur nasłuchowy w pracy sieci i odebrała / odebrał kierowany doń radiogram.",
                "5. Dokonała / dokonał stu nasłuchów z co najmniej dziesięciu krajów.",   
            ],
            group="Łącznościowe",
        ),
        schemas.CreateBadge(
            name="RADIOOPERATORKA / RADIOOPERATOR **",
            description=[
                "1. Przeprowadziła / przeprowadził na stacji klubowej co najmniej dwadzieścia łączności.",
                "2. Poznała / poznał procedurę pracy amatorskiej, międzynarodowy system głoskowania, sposoby budowy znaków rozpoznawczych oraz pamięta prefiksy krajów sąsiadujących z Polską, krajów Unii Europejskiej oraz USA. Zna organizację krótkofalarstwa w Polsce.",
                "3. Pracowała / pracował w sieci służbowej łączności radiotelefonicznej i przekazała / przekazał co najmniej dwadzieścia radiogramów, zna procedurę pracy służbowej oraz sposób prowadzenia dokumentacji stacyjnej (radiogramy, log).",
                "4. Poznała / poznał zasady rozchodzenia się fal KF i UKF, wybrała / wybrał właściwe miejsce w terenie dla usytuowania anteny oraz dobrała / dobrał odpowiedni typ anteny w zależności od wymaganego zasięgu.",
                "5. Przygotowała / przygotował do pracy przenośną radiostację i przeprowadziła / przeprowadził szkolenie zastępu w tym zakresie.",   
            ],
            group="Łącznościowe",
        ),
        schemas.CreateBadge(
            name="RADIOTELEGRAFISTKA / RADIOTELEGRAFISTA ***",
            description=[
                "1. Odebrała / odebrał i nadała / nadał kluczem 60 znaków na minutę według PARIS.",
                "2. Poznała / poznał minimum 20 znaków Q-kodu oraz znaki służbowe dotyczące korespondencji radiowej.",
                "3. Nawiązała / nawiązał co najmniej 20 łączności telegrafią na radiostacji klubowej i przekazała / przekazał telegrafią co najmniej 10 radiogramów podczas pracy amatorskiej lub służbowej.",
                "4. Pracowała / pracował co najmniej raz z terenowego stanowiska (obóz, biwak), utrzymując łączność z wybranym korespondentem w macierzystej miejscowości.",
                "5. Wykonała / wykonał proste urządzenie telegraficzne, np. generator do nauki telegrafii, wykorzystała / wykorzystał je podczas swoich zajęć z zastępem.",   
            ],
            group="Łącznościowe",
        ),
        schemas.CreateBadge(
            name="ELEKTROTECHNIK **",
            description=[
                "1. Poznała / poznał zasady działania maszyn elektrycznych: prądnicy, transformatora, prostownika, akumulatora, silnika.",
                "2. Zna i stosuje się do przepisów BHP w pracy w zakresie prądów silnych",
                "3. Wykryła / wykrył − poszukując w systematyczny sposób − uszkodzenia w urządzeniach elektrycznych codziennego użytku (lampa, żelazko itp.), naprawiła / naprawił popsute urządzenie.",
                "4. Wykonała / wykonał poprawnie sama / sam lub w zespole aparat, urządzenie lub część instalacji elektrycznej, np. napęd elektryczny do modelu, oświetlenie na obozie.",
                "5. Nauczyła / nauczył młodszych kolegów obsługi lub naprawy prostego urządzenia elektrycznego.",   
            ],
            group="Łącznościowe",
        ),
        schemas.CreateBadge(
            name="RADIOAMATOR ***",
            description=[
                "1. Wykonała / wykonał prosty odbiornik nasłuchowy lub radiolokacyjny.",
                "2. Korzystała / korzystał z prostych schematów radiowych, wytłumaczyła / wytłumaczył na ich podstawie zasadę pracy urządzenia.",
                "3. Poznała / poznał zasady racjonalnej eksploatacji sprzętu elektronicznego, którym się posługuje, zademonstrowała / zademonstrował drużynie poprawną obsługę.",
                "4. Poznała / poznał i stosuje podstawowe zasady bezpieczeństwa w zakresie pracy ze sprzętem łączności.",
                "5. Poznała / poznał zasady miernictwa, posługując się miernikiem uniwersalnym i generatorem−falomierzem.",   
            ],
            group="Łącznościowe",
        ),
        schemas.CreateBadge(
            name="RADIOTROPICIELKA / RADIOTROPICIEL *",
            description=[
                "1. Startowała / startował w radiowych „łowach na lisa” i wytropiła / wytropił wszystkie ukryte nadajniki.",
                "2. Przeprowadziła / przeprowadził skuteczne radionamierzanie „lisa” i wykreśliła / wykreślił jego stanowisko na mapie. Oszacowała / oszacował błąd pomiaru.",
                "3. Zorientowała / zorientował mapę w terenie za pomocą radionamierzania na stacje radiofoniczne średnio- i długofalowe.",
                "4. Przeprowadziła / przeprowadził pokaz wykrywania nadajnika „lisa” w terenie.",
            ],
            group="Łącznościowe",
        ),
    ]

    for badge in badges:
        crud.create_badge(db, badge=badge)


#def init_groups(db: Session) -> None:
#    groups = [
#        schemas.CreateGroup(
#            name="Forward", number=7, szczep="Zielona Siódemka", city="Bydgoszcz"
#        )
#    ]
#
#    for group in groups:
#        crud.create_group(db, group=group)


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
