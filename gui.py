from tkinter import simpledialog

cena = simpledialog.askfloat("Cena Pojazdu","Podaj cenę pojazdu w PLN:                    ",minvalue = 1000, maxvalue = 100000, initialvalue = 50000)

marka = simpledialog.askstring("Marka Pojazdu","Podaj markę pojazdu                    ")
marka = marka.strip().title()

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