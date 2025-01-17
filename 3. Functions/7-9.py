# Create a function f(number, even) that computes the sum of the digits of a number.
# When the value of the even parameter is True, the function returns the sum of the even digits.
# When the value of the even parameter is False, the function returns the sum of the odd digits. Sample result:

# f(3124,True) returns 6
# f(3124,False) returns 4
# f(20576,False) returns 12
# f(20576,True) returns 8
# f(13115,True) returns 0

# Funkcja obliczająca sumę cyfr liczby na podstawie parametru even
def f(number, even):
    # Inicjalizacja sumy
    digit_sum = 0
    
    # Przechodzimy przez każdą cyfrę liczby
    for digit in str(number):
        digit = int(digit)  # Konwersja znaku na liczbę całkowitą
        
        # Sprawdzanie warunku dla cyfr parzystych lub nieparzystych
        if even and digit % 2 == 0:  # Jeśli even jest True i cyfra jest parzysta
            digit_sum += digit
        elif not even and digit % 2 != 0:  # Jeśli even jest False i cyfra jest nieparzysta
            digit_sum += digit
    
    return digit_sum  # Zwracamy sumę cyfr

# Testowanie funkcji
print(f(3124, True))  # Powinno zwrócić 6 (2+4)
print(f(3124, False))  # Powinno zwrócić 4 (3+1)
print(f(20576, False))  # Powinno zwrócić 12 (5+7+1)
print(f(20576, True))  # Powinno zwrócić 8 (2+6)
print(f(13115, True))  # Powinno zwrócić 0 (brak cyfr parzystych)
