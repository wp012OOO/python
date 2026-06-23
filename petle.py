cars = ["audi","bmw","opel","skoda"]

#iteracja po liście
for car in cars:
    print ("Pojazd:", car)

#alternatywa
ile_razy=len(cars)
for element in range(ile_razy):
    print(f'pokazuje element: {element} tablicy o wartości: {cars[element]}')

#alternatywa 2
for ile, cars in enumerate(cars, start = 0):
    print("Pojazd nr = ", ile, end= ' ')
    print("to: ", car)
