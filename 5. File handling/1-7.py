# The file car_park.txt contains data on the number of parked cars for
# the last five days. Complete the following program to calculate
# the total number of parked cars.

# Funkcja odczytuje całą zawartość pliku
def read_from_file(name):
   # Otwieramy plik w trybie odczytu ('r')
   with open(name) as file:
      # Odczytujemy całą zawartość pliku
      content = file.read()
   # Zwracamy odczytaną zawartość pliku
   return content

# Odczytujemy całą zawartość pliku 'car_park.txt'
file_content = read_from_file('car_park.txt')

# Rozdzielamy zawartość pliku na linie i zapisujemy je w liście 'file_lines'
file_lines = file_content.splitlines()

# Inicjalizujemy zmienną 'total', która będzie przechowywać sumę zaparkowanych samochodów
total = 0

# Iterujemy przez każdą linię w pliku, każda linia zawiera liczbę zaparkowanych samochodów
for line in file_lines:
   # Przekształcamy wartość w linii na liczbę całkowitą i dodajemy ją do 'total'
   total += int(line)

# Po zakończeniu pętli, wypisujemy całkowitą liczbę zaparkowanych samochodów
print('Total cars parked:', total)
