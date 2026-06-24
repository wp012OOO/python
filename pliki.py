#otwarcie pliku
plik = open (r"C:\Users\Szkolenie_03\Desktop\WP01\dane_tekstowe.txt" , "rt" , encoding = "utf8")   #r pozwala czytać /\

#odczyt całości
zawartosc = plik.read()
print(zawartosc)

#restart kursora na pczątek pliku
plik.seek(0)

i = 0
for wiersz in plik:
    i += 1
    print("WIERSZ",i, "=", wiersz.strip())

#zamykanie plików
plik.close()





#Varia
#alternatywa niewymagająca zamykania
with open (r"C:\Users\Szkolenie_03\Desktop\WP01\dane_tekstowe.txt" , "rt" , encoding = "utf8") as plik:
    zawartosc = plik.read()
    #print(zawartosc)
