# Słownik zawierający przedmioty oraz liczbę godzin w semestrze zimowym
winter_semester = {
   "math": 60,
   "programming": 30,
   "history": 15
}

# Obliczamy łączną liczbę godzin, sumując wartości w słowniku
total_hours = sum(winter_semester.values())

# Wyświetlamy wynik
print(f"The total number of hours in the winter semester is {total_hours}")
