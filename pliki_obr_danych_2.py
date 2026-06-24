from prettytable import PrettyTable as pt, SINGLE_BORDER
import os

#pomocnicze zmienne
pojazdy = {}
tbl = pt()
tbl.set_style(SINGLE_BORDER)
tbl.field_names = (["Marka","Ile","Suma Cen","Średni Przebieg"])

#odczyt
with open("dane.csv",encoding="utf8") as plik:

    #odczyt danych wiersz po wierszu, najpierw nagłówki i przesunięcie na kolejny wiersz
    naglowki = plik.readline()

    for wiersz in plik:
        lista_rekord = wiersz.strip().split(";")
        marka = lista_rekord[1]

        if marka not in pojazdy:
            pojazdy[marka] = {"suma_cen": 0, "śr_przebieg":0, "ile":0}

        pojazdy[marka]["ile"] += 1
        pojazdy[marka]["suma_cen"] += int(lista_rekord[2])
        pojazdy[marka]["śr_przebieg"] += int(lista_rekord[8])

    #dodanie wierszy
    for m in pojazdy.keys():
        pojazdy[m]["śr_przebieg"] = round(pojazdy[m]["śr_przebieg"] / pojazdy [m]["ile"], 2)
        tbl.add_row( [m, pojazdy[m]["ile"],
                         pojazdy[m]["suma_cen"],
                         pojazdy[m]["śr_przebieg"]] )

    print(tbl)

#export na zewnątrz
if not os.path.exists(Folder_wynikowy):
     os.makedirs(Folder_wynikowy)

with open("Folder_wynikowy\dane_po_obrobce2.csv","w",encoding='utf8') as plik:
    for m in pojazdy.keys():
        plik.write( "pojazd: " + m + " ile: " + str(pojazdy[m]) + "\n")
