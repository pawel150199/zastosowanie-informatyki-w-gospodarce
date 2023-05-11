from sqlalchemy.orm import Session

from src import crud, schemas
from src.core.settings import settings


def init_badges(db: Session) -> None:

    badges = [
        #SPRAWNOŚCI SAMARYTAŃSKIE
        schemas.CreateBadge(name="HIGIENISTKA / HIGIENISTA *", description=["1. Założyła /założył opatrunek, nakleiła /nakleił plaster z opatrunkiem, zabandażowała /zabandażował kończynę, wykorzystała /wykorzystał do założenia opatrunku chustę trójkątną.","2. Zabezpieczyła / zabezpieczył się przed przeziębieniem, odmrożeniem.","3. Potrafi prawidłowo postąpić w przypadku skaleczenia, otarcia nogi, niewielkiego oparzenia, krwotoku z nosa, użądlenia przez pszczołę lub osę.","4. Zmierzyła / zmierzył temperaturę. Wie, jaka jest prawidłowa temperatura ciała.","5. Poznała / poznał alarmowe numery telefonów. Wie, kiedy i w jaki sposób należy z nich korzystać."], group="Samarytańskie"),
        schemas.CreateBadge(name="SANITARIUSZKA / SANITARIUSZ **", description=["1. Poznała/poznał zasady kompletowania apteczki. Skompletowała/skompletował apteczkę osobistą.","2. Potrafi prawidłowo postąpić w przypadku: krwotoku (np. z kończyny), stłuczenia, zaprószenia oka, omdlenia, konieczności unieruchomienia kończyny, konieczności udrożnienia górnych dróg oddechowych.","3. Pełniła / pełnił służbę samarytańską na wycieczce, biwaku lub obozie.","4. Prawidłowo sprawdziła /sprawdził tętno."], group="Samarytańskie"),
        schemas.CreateBadge(name="RATOWNICZKA / RATOWNIK ***", description=["1. Skompletowała / skompletował torbę pierwszej pomocy dla drużyny na rajd, wycieczkę lub biwak.","2. Wie, jak postąpić w przypadku zatrucia pokarmowego (substancjami chemicznymi, grzybami, zepsutą żywnością).","3. Potrafi udzielić pomocy w przypadku utraty przytomności. Ułożyła / ułożył poszkodowanego w pozycji bocznej bezpiecznej.","4. Umie zorganizować transport chorego. Zastosowała/zastosował różne sposoby przenoszenia rannych. Kierując patrolem noszowym, pokonała/pokonał kilka przeszkód (zejście do dołu, podejście pod górę, pokonanie ogrodzenia).","5. Brała / brał udział w zawodach w ratownictwie lub ratowniczej grze terenowej. Pełniła / pełnił służbę w ambulatorium obozowym lub podczas dużej imprezy, opiekowała/opiekował się chorym."], group="Samarytańskie"),
        schemas.CreateBadge(name="LIDER ZDROWIA ***", description=["1. Włączyła / włączył do swojego postępowania jak najwięcej elementów zdrowego stylu życia (np. zdrowe odżywianie, higiena nauki i pracy, zwalczanie stresu, uprawianie sportu).","2. Wskazała / wskazał rówieśnikom korzyści płynące ze zdrowego trybu życia.","3. Zorganizowała / zorganizował i przeprowadziła / przeprowadził z drużyną akcję promującą zdrowy tryb życia.","4. Potrafi wymienić metody i ośrodki leczenia uzależnienia od nikotyny, alkoholu i narkotyków.","5. Wykorzystuje posiadaną wiedzę na temat uzależnień − od nikotyny, alkoholu i narkotyków − w codziennym postępowaniu i kontaktach z innymi ludźmi."], group="Samarytańskie"),
        
        #SPRAWNOŚCI PRZYRODNICZE
        schemas.CreateBadge(name="PRZYRODNICZKA / PRZYRODNIK *", description=["1. Rozpoznała / rozpoznał po sylwetkach i liściach dziesięć drzew (np. dąb, brzozę, klon, leszczynę, wierzbę, topolę, lipę, sosnę, świerk, jodłę, modrzew).","2. Rozpoznała / rozpoznał na rysunku lub zdjęciu po pięć gatunków roślin i zwierząt chronionych występujących w Polsce.","3. Uczestniczyła / uczestniczył w wycieczce do lasu, ułożyła / ułożył i przedstawiła / przedstawił w zastępie pięć zasad zachowania się w lesie.","4. Samodzielnie lub z zastępem zasadziła/zasadził drzewko w pobliżu swojego domu, na działce lub przy szkole."], group="Przyrodnicze"),
        schemas.CreateBadge(name="PRZYJACIEL PRZYRODY **", description=["1. Wskazała / wskazał na mapie Polski parki narodowe oraz znajdujące się w okolicy (np. w gminie lub powiecie) rezerwaty przyrody, parki krajobrazowe i wybrane pomniki przyrody. Wyjaśniła / wyjaśnił cele, dla których je utworzono.","2. Uczestniczyła / uczestniczył w wycieczce do rezerwatu przyrody lub parku narodowego. Zachowywała / zachowywał się zgodnie z obowiązującym tam regulaminem.","3. Brała /brał udział w pracy na rzecz środowiska naturalnego, np. w parku, na szlaku turystycznym, podczas imprezy ekologicznej.","4. W swoim domu oszczędza wodę i energię elektryczną, dba o wykorzystanie surowców wtórnych."], group="Przyrodnicze"),
        schemas.CreateBadge(name="ZNAWCA PRZYRODY ***", description=["1. Skompletowała / skompletował biblioteczkę (książki, artykuły, foldery, adresy stron internetowych) o tematyce ekologicznej.","2. Poznała / poznał zasady ekologicznego obozowania. Zastosowała / zastosował je w praktyce.","3. Wzięła / wziął udział w akcji na rzecz ratowania lub ochrony środowiska naturalnego.","4. Przygotowała / przygotował i przeprowadziła / przeprowadził zbiórkę na temat znaczenia przyrody dla zdrowia człowieka oraz potrzeby jej ochrony przed zagrożeniami cywilizacyjnymi.","5. Zapoznała / zapoznał się z celami i działaniami kilku wybranych organizacji ekologicznych"], group="Przyrodnicze"),
        schemas.CreateBadge(name="EKOLOG (mistrzowska)", description=["1. Poznała / poznał systematykę roślin i zwierząt. Poznała / poznał rośliny i zwierzęta chronione w Polsce.","2. Przedstawiła / przedstawił w interesującej formie bogactwo polskich lasów oraz znaczenie lasów dla przyszłości człowieka na Ziemi.","3. Wskazała / wskazał występujące w polskich lasach zagrożenia dotyczące drzew, ptaków i zwierząt.","4. Poznała / poznał zasady ekologicznego obozowania. Zastosowała / zastosował je w praktyce.","5. Wyznaczyła / wyznaczył sobie dodatkowe zadania mistrzowskie."], group="Przyrodnicze"),
        schemas.CreateBadge(name="PRZYJACIEL ROŚLIN *", description=["1. Opiekowała / opiekował się roślinami w domu, w harcówce, w szkolnej pracowni lub na działce przez cały okres próby na sprawność.","2. Odwiedziła / odwiedził ogród botaniczny (była / był na łące, w lesie, w polu itp.) i opowiedziała / opowiedział na zbiórce o swoich obserwacjach dotyczących występującej tam roślinności.","3. Rozpoznała / rozpoznał na zdjęciach i w naturze po pięć roślin trujących, leczniczych, chwastów i zbóż.","4. Zna rośliny i owoce jadalne występujące w lesie. Przygotowała / przygotował z nich posiłek, np. podwieczorek dla zastępu."], group="Przyrodnicze"),
        schemas.CreateBadge(name="ZIELARKA / ZIELARZ **", description=["1. Prowadziła / prowadził zbiór roślin (zna kalendarz ich zbierania i wie, jakie części roślin należy zbierać). Zbiera, suszy i przechowuje rośliny tak, aby nie straciły swoich właściwości.","2. Przygotowała / przygotował do apteczki drużyny zestaw ziół oraz krótki opis sposobu ich stosowania.","3. Przygotowała / przygotował informację o wybranych 15 roślinach chronionych występujących w Polsce i przedstawiła/przedstawił ją na zbiórce zastępu, drużyny lub w klasie.","4. Przyrządziła / przyrządził ziołowy środek przydatny w leczeniu, kosmetyce lub gospodarstwie domowym.","5. Rozpoznała / rozpoznał grzyby jadalne i trujące."], group="Przyrodnicze"),
        schemas.CreateBadge(name="BOTANIK ***", description=["1. Przedstawiła / przedstawił na zbiórce drużyny wybrane gatunki występujących na świecie roślin zagrożonych wyginięciem („czerwona księga”).","2. Opowiedziała / opowiedział w drużynie o interesujących roślinach, występujących w rezerwacie lub parku narodowym w swojej okolicy.","3. Przedstawiła/przedstawił zastępowi lub drużynie swoje zbiory: albumy, atlasy i inne publikacje na temat roślin, zaprezentowała/zaprezentował ich zawartość.","4. Zorganizowała / zorganizował i poprowadziła / poprowadził wyprawę drużyny (lub klasy) w celu poznania środowiska roślinnego (np. lasu, łąki) lub wyprawę do ogrodu botanicznego albo muzeum przyrodniczego.","5. Wykonała / wykonał projekt przydomowego, działkowego lub przyszkolnego ogródka."], group="Przyrodnicze"),
        schemas.CreateBadge(name="KWIACIARKA / KWIACIARZ *", description=["1. W bukiecie 15 kwiatów rozpoznała / rozpoznał kwiaty ogrodowe, doniczkowe, polne i chwasty.","2. Wie, w jakich miesiącach i porach roku kwitną w Polsce poszczególne kwiaty.","3. Założyła / założył w czasie próby własny ogródek kwiatowy, np. na klombie, w doniczkach, na działce.","4. Ułożyła / ułożył bukiet z kwiatów lub przedstawiła / przedstawił na zbiórce foldery, zdjęcia i rysunki najciekawszych okazów."], group="Przyrodnicze"),
        schemas.CreateBadge(name="MIŁOŚNICZKA KWIATÓW / MIŁOŚNIK KWIATÓW **", description=["1. Ułożyła / ułożył bukiety ze świeżych kwiatów na różne okazje.","2. Wie, co to jest ikebana. Wykonała / wykonał kwiatową dekorację na wybraną uroczystość w rodzinie, szkole lub drużynie.","3. Zastosowała / zastosował suszone rośliny do wykonania różnych ozdób.","4. Pielęgnowała / pielęgnował w czasie próby rzadki lub trudny w uprawie okaz rośliny. Swoje doświadczenia z uprawy przedstawiła / przedstawił w zastępie.","5. Wie, jakie kwiaty można uprawiać w Polsce i jakie sprowadza się z zagranicy."], group="Przyrodnicze"),
        schemas.CreateBadge(name="LEŚNIK ***", description=["1. Śledziła/śledził życie lasu o różnych porach dnia i nocy, w tym tropiła/tropił zwierzęta, rozpoznawała/rozpoznawał ich legowiska i znała/znal jego zwyczaje.", "2. Wykazywała/wykazywał znajomość drzew i umiejętność ich rozpoznawania, np. podczas odbycia obchodu lasu z leśniczym.", "3. Zorganizowała/zorganizował zwiad lub wycieczkę do lasu dla młodszych członków zastępu lub drużyny, pokazując bogactwo lasu.", "4. Uczestniczyła/uczestniczył w pracach leśnych, takich jak prace w szkółce, oczyszczanie pasów przeciwpożarowych lub sadzenie drzew.", "5. Przedstawiła/przedstawił na zbiórce drużyny bogactwo polskich lasów oraz ich znaczenie dla człowieka na Ziemi, wskazując zagrożenia dla drzew, ptaków i zwierząt występujące w lasach."], group="Przyrodnicze"),
        schemas.CreateBadge(name="OGRODNICZKA / OGRODNIK ***", description=["1. Na zbiórce zastępu przedstawiła / przedstawił znaczenie gleby i nawożenia dla uprawy warzyw.","2. Rozpoznała / rozpoznał nasiona marchwi, pietruszki, sałaty, ogórków i buraczków. Wyhodowała/wyhodował własne rośliny z nasion i rozsady.","3. Przygotowała / przygotował kompost z odpadów ogrodniczych.","4. Zaplanowała / zaplanował siew i zbieranie plonów na działce lub w ogrodzie.","5. Przygotowała / przygotował wybrane warzywa do przechowania podczas zimy."], group="Przyrodnicze"),
        schemas.CreateBadge(name="SADOWNICZKA / SADOWNIK * * *", description=["1. Rozpoznała / rozpoznał po pniach i liściach popularne drzewa owocowe: jabłonie, grusze, śliwy, wiśnie, czereśnie.","2. Zerwała / zerwał i ułożyła/ułożył w skrzynce owoce, przygotowując je do trans-portu.","3. Przygotowała / przygotował owoce do składowania przez zimę.","4. Brała / brał udział w pielęgnacji sadu, szczepieniu drzewek i zabezpieczeniu go przed szkodnikami.","5. Przedstawiła/przedstawił na zbiórce zastępu lub drużyny zebrane przez siebie artykuły i poradniki dotyczące sadownictwa."], group="Przyrodnicze"),
        schemas.CreateBadge(name="PRZYJACIEL ZWIERZĄT *", description=["1. Wzięła / wziął udział w zimowym dokarmianiu dzikich zwierząt w najbliższych lasach oraz dowiedziała / dowiedział się, jakie zwierzęta należy pomagać.", "2. Rozpoznała / rozpoznał tropy dzikich zwierząt, takich jak dzik, sarna, zając.", "3. Poznała / poznał głosy pięciu różnych zwierząt, nagrywając je i odtwarzając na zbiórce drużyny po wycieczce do lasu, pola lub łąki.", "4. Obserwowała / obserwował życie zwierząt domowych przez miesiąc, zapisując najciekawsze spostrzeżenia i opowiadając o nich na zbiórce zastępu."], group="Przyrodnicze"),
        schemas.CreateBadge(name="ZNAWCA ZWIERZĄT * *", description=["1. Rozpoznała / rozpoznał na zdjęciach i rysunkach 15 gatunków zwierząt.","2. Przygotowała /przygotował informację o zwierzętach chronionych w Polsce oraz o zwierzętach niebezpiecznych zamieszkujących w Polsce i przedstawiła / przed-stawił ją na zbiórce zastępu lub drużyny.","3. Pomogła / pomógł w przetrwaniu zimy potrzebującym zwierzętom (ptakom, zwierzętom w lesie, bezdomnym psom).","4. Wie, jakie niebezpieczne zwierzęta żyją w Polsce. Opowiedziała / opowiedział koleżankom/kolegom, jak należy postępować w przypadku spotkania z nimi."], group="Przyrodnicze"),
        schemas.CreateBadge(name="ZOOLOG ***", description=["1.Przedstawiła / przedstawił wybrane gatunki zwierząt żyjących na całym świecie, zagrożonych wyginięciem („czerwona księga”).","2. Zna systematykę zwierząt. Przedstawiła / przedstawił na zbiórce lub na lekcji życie wybranego gatunku.","3. Zaprezentowała / zaprezentował zastępowi lub drużynie swoje zbiory: albumy, atlasy i inne publikacje na temat zwierząt, opowiedziała / opowiedział o ich zawartości.","4. Zorganizowała / zorganizował dla zastępu wyprawę do zoo, muzeum przyrodniczego lub lasu, opowiedziała / opowiedział o wybranych gatunkach zwierząt. Nauczyła / nauczył zastęp sposobów obserwacji zwierząt."], group="Przyrodnicze"),
        schemas.CreateBadge(name="PSZCZELARZ ***", description=["1. Od wiosny do jesieni pracowała / pracował w pasiece i prowadziła / prowadził notatnik swoich czynności.","2. Nauczyła / nauczył się zabezpieczać pszczoły przed zimą.","3. Potrafi postępować w przypadku użądlenia przez owady.","4. Opowiedziała / opowiedział na zbiórce o właściwościach leczniczych produktów wytwarzanych przez pszczoły.","5. Urządziła / urządził w harcówce, szkole lub w gminie wystawę wydawnictw dotyczących pszczelarstwa i produktów wytworzonych przez pszczoły."], group="Przyrodnicze"),
        schemas.CreateBadge(name="HODOWCA (GOŁĘBI, KRÓLIKÓW, RYBEK) **", description=["1. Przeczytała / przeczytał literaturę dotyczącą hodowli wybranych zwierząt.","2. Przygotowała / przygotował dla swoich zwierząt pomieszczenia i utrzymuje je w stałej czystości.","3. Zaprezentowała/zaprezentował na zbiórce zastępu wyhodowane przez siebie zwierzęta, opowiedziała/opowiedział o ich zwyczajach, sposobach żywienia i zapobiegania chorobom.","4. Zwraca uwagę osobom, które źle odnoszą się do zwierząt i ptaków."], group="Przyrodnicze"),

        #WYROBIENIE HARCERSKIE
        schemas.CreateBadge(name="ROBINSON **", description=["1. Przeprowadziła / przeprowadził w pobliżu obozu w samotności kilkugodzinną obserwację życia lasu o wschodzie Słońca.","2. W dowolnej formie udokumentowała / udokumentował swoje spostrzeżenia (zauważone zwierzęta i ich tropy, zjawiska przyrody, występujące rośliny chronione, jadalne itp.), zaprezentowała / zaprezentował je na zbiórce zastępu.","3. Przygotowała / przygotował dla zastępu posiłek, korzystając z zebranych owoców lasu.","4. Wraz z kolegą / koleżanką biwakowała / biwakował w pobliżu obozu przez 24 godziny."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="LEŚNY CZŁOWIEK ***", description=["1. Odbyła / odbył samotną wędrówkę po lesie (od świtu do zmroku), zdobyła / zdobył pożywienie z dziko rosnących roślin.", "2. Przeprowadziła / przeprowadził obserwacje i poznała / poznał różnorodność ekosystemów leśnych w Polsce.", "3. Przygotowała / przygotował prezentację multimedialną lub gawędę o ekologii lasu i przedstawiła / przedstawił ją na zbiórce zastępu, drużyny lub w klasie.", "4. Znajdując się w lesie, zbudowała / zbudował schronienie i zaprezentowała / zaprezentował swój sposób na przetrwanie w warunkach naturalnych.", "5. Poprowadziła / poprowadził wyprawę drużyny (lub klasy) po lesie, zwracając uwagę na najważniejsze cechy i zasady zachowania się w lesie."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="TRZY PIÓRA (mistrzowska)", description=["Przeszła / przeszedł pomyślnie trzy próby − milczenia, głodu i samotności − przez kolejne trzy doby: w czasie pierwszej doby powstrzymała / powstrzymał się od spożywania jakich-kolwiek pokarmów i napojów (z wyjątkiem czystej wody), uczestnicząc we wszystkich zajęciach obozowych, w czasie drugiej doby zachowała / zachował całkowite milczenie, trzecią dobę spędziła / spędził w lesie, niezauważona / niezauważony przez ludzi, żywiąc się pokarmem leśnym."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="HARCOWNIK *", description=["1. Uczestniczyła / uczestniczył w pięciu grach terenowych, przestrzegała / przestrzegał obowiązujących w nich zasad.","2. Poznała / poznał 10 ćwiczeń rozwijających spostrzegawczość, refleks, pamięć.","3. Uczestniczyła / uczestniczył razem z zastępem w zawodach, turnieju, meczu lub innej formie współzawodnictwa między zastępami.","4. Brała / brał udział w INO, grze ekologicznej lub biegu patrolowym."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="ORGANIZATORKA HARCÓW / ORGANIZATOR HARCÓW **", description=["1. Przeprowadziła / przeprowadził dziesięć gier terenowych i sportowych, ucząc kolegów zasad w nich obowiązujących.","2. Zorganizowała / zorganizował dla zastępu (drużyny) ćwiczenia typu „kim” w harcówce i w terenie.","3. Zorganizowała / zorganizował mecz, olimpiadę lub inne zawody między zastępami.","4. Prowadzi własny notatnik zawierający zbiór gier i ćwiczeń do wykorzystania w pomieszczeniu i w terenie."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="MISTRZYNI HARCÓW / MISTRZ HARCÓW ***", description=["1. Przedstawiła / przedstawił zestaw gier i ćwiczeń, zebranych w czasie próby.","2. Przeprowadziła / przeprowadził po kilkanaście gier terenowych i świetlicowych w drużynie (szczepie) lub dla dzieci spoza ZHP.","3. Przygotowała / przygotował trasę i program harcerskiego biegu terenowego, sprawdzającego znajomość technik harcerskich.","4. Nauczyła / nauczył młodszych kilku gier i ćwiczeń do wykorzystania na zbiórkach i w szkole."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="ZNAWCA OBRZĘDÓW I ZWYCZAJÓW DRUŻYNY *", description=["1. Poznała / poznał znaczenie słów „zwyczaje” i „obrzędy”.","2. Poznała / poznał historię swojej drużyny.","3. Dotarła / dotarł do kroniki lub kronik drużyny, przeczytała / przeczytał je.","4. Pozyskane informacje dotyczące zwyczajów swojej drużyny przedstawiła / przedstawił na zbiórce zastępu.","5. Poznała / poznał harcerskie piosenki śpiewane w drużynie, nauczyła / nauczył się ich."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="ZNAWCA ZWYCZAJÓW I TRADYCJI HARCERSTWA **", description=["1. Wie, jak powstała pieśń „Wszystko, co nasze”.","2. Wie, skąd wywodzi się tradycja pozdrowienia „czuwaj” i co ono oznacza. Przygotowała / przygotował krótką gawędę dla zastępu na ten temat.","3. Poznała / poznał harcerskie zwyczaje związane z ogniskiem, napisała/ napisał artykuł do gazetki hufca (drużyny, szkoły) o tych zwyczajach.","4. Zna pieśni obrzędowe, np. „Bratnie słowo”, „Płonie ognisko”. Nauczyła / nauczył młodszą harcerkę/młodszego harcerza tych pieśni.","5. Zorganizowała / zorganizował przedsięwzięcie dotyczące historii lub tradycji harcerstwa (dla harcerzy,społeczności lokalnej, koleżanek i kolegów w szkole)."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="BI-PI *", description=["1. Wie, co oznacza zwyczaj zawiązywania węzełka na chuście. Przestrzega tego zwyczaju.","2. Wie, do jakich organizacji skautowych należy ZHP oraz jakie są ich symbole (lilia i koniczyna). Zaprezentowała / zaprezentował je drużynie (np. w postaci prezentacji multimedialnej lub planszy do harcówki).","3. Poznała / poznał życiorys twórcy skautingu gen. Roberta Baden-Powella. Podczas zbiórki zastępu przedstawiła / przedstawił w dowolnej formie jedną z jego przy- gód."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="LILIA I KONICZYNA **", description=["1. Zna symbolikę skautowej lilijki i koniczynki, wie, jak wyglądają oraz jaka jest ich historia.","2. Wie, kiedy powstał skauting i kto go założył.","3. Wie, co oznaczają skróty WOSM i WAGGGS (nauczyła/nauczył się pełnej nazwy obu organizacji w języku angielskim).","4. Zdobyła / zdobył informacje o organizacji skautowej w wybranym kraju. Wybrane informacje przedstawiła / przedstawił na zbiórce drużyny","5. Wzięła / wziął udział w przygotowaniu zbiórki z okazji Dnia Myśli Braterskiej. Wysłała / wysłał kartkę z życzeniami do wybranej organizacji skautowej, drużyny lub skauta."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="ZNAWCA SKAUTINGU ***", description=["1. Zna historię skautingu − wie, jak powstał skauting i jak rozwinął się w ruch ogólnoświatowy.","2. Wie, na czym polega działanie światowych organizacji skautowych (WOSM i WAGGGS).","3. Zna najważniejsze organizacje skautowe działające w krajach europejskich.","4. Dobrze poznała / poznał wybraną organizację skautową − zna jej historię i współczesną działalność, nawiązała / nawiązał kontakt ze skautami tej organizacji.","5. Samodzielnie przygotowała / przygotował zbiórkę na temat skautingu."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="RZECZNICZKA DRUŻYNY / RZECZNIK DRUŻYNY ***", description=["1. Zdobyła / zdobył podstawową wiedzę dotyczącą przekazu informacji, dowiedziała / dowiedział się, jak należy formułować informacje.","2. Zredagowała / zredagował kilka ogłoszeń lub informacji związanych z działalnością drużyny, wywiesił je w szkole, w hufcu lub zamieścił na stronie internetowej drużyny.","3. Napisała / napisał artykuł o drużynie do lokalnego pisma (wychodzącego w mieście, gminie lub powiecie).","4. Systematycznie pisze artykuły o drużynie do gazetki hufca (gazetki szkolnej) lub zamieszcza teksty na stronie internetowej drużyny."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="RZECZNIK HARCERSTWA (mistrzowska)", description=["1. Przeczytała / przeczytał trzy pozycje książkowe dotyczące przekazywania informacji.","2. Poznała / poznał specyfikę strony internetowej ZHP, śledziła / śledził na bieżąco informacje dotyczące ZHP.","3. Napisała / napisał artykuł do lokalnej gazety o przebiegu dowolnego przedsięwzięcia hufca, chorągwi.","4. Zaprosiła / zaprosił lokalnych dziennikarzy i opiekowała / opiekował się nimi w czasie imprezy hufca.","5. Ukończyła / ukończył warsztaty dziennikarskie. Uczestniczy w pracach zespołu promocji i informacji w hufcu lub w chorągwi."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="ZNAWCA MUSZTRY **", description=["1. Zapoznała / zapoznał się z zasadami musztry.","2. Nienagannie wydaje i wykonuje komendy.","3. Przeprowadziła / przeprowadził zajęcia z musztry z zastępem lub drużyną.","4. Brała / brał udział w pokazie musztry zastępu, drużyny lub obozu."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="MISTRZYNI MUSZTRY / MISTRZ MUSZTRY ***", description=["1. Poznała / poznał regulamin musztry i ceremoniału harcerskiego, przestrzega go.","2. Przygotowała / przygotował drużynę do uroczystości na placu, ucząc musztry i dopilnowując regulaminowego umundurowania.","3. Przeprowadziła / przeprowadził pokaz musztry drużyny.","4. Przeprowadziła / przeprowadził szkolenie zastępowych z zakresu musztry."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="WARTOWNICZKA / WARTOWNIK **", description=["1. Zna i stosuje zasady służby wartowniczej ZHP.","2. Pełniła/pełnił bez zarzutu służbę wartowniczą łącznie przez 12 godzin w nocy i 8 godzin w dzień.","3. Pełniła / pełnił wartę na posterunku honorowym podczas trwania uroczystości.","4. Wie, jakie znaczenie ma służba wartownicza dla bezpieczeństwa osób i mienia znajdującego się na terenie obozu (biwaku).","5. Brała / brał udział w przynajmniej pięciu grach doskonalących czujność, spostrzegawczość itp."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="DOWÓDCA WARTY ***", description=["1. Zdobyła / zdobył sprawność „wartownika”.","2. Pełniła / pełnił funkcję dowódcy warty (instruktora służbowego na obozie, biwaku). Pokierowała / pokierował budową wartowni obozowej.","3. Potrafi rozstawić wartowników, dokonać zmiany warty. Dokonała / dokonał zmiany wartowników na posterunku honorowym podczas trwania uroczystości.","4. Zorganizowała / zorganizował co najmniej pięć gier doskonalących czujność oraz spostrzegawczość.","5. Opiekowała/opiekował się harcerką/harcerzem zdobywającą/zdobywającym sprawność „wartownika”."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="OGNIK *", description=["1. Zapoznała / zapoznał się ze znaczeniem odkrycia i poskromienia ognia.","2. Pod opieką zastępowej / zastępowego ułożyła / ułożył ognisko i rozpaliła / rozpalił je.","3. Pełniła / pełnił funkcję strażnika ognia.","4. Zna gatunki drewna odpowiedniego do budowania ognisk harcerskich.","5. Zatarła / zatarł ślady ogniska po jego wygaszeniu, zabezpieczyła / zabezpieczył zapałki przed zamoknięciem."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="STRAŻNICZKA OGNIA / STRAŻNIK OGNIA **", description=["1. Pełniła / pełnił trzy służby przy ognisku, umiejętnie podkładając drwa lub gałęzie, regulując wysokość płomienia i ograniczając iskrzenie.","2. Poznała / poznał przepisy przeciwpożarowe na obozach i biwakach. Dowiedziała / dowiedział się, jak ugasić na człowieku płonące ubranie. Nauczyła / nauczył się posługiwać podstawowym sprzętem gaśniczym.","3. Poprawnie zbudowała / zbudował podstawowe stosy ogniskowe.","4. Poznała / poznał obrzędowość związaną z harcerskim ogniskiem.","5. Rozróżnia trzy podstawowe stopnie oparzenia i potrafi udzielić pierwszej pomocy w przypadku oparzenia."], group="Wyrobienie Harcerskie"),
        schemas.CreateBadge(name="MISTRZYNI OGNISK / MISTRZ OGNISK ***", description=["1. Rozpoznaje różne gatunki drewna. Wie, czym się charakteryzują i jak się palą.","2. Wygłosiła/wygłosił gawędę na temat ognia i zasad zachowania się przy ognisku harcerskim.","3. Przygotowała / przygotował strażników ognia do pełnienia obowiązków przy ognisku.","4. Poznała / poznał różne rodzaje stosów ogniskowych, nauczyła / nauczył się je układać.","5. Nauczyła / nauczył się rozpalać ognisko w trudnych warunkach atmosferycznych (wiatr, deszcz, śnieg)."], group="Wyrobienie Harcerskie"),
    ]

    for badge in badges:
        crud.create_badge(db, badge=badge)


def init_groups(db: Session) -> None:
    groups = [
        schemas.CreateGroup(name="Forward", number=7, szczep="Zielona Siódemka", city="Bydgoszcz")
    ]

    for group in groups:
        crud.create_group(db, group=group)
        

def init_users(db: Session) -> None:
    users = [
        schemas.CreateUser(
            first_name="admin",
            last_name="admin",
            email="admin@harcownik.com",
            level="admin", function="admin",
            password="admin",
            group_id=1,
            badge_id=1
        )
    ]

    for user in users:
        crud.create_user(db, user=user)