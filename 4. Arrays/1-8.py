# Write a program that prints popular computer games,
# each game name on a separate line. Use the while statement.
# Additionally, number the list (print the next number before each list item)
# and sort the list alphabetically
# (use one of a Python built-in functions for sorting)

# Lista popularnych gier komputerowych
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# Sortujemy listę alfabetycznie
computer_games_sorted = sorted(computer_games)

# Inicjujemy indeks do iteracji i numerowanie listy
index = 0  # Początkowy indeks
number = 1  # Numeracja zaczyna się od 1

# Pętla while, aby przejść przez posortowaną listę
while index < len(computer_games_sorted):
    # Wypisujemy numer i nazwę gry
    print(f"{number}. {computer_games_sorted[index]}")
    index += 1  # Zwiększamy indeks
    number += 1  # Zwiększamy numer
