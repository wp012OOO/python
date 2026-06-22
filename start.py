#komunikacja - pol. print
"""
kom
wielolinijkowy
"""

print("Czesc" , "Rafal")
print("Czesc" + "Rafal")
print("*" * 40)

#zmienne
imię = "Rafał"
print("Cześć" , imię)

X = None #Brak wartości

#Słowa zastrzeżone
import keyword
print( keyword.kwlist )

#definiowanie wielu zmiennych na raz
x,y,z = 2, "Ala", 5.9
print(x,y,z)

#typy zmiennych
a=5 #int
b = 5.99 #float
c = False #bool

q = a + b * 4
print(q)

#typy zmiennych
a=5 #int
b = "5.99" #float
c = False #bool

q = a + float(b) * 4
print(q)

#śmieci numeryczne
a1=16.48
a2=16.71
a3=(a1-a2)
print(f"{a3:.2f}")
a3=round(a3,2)
print(a3)

print("jestem" , f"imie {imię}" , f"wartosc {q}" , sep=".")
print("jestem")
print(f"imie {imię}" , end =".")
print(f"wartosc {q}")

a3 *=5
print(a3)

print(type(a3))

print("Lista zakupów:\n\t* Chleb\n\t* Mleko")

liczba = 123123123123123.5656565656
print(liczba)
print(f"Wynik: {liczba:_}")
print(f"Wynik: {liczba:,}")

t1 = "Ala ma kota"
t2 = t1.replace("Ala", "Zuzia")
print(t2)

liczbapl = f"{liczba:_.2f}".replace(","   ,   "").replace("."  ,  ",")
print(liczbapl)