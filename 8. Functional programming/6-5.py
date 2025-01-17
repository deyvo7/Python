# Tworzymy tablicę zawierającą liczby od 1 do 20
numbers = list(range(1, 21))

# Używamy funkcji filter() do wybrania liczb, które są podzielne przez 2 i 3
# Funkcja lambda sprawdza, czy liczba jest podzielna zarówno przez 2, jak i 3 (x % 2 == 0 i x % 3 == 0)
divisible_by_2_and_3 = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, numbers))

# Wypisujemy wynik - liczby podzielne przez 2 i 3
print(f"Numbers divisible by 2 and 3: {divisible_by_2_and_3}")
