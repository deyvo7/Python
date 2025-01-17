# Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. Sample result:

# f(-7,8) returns 3
# f(-1,11) returns 0

# Funkcja zwracająca liczbę ujemnych liczb parzystych w przedziale <x, y>
def f(x, y):
    # Inicjalizacja licznika
    count = 0
    
    # Przechodzimy przez każdą liczbę w przedziale <x, y>
    for num in range(x, y + 1):
        # Sprawdzamy, czy liczba jest ujemna i parzysta
        if num < 0 and num % 2 == 0:
            count += 1  # Zwiększamy licznik, jeśli warunek jest spełniony
    
    return count  # Zwracamy liczbę ujemnych liczb parzystych

# Testowanie funkcji
print(f(-7, 8))  # Powinno zwrócić 3 (liczby -6, -4, -2 są ujemne i parzyste)
print(f(-1, 11))  # Powinno zwrócić 0 (brak ujemnych liczb parzystych)
