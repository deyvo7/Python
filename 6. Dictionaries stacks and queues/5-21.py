import json

# Tworzymy słownik z danymi na temat ulubionego filmu
favorite = {
   "title": "The Matrix",  # Tytuł filmu
   "director": "Wachowski Brothers",  # Reżyserzy filmu
   "release_year": 1999,  # Rok wydania
   "genre": "Science Fiction",  # Gatunek filmu
   "rating": 8.7  # Ocena filmu
}

# Określamy nazwę pliku, do którego zapiszemy dane
file_name = "favourite.json"

# Otwieramy plik w trybie zapisu i używamy json.dump() do zapisania danych w pliku
with open(file_name, 'w') as file:
   json.dump(favorite, file, indent=4)  # Zapisujemy dane w pliku z wcięciem dla czytelności

print("Dane zostały zapisane do pliku", file_name)  # Informacja o zapisaniu danych
