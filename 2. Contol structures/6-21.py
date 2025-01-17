# There are coins of 1, 2 and 5 Polish Zlotys (PLN).
# Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

# Enter the amount in PLN: 18
# The amount of PLN 18 in coins:
# 5 PLN coins: 3
# 2 PLN coins: 1
# 1 PLN coins: 1

# Program do przedstawienia dowolnej kwoty w PLN z minimalną liczbą monet

amount = int(input("Enter the amount in PLN: "))  # Pobranie kwoty od użytkownika

# Liczenie monet 5 PLN
five_pln = amount // 5
amount = amount % 5  # Pozostająca kwota po wykorzystaniu monet 5 PLN

# Liczenie monet 2 PLN
two_pln = amount // 2
amount = amount % 2  # Pozostająca kwota po wykorzystaniu monet 2 PLN

# Liczenie monet 1 PLN
one_pln = amount // 1  # Pozostaje już tylko moneta 1 PLN

# Wyświetlenie wyniku
print(f"The amount of PLN {five_pln * 5 + two_pln * 2 + one_pln} in coins:")  # Pokazuje oryginalną kwotę
print(f"5 PLN coins: {five_pln}")  # Liczba monet 5 PLN
print(f"2 PLN coins: {two_pln}")   # Liczba monet 2 PLN
print(f"1 PLN coins: {one_pln}")   # Liczba monet 1 PLN
