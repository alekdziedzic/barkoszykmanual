import streamlit as st
from PIL import Image
st.set_page_config(page_title="Manual Koktajli", page_icon=Image.open("logo.png"))
st.title("Manual Koktajli")

amaretto_sour = st.expander("Amaretto sour")
amaretto_sour.write('''40ml Amaretto\n
20ml Balantinnes\n
30ml sok z limonki\n
15ml białko\n
5ml syrop cukrowy\n
2d angostura\n''')
amaretto_sour.image("CocktailImages/amaretto.jpg")
amaretto_sour.write('''Metoda: reverse shake\n
Szkło: Coupe glass\n''')

americano = st.expander("Americano")
americano.write('''30 ml Martini Bitter\n
30 ml Martini Riserva Rubino\n
Top up soda\n''')
americano.image("CocktailImages/americano.jpg")
americano.write('''Metoda: Build + zamieszać\n
Lód: Kości\n
Szkło: highball\n
Garnish: Pół plasterka pomarańczy, zest z cytryny\n''')

aviation = st.expander("Aviation")
aviation.write('''40ml Beefeater\n
20ml Sour\n
15ml :red[Luxardo Maraschino]/Lazaroni Maraschino\n
10ml Crème de Violette\n
5ml Sweet\n
''')
aviation.image("CocktailImages/aviation.jpg")
aviation.write('''Metoda: Shake, fine strain\n
Szkło: Coupe glass\n
Garnish: Wisienka maraschino na szpadce\n''')

Bees_Knees = st.expander("Bees Knees")
Bees_Knees.write('''60ml Beefeater\n
20ml sok z cytryny\n
20ml sok pomarańczowy\n
15ml syrop miodowy\n''')
Bees_Knees.image("CocktailImages/bees_knees.jpg")
Bees_Knees.write('''Metoda: shake\n
Szkło: Coupe glass\n
Garnish: zest z pomarańczy\n''')

Bellini = st.expander("Bellini")
Bellini.write('''100ml prosecco\n
40ml :red[puree brzoskwiniowe]/liker brzoskwiniowy\n''')
Bellini.image("CocktailImages/bellini.jpg")
Bellini.write('''Metoda: build\n
Szkło: flute glass\n''')

Bijou = st.expander("Bijou")
Bijou.write('''40ml :red[Tanqueray Ten]\n
20ml :red[Chartreause Green]\n
30ml Martini Rubino\n
2d Orange bitters\n''')
Bijou.image("CocktailImages/bijou.jpg")
Bijou.write('''Metoda: Stir\n
Szkło: Coupe glass\n''')

Boulevardier = st.expander("Boulevardier")
Boulevardier.write('''20ml Jim Beam Rye\n
20ml Martini Bitter\n
20ml Martini Rubino\n''')
Boulevardier.image("CocktailImages/boulevardier.jpg")
Boulevardier.write('''Metoda: Stir\n
Szkło: Old fashioned\n
Garnish: Zest z pomarańczy\n''')

Bramble = st.expander("Bramble")
Bramble.write('''40ml Beefeater\n
25ml sok z cytryny\n
15ml syrop cukrowy\n
15ml briottet creme de cassis\n''')
Bramble.image("CocktailImages/bramble.jpg")
Bramble.write('''Metoda: Shake, top creme de cassis\n
Szkło: Old fashioned\n
Lód: Kruszonka\n
Garnish: Top mięty, świeże owoce\n''')

Brandy_Alexander = st.expander("Brandy Alexander")
Brandy_Alexander.write('''30 ml Martel VS\n
20 ml Crème de Cacao\n
30 ml Half&Half\n
Dash chocolate bitters\n''')
Brandy_Alexander.image("CocktailImages/brandy_alexander.jpg")
Brandy_Alexander.write('''Metoda: Shake, Fine Strain\n
Szkło: Coupe glass\n
Garnish: Tarta gałka muszkatołowa\n''')

Breakfast_Martini = st.expander("Breakfast Martini")
Breakfast_Martini.write('''50 ml Beefeater\n
20 ml Cointreau\n
20 ml soku z cytryny\n
2 :red[łyżki marmolady pomarańczowej]\n''')
Breakfast_Martini.image("CocktailImages/breakfast_martini.jpg")
Breakfast_Martini.write('''Metoda: Shake\n
Szkło: Coupe glass\n
Garnish: Zest z pomarańczy\n''')

