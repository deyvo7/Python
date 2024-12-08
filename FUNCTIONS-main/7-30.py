# Define a function sum_natural(n) that for the given natural number n calculates the sum of all natural numbers
# between 1 and n. Apply recursion. Then, create a program that calculates the sum of natural numbers in the range <1,10>.

def sum_natural(n):
    """
    Funkcja oblicza sumę liczb naturalnych od 1 do n za pomocą rekurencji.
    """
    # Przypadek bazowy: jeśli n to 1, zwróć 1
    if n == 1:
        return 1

    # Przypadek rekurencyjny: n + suma liczb od 1 do n-1
    return n + sum_natural(n - 1)

# Program główny: obliczenie sumy liczb w zakresie <1,10>
n = 10
wynik = sum_natural(n)
print(f"Suma liczb naturalnych w zakresie <1, {n}> wynosi: {wynik}")
