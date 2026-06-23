from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# --- PALETA KOLORÓW DARK MODE ---
BG_DARK = "#1E1E1E"          # Główne tło (antracyt)
BG_FIELD = "#2D2D2D"         # Tło pól Entry i Combobox
FG_LIGHT = "#E0E0E0"         # Jasny tekst
ACCENT_COLOR = "#3A3A3A"     # Kolor przycisków i ramek
HIGHLIGHT = "#0078D4"        # Niebieski akcent (np. przycisk OK)

def callback_ok():
    nazwa_str = nazwa.get().strip()
    cena_str = cena.get().strip()
    if not nazwa_str or not cena_str:
        messagebox.showwarning("Błąd", "Wypełnij dane!")
        return
    print(f"Zapisano: {nazwa_str}, Cena: {cena_str}")

master = Tk()
master.title("Pojazdy - Dark Mode")
master.configure(bg=BG_DARK)
master.geometry("450x400")

# --- KONFIGURACJA STYLI TTK (DARK) ---
style = ttk.Style()
style.theme_use('clam')

# Styl dla etykiet
style.configure("TLabel", background=BG_DARK, foreground=FG_LIGHT, font=("Segoe UI", 10))

# Styl dla pól tekstowych
style.configure("TEntry", fieldbackground=BG_FIELD, foreground=FG_LIGHT, bordercolor=ACCENT_COLOR, lightcolor=ACCENT_COLOR)

# Styl dla listy rozwijanej (Combobox)
style.configure("TCombobox", fieldbackground=BG_FIELD, foreground=FG_LIGHT, background=ACCENT_COLOR, arrowcolor=FG_LIGHT)

# Styl dla przycisków (ciemne)
style.configure("TButton", background=ACCENT_COLOR, foreground=FG_LIGHT, borderwidth=0, focuscolor=HIGHLIGHT)
style.map("TButton", background=[('active', '#4A4A4A')]) # Kolor po najechaniu

# Styl dla Radio i Checkbutton
style.configure("TRadiobutton", background=BG_DARK, foreground=FG_LIGHT, indicatorcolor=BG_FIELD)
style.map("TRadiobutton", indicatorcolor=[('selected', HIGHLIGHT)])
style.configure("TCheckbutton", background=BG_DARK, foreground=FG_LIGHT, indicatorcolor=BG_FIELD)
style.map("TCheckbutton", indicatorcolor=[('selected', HIGHLIGHT)])

# --- UKŁAD ELEMENTÓW ---
M_X, M_Y = 20, 10
SZEROKOSC = 25

# Wiersze (analogicznie do poprzedniego kodu)
ttk.Label(master, text="Nazwa pojazdu:").grid(row=0, column=0, sticky="e", padx=M_X, pady=(30, M_Y))
nazwa = ttk.Entry(master, width=SZEROKOSC)
nazwa.grid(row=0, column=1, pady=(30, M_Y), sticky="w")

ttk.Label(master, text="Cena (PLN):").grid(row=1, column=0, sticky="e", padx=M_X, pady=M_Y)
cena = ttk.Entry(master, width=SZEROKOSC)
cena.grid(row=1, column=1, pady=M_Y, sticky="w")

ttk.Label(master, text="Kolor:").grid(row=2, column=0, sticky="e", padx=M_X, pady=M_Y)
wybrany_kolor = StringVar(value="Czarny")
dropdown = ttk.Combobox(master, textvariable=wybrany_kolor, values=["Czerwony", "Czarny", "Biały"], width=SZEROKOSC-2, state="readonly")
dropdown.grid(row=2, column=1, sticky="w", pady=M_Y)

# Stan
stan_pojazdu = IntVar(value=1)
ttk.Label(master, text="Stan:").grid(row=3, column=0, sticky="e", padx=M_X, pady=M_Y)
f_radio = Frame(master, bg=BG_DARK)
f_radio.grid(row=3, column=1, sticky="w")
ttk.Radiobutton(f_radio, text="Nowy", variable=stan_pojazdu, value=1).pack(side=LEFT, padx=5)
ttk.Radiobutton(f_radio, text="Używany", variable=stan_pojazdu, value=2).pack(side=LEFT, padx=5)

# Dodatki
klima_var = IntVar()
ttk.Label(master, text="Wyposażenie:").grid(row=4, column=0, sticky="e", padx=M_X, pady=M_Y)
ttk.Checkbutton(master, text="Klimatyzacja", variable=klima_var).grid(row=4, column=1, sticky="w")

# Przyciski
btn_container = Frame(master, bg=BG_DARK)
btn_container.grid(row=5, column=0, columnspan=2, pady=30)

btn_ok = ttk.Button(btn_container, text="ZAPISZ", width=15, command=callback_ok)
btn_ok.pack(side=LEFT, padx=10)

btn_cancel = ttk.Button(btn_container, text="ZAMKNIJ", width=15, command=master.destroy)
btn_cancel.pack(side=LEFT, padx=10)

master.mainloop()