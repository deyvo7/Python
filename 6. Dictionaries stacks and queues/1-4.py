# Tworzymy słownik (dictionary) opisujący osobę.
# Wartości w parach klucz-wartość mogą mieć różne typy, np. string (tekst), liczby całkowite, listy, czy nawet inne słowniki.
person = {
    "name": "Marek",                       # Tekst (string) - imię osoby
    "surname": "Banach",                   # Tekst (string) - nazwisko osoby
    "age": 25,                             # Liczba całkowita (integer) - wiek osoby
    "hobby": ["swimming", "excursions"],   # Lista (list) - lista hobby osoby
    "married": True,                       # Wartość logiczna (boolean) - czy osoba jest w związku małżeńskim
    "phone": {                             # Słownik (dictionary) - różne numery telefonów
        "landline": "123444321",           # Tekst (string) - numer stacjonarny
        "mobile": "777888999"              # Tekst (string) - numer komórkowy
    }
}

# 1. Wyświetlamy imię osoby.
print(f"Name: {person['name']}")  # Używamy klucza 'name', aby pobrać wartość.

# 2. Wyświetlamy hobby osoby.
print(f"Hobby: {person['hobby']}")  # Klucz 'hobby' przechowuje listę.

# 3. Wyświetlamy cały słownik.
print(f"Dictionary: {person}")  # Drukujemy pełny słownik z całą jego zawartością.

# 4. Zmieniamy nazwisko na "Nowak".
person['surname'] = "Nowak"  # Aktualizujemy wartość klucza 'surname'.
print(person['surname'])  # Wyświetlamy nowe nazwisko.

# 5. Zmieniamy status małżeństwa na False (osoba nie jest już w związku małżeńskim).
person['married'] = False  # Aktualizujemy wartość klucza 'married'.
print(person['married'])  # Wyświetlamy nowy status małżeństwa.

# 6. Dodajemy płeć osoby jako nowy klucz "gender" z wartością 'male'.
person['gender'] = 'male'  # Dodajemy nowy klucz i przypisujemy wartość.
print(person['gender'])  # Wyświetlamy nową wartość.

# 7. Dodajemy nowe hobby "bicycle" do istniejącej listy hobby.
person["hobby"].append("bicycle")  # Używamy metody .append(), aby dodać element do listy.

# 8. Dodajemy numer telefonu służbowego do istniejącego słownika telefonów.
person["phone"]["work"] = "313131444"  # Dodajemy nowy klucz 'work' w zagnieżdżonym słowniku 'phone'.

# 9. Wyświetlamy cały słownik, iterując przez jego elementy (klucz-wartość).
for key, value in person.items():
    print(f"{key} : {value}")  # Wyświetlamy każdy klucz i odpowiadającą mu wartość.
