import streamlit as st
from PIL import Image
import pandas as pd
st.set_page_config(page_title="Bar Koszyki", page_icon=Image.open("logo.png"))

def main():
    st.title("Bar koszyki - manual")


    submenu = st.sidebar.selectbox("Menu", ["Manual Koktajli", "Manual Alkoholi", "Piwo", "Wino"])
    if submenu == "Manual Koktajli":
        st.header("Manual Koktajli")

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
        Cointreau_Teese.image('CocktailImages/CIONTREAUTEESE.jpg')
        Cointreau_Teese.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: :red[Fiołek]/Zest z pomarańczy''', unsafe_allow_html=True)

        Corpse_reviver_1 = st.expander("Corpse Reviver no.1")
        Corpse_reviver_1.write('''40ml Cognac<br>
        20 ml :red[Calvados]<br>
        20 ml Martini Rubino<br>''', unsafe_allow_html=True)
        Corpse_reviver_1.image("CocktailImages/CORPSEREVIVER1.jpg")
        Corpse_reviver_1.write('''Metoda: Stir<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z pomarańczy<br>''', unsafe_allow_html=True)

        Corpse_Reviver_2 = st.expander("Corpse Reviver no.2")
        Corpse_Reviver_2.write('''20ml Beefeater<br>
        20ml Cointreau<br>
        20ml Lillet Blanc<br>
        20ml sok z cytryny<br>
        1d Absinth<br>''', unsafe_allow_html=True)
        Corpse_Reviver_2.image("CocktailImages/CORPSEREVIVER2.jpg")
        Corpse_Reviver_2.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z cytryny, aromatyzacja absyntem<br>''', unsafe_allow_html=True)

        Cosmopolitan = st.expander("Cosmopolitan")
        Cosmopolitan.write('''40 ml Absolut Lime<br>
        20 ml Cointreau<br>
        20 ml sok z limonki<br>
        20 ml syrop żurawina<br>''', unsafe_allow_html=True)
        Cosmopolitan.image("CocktailImages/COSMOPOLITAN.jpg")
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
        Dark_N_Stormy.image("CocktailImages/DARKNSTORMY.jpg")
        Dark_N_Stormy.write('''Metoda: build (rum i angostura na wierzchu)<br>
        :green[Szkło]: Highball<br>
        :violet[Garnish]: Wciśnięte wedge, rum ma tworzyć warstwę z angosturą<br>''', unsafe_allow_html=True)

        Dirty_Martini = st.expander("Dirty Martini")
        Dirty_Martini.write('''60 ml Beefeater<br>
        10 ml Martini extra dry<br>
        10 ml (2 łyżeczki) Zalewa z oliwek<br>''', unsafe_allow_html=True)
        Dirty_Martini.image("CocktailImages/DIRTYMARTINI.jpg")
        Dirty_Martini.write('''Metoda: Stir<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: 2 Oliwki na szpadce<br>''', unsafe_allow_html=True)

        Elderflower_Spritz = st.expander("Elderflower Spritz")
        Elderflower_Spritz.write('''100 ml Sauvignon Blanc<br>
        40 ml St. Germain<br>
        100 ml woda gaz<br>''', unsafe_allow_html=True)
        Elderflower_Spritz.image("CocktailImages/ELDERFLOWERSPRITZ.webp")
        Elderflower_Spritz.write('''Metoda: Build + zamieszać<br>
        :green[Szkło]: Wine glass<br>
        :violet[Garnish]: Lime slice<br>''', unsafe_allow_html=True)

        Espresso_Martini = st.expander("Espresso Martini")
        Espresso_Martini.write('''40 ml Ostoya<br>
        20 ml :red[Kahlua]/Bols Coffee<br>
        1 espresso<br>
        5ml syrop waniliowy<br>''', unsafe_allow_html=True)
        Espresso_Martini.image("CocktailImages/ESPRESSOMARTINI.jpg")
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
        Fiero_Spritz.write('''80ml Martini Fiero<br>
        160ml Prosecco<br>
        Top up Woda Gazowana<br>''', unsafe_allow_html=True)
        Fiero_Spritz.image("CocktailImages/FIEROSPRITZ.jpg")
        Fiero_Spritz.write('''Metoda: Najpierw wlać prosseco + woda gazowana, następnie Fiero<br>
        :green[Szkło]: Copa Martini<br>
        :violet[Garnish]: Plaster pomarańczy<br>''', unsafe_allow_html=True)

        French_75 = st.expander("French 75")
        French_75.write('''25 ml Beefeater<br>
        20 ml sok z cytryny<br>
        10 ml syrop cukrowy<br>''', unsafe_allow_html=True)
        French_75.image("CocktailImages/FRENCH75.jpg")
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
        Gimlet_classic.image("CocktailImages/GIMLETCLASSIC.jpg")
        Gimlet_classic.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Aromatyzacja pustego szkła zestem z cytryny i limonki, wedge limonki na rant szkła''', unsafe_allow_html=True)

        Gimlet_dry = st.expander("Gimlet (Dry)")
        Gimlet_dry.write('''70ml :red[Tanqueray Ten]<br>
        10ml kordiał limonkowy<br>''', unsafe_allow_html=True)
        Gimlet_dry.image("CocktailImages/GIMLETDRY.jpg")
        Gimlet_dry.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Aromatyzacja pustego szkła zestem z cytryny i limonki, wedge limonki na rant szkła''', unsafe_allow_html=True)

        Gin_Basil_Smash = st.expander("Gin Basil Smash")
        Gin_Basil_Smash.write('''40ml Beefeater<br>
        30ml soku z cytryny<br>
        20ml syrop cukrowy<br>
        Garść bazylia<br>''', unsafe_allow_html=True)
        Gin_Basil_Smash.image("CocktailImages/GINBASILSMASH.jpg")
        Gin_Basil_Smash.write('''Metoda: smash, shake<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Top bazylia''', unsafe_allow_html=True)

        Hanky_Panky_Martini = st.expander("Hanky Panky Martini")
        Hanky_Panky_Martini.write('''30ml :red[Tanqueray Ten]<br>
        30ml Martini rubino<br>
        5ml Fernet Branca<br>''', unsafe_allow_html=True)
        Hanky_Panky_Martini.image("CocktailImages/HANKYPANKYMARTINI.jpg")
        Hanky_Panky_Martini.write('''Metoda: Stir<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z pomarańczy''', unsafe_allow_html=True)

        Hemingway_Daiquiri = st.expander("Hemingway Daiquiri")
        Hemingway_Daiquiri.write('''60 ml Havana 3yo<br>
        40 ml soku z grejpfruta<br>
        15 ml soku z limonki<br>
        10 ml likieru maraschino<br>''', unsafe_allow_html=True)
        Hemingway_Daiquiri.image("CocktailImages/HEMINGWAYDAIQUIRI.jpg")
        Hemingway_Daiquiri.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Wedge limonki''', unsafe_allow_html=True)

        Horses_Neck = st.expander("Horse's Neck")
        Horses_Neck.write('''40 ml Jameson<br>
        1 Puszka Ginger beer<br>
        2 Cząstka limonki<br>
        2 Dash Angostura<br>''', unsafe_allow_html=True)
        #Horses_Neck.image("")
        Horses_Neck.write('''Metoda: Limonka i Ginger beer na początek, Jameson i Angostura tak, by powstały warstwy<br>
        :green[Szkło]: Highball<br>
        :blue[Lód]: Kości<br>
        :violet[Garnish]: Wciśnięta cząstka limonki''', unsafe_allow_html=True)

        Hugo = st.expander("Hugo")
        Hugo.write('''100 ml prosecco<br>
        20 ml St. Germain<br>
        20 ml soda water<br>
        Garść liści mięty<br>''', unsafe_allow_html=True)
        Hugo.image("CocktailImages/HUGO.jpg")
        Hugo.write('''Metoda: Build<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Liście mięty, wedge lime''', unsafe_allow_html=True)

        Irish_Coffee = st.expander("Irish Coffee")
        Irish_Coffee.write('''40ml Jameson<br>
        1szt. Espresso dopio<br>
        100ml śmietanka 36%<br>
        20ml syrop cukrowy<br>''', unsafe_allow_html=True)
        Irish_Coffee.image("CocktailImages/IRISHCOFFEE.jpg")
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
        Japanese_Cocktail.image("CocktailImages/JAPANESECOCKTAIL.jpg")
        Japanese_Cocktail.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z cytryny''', unsafe_allow_html=True)

        Lillet_Spritz = st.expander("Lillet Spritz")
        Lillet_Spritz.write('''40 ml Lillet Blanc/ Lillet Rouge<br>
        Tonik Fentimans<br>''', unsafe_allow_html=True)
        Lillet_Spritz.image("CocktailImages/LILLETSPRITZ.webp")
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
        Mai_Tai.image("CocktailImages/MAI-TAI.jpg")
        Mai_Tai.write('''Metoda: Shake<br>
        :green[Szkło]: Highball<br>
        :blue[Lód]: Kruszonka<br>
        :violet[Garnish]: Tiki deko (na bogato)''', unsafe_allow_html=True)

        Manhattan = st.expander("Manhattan")
        Manhattan.write('''40 ml Maker’s Mark<br>
        20 ml Martini Rubino<br>
        1 dash Angostura<br>''', unsafe_allow_html=True)
        Manhattan.image("CocktailImages/MANHATTAN.jpg")
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
        Martini_Negroni.image("CocktailImages/MARTININEGRONI.jpg")
        Martini_Negroni.write('''Metoda: Stir lub Throwing lub Bulid<br>
        :green[Szkło]: Old fashioned<br>
        :blue[Lód]: Kości<br>
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
        Milano_Torino.image("CocktailImages/MILANOTORINO.jpg")
        Milano_Torino.write('''Metoda: Stir<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Pół plasterka pomarańczy''', unsafe_allow_html=True)

        Mint_Julep = st.expander("Mint Julep")
        Mint_Julep.write('''40ml Maker’s Mark<br>
        5ml syrop cukrowy<br>
        Garść liści mięty<br>''', unsafe_allow_html=True)
        Mint_Julep.image("CocktailImages/MINTJULEP.jpg")
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
        Mojito.image("CocktailImages/MOJITO.jpg")
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
        Morning_Glory_Fizz.image("CocktailImages/MORNINGGLORYFIZZ.jpg")
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
        Negroni_Sbagliato.image("CocktailImages/NEGRONISBAGLIATO.jpg")
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
        newyorksour = st.expander("New York Sour")
        newyorksour.write('''40 ml Maker’s Mark<br>
        20 ml sok z cytryny<br>
        10 ml syrop cukrowy<br>
        20 ml białko cukiernicze<br>
        1 dash Angostura<br>
        20 ml Porto (float)<br>''', unsafe_allow_html=True)
        newyorksour.image("CocktailImages/NEWYORKSOUR.jpg")
        newyorksour.write('''Metoda: Shake (dry shake) 6 pierwszych składników, fine strain, float z Porto<br>
        :green[Szkło]: Old fashioned<br>
        :blue[Lód]: Kości<br>
        :violet[Garnish]: Zest z pomarańczy''', unsafe_allow_html=True)

        oldcuban = st.expander("Old Cuban")
        oldcuban.write('''40 ml Havana 7yo<br>
        20 ml sok z limonki<br>
        10 ml syrop demerara<br>
        1 dash Angostura<br>
        Garść mięty<br>
        Top up Prosecco<br>''', unsafe_allow_html=True)
        # oldcuban.image("")
        oldcuban.write('''Metoda: Shake + fine strain<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Szczyt mięty w suszce limonki''', unsafe_allow_html=True)

        oldfashioned = st.expander("Old Fashioned")
        oldfashioned.write('''40 ml Maker’s Mark<br>
        5 ml Demerara<br>
        2 dash Angostura<br>
        2 dash Orange bitter<br>''', unsafe_allow_html=True)
        oldfashioned.image("CocktailImages/OLDFASHIONED.jpg")
        oldfashioned.write('''Metoda: Stir, strain on the rocks<br>
        :green[Szkło]: Old fashioned<br>
        :blue[Lód]: Kości<br>
        :violet[Garnish]: Zest z pomarańczy''', unsafe_allow_html=True)

        orangeclub = st.expander("Orange Club")
        orangeclub.write('''40 ml Beefeater blood orange<br>
        10 ml Lillet Blanc<br>
        15 ml syrop malina<br>
        20 ml limonka<br>
        10 ml białko<br>''', unsafe_allow_html=True)
        orangeclub.image("CocktailImages/ORANGECLUB.jpg")
        orangeclub.write('''Metoda: Shake + fine strain<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Puder''', unsafe_allow_html=True)

        paloma = st.expander("Paloma")
        paloma.write('''40 ml Olmeca Altos Bianco<br>
        20ml kordiał grejpfrutowy<br>
        2 cząstki limonki (wciśnięte)<br>
        1 dash tynktury hibiskusowej<br>
        Top woda gazowana<br>''', unsafe_allow_html=True)
        # paloma.image("")
        paloma.write('''Metoda: Build + Stir<br>
        :green[Szkło]: Mały pokal<br>
        :violet[Garnish]: Cząstka grejpfruta''', unsafe_allow_html=True)

        paperplane = st.expander("Paper Plane")
        paperplane.write('''20ml Burbon<br>
        20ml Amaro<br>
        20ml Aperitivo<br>
        20ml Sour<br>''', unsafe_allow_html=True)
        paperplane.image("CocktailImages/PAPERPLANE.jpg")
        paperplane.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z cytryny''', unsafe_allow_html=True)

        penicillin = st.expander("Penicillin")
        penicillin.write('''40ml Ballantines<br>
        20ml sok z cytryny<br>
        20ml :red[syrop miodowo-imbirowy]<br>
        Top 10ml Ardbeg 10<br>''', unsafe_allow_html=True)
        penicillin.image("CocktailImages/PENICILLIN.jpg")
        penicillin.write('''Metoda: Shake, top Ardbeg 10<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Plaster imbiru''', unsafe_allow_html=True)

        pinklady = st.expander("Pink Lady")
        pinklady.write('''40ml Beefeater Pink<br>
        20ml Cointreau<br>
        20ml Limonka<br>
        15ml Białko<br>
        10ml Syrop truskawka<br>''', unsafe_allow_html=True)
        # pinklady.image("")
        pinklady.write('''Metoda: Dry shake + shake , Fine strain<br>
        :green[Szkło]: martini glass<br>
        :violet[Garnish]: Puder hibiskus''', unsafe_allow_html=True)

        piscosour = st.expander("Pisco Sour")
        piscosour.write('''40 ml Pisco<br>
        25ml sok z limonki<br>
        10 ml Syrop cukrowy<br>
        3 dash angostura<br>
        20ml białko<br>''', unsafe_allow_html=True)
        piscosour.image("CocktailImages/PISCOSOUR.jpg")
        piscosour.write('''Metoda: Dry shake + shake , Fine strain<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: 3 Krople Angostury''', unsafe_allow_html=True)

        pornstar = st.expander("Pornstar Martini")
        pornstar.write('''40 ml Ostoya<br>
        20 ml Sok z limonki<br>
        20 ml Marakuja<br>
        20 ml Syrop waniliowy<br>
        40 ml Prosecco<br>''', unsafe_allow_html=True)
        pornstar.image("CocktailImages/PORNSTARMARTINI.jpg")
        pornstar.write('''Metoda: Wszystkie składniki oprócz prosecco 
        shakeujemy i przelewamy do szkła, w kieliszku
        obok wlewamy prosecco<br>
        :green[Szkło]: Coupe glass, kieliszek do wódki<br>
        :violet[Garnish]: Suszka z limonki''', unsafe_allow_html=True)

        ramos = st.expander("Ramos Gin Fizz")
        ramos.write('''60ml Beefeater<br>
        15ml Sok z limonki<br>
        15ml Sok z cytryny<br>
        20ml Syrop cukrowy<br>
        3d Pomarańczowa woda kwiatowa<br>
        20ml Białko<br>
        20ml Half&half<br>
        Top woda gazowana<br>''', unsafe_allow_html=True)
        ramos.image("CocktailImages/RAMOSGINFIZZ.jpg")
        ramos.write('''Metoda: Shake (b. długi)<br>
        :green[Szkło]: Highball<br>
        :violet[Garnish]: Pianka wystająca ponad rant''', unsafe_allow_html=True)

        rev_vesper = st.expander("Reverse Vesper Martini")
        rev_vesper.write('''30ml Lillet Blanc<br>
        10ml Beefeater<br>
        20ml Ostoya<br>''', unsafe_allow_html=True)
        rev_vesper.image("CocktailImages/REVERSEVESPERMARTINI.jpg")
        rev_vesper.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z cytryny''', unsafe_allow_html=True)

        righthand = st.expander("(The) Right Hand")
        righthand.write('''20ml Havana Especial<br>
        20ml Martini Bitter<br>
        20ml Martini rubino<br>
        2d Chocolate bitters<br>''', unsafe_allow_html=True)
        # righthand.image("")
        righthand.write('''Metoda: Stir<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Zest z pomarańczy''', unsafe_allow_html=True)

        rosita = st.expander("Rosita")
        rosita.write('''50 ml Tequila Reposado<br>
        15 ml Martini Bitter<br>
        15 ml Martini Rubino<br>
        15 ml :red[Dolin Dry]<br>
        2d Angostura<br>''', unsafe_allow_html=True)
        rosita.image("CocktailImages/ROSITA.jpg")
        rosita.write('''Metoda: Stir<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Zest z cytryny''', unsafe_allow_html=True)

        russianpunch = st.expander("Russian Spring Punch")
        russianpunch.write('''45 ml Ostoya<br>
        25 ml Soku z cytryny<br>
        10 ml likieru Creme de cassis<br>
        10 ml Syropu truskawkowego<br>
        Top Prosecco<br>''', unsafe_allow_html=True)
        # russianpunch.image("")
        russianpunch.write('''Metoda: Shake, top Prossceco<br>
        :green[Szkło]: Copa/highball<br>
        :violet[Garnish]: Top mięty, zest z pomarańczy''', unsafe_allow_html=True)

        sazerac = st.expander("Sazerac")
        sazerac.write('''25ml Jim Beam Rye<br>
        25ml Martel VS<br>
        5ml Syrop cukrowy<br>
        3d Peychoud’s bitters<br>
        1d Absynt<br>''', unsafe_allow_html=True)
        sazerac.image("CocktailImages/SAZERAC.jpg")
        sazerac.write('''Metoda: Stir + aromatyzacja szkła absyntem<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Zest z cytryny''', unsafe_allow_html=True)

        sidecard = st.expander("Sidecard")
        sidecard.write('''40ml Martel VS<br>
        20ml Cointreau<br>
        10ml sok z cytryny<br>''', unsafe_allow_html=True)
        sidecard.image("CocktailImages/SIDECARD.jpg")
        sidecard.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Crusta z cukru pudru, zest z cytryny''', unsafe_allow_html=True)

        silverfizz = st.expander("Silver Gin Fizz")
        silverfizz.write('''45ml Beefeater<br>
        15ml Sok z cytryny<br>
        15ml Sok z limonki<br>
        20ml Syrop cukrowy<br>
        20ml Białko<br>
        Top Woda gazowana<br>''', unsafe_allow_html=True)
        silverfizz.image("CocktailImages/SILVERGINFIZZ.jpg")
        silverfizz.write('''Metoda: Reverse shake<br>
        :green[Szkło]: Highball<br>
        :violet[Garnish]: Top mięta''', unsafe_allow_html=True)

        tomcollins = st.expander("Tom Collins")
        tomcollins.write('''40ml Beefeater<br>
        20 ml Sok z cytryny<br>
        10ml Syrop cukrowy<br>
        Top Woda gazowana<br>''', unsafe_allow_html=True)
        tomcollins.image("CocktailImages/TOMCOLLINS.jpg")
        tomcollins.write('''Metoda: Shake<br>
        :green[Szkło]: Mały pokal<br>
        :violet[Garnish]: Plaster pomarańczy i wisienka maraschino''', unsafe_allow_html=True)

        tommymargarita = st.expander("Tommy's Margarita")
        tommymargarita.write('''40ml Olmeca Altos Reposado<br>
        20ml Sok z limonki<br>
        10ml Syrop z agawy<br>''', unsafe_allow_html=True)
        tommymargarita.image("CocktailImages/TOMMYSMARGARITA.jpg")
        tommymargarita.write('''Metoda: Shake<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Suszka z limonki<br>''', unsafe_allow_html=True)

        torinorickey = st.expander("Torino Rickey")
        torinorickey.write('''60ml Martini rubino<br>
        Pół limonki<br>
        Top soda<br>''', unsafe_allow_html=True)
        torinorickey.image("CocktailImages/TORINORICKEY.png")
        torinorickey.write('''Metoda: Build<br>
        :green[Szkło]: Highball<br>
        :violet[Garnish]: Wciśnięta limonka''', unsafe_allow_html=True)

        vesper = st.expander("Vesper Dry Martini")
        vesper.write('''60ml Beefeater<br>
        20ml Ostoya<br>
        10ml Lillet Blanc<br>''', unsafe_allow_html=True)
        vesper.image("CocktailImages/VESPERDRYMARTINI.jpg")
        vesper.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z cytryny''', unsafe_allow_html=True)

        vieux = st.expander("Vieux Carre")
        vieux.write('''25ml Jim Beam Rye<br>
        25ml Martel VS<br>
        25ml Martini rubino<br>
        5ml :red[Benedictine]<br>
        2d Peychoud’s<br>
        2d Angostura<br>''', unsafe_allow_html=True)
        vieux.image("CocktailImages/VIEUXCARRE.jpg")
        vieux.write('''Metoda: Stir<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Zest z cytryny''', unsafe_allow_html=True)

        vodkamartini = st.expander("Vodka Martini")
        vodkamartini.write('''60 ml Wyborowa Exquisite<br>
        15 ml Martini Extra Dry<br>''', unsafe_allow_html=True)
        vodkamartini.image("CocktailImages/VODKAMARTINI.jpg")
        vodkamartini.write('''Metoda: Stir<br>
        :green[Szkło] : Coupe glass<br>
        :violet[Garnish]: Zest z cytryny''', unsafe_allow_html=True)

        vodkasour = st.expander("Vodka Sour")
        vodkasour.write('''40 ml Ostoya<br>
        20 ml Sok z cytryny<br>
        20 ml Białko<br>
        10 ml Syrop cukrowy<br>
        2 dash Angostura<br>''', unsafe_allow_html=True)
        vodkasour.image("CocktailImages/WHISKY SOUR1.jpg")
        vodkasour.write('''Metoda: Dry Shake + shake<br>
        :green[Szkło]: Old fashioned<br>
        :blue[Lód]: Kości<br>
        :violet[Garnish]: Zest z cytryny''', unsafe_allow_html=True)

        whiskysmash = st.expander("Whisky Smash")
        whiskysmash.write('''40ml Jim Beam<br>
        Pół Cytryny<br>
        20ml Syrop cukrowy<br>
        Garść mięty<br>''', unsafe_allow_html=True)
        whiskysmash.image("CocktailImages/WHISKYSMASH.png")
        whiskysmash.write('''Metoda: Smash, shake<br>
        :green[Szkło]: Old fashioned<br>
        :violet[Garnish]: Szczyt mięty, plaster cytryny''', unsafe_allow_html=True)

        whiskysour = st.expander("Whisky Sour")
        whiskysour.write('''40 ml Ballantines<br>
        30 ml Sok z cytryny<br>
        15 ml Syrop cukrowy<br>
        15 ml Białko<br>
        2 dash Angostura<br>''', unsafe_allow_html=True)
        whiskysour.image("CocktailImages/WHISKYSOUR2.jpg")
        whiskysour.write('''Metoda: Dry Shake + shake<br>
        :green[Szkło]: Old fashioned<br>
        :blue[Lód]: Kości<br>
        :violet[Garnish]: Zest z pomarańczy''', unsafe_allow_html=True)

        whitelady = st.expander("White Lady")
        whitelady.write('''40ml Beefeater<br>
        20ml Cointreau<br>
        20ml Sok z cytryny<br>
        10ml Syrop cukrowy<br>
        15ml Białko<br>''', unsafe_allow_html=True)
        whitelady.image("CocktailImages/WHITELADY.jpg")
        whitelady.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z cytryny''', unsafe_allow_html=True)

        whiterussian = st.expander("White Russian")
        whiterussian.write('''40ml Ostoya<br>
        20ml :red[Kahlua]/Bols Coffee<br>
        Top 20ml half&half<br>''', unsafe_allow_html=True)
        whiterussian.image("CocktailImages/WHITERUSSIAN.jpg")
        whiterussian.write('''Metoda: Build; na top delikatnie half&half, by 
        ładnie spływało po kościach<br>
        :green[Szkło]: Old fashioned<br>
        :blue[Lód]: Kości<br>
        :violet[Garnish]: Brak''', unsafe_allow_html=True)

        xxcentury = st.expander("XX Century Cocktail")
        xxcentury.write('''40ml :red[Magellan Gin]<br>
        20ml Lillet Blanc<br>
        15ml Creme de Cacao<br>
        20ml Sok z cytryny<br>''', unsafe_allow_html=True)
        xxcentury.image("CocktailImages/XXCENTURYCOCKTAIL.jpg")
        xxcentury.write('''Metoda: Shake<br>
        :green[Szkło]: Coupe glass<br>
        :violet[Garnish]: Zest z pomarańczy''', unsafe_allow_html=True)

        zombie = st.expander("Zombie")
        zombie.write('''40 ml Havana Especial<br>
        40 ml Havana 7YO<br>
        20ml :red[Rum overproof]/ Havana 3<br>
        25 ml Soku z limonki<br>
        15 ml Falernum<br>
        5-7 ml :red[Grenadyna]<br>
        15 ml :red[Don's Mix (sok grejpfrutowy i syrop cynamonowy w stosunku 1:2)]<br>
        5-7 ml :red[Likier anyżowy]/Absynt<br>
        2 dash Angostura<br>''', unsafe_allow_html=True)
        zombie.image("CocktailImages/ZOMBIE.png")
        zombie.write('''Metoda: Shake<br>
        :green[Szkło]: Copa<br>
        :violet[Garnish]: Tiki (na bogato)''', unsafe_allow_html=True)

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

        amaretto = st.expander("**Amaretto** _(Likier, Migdały, Włochy)_")
        amaretto.write('''Ciemnobrązowy włoski likier o gorzkim smaku i zapachu migdałów.
        Kompozycja zawiera winogrona, migdały orzechy (lub nasion moreli), wanilia, przyprawy i zioła.
        Tradycyjny obszar produkcji - miasto Saronno, położony w prowincji Lombardii. Nazwa
        „Amaretto” pochodzi od włoskiego słowa „Amaro”, co tłumaczy się jako „lekko gorzki”.''')
        amaretto.image('AlcoholImages/amaretto.jpg')

        averna = st.expander("**Amaro Averna** _(Likier, Amaro, Włochy)_")
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

        lucano = st.expander("**Amaro Lucano** _(Likier, Amaro, Włochy)_")
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

        dram = st.expander("**Drambuie** _(Likier, Szkocja)_")
        dram.caption('''Nazwa Drambuie pochodzi od szkocko gaelickiego zwrotu _"an dram buidheach"_, oznaczającego napój, 
        który zadowala i została zastrzeżona w 1892''')
        dram.write('''Jego bazę stanowi single malt whisky (15-17 letnia), miód i zioła ze szkockich wrzosowisk. Smak i
        zapach whisky słodowej i miodu w połączeniu z aromatem ziół.''')
        dram.image('AlcoholImages/drambuie.jpg')

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
