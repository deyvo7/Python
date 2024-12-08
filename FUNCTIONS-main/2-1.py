# Using built-in Python functions, write a program that calculates and prints:

# the largest number: 7,5,6,3,8,2
# the smallest number: 4,7,2,3,9,8
# length of the phrase: "computer science"
# letter read from the keyboard
# number representing the string "20303"
# binary string representing decimal number 304
# hexadecimal string representing decimal number 304
# integer representing the Unicode code of the € sign
# absolute value of -17

# Program do testowania wbudowanych funkcji Pythona
#

# Znajduje największą liczbę spośród podanych wartości
max_number = max(7, 5, 6, 3, 8, 2)
print('Największa liczba spośród 7, 5, 6, 3, 8, 2 to', max_number)

# Znajduje najmniejszą liczbę spośród podanych wartości
min_number = min(4, 7, 2, 3, 9, 8)
print('Najmniejsza liczba spośród 4, 7, 2, 3, 9, 8 to', min_number)

# Oblicza długość ciągu znaków (liczba znaków)
str_length = len("computer science")
print('Liczba znaków w "computer science" to', str_length)

# Odczytuje literę od użytkownika z klawiatury
letter = input("Wprowadź literę: ")
print("Wprowadzona litera to: ", letter)

# Konwertuje ciąg znaków na liczbę całkowitą
string_to_number = int("20303")
print("Liczba reprezentująca ciąg znaków '20303': ", string_to_number)

# Konwertuje liczbę dziesiętną na łańcuch znaków w systemie binarnym
decimal_to_binary = str(bin(304))
print("Ciąg binarny reprezentujący liczbę dziesiętną 304:  ", decimal_to_binary)

# Konwertuje liczbę dziesiętną na łańcuch znaków w systemie szesnastkowym
decimal_to_hexadecimal = str(hex(304))
print("Ciąg szesnastkowy reprezentujący liczbę dziesiętną 304:  ", decimal_to_hexadecimal)

# Znajduje kod Unicode dla znaku €
unicode = ord("€")
print("Całkowita liczba reprezentująca kod Unicode znaku €: ", unicode)

# Oblicza wartość bezwzględną liczby -17
absolute = abs(-17)
print("Wartość bezwzględna liczby -17: ", absolute)
