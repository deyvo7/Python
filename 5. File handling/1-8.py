# The file pets.txt contains humorous text about animals.
#  Write a program that prints the text and counts the number of words in the text.

# To calculate the number of words in a line, use the split() method,
# which splits a string into a list where each word is a list item.
# Then read the length of this list. Use the len() function. Finally, sum the number of words in each line.
# https://www.w3schools.com/python/ref_string_split.asp

# Funkcja do odczytywania zawartości pliku
def read_from_file(name):
   # Otwieramy plik w trybie odczytu i odczytujemy całą jego zawartość
   with open(name) as file:
      content = file.read()
   return content

# Zmienna total, która będzie przechowywać liczbę słów w całym pliku
total = 0

# Odczytujemy zawartość pliku "pets.txt"
file_content = read_from_file("pets.txt")

# Rozdzielamy zawartość pliku na poszczególne linie
file_lines = file_content.splitlines()

# Wypisujemy linie w pliku (można to usunąć, jeśli nie potrzebujemy wyświetlania tych danych)
print(file_lines)

# Iterujemy przez każdą linię w pliku
for line in file_lines:
   # Dzielimy linię na słowa, rozdzielając ją na podstawie spacji
   words = line.split()
   # Dodajemy liczbę słów w danej linii do zmiennej total
   total += len(words)

# Wypisujemy całkowitą liczbę słów
print(total, "words")

# Wypisujemy pełną zawartość pliku
print(file_content)
