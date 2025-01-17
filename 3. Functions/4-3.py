# Define a function triangle_area that calculates and returns the area of ​​a triangle with sides a, b, and c. Use Heron's formula:

# https://en.wikipedia.org/wiki/Heron's_formula

# Write a program that calculates the area of ​​a triangle based on the lengths of the triangle's sides read from the keyboard. Use the defined function. Then calculate the area of ​​the triangle for the following dimensions of sides a, b, and c:

# 3, 4, 5 (result is 6)
# 5, 12, 13 (result is 30)
# 7, 24, 25 (result is 84)


# Importujemy moduł math, aby móc używać funkcji matematycznych, takich jak pierwiastek kwadratowy
import math

# Prosimy użytkownika o podanie długości boków trójkąta
a = float(input("Enter the length of a: "))  # Wczytujemy długość boku a i konwertujemy ją na liczbę zmiennoprzecinkową
b = float(input("Enter the length of b: "))  # Wczytujemy długość boku b i konwertujemy ją na liczbę zmiennoprzecinkową
c = float(input("Enter the length of c: "))  # Wczytujemy długość boku c i konwertujemy ją na liczbę zmiennoprzecinkową

# Definiujemy funkcję do obliczania pola powierzchni trójkąta na podstawie długości jego boków
def triangle_area(a, b, c):
    # Obliczamy połowę obwodu trójkąta (s), zgodnie z wzorem Herona
    s = (a + b + c) / 2
    
    # Obliczamy pole trójkąta przy użyciu wzoru Herona: sqrt(s * (s - a) * (s - b) * (s - c))
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    # Zwracamy obliczone pole
    return area

# Obliczamy pole trójkąta dla podanych długości boków i wyświetlamy wynik
print(f'The area of a triangle with sides {a}, {b}, {c} is: {triangle_area(a, b, c)}')

# Testowanie funkcji z określonymi wartościami boków
# Obliczamy pole dla trójkąta o bokach 3, 4, 5 (spodziewany wynik to 6)
print(f'The area of a triangle with sides 3, 4, 5 is: {triangle_area(3, 4, 5)}')

# Obliczamy pole dla trójkąta o bokach 5, 12, 13 (spodziewany wynik to 30)
print(f'The area of a triangle with sides 5, 12, 13 is: {triangle_area(5, 12, 13)}')

# Obliczamy pole dla trójkąta o bokach 7, 24, 25 (spodziewany wynik to 84)
print(f'The area of a triangle with sides 7, 24, 25 is: {triangle_area(7, 24, 25)}')
