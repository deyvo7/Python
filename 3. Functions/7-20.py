# Define the function f(n) that returns the n-th prime number.
# A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:

# f(1) returns 2
# f(5) returns 11

def is_prime(number):
    # Funkcja pomocnicza sprawdzająca, czy liczba jest liczbą pierwszą
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def f(n):
    # Funkcja zwracająca n-tą liczbę pierwszą
    count = 0  # Licznik znalezionych liczb pierwszych
    num = 1  # Rozpoczynamy od liczby 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

# Testowanie funkcji
print(f(1))  # Zwraca 2
print(f(5))  # Zwraca 11
