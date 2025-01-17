# Define the function f(n1,n2,n3), which returns True if at least one of the numbers n1,n2,n3 is negative or False otherwise.
# Sample result:

# f(11,6,-4) returns True
# f(5,4,14) returns False

# Funkcja zwracająca True, jeśli co najmniej jedna z liczb n1, n2, n3 jest ujemna, w przeciwnym razie zwraca False
def f(n1, n2, n3):
    # Sprawdzamy, czy którakolwiek z liczb jest ujemna
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True  # Zwracamy True, jeśli warunek jest spełniony
    else:
        return False  # Zwracamy False, jeśli żadna liczba nie jest ujemna

# Testowanie funkcji
print(f(11, 6, -4))  # Powinno zwrócić True (liczba -4 jest ujemna)
print(f(5, 4, 14))   # Powinno zwrócić False (wszystkie liczby są dodatnie)
print(f(124,-5432,123))