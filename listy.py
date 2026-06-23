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

macierz = [[1,2,3],[4,5,6],[7,8,9]]
macierz[0].append(4)
print(macierz)
print(macierz[2][2])
macierz[2][2]=50
print(macierz[2][2])
print(macierz)