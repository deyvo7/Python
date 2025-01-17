# Using functions and constants available in the 'math' module, write a program that calculates and prints:

# square root of 7
# natural logarithm of 5
# sine of 90 degrees

###
# To use the functions available in an external module,
# you must include that module in your program.

# Importuje moduł math, który zawiera funkcje matematyczne, takie jak pierwiastki, logarytmy i funkcje trygonometryczne.
import math

# Oblicza pierwiastek kwadratowy z liczby 7
square_root = math.sqrt(7)
print('Pierwiastek kwadratowy z 7 to', square_root)

# Oblicza logarytm naturalny z liczby 5 (logarytm o podstawie e)
nat_log = math.log(5)
print(f"Logarytm naturalny z 5 to {nat_log}")

# Oblicza sinus kąta 90 stopni. Kąty muszą być podane w radianach, więc konwertujemy 90 stopni na radiany.
sin = math.sin(math.radians(90))
print(f"Sinus kąta 90 stopni to {sin}")