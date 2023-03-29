import streamlit as st
from PIL import Image
import os
import pandas as pd
st.set_page_config(page_title="Bar Koszyki", page_icon=Image.open("logo.png"))

def main():
    st.title("Bar koszyki - manual")


    submenu = st.sidebar.selectbox("Menu", ["Manual Koktajli", "Piwo", "Wino"])
    if submenu == "Manual Koktajli":
        st.title("Manual Koktajli")

        amaretto_sour = st.expander("Amaretto sour")
        amaretto_sour.write("""40ml Amaretto</br>
        20ml Balantinnes</br>
        30ml sok z limonki</br>
        15ml białko</br>
        5ml syrop cukrowy</br>
        2d angostura</br>""", unsafe_allow_html=True)
        amaretto_sour.image("CocktailImages/amaretto.jpg")
        amaretto_sour.write('''Metoda: reverse shake</br>
        :green[Szkło]: Coupe glass''', unsafe_allow_html=True)

        americano = st.expander("Americano")
        americano.write('''30 ml Martini Bitter<br>
        30 ml Martini Riserva Rubino<br>
        Top up soda<br>''', unsafe_allow_html=True)
        americano.image("CocktailImages/americano.jpg")
        americano.write('''Metoda: Build + zamieszać<br>
        :blue[Lód]: Kości<br>
        :green[Szkło]: highball<br>
        :violet[Garnish]: Pół plasterka pomarańczy, zest z cytryny<br>''', unsafe_allow_html=True)

        aviation = st.expander("Aviation")
        aviation.write('''40ml Beefeater<br>
        20ml Sour<br>
        15ml :red[Luxardo Maraschino]/Lazaroni Maraschino<br>
        10ml Crème de Violette<br>
        5ml Sweet<br>
        ''', unsafe_allow_html=True)
        aviation.image("CocktailImages/aviation.jpg")
        aviation.write('''Metoda: Shake, fine strain<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Wisienka maraschino na szpadce<br>''', unsafe_allow_html=True)

        Bees_Knees = st.expander("Bees Knees")
        Bees_Knees.write('''60ml Beefeater<br>
        20ml sok z cytryny<br>
        20ml sok pomarańczowy<br>
        15ml syrop miodowy<br>''', unsafe_allow_html=True)
        Bees_Knees.image("CocktailImages/bees_knees.jpg")
        Bees_Knees.write('''Metoda: shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: zest z pomarańczy<br>''', unsafe_allow_html=True)

        Bellini = st.expander("Bellini")
        Bellini.write('''100ml prosecco<br>
        40ml :red[puree brzoskwiniowe]/liker brzoskwiniowy<br>''', unsafe_allow_html=True)
        Bellini.image("CocktailImages/bellini.jpg")
        Bellini.write('''Metoda: build<br>
        :green[Szkło]: flute glass<br>''', unsafe_allow_html=True)

        Bijou = st.expander("Bijou")
        Bijou.write('''40ml :red[Tanqueray Ten]<br>
        20ml :red[Chartreause Green]<br>
        30ml Martini Rubino<br>
        2d Orange bitters<br>''', unsafe_allow_html=True)
        Bijou.image("CocktailImages/bijou.jpg")
        Bijou.write('''Metoda: Stir<br>
        :green[Szkło]: Coupe glass<br>''', unsafe_allow_html=True)

        Boulevardier = st.expander("Boulevardier")
        Boulevardier.write('''20ml Jim Beam Rye<br>
        20ml Martini Bitter<br>
        20ml Martini Rubino<br>''', unsafe_allow_html=True)
        Boulevardier.image("CocktailImages/boulevardier.jpg")
        Boulevardier.write('''Metoda: Stir<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Zest z pomarańczy<br>''', unsafe_allow_html=True)

        Bramble = st.expander("Bramble")
        Bramble.write('''40ml Beefeater<br>
        25ml sok z cytryny<br>
        15ml syrop cukrowy<br>
        15ml briottet creme de cassis<br>''', unsafe_allow_html=True)
        Bramble.image("CocktailImages/bramble.jpg")
        Bramble.write('''Metoda: Shake, top creme de cassis<br>
        :green[Szkło]: Old fashioned<br>
        :blue[Lód]: Kruszonka<br>
        :violet[Garnish]: Top mięty, świeże owoce<br>''', unsafe_allow_html=True)

        Brandy_Alexander = st.expander("Brandy Alexander")
        Brandy_Alexander.write('''30 ml Martel VS<br>
        20 ml Crème de Cacao<br>
        30 ml Half&Half<br>
        Dash chocolate bitters<br>''', unsafe_allow_html=True)
        Brandy_Alexander.image("CocktailImages/brandy_alexander.jpg")
        Brandy_Alexander.write('''Metoda: Shake, Fine Strain<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Tarta gałka muszkatołowa<br>''', unsafe_allow_html=True)

        Breakfast_Martini = st.expander("Breakfast Martini")
        Breakfast_Martini.write('''50 ml Beefeater<br>
        20 ml Cointreau<br>
        20 ml soku z cytryny<br>
        2 :red[łyżki marmolady pomarańczowej]<br>''', unsafe_allow_html=True)
        Breakfast_Martini.image("CocktailImages/breakfast_martini.jpg")
        Breakfast_Martini.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z pomarańczy<br>''', unsafe_allow_html=True)

        Brooklyn = st.expander("Brooklyn")
        Brooklyn.write('''40 ml Rye Whisky<br>
        20 ml Dry Vermouth<br>
        5 ml :red[Luxardo Marashino]/Lazaroni Maraschino<br>
        5 ml Amaro<br>
        2 dash orange bitter<br>''', unsafe_allow_html=True)
        Brooklyn.image("CocktailImages/brooklyn.jpg")
        Brooklyn.write('''Metoda: Stir<br>
        :green[Szkło] : Coupe glass<br>
        :violet[Garnish]: Zest z pomarańczy, wisienka maraschino<br>''', unsafe_allow_html=True)

        Caipirinha = st.expander("Caipirinha")
        Caipirinha.write('''40 ml Cachaca<br>
        3 łyżeczki barmańskie cukru trzcinowego<br>
        4 cząstki limonki<br>''', unsafe_allow_html=True)
        Caipirinha.image("CocktailImages/caipirinha.jpg")
        Caipirinha.write('''Metoda: muddlujemy limonki z cukrem, zasypujemy kruszonym lodem, wlewamy cachace,
        mieszamy. Usypujemy górkę z lodu i dekorujemy cząstkami z limonki.<br>
        :green[Szkło]: Old fashioned<br>
        :blue[Lód]: Kruszonka <br>
        :violet[Garnish]: Cząstka limonki, pokruszony lód<br>''', unsafe_allow_html=True)

        Champagne_Cocktail = st.expander("Champagne Cocktail")
        Champagne_Cocktail.write('''100 ml Mumm Brut<br>
        10 ml Martell VS<br>
        2 dash Angostura<br>
        1 kostka cukru<br>''', unsafe_allow_html=True)
        Champagne_Cocktail.image("CocktailImages/champagne_cocktail.jpg")
        Champagne_Cocktail.write('''Metoda: umieść nasączoną kostkę cukru dwoma kroplami angostury, dodaj koniak następnie
        szampan.<br>
        :green[Szkło]: champagne glass<br>
        :blue[Lód]: -<br>
        :violet[Garnish]: Zest z pomarańczy i wisienka maraschino<br>''', unsafe_allow_html=True)

        Clover_Club = st.expander("Clover Club")
        Clover_Club.write('''40ml Beefeater<br>
        15ml Martini Extra Dry<br>
        25ml soku z cytryny<br>
        15ml :red[grenadine]<br>
        10ml białko<br>''', unsafe_allow_html=True)
        Clover_Club.image("CocktailImages/clover_club.jpg")
        Clover_Club.write('''Metoda: Shake, double strain<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: :red[Maliny na szpadce], cukier puder<br>''', unsafe_allow_html=True)

        Cointreau_Teese = st.expander("Cointreau Teese")
        Cointreau_Teese.write('''40ml cointreau<br>
        40ml sok jabłkowy<br>
        15ml Creme de violette<br>
        15ml sok z limonki<br>''', unsafe_allow_html=True)
        # Cointreau_Teese.image("")
        Cointreau_Teese.write('''Metoda: Shake
        :green[Szkło]: Coupe glass
        :violet[Garnish]: :red[Fiołek]/Zest z pomarańczy''', unsafe_allow_html=True)

        Corpse_reviver_1 = st.expander("Corpse Reviver no.1")
        Corpse_reviver_1.write('''40ml Cognac<br>
        20 ml :red[Calvados]<br>
        20 ml Martini Rubino<br>''', unsafe_allow_html=True)
        # Corpse_reviver_1.image("")
        Corpse_reviver_1.write('''Metoda: Stir<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z pomarańczy<br>''', unsafe_allow_html=True)

        Corpse_Reviver_2 = st.expander("Corpse Reviver no.2")
        Corpse_Reviver_2.write('''20ml :red[Tanqueray Ten]<br>
        20ml Cointreau<br>
        20ml Lillet Blanc<br>
        20ml sok z cytryny<br>
        1d Absinth<br>''', unsafe_allow_html=True)
        # Corpse_Reviver_2.image("")
        Corpse_Reviver_2.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z cytryny, aromatyzacja absyntem<br>''', unsafe_allow_html=True)

        Cosmopolitan = st.expander("Cosmopolitan")
        Cosmopolitan.write('''40 ml Absolut Lime<br>
        20 ml Cointreau<br>
        20 ml sok z limonki<br>
        20 ml syrop żurawina<br>''', unsafe_allow_html=True)
        # Cosmopolitan.image("")
        Cosmopolitan.write('''Metoda: Shake, fine strain<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z pomarańczy<br>''', unsafe_allow_html=True)

        Cynar_Szprycer_1 = st.expander("Cynar Szprycer No.1")
        Cynar_Szprycer_1.write('''40 ml Cynar<br>
        10 ml Strega<br>
        140 ml Woda Gazowana<br>
        20 ml Ginger beer<br>''', unsafe_allow_html=True)
        # Cynar_Szprycer_1.image("")
        Cynar_Szprycer_1.write('''Metoda: Bulid + zamieszać<br>
        :blue[Lód]: Kości na full<br>
        :green[Szkło]: Copa<br>
        :violet[Garnish]: 2 plasterki imbiru + pokruszona laska cynamonu<br>''', unsafe_allow_html=True)

        Cynar_Szprycer_2 = st.expander("Cynar Szprycer No.2")
        Cynar_Szprycer_2.write('''40 ml Cynar<br>
        40 ml syrop :red[rabarbar] / jabłkowy<br>
        20 ml sour<br>
        Top up Woda Gazowana<br>''', unsafe_allow_html=True)
        # Cynar_Szprycer_2.image("")
        Cynar_Szprycer_2.write('''Metoda : Shake<br>
        :blue[Lód] : Kości<br>
        :green[Szkło] : Highball<br>
        :violet[Garnish] : Pół plasterka pomarańczy<br>''', unsafe_allow_html=True)

        Daiquiri = st.expander("Daiquiri")
        Daiquiri.write('''40 ml Havana 3yo/Dictator 12yo<br>
        25 ml sok z limonki<br>
        15 ml syrop cukrowy<br>
        5 dash :red[luxardo maraschino]/Lazaroni Maraschino<br>''', unsafe_allow_html=True)
        # Daiquiri.image("")
        Daiquiri.write('''Metoda: Shake, fine strain<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Suszka z limonki + aromatyzacja zestem z limonki<br>''', unsafe_allow_html=True)

        Dark_N_Stormy = st.expander("Dark n'Stormy")
        Dark_N_Stormy.write('''40ml Havana Especial<br>
        1x Puszka Ginger Beer<br>
        2x Wedge limonka<br>
        2d Angostura bitters<br>''', unsafe_allow_html=True)
        # Dark_N_Stormy.image("")
        Dark_N_Stormy.write('''Metoda: build (rum i angostura na wierzchu)<br>
        :green[Szkło]: Highball<br>
        :violet[Garnish]: Wciśnięte wedge, rum ma tworzyć warstwę z angosturą<br>''', unsafe_allow_html=True)

        Dirty_Martini = st.expander("Dirty Martini")
        Dirty_Martini.write('''60 ml Beefeater<br>
        10 ml Martini extra dry<br>
        10 ml (2 łyżeczki) Zalewa z oliwek<br>''', unsafe_allow_html=True)
        # Dirty_Martini.image("")
        Dirty_Martini.write('''Metoda: Stir<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: 2 Oliwki na szpadce<br>''', unsafe_allow_html=True)

        Elderflower_Spritz = st.expander("Elderflower Spritz")
        Elderflower_Spritz.write('''100 ml Sauvignon Blanc<br>
        40 ml St. Germain<br>
        100 ml woda gaz<br>''', unsafe_allow_html=True)
        # Elderflower_Spritz.image("")
        Elderflower_Spritz.write('''Metoda: Build + zamieszać<br>
        :green[Szkło]: Wine glass<br>
        :violet[Garnish]: Lime slice<br>''', unsafe_allow_html=True)

        Espresso_Martini = st.expander("Espresso Martini")
        Espresso_Martini.write('''40 ml Ostoya<br>
        20 ml :red[Kahlua]/Bols Coffee<br>
        1 espresso<br>
        5ml syrop waniliowy<br>''', unsafe_allow_html=True)
        # Espresso_Martini.image("")
        Espresso_Martini.write('''Metoda: Shake, fine strain<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: 3 Ziarenka kawy ułożone w koniczynkę<br>''', unsafe_allow_html=True)

        Fancy_Vermouth_Cocktail = st.expander("Fancy Vermouth Cocktail")
        Fancy_Vermouth_Cocktail.write('''60ml Martini Extra Dry<br>
        5ml :red[Luxardo Maraschino]/Lazaroni Maraschino<br>
        2,5ml Syrop cukrowy<br>
        2d angostura<br>''', unsafe_allow_html=True)
        # Fancy_Vermouth_Cocktail.image("")
        Fancy_Vermouth_Cocktail.write('''Metoda: Stir<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Wedge limonka<br>''', unsafe_allow_html=True)

        Fiero_Spritz = st.expander("Fiero Spritz")
        Fiero_Spritz.write('''60ml Martini Fiero<br>
        160ml Prosecco<br>
        Top up Woda Gazowana<br>''', unsafe_allow_html=True)
        # Fiero_Spritz.image("")
        Fiero_Spritz.write('''Metoda: Najpierw wlać prosseco + woda gazowana, następnie Fiero<br>
        :green[Szkło]: Copa Martini<br>
        :violet[Garnish]: Plaster pomarańczy<br>''', unsafe_allow_html=True)

        French_75 = st.expander("French 75")
        French_75.write('''25 ml Beefeater<br>
        20 ml sok z cytryny<br>
        10 ml syrop cukrowy<br>''', unsafe_allow_html=True)
        # French_75.image("")
        French_75.write('''Top up (ok 50 ml) Champagne (Mumm Brut)<br>
        Metoda: Shake + fine strain & top up<br>
        :green[Szkło]: Flute glass<br>
        :violet[Garnish]: Zest z cytryny<br>''', unsafe_allow_html=True)

        French_Martini = st.expander("French Martini")
        French_Martini.write('''50 ml Ostoya<br>
        40 ml :red[soku z ananasa]<br>
        15 ml Chambord<br>''', unsafe_allow_html=True)
        # French_Martini.image("")
        French_Martini.write('''Metoda: Shake<br>
        :green[Szkło]: Flute glass<br>
        :violet[Garnish]: Kwiaty hibiskusa<br>''', unsafe_allow_html=True)

        Gimlet_classic = st.expander("Gimlet (Classic)")
        Gimlet_classic.write('''60ml :red[Tanqueray Ten]<br>
        5ml sok z limonki<br>
        5ml sok z cytryny<br>
        10ml kordiał limonkowy<br>''', unsafe_allow_html=True)
        # Gimlet_classic.image("")
        Gimlet_classic.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Aromatyzacja pustego szkła zestem z cytryny i limonki, wedge limonki na rant szkła''', unsafe_allow_html=True)

        Gimlet_dry = st.expander("Gimlet (Dry)")
        Gimlet_dry.write('''70ml :red[Tanqueray Ten]<br>
        10ml kordiał limonkowy<br>''', unsafe_allow_html=True)
        # Gimlet_dry.image("")
        Gimlet_dry.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Aromatyzacja pustego szkła zestem z cytryny i limonki, wedge limonki na rant szkła''', unsafe_allow_html=True)

        Gin_Basil_Smash = st.expander("Gin Basil Smash")
        Gin_Basil_Smash.write('''40ml Beefeater<br>
        30ml soku z cytryny<br>
        20ml syrop cukrowy<br>
        Garść bazylia<br>''', unsafe_allow_html=True)
        # Gin_Basil_Smash.image("")
        Gin_Basil_Smash.write('''Metoda: smash, shake<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Top bazylia''', unsafe_allow_html=True)

        Hanky_Panky_Martini = st.expander("Hanky Panky Martini")
        Hanky_Panky_Martini.write('''30ml :red[Tanqueray Ten]<br>
        30ml Martini rubino<br>
        5ml Fernet Branca<br>''', unsafe_allow_html=True)
        # Hanky_Panky_Martini.image("")
        Hanky_Panky_Martini.write('''Metoda: Stir<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z pomarańczy''', unsafe_allow_html=True)

        Hemingway_Daiquiri = st.expander("Hemingway Daiquiri")
        Hemingway_Daiquiri.write('''60 ml Havana 3yo<br>
        40 ml soku z grejpfruta<br>
        15 ml soku z limonki<br>
        10 ml likieru maraschino<br>''', unsafe_allow_html=True)
        # Hemingway_Daiquiri.image("")
        Hemingway_Daiquiri.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Wedge limonki''', unsafe_allow_html=True)

        Hugo = st.expander("Hugo")
        Hugo.write('''100 ml prosecco<br>
        20 ml St. Germain<br>
        20 ml soda water<br>
        Garść liści mięty<br>''', unsafe_allow_html=True)
        # Hugo.image("")
        Hugo.write('''Metoda: Build<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Liście mięty, wedge lime''', unsafe_allow_html=True)

        Irish_Coffee = st.expander("Irish Coffee")
        Irish_Coffee.write('''40ml Jameson<br>
        1szt. Espresso dopio<br>
        100ml śmietanka 36%<br>
        20ml syrop cukrowy<br>''', unsafe_allow_html=True)
        # Irish_Coffee.image("")
        Irish_Coffee.write('''Metoda: Shake, warstwy<br>
        Kawę z whiskey przelewy do szklanki z uszkiem. Śmietankę mocno shakujemy z syropem i 2
        kostkami lodu (można dodać sprężynkę z straynera), by była prawie sztywna. Potem wlewamy po
        łyżce by utworzyła warstwę.<br>
        :green[Szkło]: szklanka z uchem''', unsafe_allow_html=True)

        Jameson_Apple = st.expander("Jameson Apple")
        Jameson_Apple.write('''40 ml Jameson<br>
        20 ml Syrop :red[Jabłko korzeń]/Jabłko<br>
        1d Angostura<br>
        Top up Woda gaz.<br>''', unsafe_allow_html=True)
        # Jameson_Apple.image("")
        Jameson_Apple.write('''Metoda: Build<br>
        :green[Szkło]: Highball<br>
        :blue[Lód]: Kości<br>
        :violet[Garnish]: Laska cynamonu, jabłko suszone''', unsafe_allow_html=True)

        Japanese_Cocktail = st.expander("Japanese Cocktail")
        Japanese_Cocktail.write('''40 ml Martel VS<br>
        10ml orgeat<br>
        3d angostury<br>''', unsafe_allow_html=True)
        # Japanese_Cocktail.image("")
        Japanese_Cocktail.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z cytryny''', unsafe_allow_html=True)

        Lillet_Spritz = st.expander("Lillet Spritz")
        Lillet_Spritz.write('''40 ml Lillet Blanc/ Lillet Rouge<br>
        Tonik Fentimans<br>''', unsafe_allow_html=True)
        # Lillet_Spritz.image("")
        Lillet_Spritz.write('''Metoda: Build<br>
        :green[Szkło]: Lillet<br>
        :blue[Lód]: Kości<br>
        :violet[Garnish]: Ogórek, mięta / :red[mrożona truskawka]''', unsafe_allow_html=True)

        Long_Island = st.expander("Long Island Iced Tea")
        Long_Island.write('''20 ml Ostoya<br>
        20 ml Beefeater<br>
        20 ml Olmeca Blanco<br>
        20 ml Havana Club 3yo<br>
        20 ml Cointreau<br>
        20 ml sok z cytryny<br>
        10 ml syrop cukrowy<br>
        1 szt. Pepsi (ok. 70 ml)<br>''', unsafe_allow_html=True)
        # Long_Island.image("")
        Long_Island.write('''Metoda: Shake (pierwsze 7 pozycji), warstwowo (najpierw pepsi potem reszta).<br>
        :green[Szkło]: Mały pokal<br>
        :blue[Lód]: Kości<br>
        :violet[Garnish]: Cząstka limonki''', unsafe_allow_html=True)

        Mai_Tai = st.expander("Mai-Tai")
        Mai_Tai.write('''30ml Havana especial<br>
        30ml Havana 7YO<br>
        10ml Falernum<br>
        10ml Cointreau<br>
        10ml Orgeat<br>
        30ml sok z limonki<br>
        2d absinthe<br>''', unsafe_allow_html=True)
        # Mai_Tai.image("")
        Mai_Tai.write('''Metoda: Shake<br>
        :green[Szkło]: Highball<br>
        :blue[Lód]: Kruszonka<br>
        :violet[Garnish]: Tiki deko (na bogato)''', unsafe_allow_html=True)

        Manhattan = st.expander("Manhattan")
        Manhattan.write('''40 ml Maker’s Mark<br>
        20 ml Martini Rubino<br>
        1 dash Angostura<br>''', unsafe_allow_html=True)
        # Manhattan.image("")
        Manhattan.write('''Metoda: Stir, straight-up<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Maraska do kieliszka, a pomarańczowy zest tylko do aromatu''', unsafe_allow_html=True)

        Margarita = st.expander("Margarita")
        Margarita.write('''40 ml Olmeca Altos Blanco<br>
        20 ml Cointreau<br>
        20 ml sok z limonki<br>
        5 ml syrop cukrowy<br>''', unsafe_allow_html=True)
        # Margarita.image("")
        Margarita.write('''Metoda: Shake + fine strain<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Crusta z soli na połowie kieliszka''', unsafe_allow_html=True)

        Martini_Negroni = st.expander("Martini Negroni")
        Martini_Negroni.write('''20 ml Beefeater<br>
        20 ml Martini Bitteri<br>
        20 ml Martini Riserva Rubino<br>''', unsafe_allow_html=True)
        # Martini_Negroni.image("")
        Martini_Negroni.write('''Metoda: Stir lub Throwing lub Bulid
        :green[Szkło]: Old fashioned
        :blue[Lód]: Kości
        :violet[Garnish]: Zest z cytryny + cząstka pomarańczy/zest z pomarańczy''', unsafe_allow_html=True)

        Mary_Pickford = st.expander("Mary Pickford")
        Mary_Pickford.write('''60 ml Havana 3<br>
        45 ml :red[sok ananasowy]<br>
        5 ml :red[grenadyna]<br>
        5 ml likier maraschino<br>''', unsafe_allow_html=True)
        # Mary_Pickford.image("")
        Mary_Pickford.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: :red[chips z ananasa]''', unsafe_allow_html=True)

        Milano_Torino = st.expander("Milano Torino(Mi-To)")
        Milano_Torino.write('''40 ml Campari<br>
        40 ml Martini Rubino<br>''', unsafe_allow_html=True)
        # Milano_Torino.image("")
        Milano_Torino.write('''Metoda: Stir<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Pół plasterka pomarańczy''', unsafe_allow_html=True)

        Mint_Julep = st.expander("Mint Julep")
        Mint_Julep.write('''40ml Maker’s Mark<br>
        5ml syrop cukrowy<br>
        Garść liści mięty<br>''', unsafe_allow_html=True)
        # Mint_Julep.image("")
        Mint_Julep.write('''Metoda: Julep<br>
        :green[Szkło]: Highball<br>
        :blue[Lód]: Kruszonka<br>
        :violet[Garnish]: Szczyt mięty, cukier puder''', unsafe_allow_html=True)

        Mojito = st.expander("Mojito")
        Mojito.write('''40 ml Havana Club 3yo<br>
        25 ml sok z limonki<br>
        15 ml syrop cukrowy<br>
        Garść mięty<br>
        Top woda gazowana<br>''', unsafe_allow_html=True)
        # Mojito.image("")
        Mojito.write('''Metoda: Build<br>
        :green[Szkło]: Highball Havana<br>
        :blue[Lód]: Kości<br>
        :violet[Garnish]: Top mięty''', unsafe_allow_html=True)

        Morning_Glory_Fizz = st.expander("Morning Glory Fizz")
        Morning_Glory_Fizz.write('''40ml Monkey shoulder<br>
        5ml Absinth<br>
        15ml sok z limonki<br>
        15ml sok z cytryny<br>
        20ml syrop cukrowy<br>
        20ml białko<br>
        Top woda gazowana<br>''', unsafe_allow_html=True)
        # Morning_Glory_Fizz.image("")
        Morning_Glory_Fizz.write('''Metoda: Reverse shake<br>
        :green[Szkło]: Highball<br>
        :violet[Garnish]: Plaster limonki''', unsafe_allow_html=True)

        Moscow_Mule = st.expander("Moscow Mule")
        Moscow_Mule.write('''40 ml Ostoya<br>
        1 szt. Ginger Beer<br>
        2 cząstki limonki(wciśnięte)<br>
        Splash syropu cukrowego<br>''', unsafe_allow_html=True)
        # Moscow_Mule.image("")
        Moscow_Mule.write('''Metoda: Build<br>
        :green[Szkło]: Old fashioned<br>
        :blue[Lód]: Kosci<br>
        :violet[Garnish]: Top mięty''', unsafe_allow_html=True)

        Negroni_Sbagliato = st.expander("Negroni Sbagliato")
        Negroni_Sbagliato.write('''20ml Martini Bitter<br>
        20ml Martini Rubino<br>
        Top Prosecco<br>''', unsafe_allow_html=True)
        # Negroni_Sbagliato.image("")
        Negroni_Sbagliato.write('''Metoda: build, bardzo delikatnie by nie stracić bąbla<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Pół plasterka pomarańczy''', unsafe_allow_html=True)

        Negroni_Spumante = st.expander("Negroni Spumante")
        Negroni_Spumante.write('''20ml Beefeater<br>
        20ml Martini Bitter<br>
        20ml Martini Rubino<br>
        Top Prosecco<br>''', unsafe_allow_html=True)
        # Negroni_Spumante.image("")
        Negroni_Spumante.write('''Metoda: Stir, Top Prosecco i delikatny stir<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Pół plasterka pomarańczy''', unsafe_allow_html=True)
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
        marcowe = st.subheader("Bierhalle Marcowe (podwójnie słodowany lager)")
        st.write('''Piwo marcowe, zwane również Oktoberfestbier, dawniej warzone było 
                  tylko sezonowo. Dzisiaj, dzięki nowoczesnym systemom chłodzenia można produkować 
                  je okrągły rok. Piwo jest pełne smaków pochodzących z mieszaniny słodów 
                  jęczmiennych i aromatycznego chmielu. <br> <br>
                  Alkohol: 5.2%''', unsafe_allow_html=True)
        pilsner = st.subheader("Pilsner Urquell")
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
                  fermentacjidla drożdży górnej fermentacji wynosi w przybliżeniu 20°C.
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
                  przy warzeniu koźlaków, piw pszenicznych lub pilznerów.''')

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
        
if __name__ == '__main__':
    main()
