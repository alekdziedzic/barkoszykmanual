import streamlit as st
from PIL import Image
import pandas as pd
st.title("Wino")
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
\n \n
Nos to czerwone owoce, także jeżyny, akcenty czekolady i wanilii.\n \n
:blue[Sugestie kulinarne]: łagodne sosy, pieczenie, kaczki, dania z grilla.''')

monte = st.expander("Gran Sasso Montepulciano D’Abruzzo")
monte.write('''
Winnice zlokalizowane w Crecchio, San Salvo oraz Pollutri. 
Odszypułkowanie i delikatne prasowanie gron. Maceracja przez 15 dni w 
kadziach ze stalli nierdzewnej. Fermentacja i dojrzewanie w 
beczkach z francuskiego dębu przez dwa do trzech miesięcy.
\n \n
Dobrze zbudowane wino o mocnych aromatach owocowych 
( jeżyny, śliwki, porzeczki i wiśnie), z lekkim akcentem ziołowym. 
W ustach soczyste, zmysłowe, o miękkich garbnikach i stonowanej kwasowości.\n \n
:blue[Sugestie kulinarne]: wędliny, mięsa z grilla, dojrzewające sery. 
''')

malbec = st.expander("Elsa Bianchi Malbec San Rafael Mendoza")
malbec.write('''
Klasyczny Malbec z aromatami dojrzałych śliwek i fiołków z aluwialnych gleb 
w winnicach Finca Doña Elsa i Finca Asti (750 m n.p.m.), które 
przekazują winu swoje mineralne nuty. Ręczny zbiór, fermentacja w kadziach
ze stali nierdzewnej, dojrzewanie w dębinie.
\n \n
Aromaty dojrzałych śliwek i fiołków, podkreślonych delikatną nutą dębu. 
W ustach zmysłowe, pełne owocu z dobrze ułożonymi taninami, jedwabistą fakturą
i intensywnym owocowym posmakiem. Wszystkie te cechy dają w efekcie eleganckie,
dobrze zbalansowane wino, które może być idealnym partnerem przy stole.\n \n
:blue[Sugestie kulinarne]: Grillowane mięso
''')

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
\n \n
Nos niezwykle owocowy z przewagą wiśni, czereśni i morwy czerwonej. 
Nuty wanilii, cynamonu, szałwii, mięty i tytoniu dopełniają aromatycznej całości.
Krągłe, otulające bardzo lekkimi taninami, eleganckie i pachnące wino, z nutami 
porzeczek, śliwek, czarnego pieprzu i czekolady. \n \n
:blue[Sugestie kulinarne]: wędliny, sery, jagnięcina z grilla i dziczyzna.
''')

st.header("Białe wina")