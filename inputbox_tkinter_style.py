from tkinter import *
from tkinter import messagebox
from tkinter import ttk  # Importujemy nowoczesne widżety

def callback_ok():
    nazwa_str = nazwa.get().strip()
    cena_str = cena.get().strip()
    kolor_str = wybrany_kolor.get()
    stan_str = "Nowy" if stan_pojazdu.get() == 1 else "Używany"
    dodatki = "Klimatyzacja" if klima_var.get() == 1 else "brak"

    if not nazwa_str or not cena_str:
        messagebox.showwarning("Błąd", "Wypełnij nazwę i cenę!")
        return

    try:
        cena_float = float(cena_str.replace(",", "."))
        print(f"ZAPISANO: {nazwa_str} | {cena_float} PLN | Kolor: {kolor_str} | Stan: {stan_str} | Dodatki: {dodatki}")
        
        # Czyszczenie
        nazwa.delete(0, END)
        cena.delete(0, END)
        nazwa.focus_set()
    except ValueError:
        messagebox.showerror("Błąd", "Cena musi być liczbą!")

master = Tk()
master.title("Rejestracja Pojazdu")
master.configure(bg="white")
master.geometry("450x400")

# --- KONFIGURACJA STYLU TTK ---
style = ttk.Style()
style.theme_use('clam')  # Nowoczesny silnik graficzny
style.configure("TLabel", background="white", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10, "bold"))
style.configure("TEntry", padding=5)
style.configure("TRadiobutton", background="white", font=("Segoe UI", 10))
style.configure("TCheckbutton", background="white", font=("Segoe UI", 10))

# Ustawienia odstępów
M_X = 20
M_Y = 10
SZEROKOSC = 25

# --- UKŁAD ---
# 1. Nazwa
ttk.Label(master, text="Nazwa pojazdu:").grid(row=0, column=0, sticky="e", padx=M_X, pady=(30, M_Y))
nazwa = ttk.Entry(master, width=SZEROKOSC)
nazwa.grid(row=0, column=1, pady=(30, M_Y), sticky="w")

# 2. Cena
ttk.Label(master, text="Cena (PLN):").grid(row=1, column=0, sticky="e", padx=M_X, pady=M_Y)
cena = ttk.Entry(master, width=SZEROKOSC)
cena.grid(row=1, column=1, pady=M_Y, sticky="w")

# 3. Kolor (Combobox zamiast OptionMenu - wygląda lepiej w ttk)
ttk.Label(master, text="Kolor:").grid(row=2, column=0, sticky="e", padx=M_X, pady=M_Y)
opcje_kolorow = ["Czerwony", "Niebieski", "Czarny", "Srebrny", "Biały"]
wybrany_kolor = StringVar(value=opcje_kolorow[0])
dropdown = ttk.Combobox(master, textvariable=wybrany_kolor, values=opcje_kolorow, width=SZEROKOSC-2, state="readonly")
dropdown.grid(row=2, column=1, sticky="w", pady=M_Y)

# 4. Stan (Radio)
stan_pojazdu = IntVar(value=1)
ttk.Label(master, text="Stan:").grid(row=3, column=0, sticky="e", padx=M_X, pady=M_Y)
f_radio = Frame(master, bg="white")
f_radio.grid(row=3, column=1, sticky="w")
ttk.Radiobutton(f_radio, text="Nowy", variable=stan_pojazdu, value=1).pack(side=LEFT, padx=5)
ttk.Radiobutton(f_radio, text="Używany", variable=stan_pojazdu, value=2).pack(side=LEFT, padx=5)

# 5. Dodatki (Check)
klima_var = IntVar()
ttk.Label(master, text="Wyposażenie:").grid(row=4, column=0, sticky="e", padx=M_X, pady=M_Y)
ttk.Checkbutton(master, text="Klimatyzacja", variable=klima_var).grid(row=4, column=1, sticky="w")

# --- PRZYCISKI ---
btn_container = Frame(master, bg="white")
btn_container.grid(row=5, column=0, columnspan=2, pady=30)

btn_ok = ttk.Button(btn_container, text="ZAPISZ", width=15, command=callback_ok)
btn_ok.pack(side=LEFT, padx=10)

btn_cancel = ttk.Button(btn_container, text="ANULUJ", width=15, command=master.destroy)
btn_cancel.pack(side=LEFT, padx=10)

# Obsługa klawiszy i focus
master.bind('<Return>', lambda e: callback_ok())
nazwa.focus_set()

master.mainloop()