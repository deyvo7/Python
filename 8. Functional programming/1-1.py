# Funkcja obliczająca średnią arytmetyczną dwóch liczb
def mean(x, y):
    # Obliczamy średnią arytmetyczną jako sumę dwóch liczb podzieloną przez 2
    mean_value = (x + y) / 2
    # Zwracamy wynik obliczeń
    return mean_value

# Pobieramy dwie liczby od użytkownika z klawiatury
# Funkcja input() pobiera dane wejściowe jako tekst, dlatego zamieniamy je na liczby całkowite za pomocą int()
n1 = int(input("N1: "))  # Pierwsza liczba całkowita
n2 = int(input("N2: "))  # Druga liczba całkowita

# Wywołujemy funkcję mean() aby obliczyć średnią arytmetyczną dwóch liczb
result = mean(n1, n2)

# Wypisujemy wynik na ekranie
# f-string pozwala na łatwe wstawianie wartości zmiennych do tekstu
# W tym przypadku wypisujemy obie liczby i ich średnią arytmetyczną
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')
