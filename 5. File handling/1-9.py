# The file it_company.csv contains a list of employees.
# Write a program that displays only employees with the position "Software Engineer".
# Number the items on the printed list.

# Hint: You can check if a string is contained within another string using the 'in' operator.

# Nazwa pliku, który zawiera dane o pracownikach
file_name = 'it_company.csv'

# Tytuł stanowiska, który chcemy znaleźć
job_title = 'Software Engineer'

# Otwieramy plik w trybie do odczytu
with open(file_name, "r") as file:
   # Odczytujemy zawartość pliku
   content = file.read()

   # Dzielimy zawartość pliku na linie
   file_lines = content.splitlines()

   # Zmienna 'number' będzie numerować pracowników
   number = 1
  
   # Iterujemy po każdej linii w pliku
   for line in file_lines:
      # Sprawdzamy, czy tytuł stanowiska "Software Engineer" jest w danej linii
      if job_title in line:
        # Jeśli tak, drukujemy numer i linię (informacje o pracowniku)
        print(f"{number}. {line}")
        # Zwiększamy numer o 1 dla kolejnego pracownika
        number += 1
