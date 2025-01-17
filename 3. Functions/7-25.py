# Define the function f(x,y), which returns the sum of numbers in the range <x,y> that are completely divisible
# by 2 and 3 and not divisible by 4. Sample result:

# f(1,20) returns 24
# f(10,30) returns 48

def f(x, y):
    # Funkcja oblicza sumę liczb w przedziale <x, y>, które są podzielne przez 2 i 3, ale nie są podzielne przez 4.
    
    total_sum = 0  # Inicjalizujemy zmienną do przechowywania sumy
    
    # Iterujemy przez wszystkie liczby w przedziale od x do y (włącznie)
    for number in range(x, y + 1):
        # Sprawdzamy warunki: liczba musi być podzielna przez 2 i 3 oraz nie może być podzielna przez 4
        if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
            total_sum += number  # Dodajemy liczbę do sumy
    
    return total_sum  # Zwracamy końcową sumę

# Przykłady testowe
print(f(1, 20))  # Powinno zwrócić 24
print(f(10, 30))  # Powinno zwrócić 48
