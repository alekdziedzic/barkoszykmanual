import streamlit as st
from PIL import Image
st.set_page_config(page_title="Piwo", page_icon=Image.open("logo.png"))
#hide_menu_style = '''
        #<style>
        #MainMenu {visibility: hidden; }
        #footer {visibility: hidden;}
        #</style>
        #'''
#st.markdown(hide_menu_style, unsafe_allow_html=True)

st.header("Opis piw")
st.subheader("Bierhalle Pills (lager)",)
st.write('''Pils to najbardziej rozpowszechniony gatunek piwa na świecie\n
(mocno powiązany z pilsnerem). Piwo jasne, dolnej fermentacji (przypis poniżej),\n
istensywna chmielowa goryczka połączona ze smakiem słodu jęczmiennego.\n
Alkohol: 5.0%''')

st.subheader("Bierhalle Weizen (pszeniczne)")
st.write('''Weizen jest piwem górnej fermentacji (przypis poniżej)\n
o wyczuwalnym zapachu: bananowo-goździkowym, cynamonu oraz aromatycznego chmielu.\n 
Goryczka przeplata się ze smakiem pszenicznego słodu. Większa ilość "bąbelków" \n
sprawia, że piwo pszeniczne nabiera lekko kwaskowatego smaku i doskonale gasi\n
pragnienie. Słód pszeniczny stanowi ponad 50% całkowitego zasypu.\n
Alkohol: 5.2%''')
marcowe = st.subheader("Bierhalle Marcowe (podwójnie słodowany lager)")
st.write('''Piwo marcowe, zwane również Oktoberfestbier, dawniej warzone było \n
tylko sezonowo. Dzisiaj, dzięki nowoczesnym systemom chłodzenia można produkować\n
je okrągły rok. Piwo jest pełne smaków pochodzących z mieszaniny słodów\n
jęczmiennych i aromatycznego chmielu.\n
Alkohol: 5.2%''')
pilsner = st.subheader("Pilsner Urquell")
st.write('''Prekursor piw typu lager. Tworzony metodą równoległego warzenia.\n
Swoją wyjątkowość zawdzięcza wielu innowacjom w produkcji piwa, niezmiennym \n
od ponad 175 lat sposobem produkcji, oraz stosowaniu rzadko już spotykanej \n
techniki potrójnej dekokcji (przypis poniżej). \n \n
Od pierwszego łyku atakuje wyraźna ziołowa goryczka — krótka i przyjemna.\n
Dobrze równoważy smak jasnego słodu, maślany finisz. Smak jest kwintesencją\n
zwrotu czysty profilowo pils. Nic tutaj się nie kłóci, każdy akcent jest wyważony\n
i ma dla siebie odpowiednio dużo miejsca, aby wybrzmieć. Pilsner pachnie mieszanką\n
ziół, kojarzącą się z miksem tymianku i trawy cytrynowej. \n
(Czysto, rześko, przyjemnie.)\n
Alkohol: 4.4%
''')

slide1 = st.expander("Ciężkie słowa (pojęcia dla nerdów)")

slide1.header("Drożdże dolnej fermentacji")
slide1.write('''Podczas fermentacji, drożdże dolnej fermentacji zbierają się\n
na dnie (stąd nazwa). Optymalna temperatura fermentacji dla drożdży dolnej\n
fermentacji wynosi w przybliżeniu 10°C. Wykorzystywane przy produkcji lagerów.\n''')

slide1.header("Drożdże górnej fermentacji")
slide1.write('''
Podczas fermentacji, drożdże górnej fermentacji "wspinają" się na powierzchnię\n
młodego piwa i tworzą tam warstwę piany (stąd nazwa). Optymalna temperatura\n
fermentacjidla drożdży górnej fermentacji wynosi w przybliżeniu 20°C.\n
Główną cechą odróżniającą piwa górnej fermentacji jest ich\n
kwiatowy zapach i owocowy smak.\n''')

slide1.header("Dekokcja (zacieranie dekokcyjne)")
slide1.write('''
Typ zacierania w którym różne temperatury zacierania są osiągnięte przez \n
odebranie części zacieru, zagotowanie go w osobnym zbiorniku, następnie użycie\n
go jako woda infuzyjna aby ogrzać pozostały zacier. Jest to tradycyjna metoda\n
używana w wielu kontynentalnych europejskich stylach piw,\n
a w szczególności w niemieckich i czeskich.\n

W metodzie dekokcyjnej wyróżnia się system jednowarowy, dwuwarowy oraz\n
trójwarowy. Oznacza to, że dekokcja została przeprowadzona jednokrotnie,\n
dwukrotnie lub trzykrotnie. Ze względów ekonomicznych metoda dekokcyjna \n
zacierania słodu stosowana jest obecnie rzadko. Najczęściej stosuje się ją\n
przy warzeniu koźlaków, piw pszenicznych lub pilznerów.\n''')

