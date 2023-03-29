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
:green[Szkło]: Coupe glass\n''')

americano = st.expander("Americano")
americano.write('''30 ml Martini Bitter\n
30 ml Martini Riserva Rubino\n
Top up soda\n''')
americano.image("CocktailImages/americano.jpg")
americano.write('''Metoda: Build + zamieszać\n
:blue[Lód]: Kości\n
:green[Szkło]: highball\n
:violet[Garnish]: Pół plasterka pomarańczy, zest z cytryny\n''')

aviation = st.expander("Aviation")
aviation.write('''40ml Beefeater\n
20ml Sour\n
15ml :red[Luxardo Maraschino]/Lazaroni Maraschino\n
10ml Crème de Violette\n
5ml Sweet\n
''')
aviation.image("CocktailImages/aviation.jpg")
aviation.write('''Metoda: Shake, fine strain\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Wisienka maraschino na szpadce\n''')

Bees_Knees = st.expander("Bees Knees")
Bees_Knees.write('''60ml Beefeater\n
20ml sok z cytryny\n
20ml sok pomarańczowy\n
15ml syrop miodowy\n''')
Bees_Knees.image("CocktailImages/bees_knees.jpg")
Bees_Knees.write('''Metoda: shake\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: zest z pomarańczy\n''')

Bellini = st.expander("Bellini")
Bellini.write('''100ml prosecco\n
40ml :red[puree brzoskwiniowe]/liker brzoskwiniowy\n''')
Bellini.image("CocktailImages/bellini.jpg")
Bellini.write('''Metoda: build\n
:green[Szkło]: flute glass\n''')

Bijou = st.expander("Bijou")
Bijou.write('''40ml :red[Tanqueray Ten]\n
20ml :red[Chartreause Green]\n
30ml Martini Rubino\n
2d Orange bitters\n''')
Bijou.image("CocktailImages/bijou.jpg")
Bijou.write('''Metoda: Stir\n
:green[Szkło]: Coupe glass\n''')

Boulevardier = st.expander("Boulevardier")
Boulevardier.write('''20ml Jim Beam Rye\n
20ml Martini Bitter\n
20ml Martini Rubino\n''')
Boulevardier.image("CocktailImages/boulevardier.jpg")
Boulevardier.write('''Metoda: Stir\n
:green[Szkło]: Old fashioned\n
:violet[Garnish]: Zest z pomarańczy\n''')

Bramble = st.expander("Bramble")
Bramble.write('''40ml Beefeater\n
25ml sok z cytryny\n
15ml syrop cukrowy\n
15ml briottet creme de cassis\n''')
Bramble.image("CocktailImages/bramble.jpg")
Bramble.write('''Metoda: Shake, top creme de cassis\n
:green[Szkło]: Old fashioned\n
:blue[Lód]: Kruszonka\n
:violet[Garnish]: Top mięty, świeże owoce\n''')

Brandy_Alexander = st.expander("Brandy Alexander")
Brandy_Alexander.write('''30 ml Martel VS\n
20 ml Crème de Cacao\n
30 ml Half&Half\n
Dash chocolate bitters\n''')
Brandy_Alexander.image("CocktailImages/brandy_alexander.jpg")
Brandy_Alexander.write('''Metoda: Shake, Fine Strain\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Tarta gałka muszkatołowa\n''')

Breakfast_Martini = st.expander("Breakfast Martini")
Breakfast_Martini.write('''50 ml Beefeater\n
20 ml Cointreau\n
20 ml soku z cytryny\n
2 :red[łyżki marmolady pomarańczowej]\n''')
Breakfast_Martini.image("CocktailImages/breakfast_martini.jpg")
Breakfast_Martini.write('''Metoda: Shake\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Zest z pomarańczy\n''')

Brooklyn = st.expander("Brooklyn")
Brooklyn.write('''40 ml Rye Whisky\n
20 ml Dry Vermouth\n
5 ml :red[Luxardo Marashino]/Lazaroni Maraschino\n
5 ml Amaro\n
2 dash orange bitter\n''')
Brooklyn.image("CocktailImages/brooklyn.jpg")
Brooklyn.write('''Metoda: Stir\n
:green[Szkło] : Coupe glass\n
:violet[Garnish]: Zest z pomarańczy, wisienka maraschino\n''')

Caipirinha = st.expander("Caipirinha")
Caipirinha.write('''40 ml Cachaca\n
3 łyżeczki barmańskie cukru trzcinowego\n
4 cząstki limonki\n''')
Caipirinha.image("CocktailImages/caipirinha.jpg")
Caipirinha.write('''Metoda: muddlujemy limonki z cukrem, zasypujemy kruszonym lodem, wlewamy cachace,
mieszamy. Usypujemy górkę z lodu i dekorujemy cząstkami z limonki.\n
:green[Szkło]: Old fashioned\n
:violet[Garnish]: Cząstka limonki, pokruszony :blue[Lód]\n''')

Champagne_Cocktail = st.expander("Champagne Cocktail")
Champagne_Cocktail.write('''100 ml Mumm Brut\n
10 ml Martell VS\n
2 dash Angostura\n
1 kostka cukru\n''')
Champagne_Cocktail.image("CocktailImages/champagne_cocktail.jpg")
Champagne_Cocktail.write('''Metoda: umieść nasączoną kostkę cukru dwoma kroplami angostury, dodaj koniak następnie
szampan.\n
:green[Szkło]: champagne glass\n
:blue[Lód]: -\n
:violet[Garnish]: Zest z pomarańczy i wisienka maraschino\n''')

Clover_Club = st.expander("Clover Club")
Clover_Club.write('''40ml Beefeater\n
15ml Martini Extra Dry\n
25ml soku z cytryny\n
15ml :red[grenadine]\n
10ml białko\n''')
Clover_Club.image("CocktailImages/clover_club.jpg")
Clover_Club.write('''Metoda: Shake, double strain\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: :red[Maliny na szpadce], cukier puder\n''')

Cointreau_Teese = st.expander("Cointreau Teese")
Cointreau_Teese.write('''40ml cointreau\n
40ml sok jabłkowy\n
15ml Creme de violette\n
15ml sok z limonki\n''')
#Cointreau_Teese.image("")
Cointreau_Teese.write('''Metoda: Shake
:green[Szkło]: Coupe glass
:violet[Garnish]: :red[Fiołek]/Zest z pomarańczy''')

Corpse_reviver_1 = st.expander("Corpse Reviver no.1")
Corpse_reviver_1.write('''40ml Cognac\n
20 ml :red[Calvados]\n
20 ml Martini Rubino\n''')
#Corpse_reviver_1.image("")
Corpse_reviver_1.write('''Metoda: Stir\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Zest z pomarańczy\n''')

Corpse_Reviver_2 = st.expander("Corpse Reviver no.2")
Corpse_Reviver_2.write('''20ml :red[Tanqueray Ten]\n
20ml Cointreau\n
20ml Lillet Blanc\n
20ml sok z cytryny\n
1d Absinth\n''')
#Corpse_Reviver_2.image("")
Corpse_Reviver_2.write('''Metoda: Shake\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Zest z cytryny, aromatyzacja absyntem\n''')

Cosmopolitan = st.expander("Cosmopolitan")
Cosmopolitan.write('''40 ml Absolut Lime\n
20 ml Cointreau\n
20 ml sok z limonki\n
20 ml syrop żurawina\n''')
#Cosmopolitan.image("")
Cosmopolitan.write('''Metoda: Shake, fine strain\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Zest z pomarańczy\n''')

Cynar_Szprycer_1 = st.expander("Cynar Szprycer No.1")
Cynar_Szprycer_1.write('''40 ml Cynar\n
10 ml Strega\n
140 ml Woda Gazowana\n
20 ml Ginger beer\n''')
#Cynar_Szprycer_1.image("")
Cynar_Szprycer_1.write('''Metoda: Bulid + zamieszać\n
:blue[Lód]: Kości na full\n
:green[Szkło]: Copa\n
:violet[Garnish]: 2 plasterki imbiru + pokruszona laska cynamonu\n''')

Cynar_Szprycer_2 = st.expander("Cynar Szprycer No.2")
Cynar_Szprycer_2.write('''40 ml Cynar\n
40 ml syrop :red[rabarbar] / jabłkowy\n
20 ml sour\n
Top up Woda Gazowana\n''')
#Cynar_Szprycer_2.image("")
Cynar_Szprycer_2.write('''Metoda : Shake\n
:blue[Lód] : Kości\n
:green[Szkło] : Highball\n
:violet[Garnish] : Pół plasterka pomarańczy\n''')

Daiquiri = st.expander("Daiquiri")
Daiquiri.write('''40 ml Havana 3yo/Dictator 12yo\n
25 ml sok z limonki\n
15 ml syrop cukrowy\n
5 dash :red[luxardo maraschino]/Lazaroni Maraschino\n''')
#Daiquiri.image("")
Daiquiri.write('''Metoda: Shake, fine strain\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Suszka z limonki + aromatyzacja zestem z limonki\n''')

Dark_N_Stormy = st.expander("Dark n'Stormy")
Dark_N_Stormy.write('''40ml Havana Especial\n
1x Puszka Ginger Beer\n
2x Wedge limonka\n
2d Angostura bitters\n''')
#Dark_N_Stormy.image("")
Dark_N_Stormy.write('''Metoda: build (rum i angostura na wierzchu)\n
:green[Szkło]: Highball\n
:violet[Garnish]: Wciśnięte wedge, rum ma tworzyć warstwę z angosturą\n''')

Dirty_Martini = st.expander("Dirty Martini")
Dirty_Martini.write('''60 ml Beefeater\n
10 ml Martini extra dry\n
10 ml (2 łyżeczki) Zalewa z oliwek\n''')
#Dirty_Martini.image("")
Dirty_Martini.write('''Metoda: Stir\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: 2 Oliwki na szpadce\n''')

Elderflower_Spritz = st.expander("Elderflower Spritz")
Elderflower_Spritz.write('''100 ml Sauvignon Blanc\n
40 ml St. Germain\n
100 ml woda gaz\n''')
#Elderflower_Spritz.image("")
Elderflower_Spritz.write('''Metoda: Build + zamieszać\n
:green[Szkło]: Wine glass\n
:violet[Garnish]: Lime slice\n''')

Espresso_Martini = st.expander("Espresso Martini")
Espresso_Martini.write('''40 ml Ostoya\n
20 ml :red[Kahlua]/Bols Coffee\n
1 espresso\n
5ml syrop waniliowy\n''')
#Espresso_Martini.image("")
Espresso_Martini.write('''Metoda: Shake, fine strain\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: 3 Ziarenka kawy ułożone w koniczynkę\n''')

Fancy_Vermouth_Cocktail = st.expander("Fancy Vermouth Cocktail")
Fancy_Vermouth_Cocktail.write('''60ml Martini Extra Dry\n
5ml :red[Luxardo Maraschino]/Lazaroni Maraschino\n
2,5ml Syrop cukrowy\n
2d angostura\n''')
#Fancy_Vermouth_Cocktail.image("")
Fancy_Vermouth_Cocktail.write('''Metoda: Stir\n
:green[Szkło]: Old fashioned\n
:violet[Garnish]: Wedge limonka\n''')

Fiero_Spritz = st.expander("Fiero Spritz")
Fiero_Spritz.write('''60ml Martini Fiero\n
160ml Prosecco\n
Top up Woda Gazowana\n''')
#Fiero_Spritz.image("")
Fiero_Spritz.write('''Metoda: Najpierw wlać prosseco + woda gazowana, następnie Fiero\n
:green[Szkło]: Copa Martini\n
:violet[Garnish]: Plaster pomarańczy\n''')

French_75 = st.expander("French 75")
French_75.write('''25 ml Beefeater\n
20 ml sok z cytryny\n
10 ml syrop cukrowy\n''')
#French_75.image("")
French_75.write('''Top up (ok 50 ml) Champagne (Mumm Brut)\n
Metoda: Shake + fine strain & top up\n
:green[Szkło]: Flute glass\n
:violet[Garnish]: Zest z cytryny\n''')

French_Martini = st.expander("French Martini")
French_Martini.write('''50 ml Ostoya\n
40 ml :red[soku z ananasa]\n
15 ml Chambord\n''')
#French_Martini.image("")
French_Martini.write('''Metoda: Shake\n
:green[Szkło]: Flute glass\n
:violet[Garnish]: Kwiaty hibiskusa\n''')

Gimlet_classic = st.expander("Gimlet (Classic)")
Gimlet_classic.write('''60ml :red[Tanqueray Ten]\n
5ml sok z limonki\n
5ml sok z cytryny\n
10ml kordiał limonkowy\n''')
#Gimlet_classic.image("")
Gimlet_classic.write('''Metoda: Shake\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Aromatyzacja pustego szkła zestem z cytryny i limonki, wedge limonki na rant szkła''')

Gimlet_dry = st.expander("Gimlet (Dry)")
Gimlet_dry.write('''70ml :red[Tanqueray Ten]\n
10ml kordiał limonkowy\n''')
#Gimlet_dry.image("")
Gimlet_dry.write('''Metoda: Shake\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Aromatyzacja pustego szkła zestem z cytryny i limonki, wedge limonki na rant szkła''')

Gin_Basil_Smash = st.expander("Gin Basil Smash")
Gin_Basil_Smash.write('''40ml Beefeater\n
30ml soku z cytryny\n
20ml syrop cukrowy\n
Garść bazylia\n''')
#Gin_Basil_Smash.image("")
Gin_Basil_Smash.write('''Metoda: smash, shake\n
:green[Szkło]: Old fashioned\n
:violet[Garnish]: Top bazylia''')

Hanky_Panky_Martini = st.expander("Hanky Panky Martini")
Hanky_Panky_Martini.write('''30ml :red[Tanqueray Ten]\n
30ml Martini rubino\n
5ml Fernet Branca\n''')
#Hanky_Panky_Martini.image("")
Hanky_Panky_Martini.write('''Metoda: Stir\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Zest z pomarańczy''')

Hemingway_Daiquiri = st.expander("Hemingway Daiquiri")
Hemingway_Daiquiri.write('''60 ml Havana 3yo\n
40 ml soku z grejpfruta\n
15 ml soku z limonki\n
10 ml likieru maraschino\n''')
#Hemingway_Daiquiri.image("")
Hemingway_Daiquiri.write('''Metoda: Shake\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Wedge limonki''')

Hugo = st.expander("Hugo")
Hugo.write('''100 ml prosecco\n
20 ml St. Germain\n
20 ml soda water\n
Garść liści mięty\n''')
#Hugo.image("")
Hugo.write('''Metoda: Build\n
:green[Szkło]: Old fashioned\n
:violet[Garnish]: Liście mięty, wedge lime''')

Irish_Coffee = st.expander("Irish Coffee")
Irish_Coffee.write('''40ml Jameson\n
1szt. Espresso dopio\n
100ml śmietanka 36%\n
20ml syrop cukrowy\n''')
#Irish_Coffee.image("")
Irish_Coffee.write('''Metoda: Shake, warstwy\n
Kawę z whiskey przelewy do szklanki z uszkiem. Śmietankę mocno shakujemy z syropem i 2
kostkami lodu (można dodać sprężynkę z straynera), by była prawie sztywna. Potem wlewamy po
łyżce by utworzyła warstwę.\n
:green[Szkło]: szklanka z uchem''')

Jameson_Apple = st.expander("Jameson Apple")
Jameson_Apple.write('''40 ml Jameson\n
20 ml Syrop :red[Jabłko korzeń]/Jabłko\n
1d Angostura\n
Top up Woda gaz.\n''')
#Jameson_Apple.image("")
Jameson_Apple.write('''Metoda: Build\n
:green[Szkło]: Highball\n
:blue[Lód]: Kości\n
:violet[Garnish]: Laska cynamonu, jabłko suszone''')

Japanese_Cocktail = st.expander("Japanese Cocktail")
Japanese_Cocktail.write('''40 ml Martel VS\n
10ml orgeat\n
3d angostury\n''')
#Japanese_Cocktail.image("")
Japanese_Cocktail.write('''Metoda: Shake\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Zest z cytryny''')

Lillet_Spritz = st.expander("Lillet Spritz")
Lillet_Spritz.write('''40 ml Lillet Blanc/ Lillet Rouge\n
Tonik Fentimans\n''')
#Lillet_Spritz.image("")
Lillet_Spritz.write('''Metoda: Build\n
:green[Szkło]: Lillet\n
:blue[Lód]: Kości\n
:violet[Garnish]: Ogórek, mięta / :red[mrożona truskawka]''')

Long_Island = st.expander("Long Island Iced Tea")
Long_Island.write('''20 ml Ostoya\n
20 ml Beefeater\n
20 ml Olmeca Blanco\n
20 ml Havana Club 3yo\n
20 ml Cointreau\n
20 ml sok z cytryny\n
10 ml syrop cukrowy\n
1 szt. Pepsi (ok. 70 ml)\n''')
#Long_Island.image("")
Long_Island.write('''Metoda: Shake (pierwsze 7 pozycji), warstwowo (najpierw pepsi potem reszta).\n
:green[Szkło]: Mały pokal\n
:blue[Lód]: Kości\n
:violet[Garnish]: Cząstka limonki''')

Mai_Tai = st.expander("Mai-Tai")
Mai_Tai.write('''30ml Havana especial\n
30ml Havana 7YO\n
10ml Falernum\n
10ml Cointreau\n
10ml Orgeat\n
30ml sok z limonki\n
2d absinthe\n''')
#Mai_Tai.image("")
Mai_Tai.write('''Metoda: Shake\n
:green[Szkło]: Highball, kruszonka\n
:violet[Garnish]: Tiki deko (na bogato)''')

Manhattan = st.expander("Manhattan")
Manhattan.write('''40 ml Maker’s Mark\n
20 ml Martini Rubino\n
1 dash Angostura\n''')
#Manhattan.image("")
Manhattan.write('''Metoda: Stir, straight-up\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Maraska do kieliszka, a pomarańczowy zest tylko do aromatu''')

Margarita = st.expander("Margarita")
Margarita.write('''40 ml Olmeca Altos Blanco\n
20 ml Cointreau\n
20 ml sok z limonki\n
5 ml syrop cukrowy\n''')
#Margarita.image("")
Margarita.write('''Metoda: Shake + fine strain\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: Crusta z soli na połowie kieliszka''')

Martini_Negroni = st.expander("Martini Negroni")
Martini_Negroni.write('''20 ml Beefeater\n
20 ml Martini Bitteri\n
20 ml Martini Riserva Rubino\n''')
#Martini_Negroni.image("")
Martini_Negroni.write('''Metoda: Stir lub Throwing lub Bulid
:green[Szkło]: Old fashioned
:blue[Lód]: Kości
:violet[Garnish]: Zest z cytryny + cząstka pomarańczy/zest z pomarańczy''')

Mary_Pickford = st.expander("Mary Pickford")
Mary_Pickford.write('''60 ml Havana 3\n
45 ml :red[sok ananasowy]\n
5 ml :red[grenadyna]\n
5 ml likier maraschino\n''')
#Mary_Pickford.image("")
Mary_Pickford.write('''Metoda: Shake\n
:green[Szkło]: Coupe glass\n
:violet[Garnish]: :red[chips z ananasa]''')

Milano_Torino = st.expander("Milano Torino(Mi-To)")
Milano_Torino.write('''40 ml Campari\n
40 ml Martini Rubino\n''')
#Milano_Torino.image("")
Milano_Torino.write('''Metoda: Stir\n
:green[Szkło]: Old fashioned\n
:violet[Garnish]: Pół plasterka pomarańczy''')

Mint_Julep = st.expander("Mint Julep")
Mint_Julep.write('''40ml Maker’s Mark\n
5ml syrop cukrowy\n
Garść liści mięty\n''')
#Mint_Julep.image("")
Mint_Julep.write('''Metoda: Julep, kruszony :blue[Lód]\n
:green[Szkło]: Highball\n
:violet[Garnish]: Szczyt mięty, cukier puder''')

Mojito = st.expander("Mojito")
Mojito.write('''40 ml Havana Club 3yo\n
25 ml sok z limonki\n
15 ml syrop cukrowy\n
Garść mięty\n
Top woda gazowana\n''')
#Mojito.image("")
Mojito.write('''Metoda: Build\n
:green[Szkło]: Highball Havana\n
:blue[Lód]: Kości\n
:violet[Garnish]: Top mięty''')

Morning_Glory_Fizz = st.expander("Morning Glory Fizz")
Morning_Glory_Fizz.write('''40ml Monkey shoulder\n
5ml Absinth\n
15ml sok z limonki\n
15ml sok z cytryny\n
20ml syrop cukrowy\n
20ml białko\n
Top woda gazowana\n''')
#Morning_Glory_Fizz.image("")
Morning_Glory_Fizz.write('''Metoda: Reverse shake\n
:green[Szkło]: Highball\n
:violet[Garnish]: Plaster limonki''')

Moscow_Mule = st.expander("Moscow Mule")
Moscow_Mule.write('''40 ml Ostoya\n
1 szt. Ginger Beer\n
2 cząstki limonki(wciśnięte)\n
Splash syropu cukrowego\n''')
#Moscow_Mule.image("")
Moscow_Mule.write('''Metoda: Build\n
:green[Szkło]: Old fashioned\n
:blue[Lód]: Kosci\n
:violet[Garnish]: Top mięty''')

Negroni_Sbagliato = st.expander("Negroni Sbagliato")
Negroni_Sbagliato.write('''20ml Martini Bitter\n
20ml Martini Rubino\n
Top Prosecco\n''')
#Negroni_Sbagliato.image("")
Negroni_Sbagliato.write('''Metoda: build, bardzo delikatnie by nie stracić bąbla\n
:green[Szkło]: Old fashioned\n
:violet[Garnish]: Pół plasterka pomarańczy''')

Negroni_Spumante = st.expander("Negroni Spumante")
Negroni_Spumante.write('''20ml Beefeater\n
20ml Martini Bitter\n
20ml Martini Rubino\n
Top Prosecco\n''')
#Negroni_Spumante.image("")
Negroni_Spumante.write('''Metoda: Stir, Top Prosecco i delikatny stir\n
:green[Szkło]: Old fashioned\n
:violet[Garnish]: Pół plasterka pomarańczy''')