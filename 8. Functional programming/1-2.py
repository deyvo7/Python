# Pobieramy dwie liczby od użytkownika z klawiatury
# Funkcja input() pobiera dane wejściowe jako tekst, dlatego zamieniamy je na liczby zmiennoprzecinkowe za pomocą float()
n1 = float(input("N1: "))  # Pierwsza liczba zmiennoprzecinkowa
n2 = float(input("N2: "))  # Druga liczba zmiennoprzecinkowa

# Definiujemy anonimową funkcję (lambda), która oblicza średnią arytmetyczną dwóch liczb
# 'lambda x, y: (x + y) / 2' to sposób na utworzenie funkcji w jednej linii
# x i y to argumenty funkcji, a (x + y) / 2 to wyrażenie obliczające średnią arytmetyczną
mean = lambda x, y: (x + y) / 2

# Obliczamy średnią arytmetyczną, wywołując funkcję 'mean' z przekazanymi argumentami n1 i n2
result = mean(n1, n2)

# Wypisujemy wynik na ekranie
# Używamy f-string, aby wygodnie wstawić zmienne n1, n2 i result do tekstu
print(f"The arithmetic mean of {n1} and {n2} is {result}")