Brooklyn = st.expander("Brooklyn")
Brooklyn.write('''40 ml Rye Whisky\n
20 ml Dry Vermouth\n
5 ml :red[Luxardo Marashino]/Lazaroni Maraschino\n
5 ml Amaro\n
2 dash orange bitter\n''')
Brooklyn.image("CocktailImages/brooklyn.jpg")
Brooklyn.write('''Metoda: Stir\n
Szkło : Coupe glass\n
Garnish: Zest z pomarańczy, wisienka maraschino\n''')

Caipirinha = st.expander("Caipirinha")
Caipirinha.write('''40 ml Cachaca\n
3 łyżeczki barmańskie cukru trzcinowego\n
4 cząstki limonki\n''')
Caipirinha.image("CocktailImages/caipirinha.jpg")
Caipirinha.write('''Metoda: muddlujemy limonki z cukrem, zasypujemy kruszonym lodem, wlewamy cachace,
mieszamy. Usypujemy górkę z lodu i dekorujemy cząstkami z limonki.\n
Szkło: Old fashioned\n
Garnish: Cząstka limonki, pokruszony lód\n''')

Champagne_Cocktail = st.expander("Champagne Cocktail")
Champagne_Cocktail.write('''100 ml Mumm Brut\n
10 ml Martell VS\n
2 dash Angostura\n
1 kostka cukru\n''')
Champagne_Cocktail.image("CocktailImages/champagne_cocktail.jpg")
Champagne_Cocktail.write('''Metoda: umieść nasączoną kostkę cukru dwoma kroplami angostury, dodaj koniak następnie
szampan.\n
Szkło: champagne glass\n
Lód: -\n
Garnish: Zest z pomarańczy i wisienka maraschino\n''')

Clover_Club = st.expander("Clover Club")
Clover_Club.write('''40ml Beefeater\n
15ml Martini Extra Dry\n
25ml soku z cytryny\n
15ml :red[grenadine]\n
10ml białko\n''')
Clover_Club.image("CocktailImages/clover_club.jpg")
Clover_Club.write('''Metoda: Shake, double strain\n
Szkło: Coupe glass\n
Garnish: :red[Maliny na szpadce], cukier puder\n''')

Cointreau_Teese = st.expander("Cointreau Teese")
Cointreau_Teese.write('''40ml cointreau\n
40ml sok jabłkowy\n
15ml Creme de violette\n
15ml sok z limonki\n''')
#Cointreau_Teese.image("")
Cointreau_Teese.write('''Metoda: Shake
Szkło: Coupe glass
Garnish: :red[Fiołek]/Zest z pomarańczy''')

Corpse_reviver_1 = st.expander("Corpse Reviver no.1")
Corpse_reviver_1.write('''40ml Cognac\n
20 ml :red[Calvados]\n
20 ml Martini Rubino\n''')
#Corpse_reviver_1.image("")
Corpse_reviver_1.write('''Metoda: Stir\n
Szkło: Coupe glass\n
Garnish: Zest z pomarańczy\n''')

Corpse_Reviver_2 = st.expander("Corpse Reviver no.2")
Corpse_Reviver_2.write('''20ml :red[Tanqueray Ten]\n
20ml Cointreau\n
20ml Lillet Blanc\n
20ml sok z cytryny\n
1d Absinth\n''')
#Corpse_Reviver_2.image("")
Corpse_Reviver_2.write('''Metoda: Shake\n
Szkło: Coupe glass\n
Garnish: Zest z cytryny, aromatyzacja absyntem\n''')

Cosmopolitan = st.expander("Cosmopolitan")
Cosmopolitan.write('''40 ml Absolut Lime\n
20 ml Cointreau\n
20 ml sok z limonki\n
20 ml syrop żurawina\n''')
#Cosmopolitan.image("")
Cosmopolitan.write('''Metoda: Shake, fine strain\n
Szkło: Coupe glass\n
Garnish: Zest z pomarańczy\n''')

Cynar_Szprycer_1 = st.expander("Cynar Szprycer No.1")
Cynar_Szprycer_1.write('''40 ml Cynar\n
10 ml Strega\n
140 ml Woda Gazowana\n
20 ml Ginger beer\n''')
#Cynar_Szprycer_1.image("")
Cynar_Szprycer_1.write('''Metoda: Bulid + zamieszać\n
Lód: Kości na full\n
Szkło: Copa\n
Garnish: 2 plasterki imbiru + pokruszona laska cynamonu\n''')

