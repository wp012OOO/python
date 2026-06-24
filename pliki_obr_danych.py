from prettytable import PrettyTable as pt, SINGLE_BORDER

#pomocnicze zmienne
pojazdy = {}
tbl = pt()
tbl.set_style(SINGLE_BORDER)
tbl.field_names = (["Mrka","Ile"])

#odczyt
with open("dane.csv",encoding="utf8") as plik:

    #odczyt danych wiersz po wierszu, najpierw nagłówki i przesunięcie na kolejny wiersz
    naglowki = plik.readline()

    for wiersz in plik:
        lista_rekord = wiersz.strip().split(";")
        marka = lista_rekord[1]

        if marka not in pojazdy:
            pojazdy[marka] = 0
        pojazdy[marka] += 1

    #dodanie wierszy
    for m in pojazdy.keys():
        tbl.add_row( [m, pojazdy[m] ] )

    print(tbl)

#export na zewnątrz
with open("dane_po_obrobce.csv","w",encoding='utf8') as plik:
    for m in pojazdy.keys():
        plik.write( "pojazd: " + m + " ile: " + str(pojazdy[m]) + "\n")
    plik.write("--------------dane z PrettyTable jako CSV")
    plik.write(str(tbl))
