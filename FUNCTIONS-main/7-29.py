# The following function calculates the factorial recursively. Try to analyse the function. Do you understand how it works?
# Then, write a program and use the function to calculate the factorial value for n = 5.



def factorial(n):
    # Jeśli n to 0 lub 1, zwróć 1 (przypadek bazowy)
    if n == 0 or n == 1:
        return 1

    # Jeśli n > 1, zwróć n pomnożone przez factorial(n - 1)
    if n > 1:
        return n * factorial(n - 1)

# Obliczanie silni dla n = 5
wynik = factorial(5)
print(f"Silnia liczby 5 wynosi: {wynik}")
