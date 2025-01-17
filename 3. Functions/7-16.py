# Define the function f(n), which returns the n-th value of the Fibonacci sequence.
# The sequence is defined as follows: the first value of the sequence is 0, the second value is 1.
# Each subsequent value is the sum of the previous two. Sample result:

# f(5) returns 3
# f(9) returns 21

def f(n):
    # Sprawdzenie przypadków dla n = 1 i n = 2
    if n == 1:
        return 0
    elif n == 2:
        return 1

    # Inicjalizacja pierwszych dwóch wyrazów ciągu
    a = 0  # Pierwszy wyraz
    b = 1  # Drugi wyraz

    # Obliczanie n-tego wyrazu ciągu Fibonacciego
    for _ in range(3, n + 1):
        c = a + b  # Obliczamy kolejny wyraz
        a = b      # Przesuwamy a do wartości b (staje się drugim wyrazem)
        b = c      # Przesuwamy b do nowego wyrazu (staje się trzecim wyrazem)

    return b  # Zwracamy n-ty wyraz ciągu

# Przykładowe testy
print(f(5))  # Powinno zwrócić 3
print(f(9))  # Powinno zwrócić 21
