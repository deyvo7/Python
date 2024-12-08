# The sequence of digits contains the number of points rolled with a dice.
# Define a function f(dice) that returns a number
# specifying the number of dice rolled the most times in a row.

# Sample result:
# f("5233165554211") returns 5
# f("2133") returns 3

def f(dice):
    # Inicjalizujemy zmienne do śledzenia aktualnej i najwyższej sekwencji
    current_streak = 1
    highest_streak = 1
    number_with_highest_streak = dice[0]  # Ustawiamy pierwszą cyfrę jako domyślną

    # Pętla iterująca od drugiego znaku do końca ciągu
    for i in range(1, len(dice)):
        if dice[i] == dice[i - 1]:
            # Zwiększamy aktualną sekwencję, jeśli obecny znak jest taki sam jak poprzedni
            current_streak += 1
        else:
            # Jeśli sekwencja się kończy, sprawdzamy, czy jest najwyższa
            if current_streak > highest_streak:
                highest_streak = current_streak
                number_with_highest_streak = dice[i - 1]
            # Resetujemy aktualną sekwencję
            current_streak = 1

    # Sprawdzamy, czy ostatnia sekwencja była najwyższa
    if current_streak > highest_streak:
        highest_streak = current_streak
        number_with_highest_streak = dice[-1]

    return int(number_with_highest_streak)

# Przykłady testowe
print(f("5233165554211"))  # Powinno zwrócić 5
print(f("2133"))           # Powinno zwrócić 3
