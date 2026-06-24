from tkinter import messagebox as mb
#from preetytable import PreetyTable as pt,SINGLE_BOARD
from kursy_1 import firmy, Kurs_akcji_wczoraj, Kurs_akcji_dzis

# firmy = ["Firma 1","Firma 2","Firma 3","Firma 4","Firma 5","Firma 6","Firma 7","Firmy 8"]
# Kurs_akcji_wczoraj = [16.48, 25.24, 57.23, 37.92, 99.59, 94.39, 91.56, 127.81]  
# Kurs_akcji_dzis    = [16.71, 25.64 ,57.11, 38.16, 99.14, 94.52, 91.11, 128.99]

liczba_firm=len(firmy)

#preetytable
#table_pt = pt()
#table_pt.field_names = ["Firmy","Kurs wczoraj","Kurs dzisiaj","Wartość","Informacja"]
#table_pt.set_style(SINGLE_BOARD)

for zmiana in range(liczba_firm):
    x=-Kurs_akcji_wczoraj[zmiana]+Kurs_akcji_dzis[zmiana]
    y=round(x,2)
    if x > 0:
        zm="wzrósł"
    else:
        zm="spadł"
    print(f'Firma: {firmy[zmiana]}, kurs akcji {zm} o {y}')
    #komunikat=f'Firma: {firmy[zmiana]}, kurs akcji {zm} o {y}'
    #komunikat_mb=komunikat+

mb.showinfo("Informacja")

