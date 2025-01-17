# Definiujemy anonimową funkcję (lambda), która sprawdza, czy liczba jest parzysta
# Funkcja przyjmuje jeden argument x (liczbę) i sprawdza, czy jej reszta z dzielenia przez 2 wynosi 0
# Jeśli tak, liczba jest parzysta, funkcja zwróci True, w przeciwnym razie False
is_even = lambda x: x % 2 == 0

# Pobieramy liczbę od użytkownika
# Funkcja input() zwraca dane jako tekst, dlatego zamieniamy je na liczbę całkowitą (int)
number = int(input("Enter the number: "))

# Wywołujemy anonimową funkcję is_even() i sprawdzamy, czy liczba jest parzysta
# Wypisujemy wynik
print("Number is even: ", is_even(number))
