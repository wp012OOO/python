dict = {
    "brand": "Ford",
    "model": "Mondeo",
    "year": 2018
}

print(dict)

x = dict["model"]
#x = dict["model_auta"]
print(x)

#y = dict.get["model"]
#y = dict.get["model_auta" , "brak_danych"]
#print(y)

dict["kolor"] = "czarny"

print(dict)

y = dict.keys()
print(y)