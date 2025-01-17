# A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number.
# Write a program that finds N leading prime numbers. Read the value of N from the keyboard.
# Using loop statements check that the number N is divisible only by 1 and by N.

# Prime numbers: 2 3 5 7 11 ...

# Program znajdujący pierwsze N liczb pierwszych

# Wczytanie wartości N
N = int(input("Enter the value of N: "))

count = 0  # Licznik liczb pierwszych
num = 2  # Pierwsza liczba do sprawdzenia

# Pętla, która znajdzie N liczb pierwszych
while count < N:
    is_prime = True  # Założenie, że liczba jest pierwsza
    limit = int(num**0.5) + 1  # Optymalizacja: nie musimy sprawdzać dzielników większych niż pierwiastek z num
    for i in range(2, limit):
        if num % i == 0:  # Sprawdzenie, czy num jest podzielna przez i
            is_prime = False  # Liczba nie jest pierwsza
            break
    if is_prime:  # Jeśli liczba jest pierwsza
        print(num, end=' ')  # Wydrukowanie liczby
        count += 1  # Zwiększenie licznika
    num += 1  # Sprawdzenie następnej liczby
