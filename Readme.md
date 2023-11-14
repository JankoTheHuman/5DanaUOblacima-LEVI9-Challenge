POSTAVKA OKRUŽENJA

- Svi neophondi instalacioni putevi su hyper-linkovani, bitan je redosled instalacija


---

- Neophodna je instalirana verzija [Python 3.11.5](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe), prilikom instalacije Pythona cekirajte "Add Python to PATH"

---

- Development programa se vršio u [IDE PyCharm CommunityEdition 2023.1.3](https://download.jetbrains.com/python/pycharm-community-2023.1.3.exe?_gl=1*5eljow*_ga*MTI2MDMzNzQ5My4xNjk3ODM1MjEx*_ga_9J976DJZ68*MTcwMDAwMDU0OS4yLjEuMTcwMDAwMDYwMS42MC4wLjA.&_ga=2.223207067.1052024537.1700000550-1260337493.1697835211)

----

- Možda je neophodno podešavanje Python interpretera u PyCharmu nakon sto je projekat pullovan sa Git-a. Vratiti se na ovo ukoliko je potrebno. To se radi ovako:

1)Klikni Add New Interpreter u top-side error pop-upu

2)Navigiraj do mesta instalacije Pythona i pritisni OK, virtuelno okruzenje ce se formirati, nakon cega se mogu skinuti biblioteke prateci uputsva dalje

---
BILDOVANJE PROJEKTA

- U terminalu PyCharm-a instalirati pip komandom pa onda pullovati sve biblioteke iz requirements.txt fajla:
- python -m pip install --upgrade pip==23.3.1
- pip install -r requirements.txt

---

POKRETANJE PROJEKTA

- Otvoriti main.py i kombinacijom dugmadi shift+f10 se pokrece program
- Nakon toga u bilo kom brosweru otici na http://127.0.0.1:5000/stats/player/<playerFullName>
- playerFullName input je case i whitespace INsensitive

---

KORIŠĆENE TEHNOLOGIJE

- Flask je lagani web framework za Python. Simplifikuje proces izgradnje web aplikacija.
Klasa Flask se koristi za kreiranje web aplikacije. 
- Pandas je moćna biblioteka za manipulaciju podacima u Python-u.
Koristi se za čitanje i manipulaciju tabelarnim podacima, kao što su CSV fajlovi.
Funkcija pd.read_csv() se koristi za čitanje podataka iz CSV fajla u pandas DataFrame.
- json modul je standardna Python biblioteka za enkodiranje i dekodiranje JSON podataka.
Koristi se za pretvaranje pandas DataFrame-a u JSON formatiran string i zatim ga ponovno učitavanje u upotrebljiv JSON objekat.

---
OPIS RADA APLIKACIJE

- Flask aplikacija se kreira pomoću Flask klase.
Ruta /stats/player/< playerFullName >" je definisana za obradu GET zahteva.
- CSV fajl sa statistikama košarkaša se učitava u pandas DataFrame pomoću pd.read_csv().
- Pandas DataFrame se konvertuje u JSON formatiran string pomoću df.to_json(orient='records').
JSON string se zatim učitava u JSON objekat pomoću json.loads().
- Kod obrađuje uneseno ime igrača i traži odgovarajućeg igrača u učitanim JSON podacima.
Ako se pronađe, izračunava različite statistike vezane za slobodna bacanja, dvopojke, trojke, poene, skokove, blokade, asistencije, ukradene lopte, izgubljene lopte i druge napredne statistike.
- Izračunate statistike se strukturiraju u novi JSON objekat.
Funkcija json.dumps() se koristi za formatiranje JSON-a sa uvlačenjem radi bolje čitljivosti.
Konačan JSON odgovor se vraća sa status kodom 200 i postavljenim tipom sadržaja na 'application/json'.
- Flask razvojni server se pokreće kada se skripta izvršava direktno (name == 'main').
