#imie = input("Podaj swoje imie")
#print("Witaj, " + imie + ".")

cena = input("Podaj cenę pojazdu: ")
cena = float(cena)
marka = input("Podaj markę pojazdu: ")
marka = marka.strip().title()

# dodać warunki w jednej pętli! marka == "" exit() + komunikat

if marka == "":
     print("Nie podano marki pojazdu!")
     exit()
else:
    if marka == "Opel":
        rabat = 0.15
    elif marka == "Skoda":
        rabat = 0.18
    elif marka == "Audi":
        rabat = 0.2
    else:
        rabat = 0

    #print(cena)
    #print(marka)
    x = cena * (1-rabat)
    print("Cena po rabacie:" , x , "PLN")
