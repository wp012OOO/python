mieszana=["Ania",25,True]
print(mieszana)
print(mieszana[0])
print(mieszana[-1])
x=len(mieszana)
print(x)

mieszana=[12,25,30]
v=sum(mieszana)
print(v)

tekst_CSV = "03/22/2025 jan KOWalski wypłata PLN: 8359"
EX=tekst_CSV.split()    #Argumentem domyślnym jest spacja
print(EX)

EX.append([10000, 15000])
print(EX)
EX.extend([10000, 15000])
print(EX)