slide1.header("Metoda równoległego warzenia (Pilsner)")
slide1.write('''
[...]kiedy browar został zmodernizowany w 1992 roku i wprowadziliśmy nową \n
technologię, zaczęliśmy fermentować i leżakować większość naszego piwa w \n
zbiornikach ze stali nierdzewnej znajdujących się nad ziemią. Oznaczało to,\n 
że mogliśmy dokładniej kontrolować proces warzenia, na przykład temperaturę\n
i ilość dodawanych drożdży.\n

Oczywiście obawialiśmy się, czy ta zmiana nie wpłynie na smak naszego piwa - \n
zawsze się o to martwimy! Tak więc zespół pod kierownictwem Václava Berki, \n
naszego Mistrza Warzelnictwa, zdecydował, że powinniśmy nadal warzyć \n
niewielką porcję naszego piwa w piwnicach - w ten sposób można je porównać\n 
z piwem produkowanym w nowych zbiornikach. Nazwaliśmy to równoległym warzeniem.\n

Proces ten polega na warzeniu piwa w taki sam sposób, jak robiliśmy to od\n
zawsze, a następnie przeprowadzeniu porównawczych testów smakowych w \n
laboratorium przez zespół obecnych i emerytowanych Mistrzów Warzelnictwa,\n
a także przez panel degustatorów browaru. Chodzi nam o to, aby zespół \n
ekspertów nie znalazł między nimi żadnych różnic - w ten sposób możemy \n
być pewni, że zachowaliśmy spójność jakości naszego piwa. [...]\n
\n''')
slide1.markdown(":grey[źródło: **pilsnerurquell.com**]")

st.header("Proces produkcji piwa")
st.subheader("Do produkcji piwa wykorzystywane są cztery różne składniki")

slod = st.expander("Słód")
slod.write('''
Słód jest produkowany z ziarna, głównie jęczmiennego. Pierwszą czynnością \n
jest dokładne oczyszczenie ziarna. Oczyszczone ziarno jest moczone w \n
wodzie aż do uzyskania wymaganej wilgotności wynoszącej 44 %. Następnie\n 
ziarno kiełkuje w warunkach, gdzie kontrolowane są: temperatura i \n
wilgotność. Podczas tego procesu zawarte enzymy zostają pobudzone do\n 
działania, a skrobia i białko zawarte w ziarnie jęczmienia zostaje \n
częściowo rozłożone. Słód z kiełkami trafia do suszarni gdzie jest suszony.\n 
Im temperatura suszenia jest wyższa, tym więcej cukrów ulega karmelizacji. \n
Im więcej powstanie karmelu tym ciemniejsze piwo zostanie wyprodukowane z \n
takiego słodu. Zawartość alkoholu w piwie zależy od ilości słodu, jaką \n
używa się do jego wyprodukowania, a nie od koloru: jasnego czy \n
ciemnego piwa.\n''')

woda =st.expander("Woda")
woda.write('''
Dla produkcji piwa duże znaczenie ma to, czy woda używana do produkcji \n
jest czysta i wolna od zanieczyszczeń. W przeciwieństwie do przeszłości, \n
zawartość minerałów w wodzie (twardość wody) nie ma decydującego znaczenia \n
od czasu, kiedy możliwe jest zrównoważenie składu chemicznego wody przez \n
sposób słodowania (wytwarzania słodu) i operacje technologiczne \n
podczas produkcji piwa.\n''')

chmiel = st.expander("Chmiel")
chmiel.write('''
Prócz dostarczenia odpowiedniego zapachu i goryczki, chmiel wykonuje \n
podczas procesu produkcji piwa ważne zadanie: jest antyseptykiem. \n
Ze względu na zawartość naturalnych olejków (podobne jak rumianek i eukaliptus)\n 
zabezpiecza piwo przed jego nieoczekiwanym zepsuciem. \n
(W "Bierhalle" używane są chmiele goryczkowe i aromatyczne).\n''')

drozdze = st.expander("Drożdże")
drozdze.write('''
Podczas procesu fermentacji, zadaniem drożdży jest zamiana cukrów \n
rozpuszczonych w wodzie, a pochodzących ze słodu w alkohol i CO2. \n
Są dwa ważne typy drożdży: drożdże górnej fermentacji i drożdże dolnej\n
fermentacji. Podczas fermentacji, drożdże górnej fermentacji "wspinają" \n
się na powierzchnię młodego piwa i tworzą tam warstwę piany (stąd nazwa). \n
Optymalna temperatura fermentacji dla drożdży górnej fermentacji wynosi \n
w przybliżeniu 20°C. Podczas fermentacji, drożdże dolnej fermentacji \n
zbierają się na dnie (stąd nazwa). Optymalna temperatura fermentacji \n
dla drożdży dolnej fermentacji wynosi w przybliżeniu 10°C. Główną cechą\n 
odróżniającą piwa górnej fermentacji jest ich kwiatowy zapach i owocowy smak.\n''')

st.header("Prawo czystości piw Bierhalle")
st.write('''
Piwo w Bierhalle produkowane jest zgodnie z edyktem Reinheitsgebot (Prawo Czystości)\n
z 1516r., według którego do produkcji piwa używamy wyłącznie czterech surowców: \n
wody, słodu, chmielu i drożdży. Piwa nie zawierają żadnych stabilizatorów ani konserwantów,\n
są niepasteryzowane i niefiltrowane, wysycone naturalnym dwutlenkiem węgla, \n
pochodzącym z długotrwałego procesu fermentacji i leżakowania.\n''')