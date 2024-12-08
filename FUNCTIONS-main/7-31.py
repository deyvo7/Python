# Define a function power(x, n) that calculates xn. Apply recursion. Then, calculate 53.

def power(x, n):
    """
    Funkcja oblicza x^n za pomocą rekurencji.
    """
    # Przypadek bazowy: każda liczba do potęgi 0 wynosi 1
    if n == 0:
        return 1

    # Przypadek rekurencyjny: x * x^(n-1)
    return x * power(x, n - 1)

# Program główny: obliczenie 5^3
x = 5
n = 3
wynik = power(x, n)
print(f"{x} do potęgi {n} wynosi: {wynik}")