Cynar_Szprycer_2 = st.expander("Cynar Szprycer No.2")
Cynar_Szprycer_2.write('''40 ml Cynar\n
40 ml syrop :red[rabarbar] / jabłkowy\n
20 ml sour\n
Top up Woda Gazowana\n''')
#Cynar_Szprycer_2.image("")
Cynar_Szprycer_2.write('''Metoda : Shake\n
Lód : Kości\n
Szkło : Highball\n
Garnish : Pół plasterka pomarańczy\n''')

Daiquiri = st.expander("Daiquiri")
Daiquiri.write('''40 ml Havana 3yo/Dictator 12yo\n
25 ml sok z limonki\n
15 ml syrop cukrowy\n
5 dash :red[luxardo maraschino]/Lazaroni Maraschino\n''')
#Daiquiri.image("")
Daiquiri.write('''Metoda: Shake, fine strain\n
Szkło: Coupe glass\n
Garnish: Suszka z limonki + aromatyzacja zestem z limonki\n''')

Dark_N_Stormy = st.expander("Dark n'Stormy")
Dark_N_Stormy.write('''40ml Havana Especial\n
1x Puszka Ginger Beer\n
2x Wedge limonka\n
2d Angostura bitters\n''')
#Dark_N_Stormy.image("")
Dark_N_Stormy.write('''Metoda: build (rum i angostura na wierzchu)\n
Szkło: Highball\n
Garnish: Wciśnięte wedge, rum ma tworzyć warstwę z angosturą\n''')

Dirty_Martini = st.expander("Dirty Martini")
Dirty_Martini.write('''60 ml Beefeater\n
10 ml Martini extra dry\n
10 ml (2 łyżeczki) Zalewa z oliwek\n''')
#Dirty_Martini.image("")
Dirty_Martini.write('''Metoda: Stir\n
Szkło: Coupe glass\n
Garnish: 2 Oliwki na szpadce\n''')

Elderflower_Spritz = st.expander("Elderflower Spritz")
Elderflower_Spritz.write('''100 ml Sauvignon Blanc\n
40 ml St. Germain\n
100 ml woda gaz\n''')
#Elderflower_Spritz.image("")
Elderflower_Spritz.write('''Metoda: Build + zamieszać\n
Szkło: Wine glass\n
Garnish: Lime slice\n''')

Espresso_Martini = st.expander("Espresso Martini")
Espresso_Martini.write('''40 ml Ostoya\n
20 ml :red[Kahlua]/Bols Coffee\n
1 espresso\n
5ml syrop waniliowy\n''')
#Espresso_Martini.image("")
Espresso_Martini.write('''Metoda: Shake, fine strain\n
Szkło: Coupe glass\n
Garnish: 3 Ziarenka kawy ułożone w koniczynkę\n''')

Fancy_Vermouth_Cocktail = st.expander("Fancy Vermouth Cocktail")
Fancy_Vermouth_Cocktail.write('''60ml Martini Extra Dry\n
5ml :red[Luxardo Maraschino]/Lazaroni Maraschino\n
2,5ml Syrop cukrowy\n
2d angostura\n''')
#Fancy_Vermouth_Cocktail.image("")
Fancy_Vermouth_Cocktail.write('''Metoda: Stir\n
Szkło: Old fashioned\n
Garnish: Wedge limonka\n''')

Fiero_Spritz = st.expander("Fiero Spritz")
Fiero_Spritz.write('''60ml Martini Fiero\n
160ml Prosecco\n
Top up Woda Gazowana\n''')
#Fiero_Spritz.image("")
Fiero_Spritz.write('''Metoda: Najpierw wlać prosseco + woda gazowana, następnie Fiero\n
Szkło: Copa Martini\n
Garnish: Plaster pomarańczy\n''')

French_75 = st.expander("French 75")
French_75.write('''25 ml Beefeater\n
20 ml sok z cytryny\n
10 ml syrop cukrowy\n''')
#French_75.image("")
French_75.write('''Top up (ok 50 ml) Champagne (Mumm Brut)\n
Metoda: Shake + fine strain & top up\n
Szkło: Flute glass\n
Garnish: Zest z cytryny\n''')

French_Martini = st.expander("French Martini")
French_Martini.write('''50 ml Ostoya\n
40 ml :red[soku z ananasa]\n
15 ml Chambord\n''')
#French_Martini.image("")
French_Martini.write('''Metoda: Shake\n
Szkło: Flute glass\n
Garnish: Kwiaty hibiskusa\n''')