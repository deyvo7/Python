###
# A simple number guessing game
#
###
# Prosta gra w zgadywanie liczby
###

import random  # Importowanie modułu random do losowego wyboru liczby

# Losowo wybrana liczba, którą gracz ma zgadnąć, z zakresu od 1 do 100
number_to_guess = random.randint(1, 100)  
user_guess = 0  # Zmienna przechowująca zgadywaną liczbę

# Powitanie i instrukcje
print("Guess the number between 1 and 100!")

# Pętla, która trwa dopóki gracz nie zgadnie liczby
while user_guess != number_to_guess:  
    user_guess = int(input("Enter your guess: "))  # Prosi gracza o wpisanie liczby

    # Sprawdzanie, czy zgadywana liczba jest za mała
    if user_guess < number_to_guess:  
        print("Too low! Try again.")
    # Sprawdzanie, czy zgadywana liczba jest za duża
    elif user_guess > number_to_guess:  
        print("Too high! Try again.")
    # Jeśli zgadywana liczba jest poprawna
    else:  
        print("Congratulations! You guessed the correct number.")
