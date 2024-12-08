###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
# Prosty kalkulator
# Program prosi użytkownika o podanie symbolu operacji matematycznej (+, -, *, /)
# oraz dwóch liczb. Program powinien wykonać odpowiednią operację matematyczną
# na podanych liczbach i zwrócić wynik.

# Wczytanie pierwszej liczby od użytkownika
number1 = int(input("Enter first number: "))

# Wczytanie drugiej liczby od użytkownika
number2 = int(input("Enter second number: "))

# Wczytanie symbolu operatora od użytkownika
operator = input("Enter operator: ")

# Sprawdzenie, jaki operator został wybrany i wykonanie odpowiedniej operacji
if operator == '+':
    result = number1 + number2  # Dodawanie
elif operator == '-':
    result = number1 - number2  # Odejmowanie
elif operator == '*':
    result = number1 * number2  # Mnożenie
elif operator == '/':
    if number2 != 0:  # Sprawdzenie, czy dzielenie przez 0 jest możliwe
        result = number1 / number2  # Dzielenie
    else:
        result = 'Error: Division by zero is not allowed'  # Obsługa błędu dzielenia przez 0

# Wypisanie wyniku
print(f'{number1} {operator} {number2} = {result}')
