# Define a function that calculates and returns the sum of the digits in a number.
# Then write a program that reads a number from the keyboard and prints the sum of its digits.

# Steps of the algorithm to sum digits in a number:

# Take an integer input from the user. The number can be positive, negative, or zero.
# Handle Negative Numbers: Convert the number to its absolute value using the abs() function.
# This step ensures the algorithm correctly processes negative numbers by ignoring the negative sign.
# Convert to String: Convert the number to a string using str(). This allows iteration over each digit in the number.
# Iterate Over Digits:
# Loop through each character (digit) in the string representation of the number.
# Convert each character back to an integer.
# Sum Digits: Add each integer value to a running total.
# Output the Result: Return the sum of the digits

###
# Calculates the sum of the digits in a number
#
# Definiujemy funkcję, która oblicza i zwraca sumę cyfr w liczbie.
# Funkcja przyjmuje jeden argument - liczbę całkowitą - i zwraca sumę jej cyfr.

def sum_digits(number):
    # Zmienna 'absolute' przechowuje wartość bezwzględną liczby, aby obsłużyć liczby ujemne.
    absolute = abs(number)
    
    # Konwertujemy liczbę na ciąg znaków, aby móc przejść przez każdą cyfrę z osobna.
    string = str(absolute)
    
    # Zmienna 'result' będzie przechowywać sumę cyfr.
    result = 0
    
    # Iterujemy przez każdą cyfrę w ciągu znaków.
    for i in string:
        # Konwertujemy znak z powrotem na liczbę całkowitą.
        integer = int(i)
        
        # Dodajemy wartość cyfry do zmiennej 'result'.
        result += integer
    
    # Zwracamy sumę cyfr.
    return result

# Pobieramy od użytkownika liczbę całkowitą.
any_number = int(input('Enter integer number: '))

# Wywołujemy funkcję i zapisujemy wynik.
result = sum_digits(any_number)

# Wyświetlamy wynik sumowania cyfr liczby.
print(f'The sum of the digits in the number {any_number} is {result}')
