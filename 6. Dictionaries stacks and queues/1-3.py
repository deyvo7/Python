# Tworzymy słownik (dictionary), który opisuje nasz telefon komórkowy.
# Słownik przechowuje dane w postaci par klucz-wartość.
# Klucze to np. "OS" czy "RAM", a wartości to np. "Android" czy "6GB".
mobile = {
    "OS": "Android",          # System operacyjny telefonu (np. Android, iOS)
    "RAM": "6GB",             # Ilość pamięci RAM (Random Access Memory) w telefonie
    "Memory": "256GB",        # Pojemność pamięci wewnętrznej telefonu
    "Price": "900zł",         # Cena telefonu w złotówkach
    "Brand": "Huawei",        # Marka telefonu
    "Year": "2019"            # Rok produkcji telefonu
}

# Pętla for pozwala nam przejść przez wszystkie pary klucz-wartość w słowniku.
# Używamy metody .items(), która zwraca klucze i wartości jako pary (key, value).
for key, value in mobile.items():
    # Wyświetlamy klucz i odpowiadającą mu wartość w czytelnej formie.
    print(f"{key} : {value}")
