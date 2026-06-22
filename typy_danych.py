from datetime import datetime, date, timedelta
teraz = datetime.now()
print(f"Teraz jest: {teraz}")
print("Teraz jest:",teraz)

przyszłość = teraz + timedelta(days=100)
print(f"Za 100 dni będzie: {przyszłość.date()}")

dzisiaj = datetime.now()

print(f"Rok: {dzisiaj.year}")
print(f"Miesiąc: {dzisiaj.month}")
print(f"Dzień: {dzisiaj.day}")
print(f"Godzina: {dzisiaj.hour}")
print(f"Dzień tygodnia: {dzisiaj.weekday()}")

print("\nŁadna data:\n")
ladna_data = dzisiaj.strftime("%d.%B.%Y")
print(f"Format europejski: {ladna_data}\n")
