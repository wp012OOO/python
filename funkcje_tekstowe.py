zamiana = "Ala ma kota".replace("kota","misia")
duże_znaki = zamiana.upper()
X = zamiana.find("Ala")

print(zamiana)
print(duże_znaki)
print(X)

print(zamiana[2:6])     #zwraca d 2 do 5 znaku (6 excluded)

print("\n*** ZADANIE ***\n")

from datetime import datetime, date, timedelta

tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"

rok     =tekst_CSV[6:11].strip()
dzien =tekst_CSV[3:5].strip()
miesiac   =tekst_CSV[0:2].strip()

imienr    =tekst_CSV[11:].title().strip().find(" ")
imie    =tekst_CSV[11:].title().strip()[0:imienr]

nazwiskot    =tekst_CSV[11:].title().strip()[imienr:].strip()

nazwiskonr    =nazwiskot.find(" ")
nazwisko    =nazwiskot.title().strip()[0:nazwiskonr]

kwotnr    =tekst_CSV.find(":")
kwot_pln    =tekst_CSV[kwotnr+1:].strip()
kwot_euro  =round(float(kwot_pln)/4.33,2)

print("Data:",rok, miesiac, dzien)
print(imie, nazwisko)
print("Wypłata:",kwot_euro,"EUR\n")

data1=date(int(rok), int(miesiac), int(dzien))
print(data1)
data2=data1+timedelta(days=270)
print(data2)
