dict = {
    "W1234": {"marka": "ford" , "model": "mondeo"},
    "A5678": {"marka": "toyota" , "model": "corolla"}
}
for rejestracja, dane in dict.items():
    print(f"Auto o numerze {rejestracja}:")
    marka = dane["marka"]
    model = dane["model"]
    print(f"    --> {marka} model {model}")
    