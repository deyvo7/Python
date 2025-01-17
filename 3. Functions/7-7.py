# The binary numerical system uses two symbols to represent a number: 0 and 1.
# Define a function f(binary_number) that returns True if the given string of digits is a valid binary number, or False otherwise.

# Sample result:
# f("101101") returns True
# f("1311a10100") returns False

# Funkcja sprawdzająca, czy podany ciąg jest poprawną liczbą binarną
def f(binary_number):
    # Sprawdza, czy wszystkie znaki w ciągu są '0' lub '1'
    return all(char in '01' for char in binary_number)

# Testowanie funkcji
print(f("101101"))  # Powinno zwrócić True
print(f("1311a10100"))  # Powinno zwrócić False
