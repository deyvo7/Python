# Write a program to separate even and odd numbers of a given array of integers. Put all even numbers first, and then odd numbers.

# Sample result:

# arr = [7,9,2,4,5,6]
# ...
# ...
# arr = [2,4,6,7,9,5]

# Funkcja do rozdzielania liczb parzystych i nieparzystych
def separate_even_odd(arr):
    even_numbers = []  # Lista na liczby parzyste
    odd_numbers = []   # Lista na liczby nieparzyste
    
    # Przechodzimy po wszystkich elementach tablicy
    for num in arr:
        if num % 2 == 0:  # Sprawdzamy, czy liczba jest parzysta
            even_numbers.append(num)  # Dodajemy do listy liczb parzystych
        else:
            odd_numbers.append(num)   # Dodajemy do listy liczb nieparzystych
    
    # Łączymy obie listy (parzyste + nieparzyste) i zwracamy wynik
    return even_numbers + odd_numbers

# Program główny
arr = [7, 9, 2, 4, 5, 6]  # Przykładowa tablica

# Rozdzielamy liczby parzyste i nieparzyste
arr = separate_even_odd(arr)

# Wyświetlamy wynik
print("arr =", arr)
