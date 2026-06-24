from prettytable import PrettyTable as pt, SINGLE_BORDER

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
        skad = lista_rekord[7]

        if skad not in pojazdy:
            pojazdy[skad]={}

        if marka not in pojazdy[skad]:
            pojazdy[skad][marka] = {"suma_cen": 0, "śr_przebieg":0, "ile":0}

        pojazdy[skad][marka]["ile"] += 1
        pojazdy[skad][marka]["suma_cen"] += int(lista_rekord[2])
        pojazdy[skad][marka]["śr_przebieg"] += int(lista_rekord[8])

#koniec petli

for skad,marka in pojazdy.items():
    #dodanie wierszy
    for m in pojazdy[skad].keys():
        pojazdy[skad][m]["śr_przebieg"] = round(pojazdy[skad][m]["śr_przebieg"] / pojazdy[skad][m]["ile"], 2)
        tbl.add_row( [m, pojazdy[skad][m]["ile"],
                         pojazdy[skad][m]["suma_cen"],
                         pojazdy[skad][m]["śr_przebieg"]] )
    #print(tbl)
#export na zewnątrz
    nazwa_pliku = 'dane_' + skad + '.csv'
    with open(nazwa_pliku,"w",encoding='utf8', newline="") as plik:
        plik.write( tbl.get_csv_string(delimiter=";"))
