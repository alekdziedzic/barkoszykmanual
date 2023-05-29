import streamlit as st
from PIL import Image
import pandas as pd


st.set_page_config(page_title="Bar Koszyki", page_icon=Image.open("logo.png"))

def main():
    st.title("Bar koszyki - manual")
    submenu = st.sidebar.selectbox("Menu", ["Manual Koktajli", "Manual Alkoholi", "Piwo", "Wino"])
    if submenu == "Manual Koktajli":
        st.header("Manual Koktajli")

        df = pd.read_csv("koktajle.csv", sep=";", encoding ="Windows-1250")
        for index, row in df.iterrows():
            expand = st.expander(f"**{row['nazwa']}** _({row['tagi']})_")
            expand.write((row["receptura"]).replace(",", "<br>"), unsafe_allow_html=True)
            expand.image("CocktailImages/" + row["zdjecie"])
            expand.write(f"Metoda: {row['Metoda']}")
            if row['Lód'] == "0":
                pass
            else:
                expand.write(f":blue[Lód]: {row['Lód']}")

            expand.write(f":green[Szkło]: {row['Szkło']}")

            if row['Garnish'] == "0":
                pass
            else:
                expand.write(f":violet[Garnish]: {row['Garnish']}")

        st.caption(":grey[Materiały: Adrian Kot, Edycja: Aleksander Dziedzic]")
    elif submenu == "Manual Alkoholi":
        st.header("Manual Alkoholi")

        aberlour = st.expander("**Aberlour** _(Whisky, Szkocja, Single malt, Speyside)_")
        aberlour.caption('''Nazwa „Aberlour” wywodzi się z języka gaelickiego i oznacza „ujście szczebiocącego strumienia”.
        W Szkocji jest to miejsce gdzie górski potok Lour spotyka się z rzeką Spey. To właśnie tej
        wyjątkowo miękkiej wodzie Aberlour zawdzięcza swój niepowtarzalny styl. Pewnego mistycyzmu
        dodaje fakt, iż destylarnia została wybudowana nieopodal studni Św. Drostana – nieocenionego
        źródła krystalicznie czystej wody. Historia tejże studni sięga tysiąca lat wstecz, kiedy to stanowiła
        święte miejsce dla Druidów czczących duchy wody i dębu. W późniejszych czasach wodą z tej
        właśnie studni Święty Drostan chrzcił pierwszych na tych ziemiach Chrześcijan.''')

        aberlour.subheader("Aberlour 12")
        aberlour.write('''Dojrzewa 12 lat w beczkach po burbonie i po sherry oloroso. Następnie whisky jest ze sobą
        mieszana w proporcjach 1 do 1.''')

        aberlour.image("AlcoholImages/aberlour/aberlour12.jpg")

        aberlour.write('''**Aromat**: bogaty i zbalansowany, gruszki, jabłka, suszone śliwki, orzechy włoskie, wióry dębowe i
        oddech ziemi po deszczu.<br>
        **Smak**: gorzka czekolada, cynamon, imbir, nuty sherry.<br>
        **Finisz**: rozgrzewający, początkowo słodki, po chwili pikantny z nutami mięt.<br>''', unsafe_allow_html=True)

        aberlour.subheader("Aberlour 16")
        aberlour.write('''Aberlour 16yo to szkocka whisky single malt pochodząca z regionu Speyside. Double cask
        matured oznacza, że dojrzewa w dwóch rodzajach beczek: po bourbonie oraz po sherry Oloroso.
        Beczka po bourbonie nadaje whisky słodki, waniliowy smak, zaś Oloroso nuty korzenne i
        owocowe. Kiedy destylaty z obydwu beczek osiągną pożądany wiek, zostają ze sobą
        wymieszane, dzięki czemu uzyskiwana whisky zyskuje bogatszy smak i aromat.''')

        aberlour.image("AlcoholImages/aberlour/aberlour16.jpg")

        aberlour.write('''**Oko**: bursztynowa<br>
        **Nos**: 21 – przyjemna, lotna, ale nie ostra, potężne suszone owoce, śliwki, morele, czekolada.<br>
        **Usta**: 21 – średnio oleista i delikatna<br>
        **Finisz**: 20 – słodka, czekolada mleczna, orzechy, lekko pieprzna, trwająca.<br>
        **ABV**: 40%''', unsafe_allow_html=True)

        aberlour.subheader("Aberlour 18")
        aberlour.write('''To szkocka whisky single malt pochodząca z regionu Speyside. Double cask matured oznacza, że
        dojrzewa w dwóch rodzajach beczek: po bourbonie 70% oraz po sherry Oloroso 30%. Beczka po
        bourbonie nadaje whisky słodki, waniliowy smak, zaś Oloroso nuty korzenne i owocowe. Kiedy
        destylaty z obydwu beczek osiągną pożądany wiek, zostają ze sobą wymieszane, dzięki czemu
        uzyskiwana whisky zyskuje bogatszy smak i aromat. Podstawowym założeniem destylarni jest to
        aby w ich whisky dominowała nuta jabłka i czarnej porzeczki, zaś smak zboża powinien zostać
        zneutralizowany.
        18 lat w beczkach po bourbonie i po sherry Oloroso nada zdecydowanie innej słodyczy niż
        uraczyć możemy w młodszych edycjach. Aberlour 18 YO jest jedwabisty i maślany w smaku, ale i
        dębinowy. Podniebienia koneserów na pewno pozytywnie przyjmą tą whisky.''')

        aberlour.image("AlcoholImages/aberlour/aberlour18.jpg")

        aberlour.write('''**Aromat**: bogaty i pełny, mleczna czekolada, toffi, brzoskwinie, gorzkie pomarańcze, nuty sherry i
        dębu.<br>
        **Smak**: bogaty i zrównoważany, soczyste morele, cynamon, gałka muszkatołowa, ślady dębu i
        wytrawionej skóry.<br>
        **Finisz**: niezwykle długi, crème brulèe i w końcówce dębowa goryczka.''', unsafe_allow_html=True)

        aberlour.subheader("Aberlour A’bunadh")
        aberlour.write('''A'Bunadh (z gaelickiego “pochodzenie”) to whisky z destylarnia Aberlour, próbująca oddać
        charakter whisky z końca XIX wieku. Wiąże się z nią ciekawa historia. Ponoć podczas remontu
        destylarnii w 1975 roku, znaleziono kapsułę czasu zamurowaną za tabliczką z nazwą destylarni.
        Składała się ona z butelki whisky z 1898 roku, zawiniętą w gazetę z tegoż samego roku z
        artykułem o pożarze w destylarnii. Bytelka została w czterech piątych skonsumowana podczas
        przerwy śniadaniowej przez robotników, reszta zaś została wysłana na badania w laboratorium.
        A'Bunadh jest właśnie wzorowana na tym znalezisku. Cask Strength składający się z destylatów,
        dojrzewających w beczkach po sherry oloroso, o wieku od pięciu do dwudziestu pięciu lat.''')

        aberlour.image("AlcoholImages/aberlour/aberlour_abunadh.jpg")

        aberlour.write('''**Oko**: bursztynowa<br>
        **Nos**: 21 – kremowa, słodka i czekoladowa, podszyta znamiennymi dla Aberlour suszonymi
        owocami.<br>
        **Usta**: 21 – oleista i delikatna<br>
        **Finisz**: 22 – dobrze wyważona, odrobina melasa, wyraźny wpływ sherry, szybko zdobywa cały
        język i trwa na nim długim czekoladowym finiszem i rodzynkową słodyczą. Mocno rozgrzewająca
        co w mocy ponad 60% ABV nie jest żadnym zaskoczeniem.<br>
        **ABV**: 60,2%''', unsafe_allow_html=True)

        aberlour.subheader("Aberlour A’bunadh Alba")
        aberlour.write('''W odróżnieniu od klasycznej wersji Aberlour A’Bunadh wprowadzonej w 2019 roku edycja Alba
        leżakowała w zdecydowanej większości w wyselekcjonowanych beczkach po bourbonie 100% z
        1-go napełnienia , a w niewielkim tylko stopniu w typowych dla marki beczkach po sherry oloroso.
        Do słodowania wykorzystano lokalny jęczmień ze Speyside. Butelkowana z mocą beczek, każdy
        batch z inna mocą. Niefiltrowana na zimno dzięki czemu zachowuje całe aromatyczne bogactwo i
        pełniejszy smak o charakterystycznej, lekko kremowej teksturze.''')

        aberlour.image("AlcoholImages/aberlour/aberlour_abunadh_alba.jpg")

        aberlour.write('''**Aromat**: słodkie owoce sadu – świeże, zielone jabłka i soczyste gruszki, uzupełnione delikatnymi
        akordami lawendowego miodu, gładkiego kremu waniliowego i orzeźwiającego sorbetu
        cytrynowego.<br>
        **Smak**: pikantnie cytrusowy początek, przechodzący w bogaty akcent maślanych ciasteczek i
        pieczonych
        jabłek, który ustępuje słodkim migdałom w cukrze.<br>
        **Finish**: gładki i słodki, z nutą prażonych migdałów.''', unsafe_allow_html=True)

        absolut = st.expander("**Absolut** _(Wódka, Szwecja, Zboże Ozime)_")
        absolut.caption('''Główne składniki Absolut Vodka to woda i zboże ozime. Woda jest czerpana ze studni głębinowej
        w Åhus, szczelnie chronionej przed wszelkimi zanieczyszczeniami. Pszenicę ozimą wyróżnia od
        innych upraw to, że jest siana jesienią o tej samej porze, ale zbierana dopiero w następnym roku. Zboże rośnie pod
        szwedzkim śniegiem, rozwijając twarde ziarna, a zastosowanie nawozów jest zminimalizowane.''')
        absolut.subheader('Absolut')
        absolut.image('AlcoholImages/absolut/absolut.jpg')
        absolut.write('''**:blue[Smak]**: wyrazisty, pełny i wielowymiarowy, a jednocześnie gładki i aksamitny, z wyrazistą nutą
        ziarna i wyczuwalnym na zakończenie akcentem suszonych owoców.''')

        absolut.subheader('Absolut Pears')
        absolut.write('''Produkowana wyłącznie na bazie naturalnych składników i w odróżnieniu od
        innych wódek smakowych w ogóle nie zawiera cukru. Absolut Pears smakuje jak świeże,
        delikatne, dojrzałe gruszki z długim owocowym posmakiem na zakończenie.''')
        absolut.image('AlcoholImages/absolut/absolut_pears.jpg')

        absolut.subheader('Absolut Elyx')
        absolut.write('''Jest ręcznie destylowana w miedzianej kadzi z 1921 roku, obsługiwanej przez
        wyselekcjonowaną grupę rzemieślników, spadkobierców wiedzy i ekspertyzy przekazanej przez
        całe pokolenia wytwórców szwedzkiej wódki. Dzięki niezwykłym właściwościom miedzi, z której
        wykonano naszą kadź, powstaje naturalnie oczyszczona wódka o wysoko cenionej jedwabistej
        konsystencji i smaku.''')
        absolut.image('AlcoholImages/absolut/absolut_elyx.jpg')
        absolut.write('''**:blue[Nos]**: Czysty, bogaty i pełny zapach świeżego chleba z nutą białej czekolady i zboża z delikatnym
        pikantnym akcentem.<br>
        **:blue[Paleta]**: Pełna i jedwabista z posmakiem orzechów makadamii, zboża z nutą białej maślanej
        czekolady i świeżo upieczonego chleba. Lekka nuta świeżych orzechów z odrobiną pikantnych
        ziół i doskonale wyważony pełny smak.<br>
        **:blue[Finisz]**: Delikatny pikantny smak ze świeżym orzechowym akcentem i świetnie wyważonym
        gładkim finiszem.''' , unsafe_allow_html=True)

        absolut.subheader("Absolut Extrakt")
        absolut.write('''Wyrazisty i przepyszny, łączący w sobie jedyną w swoim rodzaju wódkę
        Absolut z ciepłym, pikantnym smakiem zielonego kardamonu. Jest on ukoronowaniem
        szwedzkiej historii, stanowiąc nowoczesne wydanie tradycyjnego szwedzkiego sznapsa.''')
        absolut.image('AlcoholImages/absolut/absolut-extrakt.png')

        amaretto = st.expander("**Amaretto** _(Likier, Włochy)_")
        amaretto.write('''Ciemnobrązowy włoski likier o gorzkim smaku i zapachu migdałów.
        Kompozycja zawiera winogrona, migdały orzechy (lub nasion moreli), wanilia, przyprawy i zioła.
        Tradycyjny obszar produkcji - miasto Saronno, położony w prowincji Lombardii. Nazwa
        „Amaretto” pochodzi od włoskiego słowa „Amaro”, co tłumaczy się jako „lekko gorzki”.''')
        amaretto.image('AlcoholImages/amaretto.jpg')

        averna = st.expander("**Amaro Averna** _(Likier, Włochy)_")
        averna.caption('''Averna to włoski likier z rodziny bitterów (gorzkawy, ziołowy likier) pochodzący z Caltanissetty na
        Sycylii. Nazwa trunku pochodzi od Salvatore Averna, który w 1868 roku zaczął wytwarzać likier o
        właściwościach terapeutycznych i tonizujących. Jego receptura pochodzi od mnichów z Zakonu
        Cystersów i została przekazana Salvatore w podziękowaniu za hojne darowizny na rzecz
        opactwa.''')
        averna.write('''Averna powstaje z olejków eterycznych cytryny i pomarańczy, granatu, które dodawane są do
        alkoholu bazowego. Po długotrwałej maceracji dodawany jest karmel.
        Głęboki rdzawy brąz. Nuty coli, skórki pomarańczowej, lukrecji i wanilii. Słodki z delikatną i
        subtelną goryczką. Jest kwaśniejsza od Amaro Lucano.''')
        averna.image('AlcoholImages/averna.jpg')

        lucano = st.expander("**Amaro Lucano** _(Likier, Włochy)_")
        lucano.caption('''tworzony jest według starej tajnej receptury, przekazywanej z pokolenia
        na pokolenie. Receptura likieru Amaro Lucano po dzisiejszy dzień pozostaje tajemnicą rodziny
        Vena. Dzięki umiejętnemu mieszaniu ponad 30 rodzajów ziół między innymi aloesu ferox, korzenia
        arcydzięgla, gorzkiej pomarańczy, bzu czarnego, goryczki, krwawnika piżma, szałwii, piołunu.
        Likier tworzony jest z dokładnie wybieranych najlepszych ziół.''')
        lucano.write('''Proces przygotowania dzieli się na siedem etapów: selekcję, infuzję, przetwarzanie, sekret,
        kontrolę, mieszanie i butelkowanie. Zioła są naturalnie suszone i rozdrabnianie. W procesie
        produkcji likieru uczestniczy woda, cukier, czysty alkohol i karmel. Kolor mahoniowy. <br>
        **:blue[Smak]**: Średnia słodycz z ziołową goryczką i nutami cynamonu, lukrecji i karmelu.''', unsafe_allow_html=True)
        lucano.image('AlcoholImages/lucano.jpg')

        monte = st.expander("**Amaro Montenegro** _(Likier, Włochy)_")
        monte.caption('''Wyprodukowany po raz pierwszy w 1885 roku w Bolonii.''')
        monte.write('''Składa się z najrzadszych i najcenniejszych ziół, czemu zawdzięcza swój wyjątkowy smak. W nosie 
        wyczuwalna skórka pomarańczy, suszona kolendra, wiśnie i świeży ogórek. W smaku początkowo słodki, 
        lecz szybko zmienia się w lekką goryczkę z nutą cytrusów.''')
        monte.image('AlcoholImages/amaromontenegro.png')

        ardbeg = st.expander("**Ardbeg 10** _(Whisky, Szkocja, Single malt, Islay)_")
        ardbeg.caption('''Ardbeg znajduje się na południowym wybrzeżu Islay. Destylarnia powstała w 1815 chociaż alkohol
        w tym miejscu destylowano nielegalnie już od ponad 20 lat. Destylarnia często zmieniała
        właścicieli i miała dużo przerw w produkcji. Z tego powodu była ona whisky bardzo cenioną, ale
        nie popularną. Prawdziwy renesans nastał dopiero w roku 1997 roku kiedy destylarnię Ardbeg
        wykupiła Glenmorangie. Rozpoczęto wtedy silną i przede wszystkim skuteczną promocję whisky,
        która pozwoliła na przywrócienie jej dawnego statusu gwiazdy z Islay. Zatorfienie Ardbeg wynosi
        około 50 ppm jest to zatem whisky bardzo torfowa. Jej torfowość jest jednak bardziej
        kontrolowana niż np. w bezpardonowo torfowym Laphroaig. Sekretem destylarni Ardbeg jest
        także „purifier” (jak okropnym słowem w języku polskim jest „oczyszczalnik!). Łabędzia szyja
        alembika połączona jest z jego dolną częścią. Oznacza to, że najmniej lotne związki, które dostają
        się do wyjścia z alembika są zawracane do ponownej destylacji. Nadaje to whisky nieco
        delikatniejszy profil i tłumaczy bardziej poskromiony charakter torfu.''')
        ardbeg.image('AlcoholImages/ardbeg.jpg')
        ardbeg.write('''**:blue[Aromaty]**: W pierwszej chwili torf, który jednak szybko ustępuje miejsca delikatniejszym aromatom. Miód,
        owoce i jodowe powietrze.<br>
        **:blue[Smak]**: Mocne uderzenie dymu, który łączy się silnym i przyjemnym finiszem za pośrednictwem wyraźnie
        wyczuwalnej pieprzności. W zrównoważony sposób przechodzi ona w przyjemny, silnie torfowy
        finisz, który trawa długo.''', unsafe_allow_html=True)


        bacardi = st.expander("**Bacardi** _(Rum, Kuba)_")
        bacardi.subheader("Bacardi OCHO")
        bacardi.write('''Dojrzewa przez 8 lat w beczkach dębowych. W jego wyrafinowanym bukiecie odnaleźć można
        akcenty suszonych śliwek, moreli, gałki muszkatołowej i wanilii.''')
        bacardi.image('AlcoholImages/bacardi/bacardi_ocho.jpg')
        bacardi.write('''**:blue[Aromat]**: delikatny z akcentami gruszek, jabłek, Świerzej trawy, tytoniu i ziela angielskiego. <br>
        **:blue[Smak]**: Słodki, z nutami starej skóry, suszonych śliwek, moreli, syropu klonowego, gaki
        muszkatołowej, wanilii. <br>
        **:blue[Finisz]**: długi, z nutami przypraw i dębiny.''', unsafe_allow_html=True)

        bacardi.subheader("Bacardi 10")
        bacardi.write('''Bacardi Gran Res Diez to rum na bazie melasy, dojrzewany przez 10 lat w mocno wypalanych
        dębowych beczkach po amerykańskim burbonie. Przed butelkowaniem poddany jest filtracji przez
        warstwę węgla drzewnego.''')
        bacardi.image('AlcoholImages/bacardi/bacardi10.jpg')
        bacardi.write('''**:blue[Aromat]**: wanilia, karmel, owoce, nuta dymu.<br>
        **:blue[Smak]**: wanilia, dębina, banany, gruszki, karmel.<br>
        **:blue[Finisz]**: długi z nutami dębiny.''', unsafe_allow_html=True)

        ballantines = st.expander("**Ballantines** _(Whisky, Szkocja, Blended/Single malt)_")
        ballantines.caption('''Ballantine’s to whisky typu blended, w której skład wchodzi ponad 40 rodzajów szkockich
         whisky z czterech regionów Szkocji: Speyside, Highlands, Islay oraz Lowlands. Na jej charakter szczególnie 
         wpływają whisky słodowe powstające w jednej z najstarszych destylarni w regionie Speyside, a mianowicie 
         Glenburgie nadającej mieszance smak jabłek i gruszek. Miltonduff – kolejna destylarnia uzupełnia Ballantine’s 
         o nuty kwiatowe, ziołowe oraz dodaje delikatną nutę wanilii. Z kolei malt whisky powstające w destylarni Scapa 
         nadają jej kremową słodycz.''')
        ballantines.subheader("Ballantine's Finest")
        ballantines.write('''Powstaje z 40 różnych whisky. SM wykorzystane w w jego kupażowaniu to: Glenburgie,
        Miltonduff i Scapa.''')
        ballantines.image('AlcoholImages/ballantines/ballantines_finest.jpg')
        ballantines.write('''**:blue[Nos]** – przyjemny, słodki, gruszkowy, zbożowy<br>
        **:blue[Smak]** – oleista, słodka, zbożowa, bez zbędnego alkoholu<br>
        **:blue[Finisz]** – zbożowa, słodkawa, czekoladowa, z mniej alkoholowym, ale bardzo gorzkim finiszem,
        który w dobrym humorze mógłbym nazwać czekoladowym.''', unsafe_allow_html=True)

        ballantines.subheader("Ballantine’s 12")
        ballantines.write('''Starszy przedstawiciel rodziny, którego kompozycja zawiera ponad czterdzieści składników, przy
        czym każdy dojrzewa w beczkach z białego amerykańskiego dębu przez okres minimum 12 lat. ''')
        ballantines.image('AlcoholImages/ballantines/ballantines12.jpg')
        ballantines.write('''**:blue[Aromat]**: owocowo-floralny, miód, wanilia, płatki zbożowe, jabłka, winogrona, gruszki, mieszanka
        orzechowa, ślady marcepanu i dębu.<br>
        **:blue[Smak]**: łagodny, orzeszki prażone w miodzie, wanilia, toffi, mleczna czekolada, cappuccino,
        agrest, jabłka, dąb i ulotna dymna nutka.<br>
        **:blue[Finisz]**: średnio długi, delikatny, z nutami miodu, wanilii, skórki pomarańczowej, orzechów
        włoskich, dębu i śladem torfu.''', unsafe_allow_html=True)

        ballantines.subheader("Ballantine’s 17")
        ballantines.write('''Szkocka whisky, złożona z destylatów słodowych i zbożowych o minimum 17-letniej maturacji''')
        ballantines.image('AlcoholImages/ballantines/ballantines17.jpg')
        ballantines.write(''' **:blue[Aromat]**: delikatnie dymny, miód, karmel, wanilia, grzanka z masłem, gruszki, rodzynki, dąb<br>
         **:blue[Smak]**: wanilia, toffi, miód, mleczna czekolada, karmel, pieczone jabłka i gruszki, cynamon, dąbi
        ulotna nutka dymu.<br>
         **:blue[Finisz]**: dość długi, z nutami miodu, walilii, suszonych ziół, odrobiną siana i tytoniu, dębu w
        mniejszym stopniu torfu.''', unsafe_allow_html=True)

        ballantines.subheader("Ballantine’s Glenburgie")
        ballantines.write('''Single malt starzony przez 15 lat w beczkach z białego dębu amerykańskiego.''')
        ballantines.image('AlcoholImages/ballantines/ballantines15.jpg')
        ballantines.write('''**:blue[Aromat]**: przyjemnie zbalansowany, jabłka, gruszki, śliwki, wanilia, miód, marcepan, landryny,
        mleczne krówki i odrobina skórki pomarańczowej.<br>
        **:blue[Smak]**: słodki, owocowy, pomarańcze, melon, jabłka, gruszka z masłem, miód, krem waniliowy,
        biała czekolada.<br>
        **:blue[Finisz]**: dość długi, słodki, wanilia, toffi, dżem pomarańczowy i jabłka.''', unsafe_allow_html=True)

        ballantines.subheader("Ballantine's The Miltonduff")
        ballantines.write('''Miltonduff jest sercem każdego ballantine’s. Single malt starzony przez 15 lat w beczkach z białego dębu amerykańskiego.''')
        ballantines.image('AlcoholImages/ballantines/ballantines_milton.jpg')
        ballantines.write('''**:blue[Aromat]**: jesienne liście, siano, bukiet suchych kwiatów, ślad lukrecji i cynamonu, szczypta pieprzu,
        suszone jabłka i lekka nutka migdałowa.<br>
        **:blue[Smak]**: łagodny, delikatne nuty floralne, trochę siana, szarlotka poprószona cynamonem, trawa
        cytrynowa, goździki i ślad lukrecji.<br>
        **:blue[Finisz]**: dość długi i pikantny, z nutą białego pieprzu, siana, trawy cytrynowej i suszonych jabłek.''', unsafe_allow_html=True)

        balvenie = st.expander("**Balvenie 14YO Caribbean Cask** _(Whisky, Szkocja, Single malt, Speyside)_")
        balvenie.caption('''Balvenie Distillery – destylarnia single malt whisky, znajdująca się w mieście Dufftown w Szkocji,
        w rejonie Speyside. Na początku 1892 roku rozpoczęto pracę nad przerobieniem XVIII wiecznej
        posiadłości (Balvenie New House) na destylarnię. Budynek ukończono w piętnaście miesięcy i 1
        maja 1893 w gorzelni Balvenie odbyła się pierwsza destylacja. Założycielem i długoletnim
        managerem był William Grant. Dziś destylarnia jest jednym z czołowych producentów szkockiej,
        znanym na całym świecie.''')
        balvenie.write('''Balvenie 14YO Caribbean Cask dojrzewa w tradycyjnych dębowych beczkach, następnie
        przelewana jest do beczek po rumie z Karaibów, gdzie nabiera dodatkowych nut zapachowych i
        smakowych.''')
        balvenie.image('AlcoholImages/Balvenie-14yo-Caribbean.jpg')
        balvenie.write('''**:blue[Zapach]**: Bogaty aromat owoców tropikalnych z dodatkiem kremowego toffi.<br>
        **:blue[Smak]**: Wanilia, nuty jabłek, mango oraz pomarańczy w tle.<br>
        **:blue[Finisz]**: Długi, kremowy i waniliowy.''', unsafe_allow_html=True)

        banks = st.expander("**Bank’s 5 blend** _(Rum, Blended)_")
        banks.write('''Rum Banks 5 to mieszanka 21 rumów, pochodzących z 6 różnych destylarni zlokalizowanych na 5
        wyspach - Trynidad, Jamajka, Gujana, Barbados i Jawa. Dojrzewały one od 3 do 12 lat w
        dębowych beczkach. W jego przyprawowo-owocowym bukiecie odnajdziemy także akcenty
        melasy, ziołowe, trawiaste, pieprzu, dębiny, zielonej herbaty, cytrusów.''')
        banks.image("AlcoholImages/banksblend.jpg")

        beefeater = st.expander("**Beefeater** _(Gin, Anglia, London dry)_")
        beefeater.subheader("Beefeater")
        beefeater.write('''Wytwarzany jest ze spirytusu zbożowego z dodatkiem 9 ziół i roślin: skórki z pomarańczy Sewilla,
        skórki z cytryny, jałowca, nasion kolendry, korzenia arcydzięgla, lukrecji, nasion arcydzięgla,
        korzenia irysa i migdałów. Początkowo składniki macerowane są w spirytusie, w miedzianych
        alembikach, następnie zawartość jest podgrzewana i następuje proces destylacji.''')
        beefeater.image('AlcoholImages/beefeater/beefeater.jpg')
        beefeater.write('''**:blue[Aromat]**: intensywny z nutami jałowca, cytrusów, lukrecji i arcydzięgla.<br>
        **:blue[Smak]**: wyraźny i mocny z nutami jałowca, skórki cytrusowej, pomarańczy i arcydzięgla.<br>
        **:blue[Finisz]**: średnio długi z wyraźnym akcentem jałowca''', unsafe_allow_html=True)

        beefeater.subheader("Beefeater 24")
        beefeater.write('''Wytwarzany jest ze spirytusu zbożowego z dodatkiem 12 ziół i roślin: japońskiej herbaty Sencha,
        chińskiej zielonej herbaty, skórki grejpfrutów, skórki z pomarańczy Sewilla, skórki z cytryny,
        jałowca, nasion kolendry, korzenia arcydzięgla, lukrecji, nasion arcydzięgla, korzenia irysa i
        migdałów. Gin nosi nazwę „24”, ponieważ wszystkie składniki, przed destylacją, są macerowane
        przez 24 godziny w spirytusie.''')
        beefeater.image("AlcoholImages/beefeater/beefeater24.jpg")
        beefeater.write(''' **:blue[Aromat]**: bogaty z nutami jałowca, kolendry, arcydzięgla, skórki cytrusowej, irysa, migdałów i
        azjatyckich herbat.<br>
         **:blue[Smak]**: intensywny z przewagą jałowca i nutami lukrecji, arcydzięgla, cytrusów, kolendry i
        pikantnych przypraw.<br>
         **:blue[Finisz]**: długi i wytrawny z posmakiem arcydzięgla, jałowca i cytrusów.''', unsafe_allow_html=True)

        bumbu = st.expander("**Bumbu** _(Rum/Spirit drink, Barbados/Panama)_")
        bumbu.subheader("Bumbu")
        bumbu.caption('''Bumbu Rum to doskonały rum rzemieślniczy butelkowany na Barbadosie, w skład którego
        wchodzą destylaty pochodzące z ośmiu różnych krajów : Barbadosu, Belize, Brazylii, Kostaryki,
        Dominikany, Salwadoru, Gujany i Hondurasu.
        Cała mieszanka dojrzewa przez okres 15 lat w beczkach używanych wcześniej do
        maturacji Bourbonu z Kentucky.
        Wyjątkowo czysta woda użyta do produkcji tego doskonałego trunku, oraz minerały zawarte w
        trzcinie cukrowej znacznie zwiększają jakość rumu i wpływają znacząco na paletę aromatyczno –
        smakową.''')
        bumbu.write('''Użyta trzcina cukrowa z Barbadosu zapewnia miękką i słodką teksturę oraz nuty wanilii i
        banana. Dzięki dodatkom naturalnych przypraw powstaje doskonały profil smakowy, który spełnia
        wymagania największych koneserów owego trunku.
        Mocno wyczuwalne są nuty banana, karmelu, cynamonu, orzechów, dębu i wanilii.''')
        bumbu.image('AlcoholImages/bumbu/bumbu-rum-the-original.jpg')

        bumbu.subheader('Bumbu XO')
        bumbu.caption('''Rum Bumbu XO produkowany jest w działającej od 120 lat panamskiej destylarni. Lokalnie
        zbierana trzcina cukrowa przetwarzana jest na melasę, która z kolei destylowana jest czystą wodą
        źródlaną. Wyprodukowany trunek dojrzewa potem 18 lat w zrobionych z białego dębu beczkach
        po bourbonie, a finiszowany jest przez krótki okres czasu w importowanych z Andaluzji beczkach
        po sherry – również wykonanych z białego dębu.''')
        bumbu.write('''Długi okres dojrzewania nadaje rumowi zapach, któremu trudno się oprzeć: charakterystyczne
        aromaty wanilii, palonego dębu oraz toffee. Smak natomiast zaskakuje prawdziwie egzotycznymi
        karaibskimi niuansami: wyczuwalne nuty kawy, przypraw i skórki pomarańczy.''')
        bumbu.image("AlcoholImages/bumbu/bumbu_xo.png")

        campari = st.expander("**Campari** _(Likier, Bitter, Włochy)_")
        campari.write('''Niezmienna do dziś, tajna receptura stworzona przez Gaspara Campari w 1860 roku z 60 ziół i
        innych botanikalsów.
        Rubinowo-czerwony kolor. Jasna gorzka pomarańcza zaokrąglona lekkimi nutami kwiatowymi i
        ziołową lesistością.''')
        campari.image("AlcoholImages/campari.jpg")

        capel = st.expander("**Capel Pisco** _(Pisco, Czile)_")
        capel.write('''Pisco jest destylowane z winogron gatunku Alexandria Muscatel. produkowany w miedzianych
        alembikach i butelkowany bez leżakowania jako owoc jednokrotnej destylacji. Pisco produkowane
        jest w tej chwili w Chile i Peru. Oba kraje toczą zacięty spór o pochodzenie tego alkoholu.
        Na nosie pisco jest świeże, lotne, winogronowe i cytrusowe, a na języku rozgrzewające, oleiste,
        pieprzne no i oczywiście mocno rozgrzewające''')
        capel.image('AlcoholImages/capel.jpg')

        chambord = st.expander("**Chambord** _(Likier, Francja)_")
        chambord.write('''Królewski likier na bazie koniaku z dodatkiem malin, jeżyn, miodu i wanilii, powstały ponoć w
        Dolinie Loary pod koniec XVII wieku.
        Dominują w nim słodko-kwaśne czerwone owoce (maliny, poziomki, porzeczki) oraz naturalnie
        skoncentrowane owoce leśne (zwłaszcza jeżyny), delikatnie żywiczne. Wyraźnie wyczuwalny jest
        miód, w tle nuty koniaku, wanilii i dębu.''')
        chambord.image('AlcoholImages/chambord.jpg')

        chat = st.expander("**Chartreuse** _(Likier, Francja)_")
        chat.subheader("Chartreuse Verte")
        chat.write('''Chartreuse to francuski likier 55% wytwarzany przez kartuskich mnichów od roku 1605. Składa
        się z destylowanego alkoholu (na bazie wina) leżakującego w dębowych beczkach ze 130
        ekstraktami ziołowymi a jego naturalnie zielony kolor pochodzi z chlorofilu.''')
        chat.image('AlcoholImages/chartreuse/verte.jpg')
        chat.subheader("Chartreuse Jaune")
        chat.write('''Francuski likier 40% wytwarzany przez kartuskich mnichów od roku 1605. Składa się z
        destylowanego alkoholu (na bazie wina) leżakującego w dębowych beczkach ze 130 ekstraktami
        ziołowymi. Jaśniejszy, żółty kolor wynika z użycia większej ilości miodu i szafranu. Smak bardziej
        miodowo-kwiatowy od verte.''')
        chat.image('AlcoholImages/chartreuse/jaune.png')

        chivas = st.expander("**Chivas** _(Whisky, Szkocja, Blended)_")
        chivas.subheader("Chivas regal 12")
        chivas.write('''Do jej wytworzenia wykorzystuje się 35 destylatów z różnych regionów Szkocji. Głównym
        składnikiem są destylaty z gorzelni Strathisla z regionu Speyside.''')
        chivas.image('AlcoholImages/chivas/chivas12.jpg')
        chivas.write(''' **:blue[Aromat]**: kremowy i maślany z nutami wanilii, anyżu, cytryn, toffi, banana, wiór dębowych i czarnej
        porzeczki.<br>
         **:blue[Smak]**: bogaty i kremowy z nutami banana, słodu jęczmiennego, ziela angielskiego, orzech
        włoskiego i karmelu.<br>
         **:blue[Finisz]**: lekki z nutami przypraw i słodkiego zboża.''', unsafe_allow_html=True)

        chivas.subheader("Chivas regal extra")
        chivas.write('''Kolekcja mistrza Chivasa Colina Scotta, który tym razem oparł formułę na komponentach
        starzonych w beczkach po sherry Oloroso przez 10 lat.''')
        chivas.image('AlcoholImages/chivas/chivas13.jpg')
        chivas.write(''' **:blue[Aromat]**: wyraźne nuty sherry, śliwki, pieczone jabłka, mleczna czekolada, karmel, nuty
        cynamonowe i orzechowe.<br>
         **:blue[Smak]**: miękki, karmel, marcepan, toffi,, cynamon, kandyzowany imbir i lekka goryczka dębu.<br>
         **:blue[Finisz]**: średnio długi, łagodny, z nutami kakao, karmelu, suszonych śliwek i dębowych tanin.''', unsafe_allow_html=True)

        chivas.subheader("Chivas Regal Mizunara")
        chivas.write('''Podstawą jest Chivas 12 z którego część destylatów finiszowana jest w beczkach z dębu
        japońskiego mizunara. Dąb mizunara jest porowaty, rośnie bardzo wolno, stąd też jest bardzo
        drogi i rzadko wykorzystywany w świecie whisky. Beczki są dodatkowo nacinane by zwiększyć
        oddziaływanie tanin beczki.''')
        chivas.image('AlcoholImages/chivas/chivas_mizunara.jpg')
        chivas.write('''**:blue[Aromat]**: słodki i owocowy, morele, mandarynki, kokos, miód, wanilia, orzechy włoskie, ślad ziół i
        tytoniu i lekka woń kwiatów jabłoni.<br>
        **:blue[Smak]**: owocowy z nutą pikantną, wanilia, orzeszki prażone w miodzie, morele, banany, wiórki
        kokosowe, kandyzowany imbir, szczypta pieprzu, cynamonu i lukrecji.<br>
        **:blue[Finisz]**: średnio długi, z nutami karmelu, toffi, wanilii, pieprzu i dębowych tanin.''', unsafe_allow_html=True)

        chivas.subheader("Chivas regal XV")
        chivas.write('''Starzona przez nie mniej niż 15 lat finiszowana w beczkach po koniaku pochodzących z dystryktu
        Grande Champagne.''')
        chivas.image('AlcoholImages/chivas/chivas15.jpg')
        chivas.write('''**:blue[Aromat]**: bogaty i słodki, silne tony duszonych czerwonych jabłek, domowy dżem pomarańczowy,
        miód, cynamon i soczyste sułtanki (rodzynki).<br>
        **:blue[Smak]**: nieprawdopodobnie łagodny, owocowy, gotowane gruszki, mleczne krówki i karmelowe
        toffi.<br>
        **:blue[Finisz]**: harmonijnie zbalansowany z nutami wanilii.''', unsafe_allow_html=True)

        chivas.subheader("Chivas regal 18")
        chivas.write('''18 jest dziełem Colina Scotta mistrza kupażu Chivasa.''')
        chivas.image('AlcoholImages/chivas/chivas18.jpg')
        chivas.write('''**:blue[Aromat]**: bogaty, miód, toffi, mleczna czekolada, pomarańcze, banany, czereśnie, rodzynki,
        prażone orzeszki, nuty cedru i dębu.<br>
        **:blue[Smak]**: łagodny, owocowy, karmel, wanilia, miód, mleczne krówki, rodzynki, ananas, odrobina
        kakao i odległa nutka dymna.<br>
        **:blue[Finisz]**: dość długi i kojący, z nutami słodkich suszonych owoców, mlecznej czekolady, miodu i
        odrobina dymu.''', unsafe_allow_html=True)

        chivas.subheader("Chivas regal 25")
        chivas.write('''Ekskluzywna kompozycja najbardziej wyszukanych szkockich whisky, z których najmłodsze
        leżakowały co najmniej 25 lat. Chivas Regal 25yo została wprowadzona na rynek w 1909 r.''')
        chivas.image('AlcoholImages/chivas/chivas25.jpg')
        chivas.write(''' **:blue[Aromat]**: bogaty, owocowy, czereśnie, truskawki, brzoskwinie, rodzynki, toffi, krem waniliowy,
        cynamon, trawa cytrynowa, ślad dębu.<br>
         **:blue[Smak]**: miękki, grzanka z masłem, wanilia, toffi, dżem pomarańczowy, ananasy, kandyzowany
        imbir, biały pieprz, odrobina anyżu i przyjemna goryczka dębu.<br>
         **:blue[Finisz]**: dość długi, z nutami pomarańczy, bananów, mlecznej czekolady, wanilii, pieprzu,
        mieszanki ziołowych przypraw i dębu''', unsafe_allow_html=True)

        chivas.subheader("Chivas regal ULTIS")
        chivas.write('''Formuła whisky wymienia pięć single maltów symbolizujących pięciu mistrzów kupażu Chivas
        Regal. Charles Howard, Charles Julian, Allan Baile, Jimmy Lang i obecny kustosz Colin Scott.
        Większość destylatów pochodzi z beczek po burbonie pierwszego napełnienia.''')
        chivas.image('AlcoholImages/chivas/chivas_ultis.jpg')
        chivas.write('''**:violet[Tormore]** wniósł bogate nuty pomarańczowe i cytrusowe<br>
        **:violet[Longmorn]** dołożył wanilię i toffi oraz lekko kremową strukturę<br>
        **:violet[Strathisla]**, serce Chivasa, to zniewalające tony slodowe i owocowe oraz subtelna słodycz<br>
        **:violet[Allt A’Bhainne]** dostarczy delikatnej pikanternii i tonów słodowych, które nadają blędowi
        subtelności i balansu<br>
        **:violet[Braeval]** dodał whisky świeżości, nut floralnych, miodowych i skórzanych czyniąc jej paletę
        niezwykle harmonijną i kompleksową''', unsafe_allow_html=True)

        coin = st.expander("**Cointreau** _(Likier, Francja)_")
        coin.subheader("Cointreau")
        coin.write('''Przeźroczysty likier pomarańczowy, charakteryzuje się łagodnym i
        wyrazistym smakiem słodko-gorzkich skórek pomarańczy i koniaku, unikatową cechą jest reakcja
        na chłód - w temperaturze pokojowej jest krystalicznie przezroczysty, po oziębieniu zaś lub
        dodaniu lodu pojawiają się w nim pięknie opalizujące chmurki.''')
        coin.image('AlcoholImages/cointreau/cointreau.jpg')

        coin.subheader("Cointreau NOIR")
        coin.write('''Połączenie Cointreau oraz koniaku Remy Martin. Uwodzi on swoją
        świeżością, aromatem pomarańczy z aksamitnie gładką nutą koniaku.
        Master Distiller wzbogacił oryginalną recepturę dodając do maceracji odrobinę orzechów i
        migdałów, co przynosi jeszcze bardziej wyrafinowane aromaty i smaki. Odrobina pikanterii,
        zaokrąglona z nutami wanilii, miodu, orzechów i migdałów''')
        coin.image('AlcoholImages/cointreau/cointreau-noir.jpg')

        dewars = st.expander("**Dewar’s 15YO** _(Whisky, Szkocja, Blended, Highland)_")
        dewars.write('''Kreacja mistrzyni kupażu Stephanie Mcleod, której formuła wymienia około 40 whisky starzonych
        niemal wyłącznie w beczkach po burbonie i po sherry.''')
        dewars.image('AlcoholImages/dewars15.jpg')
        dewars.write('''**:blue[Aromat]**: łagodny z subtelną nutą sherry, miód, karmel, jabłka, śliwki, wiórki kokosowe,
        kandyzowana skórka cytrynowa i odległy ślad dymu.<br>
        **:blue[Smak]**: łagodny i słodki, miód, wanilia, mleczne krówki, pomarańcze, morele, szczypta białego
        pieprzu i subtelna goryczka dębu.<br>
        **:blue[Finisz]**: średnio długi, z nutami wanilii, dębu i cytrusów.''', unsafe_allow_html=True)

        deveron = st.expander("**Deveron** _(Whisky, Szkocja, Single malt, Highland)_")
        deveron.caption('''The Deveron powstaje w destylarnii o nazwie Macduff. Zbudowano ją w 1960 roku w czasie 
        powojennego boomu na whisky. Oryginalnymi właścicielami była grupa maklerów pochodząca z Glasgow. Autorem 
        projektu gorzelni był szeroko znany i ceniony w branży whisky architekt William Delme-Evans. Potem, w 1972 roku 
        w posiadanie interesu wszedł natomiast William Lawson. Ponieważ destylarnia stopniowo rozwijała się, właściciel 
        zwiększył liczbę aparatów destylacyjnych na jej wyposażeniu do pięciu w 1990 roku. Do tego czasu wypuszczono 
        kilka wersji single maltów, wszystkie pod nazwą Glen Deveron. Najwcześniej wydane z nich miały pięć lub osiem 
        lat. Z kolei, w 1995 roku, biznes przeszedł  pod skrzydła spółki Bacardi. W ostatnich latach whisky ta była 
        bardzo popularna w Rosji. W 2015 roku marka powróciła z nową nazwą i etykietą.''')
        deveron.write('''The Deveron 12 yo to bardzo ciekawy single malt pochodzący prosto ze znanego, szkockiego 
        regionu Highlands. Twórcy zabutelkowali go w mocy 40% ABV. Przedstawia świetnie komponującą się, przyjemną 
        mieszankę owoców, karmelu, a także wanilii i delikatnego akcentu pikanterii. Co ciekawe, marka była znana 
        wcześniej jako Glen Deveron, ale w 2015 roku zmieniła swoją nazwę, jak i etykietę. Dodatkowo, może pochwalić 
        się zdobyciem srebra w znanym konkursie International Spirits Challenge w 2019 roku oraz złota w International 
        Wine & Spirit Competition w roku 2019.''')
        deveron.image('AlcoholImages/DEVERON-12-YO-0.7L.jpg')
        deveron.write('''**:blue[Zapach]**: jabłka w toffi, brązowy cukier, nieco przypraw korzennych i imbiru. <br>
        **:blue[Smak]**: oleista i bardzo uładzona, przywodzi na myśl ciasteczka maślane, wosk, miód, szarlotkę i słodowane zboże. <br>
        **:blue[Finisz]**: nieco dębiny i wanilii, gładkie taniny i odrobina pikantnych przypraw korzennych.''', unsafe_allow_html=True)

        dictator = st.expander("**Dictator/Colombian** _(Rum/Gin, Kolumbia)_")
        dictator.caption('''Markę stworzył Severo Arango y Ferro, który pojawił się w mieście Cartagena de Indias w obecnej
        Kolumbii. Severo nie był osobą zbyt lubianą, bo jego zadaniem na ziemiach kolonialnych Hiszpanii
        w Ameryce Południowej było ściąganie podatków dla Królestwa Hiszpańskiego. Bohater tego
        krótkiego akapitu szybko otrzymał od miejscowej ludności przydomek Dictador – specjalnie
        używamy nazwy marki, aby ten fragment wskazywał skąd jej pochodzenie.
        W 1913 roku, niemal 180 lat po tym, jak narodził się mit Dictadora, powstała destylarnia
        Colombiana. Za receptury odpowiadał Don Julio Arango y Parra, który spędził lata w
        odkopywaniu szczątek informacji związanych z produkcją rumu. Obecnie za produkcję
        odpowiada wnuk Don Julio, Master Blender Hernan Parra, który kontynuuje rodzinną tradycję.
        Za produkcję butelek, do których rozlewany jest Dictador odpowiedzialni są Japończycy. Sam
        Dictador dostępny jest w kilkunastu edycjach, m.in. popularnych 12 i 20-letnich. Marka
        produkuje limitowane edycje rumów, w tym XO Perpetual, XO Insolent, czy serię 2 Masters, w
        której znajduje się sześć różnych edycji rumu. Cały koncept to unikatowa kolekcja rumów
        podkręcanych do granic możliwości przez dwóch master destilerów. Każdy z trunków
        dojrzewał przez blisko 40 lat, ze specjalnie przygotowaną recepturą. Za mieszanie rumów
        odpowiedzialni są artyści w swoim fachu, w tym specjaliści od win, sherry czy whisky, bourbonie,
        a także nawet szampanie.''')

        dictator.subheader("Dictador 12yo")
        dictator.write('''Powstaje z fermentacji świeżego cukru trzcinowego i miodu, destylowanego częściowo w
        miedzianym alembiku a częściowo w stalowej kolumnie, aby osiągnąć rum midium. Podlega
        starzeniu w dębowych używanych beczkach z wykorzystaniem metody solera. 12yo to rum o
        bursztynowym zabarwieniu. W smaku jest bardzo miękki i okrągły, z posmakiem karmelu, kakao,
        miodu i delikatnej kawy. Aromat delikatny, miodowy, wanilii oraz palonej kawy.''')
        dictator.image('AlcoholImages/dictator/dictator12.jpg')

        dictator.subheader("Dictador 20yo")
        dictator.write('''Rum Dictador 20 YO powstaje z fermentacji dziewiczego miodu z trzciny cukrowej. Destylacja
        rumu odbywa się częściowo w miedzianych alembikach, a częściowo w stalowych kolumnach
        destylacyjnych. 20yo to rum o intensywnym ciemnym kolorze bursztynu. W ustach jest bardzo
        miękki i okrągły, z posmakiem karmelu, wanilii, kakao oraz miodu. Aromat delikatny, karmelowy,
        wanilii, miodu, toffi oraz palonej kawy.''')
        dictator.image('AlcoholImages/dictator/dictator20.jpg')

        dictator.subheader("Dictador XO Perpetual")
        dictator.write('''Dojrzewa w starannie wyselekcjonowanych dębowych beczkach po burbonie, przy zastosowaniu
        tradycyjnej metody Solera. Skomponowany jest z wyjątkowych destylatów z poszczególnych
        roczników. Rum posiada szlachetny, mahoniowy kolor. W smaku wyczuwalna jest słodycz kawy i
        ciemnej czekolady. Aromat palonego miodu, kawy, toffi oraz ciemnej czekolady, dojrzały dąb.''')
        dictator.image('AlcoholImages/dictator/dictatorxo.jpg')

        dictator.subheader("Colombian Ortodoxy")
        dictator.write('''Gin produkowany jest na bazie spirytusu trzciny cukrowej z dodatkiem jagód jałowca, ziół,
        korzeni, przypraw, roślin i cytrusów.''')
        dictator.image('AlcoholImages/dictator/colombian_ortodoxy.jpg')
        dictator.write('''**:blue[Aromat]**: wyważony ze słodko-kwaśnymi tonami i nutami świeżych ziół, korzeni, jałowca,
        arcydzięgla, cynamonu i imbiru.<br>
        **:blue[Smak]**: gładki i przyjemny z akcentami cytrusów, pieprzu, jałowca, ziół, korzeni, przypraw.<br>
        **:blue[Finisz]**: długi i przyjemny z nutami przypraw i cytrusów.''', unsafe_allow_html=True)

        dictator.subheader("Colombian Treasure")
        dictator.write('''Jedyny w swoim rodzaju gin z destylatu trzciny cukrowej z domieszką ziół, przypraw, korzeni i 
        cytrusów. Starzony przez 35 tygodni w beczkach po rumie Dictador, dzięki czemu zyskuje unikatowy charakter, 
        kolor i wyrazisty smak. Barwa Pełna, wyrazista, bursztynu z refleksami złota. Wyróżnia go aromat mandarynki i 
        cytryny, świeże botaniczne nuty mięty i pieprzu oraz subtelne słodkie niuanse pochodzące z drewna i jagód.''')
        dictator.image("AlcoholImages/dictator/colombian_treasure.jpg")

        dram = st.expander("**Drambuie** _(Likier, Szkocja)_")
        dram.caption('''Nazwa Drambuie pochodzi od szkocko gaelickiego zwrotu _"an dram buidheach"_, oznaczającego napój, 
        który zadowala i została zastrzeżona w 1892''')
        dram.write('''Jego bazę stanowi single malt whisky (15-17 letnia), miód i zioła ze szkockich wrzosowisk. Smak i
        zapach whisky słodowej i miodu w połączeniu z aromatem ziół.''')
        dram.image('AlcoholImages/drambuie.jpg')

        fernet = st.expander("**Fernet Branca** _(Likier, Włochy)_")
        fernet.caption('''Likier którego sekretna receptura sięga 1846 roku. Bazuje on na wyciągu z unikalnej mieszanki 
        wyselekcjonowanych kwiatów oraz rzadkich, wyjątkowych aromatycznych ziół. Beczki z ekstraktem są starannie i 
        długo starzone w zabytkowych piwnicach Branca.''')
        fernet.write('''Fernet Branca to likier sporządzony z 27 różnych ziół oraz przypraw takich jak: szafran, mirra, 
        liście koki, aloes, kardamon i kora chininowa, pochodzących z czterech kontynentów.''')
        fernet.image('AlcoholImages/fernetbranca.jpg')

        glen = st.expander("**Glenlivet** _(Whisky, Szkocja, Single malt, Speyside)_")
        glen.caption('''Faktem jest, że to jedna z najstarszych destylarni w Szkocji. W 1824 roku właściciel destylarni
        jako pierwszy zdobył licencję na legalną produkcję whisky. Gorzelnia leży w dolinie rzeki Livet,
        w Speyside, królestwie delikatnych whisky, a jej flagowy produkt to Glenlivet 12yo.''')
        glen.subheader("Glenlivet 12")
        glen.write('''Starzona jest w beczkach po burbonie i finiszowana w beczkach wykonanych z francuskiego dębu. W 2015
        roku, z powodu braku zapasów magazynowych, został wycofany z rynku europejskiego (ciągle był
        dostępny w Stanach) i zastąpiony wersją Founder’s Reserve. Powrót jesienią 2018 roku.''')
        glen.image("AlcoholImages/glenlivet/glenlivet12.jpg")
        glen.write(''' **:blue[Aromat]**: łagodny, owocowy, jabłka, brzoskwinie, śliwki, wanilia, miód i dąb.<br>
         **:blue[Smak]**: przyjemnie zbalansowany, owocowy, jabłka, brzoskwinie, suszone śliwki, krem waniliowy,
        ślady rodzynek i orzechów włoskich oraz delikatne nuty dębu.<br>
         **:blue[Finisz]**: długi, owocowy, słodka mieszanka suszonych owoców, orzechy laskowe i dąb.''', unsafe_allow_html=True)

        glen.subheader("Glenlivet Founder’s Reserve")
        glen.write('''Destylaty wykorzystywane w tej edycji pochodziły z beczek ponownego napełnienia oraz
        świeżych beczek po burbonie. Została ona wypuszczona ze względu na braki magazynowe 12yo.
        Butelkowana jest bez oznaczenia wiekowego.''')
        glen.image("AlcoholImages/glenlivet/glenlivet_founders_reserve.jpg")
        glen.write('''**:blue[Aromat]**: świeży, lekko orzechowy, zielone jabłka, pomarańcze, wanilia, miód, dębowe wióry, ślady
        wiórków kokosowych i anyżku.<br>
        **:blue[Smak]**: łagodny i słodki, pieczone jabłka i śliwki, wanilia, toffi, bułka maślana, mleczna czekolada,
        szczypta cynamonu i białego pieprzu.<br>
        **:blue[Finisz]**: niezbyt długi, łagodny, początkowo owocowy, wkrótce przechodzący w wytrawny,
        dębowo-korzenny.''', unsafe_allow_html=True)

        glen.subheader("Glenlivet 15")
        glen.write('''12-latka zawierała whisky starzoną w beczkach po burbonie i finiszowaną w beczkach
        wykonanych z francuskiego dębu, to w przypadku 15 jedynie część (ok. 35%) destylatów finiszuje
        we wspomnianych beczkach. Odmiana dębu limousin pochodzi z okręgu Dordogne i jest
        powszechnie wykorzystywana do maturacji koniaków.''')
        glen.image("AlcoholImages/glenlivet/glenlivet15.png")
        glen.write(''' **:blue[Aromat]**: bogaty, kremowy, wanilia, karmel, zielone winogrona, jabłka, grapefruity, ślady pieprzu i
        cynamonu, żywicy sosnowej i cedrowej deszczułki.<br>
         **:blue[Smak]**: łagodny, owocowy, jabłka, gruszki, wanilia, crème brûlée, orzechy laskowe, szczypta gałki
        muszkatołowej i nuty dębowe w tle.<br>
         **:blue[Finisz]**: długi, dębowo-korzenny z wyczuwalnymi nutami orzechowymi.''', unsafe_allow_html=True)

        glen.subheader("Glenlivet 18")
        glen.write('''Około 155 destylatów pochodzi ze świeżych beczek po sherry Oloroso, pozostałe z beczek po
        burbonie oraz beczek wielokrotnego napełnienia. 18 to perfekcyjny glenlivet w którym tony
        owocowe pozostają w cudownej harmonii z korzennymi tonami i goryczką dębu.''')
        glen.image("AlcoholImages/glenlivet/glenlivet18.jpg")
        glen.write('''**:blue[Aromat]**: bogaty i złożony z delikatną nutą sherry, kwiat jabłoni, wanilia, toffi, wiśnie, suszone
        śliwki, skórka pomarańczowa, gorzka czekolada, dąb i ślad cynamonu.<br>
        **:blue[Smak]**: znakomicie zbalansowany, pomarańcze, pieczone jabłka, crème brûlée,, toffi, migdały,
        cynamon, gałka muszkatołowa, dąb ślady sherry i ziół.<br>
        **:blue[Finisz]**: niezwykle długi, cudowna harmonia słodyczy, dębu i tonów korzennych.''', unsafe_allow_html=True)

        glen.subheader("Glenlivet 21")
        glen.write('''Whisky pochodzi z kilku rodzaju beczek, od beczek po burbonie pierwszego i ponownego
        napełnienia po różne typy beczek po sherry (butt, hogshead czy puncheon), również pierwszego i
        ponownego napełnienia. Produkowana ona jest w małych partiach.''')
        glen.image("AlcoholImages/glenlivet/glenlivet21.jpg")
        glen.write('''**:blue[Aromat]**: bogaty, silne tony sherry, mleczna czekolada, prażone migdały, rodzynki, suszone śliwki,
        kawa.<br>
        **:blue[Smak]**: złożony i znakomicie zbalansowany, pieczone jabłka i śliwki, ciemne winogrona, truskawki,
        migdały prażone w miodzie, cynamon, dąb i bardzo ulotna nuta dymu.<br>
        **:blue[Finisz]**: długi i bogaty, pełna harmonia wszystkich elementów smakowych.''', unsafe_allow_html=True)

        glen.subheader("Glenlivet 25")
        glen.write('''Wykorzystując jedne z najrzadszych whisky, z których wszystkie były leżakowane przez co
        najmniej 25 lat, jest to whisky produkowana seryjnie, finiszowana beczkami po sherry. Zespół
        ekspertów indywidualnie wybiera każdą beczkę i monitoruje proces finiszowania whisky, aby
        upewnić się, że drewno nasączone Oloroso dodaje subtelnych tonów sherry.''')
        glen.image("AlcoholImages/glenlivet/glenlivet25.jpg")
        glen.write('''**:blue[Aromat]**: słodkie rodzynki sułtańskie, ciemna czekolada, ziołowe przyprawy, owoce, tytoń i beczka
        dębowa.<br>
        **:blue[Smak]**: aksamitny i łagodny, suszone owoce, orzechy, toffi, crème brulee, korzenne przyprawy.<br>
        **:blue[Finisz]**: długi, z kumulacją owocowych motywów pokreślonych korzennymi przyprawami.''', unsafe_allow_html=True)

        glenfid = st.expander("**Glenfiddich** _(Whisky, Szkocja, Single malt, Speyside)_")
        glenfid.caption('''Glenfiddich w języku gaelickim oznacza Dolina Jeleni, stąd głowa jelenia w logotypie tej marki
        whisky. Glenfiddich to najbardziej popularna whisky single malt na świecie. Swoją silną pozycję
        zawdzięcza wytrwałości Williama Granta i wielu pokoleń jego rodziny, która od 1887 roku
        prowadzi destylarnię w małym szkockim miasteczku regionu Speyside. Glenfiddich powstaje
        z najlepszego jęczmienia i krystalicznie czystej wody uzyskiwanej z podziemnego źródła Robbie
        Dhu. Niezrównany smak i aromat Glenfiddich to rezultat leżakowania w beczkach z najlepszego
        drewna z różnych części świata: hiszpańskich beczkach po sherry, beczkach po bourbonie z USA
        oraz po karaibskim rumie. Whisky Glenfiddich uzyskała od 2000 roku najwięcej nagród na
        najbardziej prestiżowych konkursach the International Wine & Spirit Competition oraz the
        International Spirits Challenge spośród wszystkich szkockich whisky single malt na świecie.''')
        glenfid.subheader("Glenfiddich 12")
        glenfid.write('''Zanim Glenfiddich trafi do butelki, starzony jest w jednej z dwóch rodzajów beczek:
        amerykańskiej beczce po bourbonie lub beczkach po sherry z Jerez de la Frontera w Hiszpanii.
        Źródłem wody używanej do produkcji tej whisky, od samego początku, jest źródło znajdujące się
        w sąsiedztwie destylarni, Robbie Dhu. Osobą odpowiadającą za jakość alkoholu jest szanowany
        w świecie whisky Brian Kinsman.''')
        glenfid.image("AlcoholImages/glenfiddich/glenfiddich12.jpg")
        glenfid.write(''' **:blue[Zapach]**: zbożowy, sporo tu suchej skoszonej trawy, świeżego drewna, wanilii, miodu
        wielokwiatowego, gałki muszkatołowej, suszonych owoców, cytrusów. Alkohol delikatnie drażni
        nos, choć moc whisky to 40% alk.<br>
         **:blue[Smak]**: przyjemny, whisky jest dość wodnista, czuć owoce: świeże jabłka, przyprawy (pieprz,
        gałka muszkatołowa), szuszone owoce; słodycz i dębina.<br>
         **:blue[Finisz]**: przyjemnie utrzymuje się na języku przez dłuższą chwilę; ciemna, gorzka czekolada, budyń
        czekoladowy, pieprzność, owocowość, alkohol.
        W whisky dominuje kilka głównych nurtów smakowo-zapachowych: owocowy, cytrusowy,
        trawiasty i roślinny. To w nich warto doszukiwać się bardziej złożonych zapachów, które i w nosie i
        na języku, są do siebie zbliżone. Whisky jest prosta w odbiorze, przyjemna i idealnie nadaje się
        tak do kieliszka degustacyjnego czy szklanki z kością lodu.''', unsafe_allow_html=True)

        glenfid.subheader("Glenfiddich 15YO Unique Solera Reserve")
        glenfid.write('''Whisky leżakowana przez 15 lat w różnych dębowych beczkach: świeżych, po bourbonie i po
        sherry, żeby na koniec połączyć się w unikalnej, ręcznie robionej i nigdy nie opróżnianej bardziej,
        niż do połowy, kadzi solera..''')
        glenfid.image("AlcoholImages/glenfiddich/uniquesolera.jpg")
        glenfid.write('''**:blue[Zapach]**: Dojrzały i bardzo miękki, z lekkim aromatem dżemu sliwkowego i pieczone jabłka.<br>
        **:blue[Smak]**: Miękki i jedwabisty z aromatami duszonych ciemnych owoców, kokosa , schnącej trawy.<br>
        **:blue[Finisz]**: Bogaty i pełny.''', unsafe_allow_html=True)

        glenfid.subheader("Glenfiddich 15YO Our Solera Fifteen")
        glenfid.write('''Kolejne wydanie 15-letniej whisky od marki Glenfiddich ukazało się latem 2019 roku, stając się
        młodszą siostrą poprzedniczek - Solera Reserve (dostępnej także jako Unique Solera Reserve)
        oraz Solera Vat.
        Wyjątkowy smak zawdzięcza ona technikom uzdolnionego Mistrza Słodowania, a pikantne,
        rozgrzewające nuty to zasługa stosowanej metody Solera (polegającej kiedyś na mieszaniu
        rocznikowych win, wykorzystując do tego kompozycję selektywnie wybieranych beczek lub tzw.
        kadzi solera).
        Glenfiddich 15 Our Solera Fifteen dojrzewa w trzech rodzajach dębowych beczek - po sherry,
        bourbonie oraz w dziewiczym dębie, które mają nasycić jej smak nutami owoców, przypraw oraz
        miodu. Kolejnym etapem jest mariaż destylatów z wyjątkową, ręcznie wykonaną kadzią Solera z
        sosny Oregon, którą każdorazowo wypełnia się przynajmniej w połowie, aby nadać trunkowi
        odpowiednią harmonię i stworzyć złożoną, ale jednocześnie zrównoważoną whisky.''')
        glenfid.image('AlcoholImages/glenfiddich/glenfiddich-15yo.jpg')
        glenfid.write('''**:blue[Zapach]**: intrygująco złożony. Słodkie nuty miodu, wrzosów oraz wanilii łączą się z lekką
        wytrawnością dojrzałych, czerwonych owoców.<br>
        **:blue[Smak]**: jedwabiście gładka tekstura, odsłaniająca niuanse dębowego sherry, marcepanu,
        cynamonu oraz imbiru. Pełna i niezwykle satysfakcjonująca na podniebieniu.<br>
        **:blue[Finisz]**: długi, pozostawiający wrażenia suszonych owoców, goździków oraz słodkich nut wanilii''', unsafe_allow_html=True)

        havana = st.expander("**Havana** _(Rum, Kuba)_")
        havana.caption('''Starzenie na kubie jak i w innych ciepłych krajach jest dosyć uciążliwe ze względu na warunki
        klimatyczne. Duża wilgotność i temperatura sprawia że angels' share nie stanowi 3% jak w
        przypadku whisky tylko 7% a nawet do 10%.''')
        havana.subheader("Havana 3")
        havana.write('''Niezwykły charakter Havana Club 3 Años to rezultat naturalnego dojrzewania w dębowych
        beczkach (między innymi po Jamesonie) przez przynajmniej trzy lata. W miarę powolnego
        starzenia w tropikalnym klimacie Kuby rum ten zyskuje słomkowy kolor i charakterystyczne nuty
        dębu, połączone z orzeźwiającym aromatem owoców i subtelnym śladem melasy z dorodnej
        kubańskiej trzciny cukrowej. Najmłodsza kropla rumu Havana Club 3 Años ma trzy lata. Po dwóch
        latach powstały w procesie produkcji mocny alkohol aguardiente zostaje poddany filtracji przez
        węgiel drzewny w celu usunięcia zanieczyszczeń, po czym wraca do beczki.''')
        havana.image("AlcoholImages/havana/havana3.jpg")

        havana.subheader("Havana Especial")
        havana.write('''Rum Havana Club Añejo Especial wyróżnia nasza metoda podwójnego starzenia. Nasz rum
        dojrzewa przez wiele lat w beczkach po amerykańskim burbonie, po czym zostaje przelany do
        beczek po irlandzkiej whiskey, gdzie przechodzi ponownie proces starzenia. Dzięki temu Havana
        Club Añejo Especial uzyskuje swój delikatny, harmonijny smak z subtelną słodyczą wanilii.''')
        havana.image("AlcoholImages/havana/havanaespecial.jpg")

        havana.subheader("Havana 7")
        havana.write('''Havana Club Anejo 7 Anos to zdecydowanie jeden z najlepszych zawodników świetnej, kubańskiej 
        reprezentacji. Esencjonalny i złożony a zarazem łagodny w smaku jest wzorcem bogatej tradycji produkcji rumu 
        na Kubie. Szlachetności dodaje mu całkowicie naturalny, siedmioletni proces leżakowania w dębowych beczkach.''')
        havana.image('AlcoholImages/havana/havana7.jpg')
        havana.write('''**:blue[Zapach]**: wanilia, kakao, suszone owoce, plaster miodu, toffi;<br>
        **:blue[Smak]**: toffi, owoce, cedrowe pudełko z cygarami, guava i bananowe liście;<br>
        **:blue[Finisz]**: kremowo-owocowy, złożony i długi.''', unsafe_allow_html=True)

        havana.subheader("Havana Maestros")
        havana.write('''W celu stworzenia "Selección de Maestros", wybiera się najlepsze starzone rumy, aby z
        wybitnych cech każdego z nich stworzyć rum najwyższej jakości. Wyselekcjonowane rumy tworzą
        bazę, następnie są ponownie nalewane w beczki z młodego dębowego drewna, po to by nadać
        trunkowi silny, dębowy aromat.
        W ostatnim etapie starzenia rumu, zbiera się wszystkie wcześniej przygotowane rumy, aby wybrać
        tylko te, które stworzą finałową kompozycję. Mieszanka zostaje zabutelkowana, sprawia to, że
        rum posiada wyższą zawartość alkoholu, w tym przypadku jest to 45%.''')
        havana.image('AlcoholImages/havana/havanaseleccion.jpg')

        havana.subheader("Havana Unión")
        havana.write('''Połączenie dwóch najpopularniejszych i flagowych tradycyjnych produktów Kuby - Rumu Havana
        Club i cygar Cohiba.
        Wynik współpracy Maestro Ronero Asbel Morales’a, odpowiedzialnego za stworzenie unikatowej
        receptury rumu oraz Fernando Fernandez Milian’a , Master Habano sommelier.
        Starannie dobrane i naturalnie starzone rumy wchodzące w skład tej mieszanki, zostały specjalnie
        wybrane przez Maestro Ronero, aby idealnie dopełnić smak cygar Cohiba. Havana Club Unión
        charakteryzuje się aromatem słodkiej wanilii i czekolady oraz smakiem suszonych owoców.''')
        havana.image('AlcoholImages/havana/havanaunion.png')

        hendricks = st.expander("**Hendrick's** _(Gin, Szkocja)_")
        hendricks.caption('''Na rynku ukazał się w 2001 produkowany przez znaną w świecie whisky rodzinną firmę William
        Grant & Sons. Destylowany jest w gorzelni Girvan, w charakterystycznych i unikatowych alembikach typu Carter-
        Head.''')
        hendricks.subheader("Hendrick’s")
        hendricks.write('''Gin komponowany jest z krwawnika pospolitego, jałowca, kwiatu bzu, korzenia arcydzięgla,
        skórki pomarańczowej, kolendry, rumianku, pieprzu kubeba, korzenia irysa, cytryny i kminku.
        Dodatkowo Hendrick’s infuzowany jest zielonym ogórkiem oraz bułgarską różą.''')
        hendricks.image("AlcoholImages/hendricks/hendricks.jpg")
        hendricks.write('''**:blue[Aromat]**: bogaty i pełny z nutami cytrusów, róży ogórka, jałowca, kwiatów i przypraw <br>
        **:blue[Smak]**: głęboki z akcentami kolendry, skórek cytrusowych, kwiatów, przypraw i jałowca<br>
        **:blue[Finisz]**: trwały z posmakiem kwiatów, cytrusów i jałowca''', unsafe_allow_html=True)

        hendricks.subheader("Hendrick’s Neptunia")
        hendricks.write('''Nowa limitowana edycja ginu Hendrick’s w serii Ms. Lesley Gracie’s Cabinet of Curiosities. Są tu
        klasyczne dla stylu Hendrick’s botaniki, czyli przede wszystkim: jałowiec, zielony ogórek i płatki
        róży, skórki pomarańczy, ale też rośliny występujące na nabrzeżu Girvan, w tym także wodorosty.
        Zapach tego ginu ma wyraźnie morski charakter – są wodorosty, omułki, ostrygi i solanka. Do
        tego uderzenie cytryny oraz nuty słodkie, kwiatowe – fiołki, wanilia. Stosunkowo mało czuć
        jałowiec, bardziej jakieś wrzosy, tuje... W smaku także czuć omułki, jest też dużo jałowca,
        czarnego pieprzu. Smak jest wyrazisty, ostry, do tego dochodzą intensywnie cytrusy. Dużo
        jałowca w finiszu, sól, rześkość (zapewne dał ją zielony ogórek), imbir, pieprz czarny, kardamon, a
        może bardziej aframon. Finisz jest długi i bardzo elegancki.''')
        hendricks.image("AlcoholImages/hendricks/hendrick-s-neptunia.jpg")

        hendricks.subheader("Hendrick’s Orbium")
        hendricks.write('''Edycja ORBIUM to nowa interpretacja dżinu Hendricka autorstwa Master Distiller Lesley Gracie.
        W przeciwieństwie do oryginalnego dżinu Hendricks, do tej edycji dodano trzy dodatkowe rośliny
        botaniczne: chininę, piołun i niebieski kwiat lotosu.''')
        hendricks.image("AlcoholImages/hendricks/hendricksorbium.jpg")
        hendricks.write('''**:blue[Zapach]**: Przejrzysty, złożony, zaskakująco świeży.<br>
        **:blue[Smak]**: Głęboki, złożony, kwiatowy, gorzki, niezwykle esencjonalny.<br>
        **:blue[Finisz]**: Długotrwałe.''', unsafe_allow_html=True)

        jameson = st.expander("**Jameson** _(Whisky, Irlandzka)_")
        jameson.caption('''''')
        jameson.subheader("Jameson")
        jameson.write('''Powolna potrójna destylacja w miedzianych alembikach. Komponowana jest z destylatów, które
        leżakowały co najmniej 4 lata w beczkach po burbonie oraz w beczkach po sherry. ''')
        jameson.image("AlcoholImages/jameson/jameson.jpeg")
        jameson.write('''**:blue[Aromat]**: pełny i gładki z nutami kwiatów, marmolady, polewy czekoladowej, miodu, wanilii, sherry,
        ściętej trawy i wiśni<br>
        **:blue[Smak]**: głęboki i bogaty z akcentami jabłka, gruszki, moreli, wiśni, wanilii, śmietany, miodu,
        wrzosu, cytrusów i karmelu.<br>
        **:blue[Finisz]**: średnio długi z posmakiem przypraw zimowych i miodu.''', unsafe_allow_html=True)

        jameson.subheader("Jameson Black Barrel")
        jameson.write('''Limitowana edycja dojrzewająca częściowo w podwójne wypalanych z amerykańskiego dębu, a
        częściowo w beczkach po sherry typu oloroso.''')
        jameson.image("AlcoholImages/jameson/jamesonblack.jpg")
        jameson.write('''**:blue[Aromat]**: bogaty i złożony. Na tyle wyrazistych akcentów zbożowych, nutki owoców tropikalnych,
        nektaryn, kokosa.<br>
        **:blue[Smak]**: Ciężki, pełny, kremowy. Bogaty, oleisty keks , a w nim mnóstwo akcentów daktyli,
        orzechów i kandyzowanych skórek pomarańczy i cytryny. Nutki cynamonu, brzoskwiń i
        nieznaczne przyprawy korzenne.<br>
        **:blue[Finisz]**: Długi, owocowy, wygasający powoli, z akcentami korzennymi i kwiatowymi.''', unsafe_allow_html=True)

        jameson.subheader("Jameson Caskmates Stout")
        jameson.write('''Wynik eksperymentu w ramach którego zostały wypożyczone beczki browarowi Franciscan Wells
        by dojrzewał w nich irlandzki stout, a następnie zostały one przywiezione z powrotem do
        destylarni i tam napełniono już dojrzałą whiskey na 3 miesiące(tzw. cask finish)''')
        jameson.image("AlcoholImages/jameson/jamesonstout.jpg")
        jameson.write('''**:blue[Aromat]**: połączenie tradycyjnych akcentów Jameson, które nie zostały przykryte, a jedynie
        uzupełnione akcentami stoutu - jest tu więcej korzenności, akcentów dębowych, a także
        czekolady.<br>
        **:blue[Smak]**: Bogaty, pełny. Akcent owoców, wanilii, czekolady. Dodatkowo pojawiają się nutki
        chmielowe i nieco goryczki.<br>
        **:blue[Finisz]**: Średnio długi, z przeplatającymi się nutkami korzennymi i czekoladowymi.''', unsafe_allow_html=True)

        jameson.subheader('Jameson Crested')
        jameson.write('''Whiskey Crested została stworzona w 1963 roku. Jest on pełniejszą, bogatszą wersją
        podstawowej whiskey Jameson. W ok. 60% składa się z destylatu jęczmiennego i jest
        leżakowana w beczkach po sherry przez 7 – 8 lat.''')
        jameson.image("AlcoholImages/jameson/jamesoncrested.jpg")
        jameson.write('''**:blue[Aromat]**: bogaty, miód, toffi, prażone orzeszki, dżem pomarańczowy, kantalupa, kandyzowany
        imbir, goździki i pięknie wplecione nuty sherry.<br>
        **:blue[Smak]**: przyjemnie zbalansowany, subtelne nuty sherry, skórka cytrynowa i pomarańczowa, miód,
        karmel, mleczna czekolada, ślady pieprzu i imbiru.<br>
        **:blue[Finisz]**: średnio długi, rozgrzewający, z nutami sherry, karmelu i czekolady.''', unsafe_allow_html=True)

        jim = st.expander("**Jim Beam** _(Bourbon)_")
        jim.caption('''''')
        jim.subheader("Jim Beam White")
        jim.write('''Charakteryzuje się tym że oprócz kukurydzy (70%) zawiera sporą ilość żyta (16%) a pozostałe
        14% to jęczmień. Destylaty leżakują 4 lata w nowych wypalanych beczkach z białego
        amerykańskiego dębu.''')
        jim.image('AlcoholImages/jimbeam/jimbeam.jpg')
        jim.write('''**:blue[Aromat]**: bardzo słodki z nutami wanilii, siana, świeżej kukurydzy, karmelu, palonego dębu
        przypraw.<br>
        **:blue[Smak]**: pełny i głęboki z nutami wanilii, palonego dębu, pieprzu, przypraw korzennych, miodu i
        siana.<br>
        **:blue[Finisz]**: średnio długi z nutami dębu, żywicy i słodyczy.''', unsafe_allow_html=True)

        jim.subheader("Jim Beam Black Extra Aged")
        jim.write('''Stworzona w 1978 roku whiskey należy do bourbonów premium . Leżakuje zdecydowanie dłużej w 
        beczkach z białego dębu amerykańskiego niż oryginalny Jim Beam White . Zmienia to całkowicie nuty smakowe i 
        zapachowe, które zaczynają się półsłodkimi akcentami, przechodząc w gładkie wykończenie dębem i karmelem.''')
        jim.image("AlcoholImages/jimbeam/jimbeamextraaged.jpg")
        jim.write('''**:blue[Aromat]**: dość słodki z nutą dymną, krem waniliowy, karmel, płatki kukurydzane, goździki, ślad
        anyżku i nadpalonego dębu.<br>
        **:blue[Smak]**: wanilia, karmel, trochę miodu, prażona kukurydza, odrobina cynamonu i goździków i
        nadpalony dąb.<br>
        **:blue[Finisz]**: dość długi i rozgrzewający, z nutami zwęglonej dębiny, karmelu, wanilii i odrobiną pieprzu.''', unsafe_allow_html=True)

        jim.subheader("Jim Beam Double Oak")
        jim.write('''W wypadku whiskey Jim Beam Double Oak, destylat w wieku 4 lat (czyli Jim Beam White) jest
        przelewany do drugiej beczki, na czas którego producent nie ujawnia. Otwartym pozostaje
        pytanie czy druga beczka jest nowa i nowowypalona czy tylko nowowypalona.''')
        jim.image("AlcoholImages/jimbeam/jimbeamdoubleoak.jpg")
        jim.write('''**:blue[Aromat]**: bardzo słodki z nutami wanilii, siana, świeżej kukurydzy, karmelu, palonego dębu i
        przypraw.<br>
        **:blue[Smak]**: pełny i głęboki z nutami wanilii, palonego dębu, pieprzu, przypraw korzennych, miodu i
        siana.<br>
        **:blue[Finisz]**: średnio długi z nutami dębu, żywicy i słodyczy.''', unsafe_allow_html=True)

        jim.subheader("Jim Beam Rye")
        jim.write('''W skład zacieru JBR wchodzi 51% żyta. Whisky leżakuje przez 4 lata w nowych dębowych
        beczkach. Destylaty żytnie są znacznie bardziej pieprzne i wytrawne więc spodziewam się, że
        będzie to łatwe do zauważenia już na samym początku.''')
        jim.image("AlcoholImages/jimbeam/jimbeamrye.jpg")
        jim.write(''' **:blue[Aromat]**: słodki i pikantny, karmel, mleczne krówki, kakao w proszku, goździki, cynamon, imbir,
        ślad lukrecji i mięty.<br>
         **:blue[Smak]**: łagodny i dość słodki, karmel, wanilia, prażona kukurydza, szarlotka poprószona
        cynamonem, goździki i delikatne nuty orzechowe i dębowe.<br>
         **:blue[Finisz]**: niezbyt długi, z nutami wanilii, syropu kukurydzianego i odrobiną korzennych przypraw.''', unsafe_allow_html=True)

        kahlua = st.expander("**Kahlúa** _(Likier, Meksyk)_")
        kahlua.write('''Ceniony kawowy likier wprost z Meksyku. Kahlua została stworzona w 1936 roku w sercu tego
        kraju. Kahlua jest produkowana z ziaren kawy Arabica rosnących u podnóży gór Meksyku.
        Esencja z kawy jest łączona następnie z importowanym rumem i słodką wanilią.''')
        kahlua.image("AlcoholImages/kahlua.jpg")

        kinobi = st.expander("**Ki No Bi** _(Gin, Japonia, Kyoto dry)_")
        kinobi.caption('''"Ki No Bi" oznacza "piękno pór roku" i jest odniesieniem do składników, 
        które zostały użyte do skomponowania tego trunku''')
        kinobi.write('''Jedyny w swoim rodzaju gin. Powstaje w destylarni rzemieślniczej z typowo japońskich roślin, 
        takich jak yuzu, cyprysik japoński, bambus, gyokuro, pachnotka, kinome i sanshō. Wyróżnia się nie tylko 
        kompozycją, ale i techniką wyrobu, która pochodzi sprzed ery przemysłowej. Świeże nuty yuzu, ciepłe niuanse jałowca, pikantny 
        imbir i aromat sanshō łączą się w harmonijny i egzotyczny bukiet, który choć raz w życiu warto poczuć i spróbować.''')
        kinobi.image("AlcoholImages/kinobi.jpg")

        lillet = st.expander("**Lillet** _(Aperitiv, Francja)_")
        lillet.subheader("Lillet Blanc")
        lillet.write('''Lillet Blanc to likier o wspaniałej, błyszczącej złotej barwie. Liczne kwiatowe aromaty przeplatają
        się tu z nutami kandyzowanych pomarańczy, miodu, żywicy sosnowej i egzotycznych owoców. W
        ustach wyczuwalna jest paleta owoców egzotycznych i miodu, wraz z długim finiszem. Głównym
        szczepem w Lillet Blanc jest Semillon, dający temu likierowi pełną, soczystą strukturę.''')
        lillet.image("AlcoholImages/lillet/lilletblanc.jpg")
        lillet.subheader("Lillet Rosé")
        lillet.write('''Jest to mieszanka win (85%) i likierów, produkowanych z różnych odmian pomarańczy. Dojrzewa
        w beczkach, które znajdują się w piwnicy gorzelni w Podensac. W nosie lekkie aromaty jagód,
        kwiatu pomarańczy i grapefruita. Smak świeży, żywy i owocowy, zrównoważony, lekko kwaśny.''')
        lillet.image("AlcoholImages/lillet/lilletrose.jpg")

        luxardo = st.expander("**Luxardo** _(Likier, Włochy)_")
        luxardo.subheader("Luxardo Bitter")
        luxardo.write('''Klasyczny włoski likier o smaku słodkich i gorzki pomarańczy, rabarbaru oraz aromatycznych
        przypraw takich jak majeranek czy tymianek.''')
        luxardo.image("AlcoholImages/luxardo/luxardobitter.jpg")

        luxardo.subheader("Luxardo Maraschino")
        luxardo.write('''Likier ten destylowany jest z wyjątkowej odmiany wiśni Marascha, która została stworzona dzięki
        firmie luxardo. Macerowane są w jesionowych kadziach przez 3 lata. Barwa tego trunku jest
        przezroczysta a aromat zniewala owocową słodyczą wiśni. Smak aksamitnie gładki o miło
        zaokrąglonej końcówce.''')
        luxardo.image("AlcoholImages/luxardo/luxardomaraschino.jpg")

        malfy = st.expander("**Malfy** _(Gin, Włochy)_")
        malfy.caption('''Malfy destylowany jest w Totino Distilati leżącej u podnóża najwyższego szczytu Piemontu, Monte
        Viso. Destylarnia pracuje od 1906r. I obecnie należy do rodziny Vergnano. Wszystkie produkty
        firmy zostały oznakowane symbolem GQDI (Gin di Qualità Distillato), który jest włoskim symbolem
        jakości oraz autentyczności.''')
        malfy.subheader("Malfy")
        malfy.write('''Podstawowymi składnikami Malfy orginale są lokalny jałowiec, korą
        cynamonowa, kolendrą, korzenie arcydzięgla i lukrecji oraz skórka cytrynowa, pomarańczowa i
        grejpfrutowa, a bazowym alkoholem spirytus pszeniczny. Po destylacji gin poddawany jest filtracji
        na zimno i rozcieńczony lokalną górską wodą do 41% aby.
        Na pierwszy plan wybija się jałowiec i pomimo swej intensywności ni tłumi nut ziołowych
        przeplecionych cytrusem, w szczególności pomarańczą i cytryną.''')
        malfy.image("AlcoholImages/malfy/malfy-originale-gin.jpg")

        malfy.subheader("Malfy Rosa Pink Grapefruit")
        malfy.write('''Tak jak Malfy orginale zawiera w sobie lokalny jałowiec, korę cynamonową, kolendrę, korzenie
        arcydzięgla i lukrecji oraz skórkę cytrynową, pomarańczową i grejpfrutową, a bazowym alkoholem
        spirytus pszeniczny. Wszystkie składniki wraz ze skórkami Sycylijskich różowych grejpfrutów
        poddane są 36 godzinnej maceracji następnie destylowane metodą próżniową. Całość dopełnia
        niewielka ilość destylatu rabarbarowego.
        Silna woń grejpfrutów łączy się z subtelną nutką rabarbaru, w smaku z kolei lekką cytrusową
        słodycz równoważą jałowiec, kolendrą oraz goryczka arcydzięgla.''')
        malfy.image("AlcoholImages/malfy/MALFY-ROSA.jpg")

        malfy.subheader("Malfy Con Arancia Blood Orange")
        malfy.write('''Zawiera w sobie lokalny jałowiec, korę cynamonową, kolendrę, korzenie arcydzięgla i lukrecji oraz
        skórkę cytrynową, pomarańczową i grejpfrutową, a bazowym alkoholem spirytus pszeniczny.
        Wszystkie składniki wraz z Sycylijskimi czerwonymi pomarańczami poddane są 36 godzinnej
        maceracji następnie destylowane metodą próżniową.
        Na podniebieniu oferuje ujmujące nuty grejpfruta, cytryny, jałowca, skórki cytrusów, czerwonej
        pomarańczy oraz pieprznych przypraw.''')
        malfy.image("AlcoholImages/malfy/malfyarancia.jpeg")

        malfy.subheader("Malfy Con Limone")
        malfy.write('''Włoski gin destylowany z jałowcem oraz dojrzewającymi w słońcu Sycylii cytrynami. Recepturę
        trunku uzupełniają także kolendra, kasja oraz arcydzięgiel. Dwa ze składników zostają utajnione
        przez gorzelnię, a destylacja odbywa się w stalowych alembikach próżniowych.''')
        malfy.image("AlcoholImages/malfy/malfylimone.jpg")

        makers = st.expander("**Maker's Mark** _(Bourbon)_")
        makers.subheader("Maker's Mark")
        makers.write('''Formuła zawiera 70% kukurydzy, 16% ozimej pszenicy i 14% jęczmiennego słodu. Jak każdy
        burbon jest starzony co najmniej 2 lata w nowych wypalanych beczkach z białego dębu.''')
        makers.image("AlcoholImages/makers/MAKERS-MARK-BOURBON-0,7L.jpg")
        makers.write('''**:blue[Aromat]**: miód , wanilia, sucha skórka pomarańczowa, suszone daktyle, rodzynki, mleczna
        czekolada, cynamon, gałka muszkatołowa i dąb.<br>
        **:blue[Smak]**: słodki, wanilia, mleczne krówki, miód, kakao w proszku, brzoskwinie, rodzynki, prażone
        orzeszki, nuty tytoniu i dębu.<br>
        **:blue[Finisz]**: długi, z nutami karmelu, wanilii, skórki pomarańczowej i dębu.''', unsafe_allow_html=True)

        makers.subheader("Maker's 46")
        makers.write('''2005r. rozpoczął serię eksperymentów, z których próba nr 46 okazała się udaną. Po zakończeniu
        podstawowej maturacji standardowy Maker’s Mark opuszcza beczkę, w której zostaje
        zamontowanych 10 wyprażonych klepek z francuskiego dębu. Destylat wraca do tak
        zmodyfikowanej beczki na 10 do 12 tygodni. W tym czasie beczka spoczywa w najchłodniejszym
        miejscu magazynu leżakowego. Francuski dąb potęguje nut karmelu i wanilii oraz dodaje whisky
        lekkiej pikanterii.''')
        makers.image("AlcoholImages/makers/maker-s-mark-no-46-700ml.jpg")
        makers.write('''**:blue[Aromat]**: dość kompleksowy, ekstrakt wanilii, karmel, syrop klonowy, drożdżówki cynamonowe,
        kandyzowana skórka pomarańczowa, pieczone jabłka i dąb.<br>
        **:blue[Smak]**: sporo karmelu i kremu waniliowego, płatki śniadaniowe z miodem, szarlotka poproszona
        cynamonem, szczypta gali muszkatołowej i dość silne nuty dębowe.<br>
        **:blue[Finisz]**: dość długi, z nutami karmelu, wanilii, słodkich przypraw, dębu i w mniejszym stopniu
        tytoniu.''', unsafe_allow_html=True)

        martell = st.expander("**Martell** _(Cognac)_")
        martell.subheader("Martell VS Fine")
        martell.write('''Jest to wydestylowany w pojedynczej destylarni z gron pochodzących z okręgów uprawy Grande i
        Petite Champagne, Les Borderies i Fins Bois i starzony przez co najmniej 2 lata e beczkach z
        francuskiego dębu z Tronçais.''')
        martell.image("AlcoholImages/martell/martellvs.jpg")
        martell.write('''**:blue[Aromat]**: owocowy i delikatnie floralny, wanilia, karmel, bukiet polnych kwiatów, pigwa, odrobina
        suchych ziół, siana i dębu.<br>
        **:blue[Smak]**: przyjemnie zbalansowany, rodzynki, suszone śliwki i wiśnie, karmel, marcepan, nuty
        cynamonu i kakao w proszku.<br>
        **:blue[Finisz]**: średnio długi, z nutami suszonych owoców, karmelu, prażonych migdałów, kroplą likieru
        fiołkowego i dębu.''', unsafe_allow_html=True)

        martell.subheader("Martell Blue Swift")
        martell.write('''Pierwszy koniak V.S.O.P finiszowany w beczkach po burbonie mniej niż sześć miesięcy. Nazwa
        trunku odnosi się do jerzyka, ptaka który może lecieć nieprzerwanie przez kilka dni pokonując
        Atlantyk.''')
        martell.image("AlcoholImages/martell/martellblueswift.jpg")
        martell.write(''' **:blue[Aromat]**: śliwki, rodzynki, brzoskwinie, crème brulèe, miodowe orzech, cynamon i dąb.<br>
         **:blue[Smak]**: bogaty, owocowy, czereśnie, śliwki, figi, rodzynki, wanilia, karmel, cynamon, nuty
        kandyzowanego imbiru i dębu.<br>
         **:blue[Finisz]**: dość długi, z nutami wanilii, karmelu, syropu klonowego, rodzynek, suszonych śliwek i
        jabłek, cynamonu i dębu.''', unsafe_allow_html=True)

        martell.subheader("Martell V.S.O.P")
        martell.write('''Starzony przez co najmniej 4 lata e beczkach z francuskiego dębu z Tronçais.''')
        martell.image("AlcoholImages/martell/martellvsop.jpg")
        martell.write(''' **:blue[Aromat]**: Owocowy, pełny. Akcenty limonki, pigwy, śliwek i lukrecji. Nieco dębiny i orzechów
        lakowych.<br>
         **:blue[Smak]**: Miękki, gładki i złożony. Bogactwo akcentów owocowych, w tym również kandyzowanych
        owoców. Odrobina korzeni i orzechów.<br>
         **:blue[Finisz]**: Długi, z akcentami owoców i korzeni''', unsafe_allow_html=True)

        martell.subheader("Martell X.O.")
        martell.write('''Kupaż eaux-du-vie starzonych od 10 do 35 lat wydestylowanych w gron pochodzących z okręków
        uprawy Grande Champagne i Les Borderies.''')
        martell.image("AlcoholImages/martell/martellxo.jpg")
        martell.write('''**:blue[Aromat]**: przyjemnie pikantny, czarny i czerwony pieprz, świąteczny piernik, orzech włoskie,
        suszone figi, pieczone jabłka, nuty drewna sandałowego i wosku.<br>
        **:blue[Smak]**: bardzo bogaty, suszone figi, wiśnie i śliwki, rodzynki, nugat orzechowy, waniliia, gałka
        muszkatołowa i kojąca goryczka dębu.<br>
        **:blue[Finisz]**: długi, pikantny z subtelną nutą floralną, cynamon, rodzynki, figi, czerwone owoce i dąb.''', unsafe_allow_html=True)

        martell.subheader("Martell Cordon Bleu")
        martell.write('''Stworzony w 1912r. Skomponowany z ponad stu różnych destylatów pochodzących z regionów
        Petite Champagne, Grande Champagne, Fins Bois i Borderies, po kupażowaniu leżakuje w
        beczkach z dębu francuskiego.''')
        martell.image("AlcoholImages/martell/cognac-martell-cordon-bleu.jpg")
        martell.write('''**:blue[Aromat]**: Śliwki i jabłka, kawa, prażone migdały, cynamon, kwiaty pomarańczy, miód i wosk
        pszczeli.<br>
        **:blue[Smak]**: krągły i łagodny. Akcenty owoców, migdałów, miodu, cynamonu.<br>
        **:blue[Finisz]**: długi, z akcentami owoców i przypraw.''', unsafe_allow_html=True)

        martell.subheader("Martell Cohiba")
        martell.write('''Wspólny projekt Martella i Habanos Cigars. Do jego stworzenia wykorzystano eaux-de-vie z
        okręgu Grande Champagne starzone od 40 do 50 lat. Oczywiście najlepiej smakuje z odpowiednio
        długo starzonym cygarem.''')
        martell.image("AlcoholImages/martell/martellcohiba.jpg")
        martell.write('''**:blue[Aromat]**: miękki lecz kompleksowy, orzechy laskowe, miód, wanilia, prażone ziarna kawy, suszone
        morele, leśne jagody, nuty tytoniu i suchych kwiatów.<br>
        **:blue[Smak]**: znakomicie zbalansowany, mieszanka suszonych owoców, prażone migdały i orzechy,
        cynamon, nuty anyżku i lukrecji i pięknie wplecione nuty dębu.<br>
        **:blue[Finisz]**: bardzo długi i elegancki, suszone owoce, prażone orzechy, dąb odrobina cynamonu.''', unsafe_allow_html=True)

        martini = st.expander("**Martini** _(Aperitivo/Wermut, Włochy)_")
        martini.subheader("Martini Riserva")
        martini.write('''Kolekcja Martini Vermouth di Torino składa się z Martini Riserva Speciale Rubino i Martini Riserva
        Speciale Ambrato. Obydwa zostały stworzone w hołdzie dla tradycyjnych metod stosowanych
        przez pierwszych mistrzowskich zielarzy Martini.
        Martini Reserva Speciale Rubino jest wykonane przy wykorzystaniu win Langhe DOC Nebbiolo i
        zmieszane ze stężonym ekstraktem roślinnym: wyciągiem z włoskiego świętego ostu i
        czerwonego drzewa sandałowego. Leżakuje w dębowej beczce ponad dwa miesiące. Jego nazwa
        jest jednocześnie określeniem koloru - "rubino" to włoski odpowiednik „ruby".
        Martini Riserva Speciale Ambrato jest produkowane przy użyciu wina Moscato d'Asti DOCG, by
        stworzyć lekko gorzki smak. Nazwa pochodzi od koloru - ambrato to po włosku bursztyn.''')
        martini.image("AlcoholImages/martini/riserva.jpeg")

        martini.subheader("Martini Bitter")
        martini.write('''Do przygotowania purpurowego, wytrawnego Martini Riserva Speciale Bitter wykorzystuje się 20
        ziół oraz przyprawy korzenne. W tym trzy niezwykle rzadkie i unikalne: szafran, korę krocienia oraz
        angosturę.W skład Martini Bitter wchodzi bylica pochodząca z lokalnych upraw we włoskiej
        Pancalieri. To ona nadaje gorzko-ziołowy charakter trunku.''')
        martini.image("AlcoholImages/martini/bitter.png")

        martini.subheader("Martini Fiero")
        martini.write('''Naturalny ekstrakt z czerwonej pomarańczy nadaje mu wyjątkowy, wyraźnie dominujący posmak.''')
        martini.image("AlcoholImages/martini/fiero.png")

        metaxa = st.expander("**Metaxa** _(Spirit drink, Grecja)_")
        metaxa.caption('''**Co oznaczają gwiazdki na Metaxie?**<br>
        Za tajemniczymi gwiazdkami, które można znaleźć na etykiecie, kryje się wewnętrzna
        segmentacja i stopniowanie produktu, zatem nie należy dosłownie przypisywać wieku destylatów
        do ilości gwiazdek. Jednakże im większa liczba gwiazdek na butelce, tym mamy do czynienia z
        dłużej leżakowanym produktem. Jest to wprowadzone z powodu tego, że nie wszystkie produkty
        Metaxy są oznaczone gwiazdkami! Najbardziej szlachetne i najstarsze destylaty trafiają do takich
        wariantów jak Grande Fine w pięknej, porcelanowej butelce czy Private Reserve produkowana
        tylko raz w roku w bardzo małych partiach. Wyróżnić warto również Metaxę Angel`s Treasure z
        długo dojrzewających destylatów czy dwie wersje o nazwie AEN, które powstały, by uczcić 120. i
        130. rocznicę powstania firmy.''', unsafe_allow_html=True)
        metaxa.write('''Metaxa jest jedynym w swoim rodzaju trunkiem alkoholowym. Nie można go sklasyfikować jako
        Brandy. Definicja tej kategorii mówi o alkoholu dwukrotnie destylowanym z wina lub innego soku
        owocowego poddanego fermentacji. Choć faktycznie pierwszym etapem stworzenia Metaxy jest
        powstanie destylatu z wina, to jednak późniejsze etapy produkcji czynią ten trunek wyjątkowym.
        Nad całością czuwa Constantinos Raptis, który jest piątym pokoleniem mistrzów destylacji i
        blendowania. Pierwszym etapem jest powstanie wina, które tworzy się tylko z trzech odmian
        winorośli: Savatiano, Sultanina i Black Corinth. Następnie poddaje się je destylacji i leżakowaniu
        w piwnicach obecnego domu Metaxy, który znajduje się w Kiffisii w północnej części Aten. W tym
        czasie Constantinos dobiera wina typu Muscat z wyspy Samos, która słynie z jej najlepszych
        odmian. Następnie łączy je wraz z wyselekcjonowanymi destylatami winnymi, które wspólnie
        znów leżakują w beczkach wykonanych z francuskiego dębu Limousin. Ostatnim etapem
        zwieńczającym proces produkcji jest dodanie specjalnej mieszanki ziół i roślin
        śródziemnomorskich wśród, których warto wyróżnić płatki róż. To wszystko wpływa na
        wyjątkowość Metaxy.''')
        metaxa.image('AlcoholImages/metaxa.jpg')

        midori = st.expander("**Midori** _(Likier, Japonia)_")
        midori.write('''Midori (jap. "zielony") to legendarny likier melonowy. Produkowany jest od 1978 roku przez firmę
        Suntory w Japonii. Firma Suntory znana jest również z produkcji doskonałych whisky Single Malt.
        Likier Midori wytwarzany jest wyłącznie z naturalnych składników, spośród których głównym jest
        dojrzały, soczysty i słodki melon.''')
        midori.image("AlcoholImages/Midori.jpg")

        mosho = st.expander("**Monkey Shoulder** _(Whisky, Szkocja, Blended malt)_")
        mosho.subheader("Monkey Shoulder")
        mosho.write('''Oryginalną formuła wymienia trzy single malty pochodzące z gorzelni należących do spółki
        (Glenfiddich, Balvenie i Kininvie) starzone w beczkach po burbonie. Nazwa Monkey Shoulder
        nawiązuje do urazu barku często nękającego pracowników słodowni, przeżuwających drewnianymi
        łopatami tony jęczmienia.''')
        mosho.image("AlcoholImages/monkeyshoulder/monkey-shoulder-blended-malt.jpg")
        mosho.write('''**:blue[Aromat]**: słodowo-owocowy, jabłka, gruszki, ananasy, mleczne krówki, karmel, wanilia, miód i ślad
        dębowych wiórów. <br>
        **:blue[Smak]**: łagodny, słodkie płatki śniadaniowe, jabłka, gruszki, banany, skórka cytrynowa, miód,
        wanilia, nugat orzechowy, ślad lukrecji i dębu. <br>
        **:blue[Finisz]**: średnio długi, z nutami nugatu orzechowego, letnich owoców, skórki pomarańczowej,
        wanilii i dębu.''', unsafe_allow_html=True)

        mosho.subheader("Monkey Shoulder Smokey")
        mosho.write('''Dymna odsłona popularnej Blended Malt Monkey Shoulder wzbogacona dodatkiem whisky
        torfowej – najprawdopodobniej pochodzącej z uruchomionej w 2007 roku gorzelni Ailsa
        Bay. Smokey Monkey posiada zdecydowanie dymny, smolisty aromat, zbalansowany łagodnymi
        nutami miodu, toffi, wanilii, jabłek, brzoskwiń oraz cytrusów. W smaku jest dość łagodna i
        owocowa, z lekką dymnością, kremową słodyczą oraz akcentami orzechów i przypraw.''')
        mosho.image("AlcoholImages/monkeyshoulder/Monkey-Shoulder-Smokey-Monkey-Batch-9.jpg")

        monkey = st.expander("**Monkey 47** _(Gin, Niemcy)_")
        monkey.write('''Niemiecki gin destylowany w gorzelni Christopha Kellera, zlokalizowanej w Schwarzwaldzie.
        Nazwa nawiązuje do małpki o imieniu Max którą to zasponsorował Montgomery Collins by
        odbudować zniszczone zoo. Liczba 47 nawiązuje do ilości ziół, roślin i owoców używanych do
        produkcji oraz mocy trunku i pijany był zazwyczaj o 4:47. Wiodącymi składnikami ginu są: jałowiec,
        lawenda, piżmian, aframon madagaskarski, pysznogłówka szkarłatna, szyszki świerkowe,
        prawoślaz lekarski kolendra.''')
        monkey.image('AlcoholImages/monkey47.jpg')
        monkey.write('''**:blue[Aromat]**: pełny z bogactwem ziół, owoców cytrusowych, kwiatów, jałowca i przypraw.<br>
        **:blue[Smak]**: bogaty i głęboki z akcentami owoców leśnych, cytrusów, kwiatów, jałowca, przypraw i
        korzeni.<br>
        **:blue[Finisz]**: długi i intensywny z bogactwem przypraw, ziół i cytrusów.''', unsafe_allow_html=True)

        olmeca = st.expander("**Olmeca** _(Tequila)_")
        olmeca.subheader("Olmeca Altos Blanco")
        olmeca.write('''Olmeca Altos Plata Blanco produkowana w 100% z niebieskiej agawy. Jest tequilą, która przyciąga
        swoją autentycznością: niezwykle łagodna, o wyjątkowym charakterze, powstaje w sercu Meksyku,
        czyli w regionie Los Altos. Jej wyjątkowo subtelny smak to efekt tradycyjnych metod produkcji oraz
        podwójnej destylacji.''')
        olmeca.image("AlcoholImages/olmeca/TEQUILA-OLMECA-BLANCO-CLASICO-0,7L.jpg")
        olmeca.write('''Olmeca Altos Plato do dokonała tequilla o niepowtarzalnym, ziołowym aromacie gotowanej
        agawy z subtelnymi nutami owoców cytrusowych, zwłaszcza cytryny. Słodki smak doskonale
        zrównoważony limonkowym akcentem. Finisz długi, dobrze zbalansowany.''')

        olmeca.subheader("Olmeca Altos Reposado")
        olmeca.write('''Olmeca Altos Reposado Gold charakteruzuje się niezwykle bogatym aromatem obfitującym w
        świeże, cytrusowe nuty pomarańczy i grapefruitów z delikatnie słodkim akcentem wanilii i
        wyczuwalną nutą drzewną. W smaku początkowa słodycz powoli ustępuje delikatnej nucie tanin i
        ponownie cytrusów z posmakiem gotowanej agawy. Finisz długi, bardzo dobrze zbalansowany.''')
        olmeca.image("AlcoholImages/olmeca/olmecareposado.jpg")

        colombo = st.expander("**Orange Colombo** _(Aperitivo, Francja)_")
        colombo.write('''Aperitif, z wyczuwalnymi aromatami kandyzowanej pomarańczy i miodu. Ten likier to kompozycja
        gorzkich i słodkich pomarańczy, kory chinowca, cukru trzcinowego i różowego wina, leżakowana w
        dębowych beczkach przez 6 tygodni.''')
        colombo.image('AlcoholImages/orangecolombo.jpg')

        ostoya = st.expander("**Ostoya** _(Wódka, Polska, Pszenica)_")
        ostoya.write('''Wóda z Bieszczad destylowana ze słodu pszenicznego, delikatna i słodka w smaku.''')
        ostoya.image("AlcoholImages/ostoya.jpg")

        oxley = st.expander("**Oxley** _(Gin, Anglia, London dry)_")
        oxley.write('''Jeden z pierwszych ginów wyprodukowanych przy użyciu próżniowej destylacji (destylacja pod
        zmniejszonym ciśnieniem). Po trwającej 15 godzin maceracji 14 składników botanicznych -
        jałowiec, cytryny, grapefruity, pomarańcze, tawuła, wanilia, anyż, korzenie irysa i lukrecji, ziarna
        raju, kakao, cynamon, gałka muszkatołowa i kolendra - destylowane jest w kolumnie próżniowej w
        temp. Sięgającej -5°C. Destylacja w podobnych warunkach gwarantuje pełną ekstrakcję
        substancji smakowych i aromatycznych nie eksponując składników botanicznych na wysoką
        temp. a także wyklucza powstawanie przedgonów i niedogonów.''')
        oxley.image("AlcoholImages/oxley.jpg")
        oxley.write('''Oxley to niezwykle elegancki gin o klasycznym profilu - jałowiec, cytrusy i tony floralne pięknie
        współpracujące z odsuniętymi nieco na drugi plan korzennymi przyprawami, balansowanymi do
        pewnego stopnia słodyczą wanilii.''')

        patron = st.expander("**Patron** _(Tequila)_")
        patron.subheader("Patron Silver")
        patron.write('''Roca Patron Silver to fenomenalna tequila rzemieślnicza wyłącznie z niebieskiej agawy: zarówno
        alkohol, jak i przedmioty i urządzenia wykorzystywane do jego wyrobu, produkowane są ręcznie, z
        zachowaniem dawnych metod i zasad recyklingu, a destylacja przebiega w bardzo ograniczonych
        partiach. Zgodnie z historycznym zwyczajem piñas (rdzenie agawy) gotowane są przez 79 godzin
        w małych, ceglanych piecach, a wcześniej miażdżone dwutonowym kołem tahona. Dzięki temu
        tequilę tę wyróżnia śmiały i zdecydowany smak, bogaty w słodkie aromaty cytrusowe.''')
        patron.image("AlcoholImages/patron/patronsilver.jpg")
        patron.write('''**:blue[Zapach]**: świeże owoce cytrusowe, zwłaszcza limonka. <br>
        **:blue[Smak]**: ziemisty i słodki z akcentami białego pieprzu, dyni, agawy i kandyzowanych cytrusów. <br>
        **:blue[Finisz]**: harmonijny z nutami białego i zielonego pieprzu.''', unsafe_allow_html=True)

        patron.subheader("Patron Anejo")
        patron.write('''Mieszanina tequili leżakowana przez minimum 12 miesięcy w niewielkich dębowych beczkach z
        dębu białego.''')
        patron.image("AlcoholImages/patron/patronanejo.jpg")
        patron.write(''' **:blue[Zapach]**: pieczona agawa, karmel<br>
         **:blue[Smak]**: agawa, karmel, odrobina przypraw korzennych, pieprz<br>
         **:blue[Finisz]**: średnio długi, karmelowe pieprzowy''', unsafe_allow_html=True)

        patron.subheader("Patron Reposado")
        patron.write('''Przed zabutelkowaniem alkohol spędził w dębowych beczkach od 3 do 6 miesięcy. Dzięki temu
        tequilę Roca Patron Reposado wyróżnia wyrazisty lecz harmonijny smak z przyjemnym,
        waniliowo-cytrusowym aromatem.''')
        patron.image("AlcoholImages/patron/patronreposado.jpg")
        patron.write('''**:blue[Zapach]**: wanilia, dębina, dojrzałe owoce cytrusowe.<br>
        **:blue[Smak]**: słodki z akcentami imbiru, karmelu i umami.<br>
        **:blue[Finisz]**: bardzo długi z nutami pikantnymi i taninowymi.''', unsafe_allow_html=True)

        passoa = st.expander("**Passoa** _(Likier, Francja)_")
        passoa.write('''Znakomity francuski likier o smaku owoców egzotycznych, produkowany z soku owoców
        marakui. Jest to świeży, egzotyczny i aromatyczny likier o niskiej zawartości alkoholu, uzyskany z
        mieszanki kwiatów i owoców tropikalnych.''')
        passoa.image("AlcoholImages/Passoa.jpg")

        peper = st.expander("**Pepperciocco** _(Likier, Włochy)_")
        peper.write('''Słodki, czekoladowy likier z nutami ostrej papryczki, o ciemno bursztynowej brawie.''')
        peper.image("AlcoholImages/pepperciocco.jpg")

        pyrat = st.expander("**Pyrat XO Reserve** _(Rum/Spirit drink, Karaiby)_")
        pyrat.write('''Mieszanina rumów karaibskich, dojrzewanych w dębowych beczkach po amerykańskim burbonie
        i beczkach z dębu francuskiego typu Limousin przez okres nawet 16 lat.
        Tradycyjny rum na bazie melasy z trzciny cukrowej.''')
        pyrat.image('AlcoholImages/pyrat.jpg')
        pyrat.write('''**:blue[Aromat]**: karmel, miód, cytrusy, melasa.<br>
        **:blue[Smak]**: skórka pomarańczy,, wanilia, karmel, miód, przyprawy.<br>
        **:blue[Finisz]**: długi, korzenny.''', unsafe_allow_html=True)

        ricard = st.expander("**Ricard Pastis** _(Aperitivo, Francja)_")
        ricard.write('''Ricard Pastis de Marseille to wyjątkowy trunek pochodzący prosto z Francji. Posiada ładny,
        bursztynowy kolor. Aromat wyróżnia się nutami trawy, anyżu, a także lukrecji. W smaku wyczuć
        można z kolei akcenty anyżu, kopru włoskiego i ziół, jak również delikatnej lukrecji, mięty i cytryny.
        Wszystko to wygasa do długiego, trwającego finiszu z lukrecją i ziołami.''')
        ricard.image("AlcoholImages/ricard.jpg")

        sambuca = st.expander("**Sambuca** _(Likier, Włochy)_")
        sambuca.write('''Bezbarwny pochodzący z Włoch likier anyżkowo-owocowo-ziołowy, zawierający zazwyczaj 38 do
        40% alkoholu. Jest produkowany na bazie kwiatów czarnego bzu (wł. Sambuco), anyżu
        gwiaździstego, kopru włoskiego, lukrecji oraz soków.''')
        sambuca.image("AlcoholImages/sambuca-bianco.jpg")

        santa = st.expander("**Santa Teresa 1796** _(Rum, Karaiby)_")
        santa.write('''Ron Santa Teresa jest jednym z pierwszych producentów rumu na Karaibach.
        Santa Teresa 1796 Ron Antiguo de Solera to rum produkowany metodą "solera" oraz
        dojrzewający ponad 15 lat w beczkach z francuskiego dębu Limousin.''')
        santa.image('AlcoholImages/santateresa.jpg')
        santa.write('''**:blue[Zapach]**: Słodki aromat owoców, miodu i czekolady.<br>
        **:blue[Smak]**: Delikatny i bogaty, z nutami tytoniu, skóry, nut dymu oraz dębu.<br>
        **:blue[Finisz]**: Nuty dębiny, lekko wytrawny.''', unsafe_allow_html=True)

        scapa = st.expander("**Scapa** _(Whisky, Szkocja, Single malt, Highland)_")
        scapa.subheader("Scapa Glansa")
        scapa.write('''Do pierwszej destylacji używa się alembiku typu lomond. Zestawiono ją z destylatów starzonych
        w beczkach po burbonie i finiszowana w beczkach, w których wcześniej dojrzewała whisky
        dymno-torfowa. „Glansa” w wolnym tłumaczeniu oznacza „niebo przed burzą”.''')
        scapa.image("AlcoholImages/scapa/scapaglansa.jpg")
        scapa.write(''' **:blue[Aromat]**: łagodny, owocowy i delikatnie dymny, brzoskwinie, ananasy, wanilia, miód, płatki
        śniadaniowe i nieco siana.<br>
         **:blue[Smak]**: jabłka i brzoskwinie, kandyzowana skórka pomarańczowa, wanilia, miód, karmel, i
        delikatne nuty dymne w tle.<br>
         **:blue[Finisz]**: średnio długi, z nutami zadymionej wanilii i miodu.''', unsafe_allow_html=True)

        scapa.subheader("Scapa Skiren")
        scapa.write('''Scapa to obok Loch Lomond jedyna szkocka destylarnia ciągle używająca alembiku typu lomond,
        w którym kontakt oparów z miedzią kontrolowany jest poprzez system perforowanych płytek.
        Skiren to młoda whisky typu small batch, starzona wyłącznie w beczkach po burbonie pierwszego
        napełnienia i butelkowana bez określenia wieku. Jej nazwa pochodzi z języka staronordyskiego i
        oznacza „bezkresny lazur nieba”.''')
        scapa.image("AlcoholImages/scapa/scapa-skiren.jpg")
        scapa.write('''**:blue[Aromat]**: słodki, wanilia, miód, wata cukrowa, szarlotka, skórka cytrynowa, nuta anyżku i odległy
        ślad morskiej bryzy.<br>
        **:blue[Smak]**: łagodny i słodki, zielone jabłka, płatki śniadaniowe ze szczyptą cynamonu, walilia, toffi i
        orzeszki prażone w miodzie.<br>
        **:blue[Finisz]**: niezbyt długi, jabłka, brązowy cukier i delikatne nuty orzechowe.''', unsafe_allow_html=True)

        small = st.expander("**Small Batch Bourbon Collection** _(Jim Beam)_")
        small.caption('''''')
        small.subheader("Baker's")
        small.write('''Trzy z pośród czterech whiskey, które wchodzą w skład tej kolekcji, w tym Baker’s, bazują na tym
        samym rodzaju słodu , jednak każda z nich ma nieco inne cechy i inny profil smakowy.
        Baker’s zawiera 53,5% alkoholu i ma siedem lat. Dojrzewanie kończy się w momencie, gdy trunek
        nabierze charakteru beczki, w której leżakuje.''')
        small.image("AlcoholImages/smallbatchbourbon/bakers.jpg")
        small.write('''**:blue[Aromat]**: susz owocowy, cynamon, goździki, pieprz, kakao w proszku, wanilia, karmel, zwęglony
        dąb i trochę skóry.<br>
        **:blue[Smak]**: słodko-pikantny, crème brulée, toffi, wanilia, prażone migdały, cynamon, goździki, nuty
        tytoniu, skóry i nadwęglonej dębiny.<br>
        **:blue[Finisz]**: długi i pełny, z nutami karmelu, kakao, wanilii, dżemu z gorzkich pomarańczy i
        nadwęglonego dębu.''', unsafe_allow_html=True)
        small.caption("Patronem bourbonu jest Baker Beam - były menedżer Jim Beam Distillery w Clermont.")

        small.subheader("Basil Hayden's")
        small.write('''Jej historia sięga 1796 roku, kiedy Master Distiller Basil Hayden złamał zasady produkcji bourbona
        i do zacieru oprócz kukurydzy dosypał sporą ilość żyta. Whiskey do dzisiaj produkowana jest w
        tradycyjny sposób i posiada najbardziej "żytni" aromat z wszystkich bourbonów. Jest starzona w nowych beczkach 
        przez co najmniej 8 lat.''')
        small.image("AlcoholImages/smallbatchbourbon/basil-hayden-s.jpg")
        small.write('''**:blue[Aromat]**: wyważony i lekko pikantny z nutami mięty pieprzowej, herbaty, miodu, imbiru, dębu, żyta
        i grejpfruta.<br>
        **:blue[Smak]**: bogaty z nutami czarnego pieprzu, miodu, skórki z pomarańczy, mięty, siana, palonego
        dębu, imbiru i żyta.<br>
        **:blue[Finisz]**: wytrawny z nutami wanilii, chili i dębu.''', unsafe_allow_html=True)
        small.caption("Bourbon nosi imię jednego z wczesnych destylatorów Kentucky.")

        small.subheader("Booker's")
        small.write('''Bourbon niefiltrowany, butelkowany prosto z beczki. Whiskey destylowana jest w Gorzelni Jima
        Beama w Clermont w stanie Kentucky. Komponowana jest z destylatów starzonych około 7 lat, w
        nowych dębowych beczkach, w centralnych miejscach magazynu, gdzie warunki do leżakowania
        są najlepsze. Booker's to najmocniejszy bourbon z kolekcji.''')
        small.image("AlcoholImages/smallbatchbourbon/bookers.jpg")
        small.write('''**:blue[Aromat]**: intensywny z nutami dębu, węgla drzewnego, wanilii, lekki aromat kawy tytoniu, karmelu,
        suszonej śliwki, cynamonu i imbiru.<br>
        **:blue[Smak]**: mocny i zdecydowany z nutami wanilii, karmelu, palonego dębu, tytoniu, drzewa
        cedrowego, cygara, śliwki i pomarańczy, kawy<br>
        **:blue[Finisz]**: długi i intensywny z nutami pikantnych przypraw, tytoniu i węgla drzewnego''', unsafe_allow_html=True)
        small.caption("Pierwszy bourbon w naturalnej formie. Stworzony przez Fredericka Bookera Noe w 1988 roku")

        germain = st.expander("**St. Germain** _(Likier, Francja)_")
        germain.write('''Francuski likier owocowy o intensywnym aromacie kwiatów bzu, zbieranych późną wiosną we
        francuskich Alpach.''')
        germain.image('AlcoholImages/stgermain.jpg')
        germain.write('''Likier mieni się złotymi i zielonymi refleksami; nos pełen jest początkowo słodkich owoców- liczi,
        mango, marakui, kolejne wyczuwalne akcenty to limonka, cytryny, pomarańcze i mięta pieprzowa,
        w finale odsłania się główny składnik likieru- kwiat czarnego bzu i owoce leśne (jagoda,
        poziomka). <br>
        W smaku kremowy, gładki i mocno owocowy, zdominowany przez świeże akcenty liczi,
        brzoskwini, gruszki i cytrusów takich jak soczyste pomarańcze i grapefruity. Przyjemny i długi
        finisz zaskakuje nutami kwiatowymi, smakiem kokosa, orzecha laskowego i marakui.''', unsafe_allow_html=True)

        strega = st.expander("**Strega** _(Likier, Włochy)_")
        strega.write('''Włoski likier ziołowo-korzenny, produkowany od 1860 roku, zawierający 40 proc. alkoholu.
        Według legendy jego receptura została stworzona przez czarownice z Benevento. Strega ma
        żółtawo-zieloną barwę i dość intensywny korzenny zapach szafranu, cynamonu i lukrecji. Do
        podstawowych składników likieru należą: piołun, owoc jałowca i mirra. Zalicza się go do
        najlepszych i najdroższych włoskich likierów.''')
        strega.image("AlcoholImages/strega.jpg")

        tan = st.expander("**Tanqueray no.10** _(Gin, Szkocja)_")
        tan.write('''Posiada unikalne cechy, które odróżniają go od innych. Pierwsza to dodatek świeżych owoców –
        różowego grejpfruta z Florydy i limonek z Meksyku w miejsce powszechnie stosowanych
        suszonych skórek cytrusowych. Druga to dodatek rumianku, dzięki któremu Tanqueray No. Ten
        Gin zyskuje smak łagodny i zrównoważony. Skład ginu zawiera osiem ingrediencji: jałowiec,
        korzeń arcydzięgla, nasiona kolendry, korzeń lukrecji, świeżego grejpfruta, świeżą limonkę, świeżą
        pomarańczę oraz rumianek. Składniki przed destylacją są macerowane w spirytusie zbożowym.
        Nazwa tej edycji nawiązuje do małego alembika o numerze 10 o pojemności 500L, w którym
        próbowano wielu receptur.''')
        tan.image("AlcoholImages/tanqueray.jpg")
        tan.write('''**:blue[Aromat]**: świeży z nutami grejpfruta, limonki, kolendry, jałowca i kwiatów.<br>
        **:blue[Smak]**: intensywny z akcentami jałowca, kolendry, pomarańczy, limonki i ziół.<br>
        **:blue[Finisz]**: średnio długi z przewagą owoców cytrusowych i jałowca.''', unsafe_allow_html=True)

        wyborowa = st.expander("**Wyborowa Exquisite** _(Wódka, Polska, Żyto)_")
        wyborowa.write('''Wyborowa Exquisite ma oddzielną linię produkcyjną i jest wyrabiana z jednej tylko odmiany żyta z
        jednego tylko pola, które znajduje się w Turwi pod Poznaniem.''')
        wyborowa.image("AlcoholImages/wyborowa-exquisite.jpg")

        zucca = st.expander("**Zucca Rabarbaro** _(Likier, Włochy)_")
        zucca.write('''Włoski likier o kolorze głębokiego i intensywnego hebanu, produkowany z rabarbaru z dodatkiem
        ziół, nasion kardamonu i innych.
        Ujawnia wyraźne aromaty rabarbaru i propolisu, wraz z gronem aromatycznych i leczniczych ziół.''')
        zucca.image("AlcoholImages/Zucca-Rabarbaro-0,7.jpg")


        st.caption(":grey[Materiały: Adrian Kot, Edycja: Aleksander Dziedzic]")
    elif submenu == "Piwo":
        st.header("Opis piw")
        st.subheader("Bierhalle Pills (lager)")
        st.write('''Pils to najbardziej rozpowszechniony gatunek piwa na świecie 
                  (mocno powiązany z pilsnerem). Piwo jasne, dolnej fermentacji (przypis poniżej), 
                  istensywna chmielowa goryczka połączona ze smakiem słodu jęczmiennego. <br> <br>
                  Alkohol: 5.0%''', unsafe_allow_html=True)

        st.subheader("Bierhalle Weizen (pszeniczne)")
        st.write('''Weizen jest piwem górnej fermentacji (przypis poniżej) 
                  o wyczuwalnym zapachu: bananowo-goździkowym, cynamonu oraz aromatycznego chmielu. 
                  Goryczka przeplata się ze smakiem pszenicznego słodu. Większa ilość "bąbelków"  
                  sprawia, że piwo pszeniczne nabiera lekko kwaskowatego smaku i doskonale gasi 
                  pragnienie. Słód pszeniczny stanowi ponad 50% całkowitego zasypu. <br> <br>
                  Alkohol: 5.2%''', unsafe_allow_html=True)
        st.subheader("Bierhalle Marcowe (podwójnie słodowany lager)")
        st.write('''Piwo marcowe, zwane również Oktoberfestbier, dawniej warzone było 
                  tylko sezonowo. Dzisiaj, dzięki nowoczesnym systemom chłodzenia można produkować 
                  je okrągły rok. Piwo jest pełne smaków pochodzących z mieszaniny słodów 
                  jęczmiennych i aromatycznego chmielu. <br> <br>
                  Alkohol: 5.2%''', unsafe_allow_html=True)
        st.subheader("Pilsner Urquell")
        st.write('''Prekursor piw typu lager. Tworzony metodą równoległego warzenia. 
                  Swoją wyjątkowość zawdzięcza wielu innowacjom w produkcji piwa, niezmiennym 
                  od ponad 175 lat sposobem produkcji, oraz stosowaniu rzadko już spotykanej 
                  techniki potrójnej dekokcji (przypis poniżej). 
                  Od pierwszego łyku atakuje wyraźna ziołowa goryczka — krótka i przyjemna. 
                  Dobrze równoważy smak jasnego słodu, maślany finisz. Smak jest kwintesencją 
                  zwrotu czysty profilowo pils. Nic tutaj się nie kłóci, każdy akcent jest wyważony 
                  i ma dla siebie odpowiednio dużo miejsca, aby wybrzmieć. Pilsner pachnie mieszanką 
                  ziół, kojarzącą się z miksem tymianku i trawy cytrynowej. 
                  (Czysto, rześko, przyjemnie.)<br> <br>
                  Alkohol: 4.4%
                  ''', unsafe_allow_html=True)

        slide1 = st.expander("Ciężkie słowa (pojęcia dla nerdów)")

        slide1.header("Drożdże dolnej fermentacji")
        slide1.write('''Podczas fermentacji, drożdże dolnej fermentacji zbierają się 
                  na dnie (stąd nazwa). Optymalna temperatura fermentacji dla drożdży dolnej 
                  fermentacji wynosi w przybliżeniu 10°C. Wykorzystywane przy produkcji lagerów.''')

        slide1.header("Drożdże górnej fermentacji")
        slide1.write('''
                  Podczas fermentacji, drożdże górnej fermentacji "wspinają" się na powierzchnię 
                  młodego piwa i tworzą tam warstwę piany (stąd nazwa). Optymalna temperatura 
                  fermentacji dla drożdży górnej fermentacji wynosi w przybliżeniu 20°C.
                  Główną cechą odróżniającą piwa górnej fermentacji jest ich
                  kwiatowy zapach i owocowy smak.''')

        slide1.header("Dekokcja (zacieranie dekokcyjne)")
        slide1.write('''
                  Typ zacierania w którym różne temperatury zacierania są osiągnięte przez 
                  odebranie części zacieru, zagotowanie go w osobnym zbiorniku, następnie użycie 
                  go jako woda infuzyjna aby ogrzać pozostały zacier. Jest to tradycyjna metoda 
                  używana w wielu kontynentalnych europejskich stylach piw, 
                  a w szczególności w niemieckich i czeskich.<br>

                  W metodzie dekokcyjnej wyróżnia się system jednowarowy, dwuwarowy oraz 
                  trójwarowy. Oznacza to, że dekokcja została przeprowadzona jednokrotnie, 
                  dwukrotnie lub trzykrotnie. Ze względów ekonomicznych metoda dekokcyjna 
                  zacierania słodu stosowana jest obecnie rzadko. Najczęściej stosuje się ją 
                  przy warzeniu koźlaków, piw pszenicznych lub pilznerów.''', unsafe_allow_html=True)

        slide1.header("Metoda równoległego warzenia (Pilsner)")
        slide1.write('''
                  [...]kiedy browar został zmodernizowany w 1992 roku i wprowadziliśmy nową 
                  technologię, zaczęliśmy fermentować i leżakować większość naszego piwa w 
                  zbiornikach ze stali nierdzewnej znajdujących się nad ziemią. Oznaczało to,  
                  że mogliśmy dokładniej kontrolować proces warzenia, na przykład temperaturę
                  i ilość dodawanych drożdży.<br> <br>

                  Oczywiście obawialiśmy się, czy ta zmiana nie wpłynie na smak naszego piwa - 
                  zawsze się o to martwimy! Tak więc zespół pod kierownictwem Václava Berki, 
                  naszego Mistrza Warzelnictwa, zdecydował, że powinniśmy nadal warzyć 
                  niewielką porcję naszego piwa w piwnicach - w ten sposób można je porównać 
                  z piwem produkowanym w nowych zbiornikach. Nazwaliśmy to równoległym warzeniem. <br> <br>

                  Proces ten polega na warzeniu piwa w taki sam sposób, jak robiliśmy to od 
                  zawsze, a następnie przeprowadzeniu porównawczych testów smakowych w 
                  laboratorium przez zespół obecnych i emerytowanych Mistrzów Warzelnictwa, 
                  a także przez panel degustatorów browaru. Chodzi nam o to, aby zespół 
                  ekspertów nie znalazł między nimi żadnych różnic - w ten sposób możemy 
                  być pewni, że zachowaliśmy spójność jakości naszego piwa. [...]
                  ''', unsafe_allow_html=True)
        slide1.caption(":grey[źródło: **pilsnerurquell.com**]")

        st.header("Proces produkcji piwa")
        st.subheader("Do produkcji piwa wykorzystywane są cztery różne składniki")

        slod = st.expander("Słód")
        slod.write('''
                  Słód jest produkowany z ziarna, głównie jęczmiennego. Pierwszą czynnością 
                  jest dokładne oczyszczenie ziarna. Oczyszczone ziarno jest moczone w 
                  wodzie aż do uzyskania wymaganej wilgotności wynoszącej 44 %. Następnie 
                  ziarno kiełkuje w warunkach, gdzie kontrolowane są: temperatura i 
                  wilgotność. Podczas tego procesu zawarte enzymy zostają pobudzone do 
                  działania, a skrobia i białko zawarte w ziarnie jęczmienia zostaje 
                  częściowo rozłożone. Słód z kiełkami trafia do suszarni gdzie jest suszony. 
                  Im temperatura suszenia jest wyższa, tym więcej cukrów ulega karmelizacji. 
                  Im więcej powstanie karmelu tym ciemniejsze piwo zostanie wyprodukowane z 
                  takiego słodu. Zawartość alkoholu w piwie zależy od ilości słodu, jaką 
                  używa się do jego wyprodukowania, a nie od koloru: jasnego czy 
                  ciemnego piwa.''')

        woda = st.expander("Woda")
        woda.write('''
                  Dla produkcji piwa duże znaczenie ma to, czy woda używana do produkcji 
                  jest czysta i wolna od zanieczyszczeń. W przeciwieństwie do przeszłości, 
                  zawartość minerałów w wodzie (twardość wody) nie ma decydującego znaczenia 
                  od czasu, kiedy możliwe jest zrównoważenie składu chemicznego wody przez 
                  sposób słodowania (wytwarzania słodu) i operacje technologiczne 
                  podczas produkcji piwa.''')

        chmiel = st.expander("Chmiel")
        chmiel.write('''
                  Prócz dostarczenia odpowiedniego zapachu i goryczki, chmiel wykonuje 
                  podczas procesu produkcji piwa ważne zadanie: jest antyseptykiem. 
                  Ze względu na zawartość naturalnych olejków (podobne jak rumianek i eukaliptus)  
                  zabezpiecza piwo przed jego nieoczekiwanym zepsuciem. 
                  (W "Bierhalle" używane są chmiele goryczkowe i aromatyczne).''')

        drozdze = st.expander("Drożdże")
        drozdze.write('''
                  Podczas procesu fermentacji, zadaniem drożdży jest zamiana cukrów 
                  rozpuszczonych w wodzie, a pochodzących ze słodu w alkohol i CO2. 
                  Są dwa ważne typy drożdży: drożdże górnej fermentacji i drożdże dolnej
                  fermentacji. Podczas fermentacji, drożdże górnej fermentacji "wspinają" 
                  się na powierzchnię młodego piwa i tworzą tam warstwę piany (stąd nazwa). 
                  Optymalna temperatura fermentacji dla drożdży górnej fermentacji wynosi 
                  w przybliżeniu 20°C. Podczas fermentacji, drożdże dolnej fermentacji 
                  zbierają się na dnie (stąd nazwa). Optymalna temperatura fermentacji 
                  dla drożdży dolnej fermentacji wynosi w przybliżeniu 10°C. Główną cechą 
                  odróżniającą piwa górnej fermentacji jest ich kwiatowy zapach i owocowy smak.''')

        st.header("Prawo czystości piw Bierhalle")
        st.write('''
                  Piwo w Bierhalle produkowane jest zgodnie z edyktem Reinheitsgebot (Prawo Czystości) 
                  z 1516r., według którego do produkcji piwa używamy wyłącznie czterech surowców: 
                  wody, słodu, chmielu i drożdży. Piwa nie zawierają żadnych stabilizatorów ani konserwantów, 
                  są niepasteryzowane i niefiltrowane, wysycone naturalnym dwutlenkiem węgla, 
                  pochodzącym z długotrwałego procesu fermentacji i leżakowania.''')
    elif submenu == "Wino":
        st.header(":red[Czerwone wina]")
        df1 = pd.read_csv("czerwone_wina.csv")
        st.table(df1)

        carmenere = st.expander("Aresti Carmenere Reserva")
        carmenere.write('''
        Carmenere z serii "CABINA 56" upamiętnia pierwszego pick-upa 
        należącego do Vicente Aresti - założyciela winnicy. Używał go 
        przez wiele lat podczas każdego zbioru. Ten model miał wielką
        charakterystyczną kabinę, dlatego od początku był nazywany "kabiną". 
        Od ponad 60 lat ten klasyczny już pojazd należy do rodziny. 
        Wino leżakowało w dębowych beczkach ok. 12 miesięcy.
        <br> <br>
        Nos to czerwone owoce, także jeżyny, akcenty czekolady i wanilii.<br> <br>
        :blue[Sugestie kulinarne]: łagodne sosy, pieczenie, kaczki, dania z grilla.''', unsafe_allow_html=True)

        monte = st.expander("Gran Sasso Montepulciano D’Abruzzo")
        monte.write('''
        Winnice zlokalizowane w Crecchio, San Salvo oraz Pollutri. 
        Odszypułkowanie i delikatne prasowanie gron. Maceracja przez 15 dni w 
        kadziach ze stalli nierdzewnej. Fermentacja i dojrzewanie w 
        beczkach z francuskiego dębu przez dwa do trzech miesięcy.
        <br> <br>
        Dobrze zbudowane wino o mocnych aromatach owocowych 
        ( jeżyny, śliwki, porzeczki i wiśnie), z lekkim akcentem ziołowym. 
        W ustach soczyste, zmysłowe, o miękkich garbnikach i stonowanej kwasowości.<br> <br>
        :blue[Sugestie kulinarne]: wędliny, mięsa z grilla, dojrzewające sery. 
        ''', unsafe_allow_html=True)

        malbec = st.expander("Elsa Bianchi Malbec San Rafael Mendoza")
        malbec.write('''
        Klasyczny Malbec z aromatami dojrzałych śliwek i fiołków z aluwialnych gleb 
        w winnicach Finca Doña Elsa i Finca Asti (750 m n.p.m.), które 
        przekazują winu swoje mineralne nuty. Ręczny zbiór, fermentacja w kadziach
        ze stali nierdzewnej, dojrzewanie w dębinie.
        <br> <br>
        Aromaty dojrzałych śliwek i fiołków, podkreślonych delikatną nutą dębu. 
        W ustach zmysłowe, pełne owocu z dobrze ułożonymi taninami, jedwabistą fakturą
        i intensywnym owocowym posmakiem. Wszystkie te cechy dają w efekcie eleganckie,
        dobrze zbalansowane wino, które może być idealnym partnerem przy stole.<br> <br>
        :blue[Sugestie kulinarne]: Grillowane mięso
        ''', unsafe_allow_html=True)

        primitivo = st.expander("Primitivo Botoromagno")
        primitivo.write('''
        Murgijskie Primitivo, jeden z najstarszych i najszlachetniejszych szczepów Apulii. 
        Sprowadzony na początku XIX wieku przez mnichów benedyktynów, prawdopodobnie z 
        Chorwacji. Winorośl prowadzona jest wyłącznie "na głowę" (goblet), o naturalnie 
        niskiej wydajności z hektara. 500 m n.p.m., niezwykła osobowość i głębia. Stare 
        winnice są zlokalizowane w Murgii. Ręczny zbiór. Dziesięciodniowa fermentacja na 
        skórkach w 26°-28°C. Fermentacja malolaktyczna, dojrzewanie w kadziach ze stali 
        nierdzewnej o kontrolowanej temperaturze przez 10 miesięcy, potem przez 
        6 miesięcy w butelce.
        <br> <br>
        Nos niezwykle owocowy z przewagą wiśni, czereśni i morwy czerwonej. 
        Nuty wanilii, cynamonu, szałwii, mięty i tytoniu dopełniają aromatycznej całości.
        Krągłe, otulające bardzo lekkimi taninami, eleganckie i pachnące wino, z nutami 
        porzeczek, śliwek, czarnego pieprzu i czekolady. <br> <br>
        :blue[Sugestie kulinarne]: wędliny, sery, jagnięcina z grilla i dziczyzna.
        ''', unsafe_allow_html=True)

        st.header("Białe wina")
        df2 = pd.read_csv("biale_wina.csv")
        st.table(df2)

        chardonnay = st.expander('Aresti Chardonnay')
        chardonnay.write('''Wytrawne wino o żółtawej barwie z zielonymi refleksami. W nosie ekspresyjny
         aromat dojrzałych owoców ananasa, gruszek, cytrusów i bananów. W ustach wino bogate, cieliste, 
         miękkie i aksamitne z posmakiem wanilii i nutą kawy. 90 punktów w Wine Advocate Roberta Parkera. <br> <br>
        :blue[Sugestie kulinarne]: Drób, zwłaszcza kurczak i indyk''', unsafe_allow_html=True)

        sauvignon = st.expander('Moulin de Gassac Sauvignon')
        sauvignon.write('''Wino białe, bardzo owocowe i rześkie z czystym aromatem agrestu i towarzyszącą mu nutą 
        cytrusów i brzoskwiń. W ustach świeże, owocowe, eleganckie.<br> <br>
        :blue[Sugestie kulinarne]: Sałatki, ryby i desery
        ''', unsafe_allow_html=True)

        trebbiano = st.expander("Gran Sasso Trebbiano d'Abruzzo")
        trebbiano.write('''Lekkie, orzeźwiające wino o aromatach żółtych owoców (brzoskwinia i nieszpułka, głóg), z 
        nutami kwiatu pomarańczy. Delikatnie wytrawne, o średnim ekstrakcie. W ustach rześkie, owocowe, świeże, z 
        mocnym smakiem cytrusów i jabłek. Łagodne, dobrze zrównoważone. Szczególnie dobrze komponuje się z 
        lekkimi potrawami.<br> <br>
        :blue[Sugestie kulinarne]: Aperitif, lekkie dania z ryb, sałatki, owoce morza.
        ''', unsafe_allow_html=True)

        riesling = st.expander('Klaus Meyer Riesling')
        riesling.write('''Żywy, wytrawny Riesling. Cytrusy, ananas i jabłka, podkreślone delikatną nutą siana i akcentem
         krzemienia. W ustach napięte, delikatnie słonawe z wyrazista owocowością i orzeźwiając kwasowością.<br> <br>
         :blue[Sugestie kulinarne]: Idealne wino do pełnych, obfitych dań.
         ''', unsafe_allow_html=True)

        
if __name__ == '__main__':
    main()
