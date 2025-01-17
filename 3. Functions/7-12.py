# Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:

# f(4) returns "*/*/*/*"
# f(1) returns "*"

# Funkcja zwracająca ciąg n gwiazdek oddzielonych znakiem "/"
def f(n):
    # Tworzymy listę z n gwiazdkami
    asterisks = ['*'] * n
    # Łączymy elementy listy za pomocą znaku "/"
    return '/'.join(asterisks)

# Testowanie funkcji
print(f(4))  # Powinno zwrócić "*/*/*/*"
print(f(1))  # Powinno zwrócić "*"
