# An array contains a list of Polish names:

# Genowefa, Onufry, Celestyna, Alojzy, Pankracy
# Create a program that prints the longest name (consisting of the largest number of characters). Sample result:

# Names: Genowefa Onufry Celestyna Alojzy Pankracy
# Longest name: Celestyna


# Lista imion
names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

# Zmienna do przechowywania najdłuższego imienia
longest_name = ""

# Pętla, która przechodzi przez każde imię w tablicy
for name in names:
    # Jeśli aktualne imię jest dłuższe niż obecnie zapisane najdłuższe, to je zamieniamy
    if len(name) > len(longest_name):
        longest_name = name

# Wypisujemy wszystkie imiona oraz najdłuższe imię
print("Names:", " ".join(names))  # Wypisujemy wszystkie imiona oddzielone spacjami
print("Longest name:", longest_name)  # Wypisujemy najdłuższe imię
