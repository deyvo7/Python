# Tworzymy tablicę zawierającą liczby od 1 do 20
numbers = list(range(1, 21))

# Używamy funkcji map() do obliczenia trzeciej potęgi każdej liczby w tablicy
# Funkcja lambda podnosi każdą liczbę do trzeciej potęgi (x**3)
third_powers = list(map(lambda x: x**3, numbers))

# Wypisujemy wynik - trzecie potęgi liczb od 1 do 20
print(f"Third powers of numbers from 1 to 20: {third_powers}")
