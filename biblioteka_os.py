import os
print(os.getcwd())

if os.path.exists(dane_Lubelskie.csv):
    os.remove(dane_Lubelskie.csv)
    print("Plik bezpiecznie usunieto.")
else:
    print("Pliku już nie ma.")