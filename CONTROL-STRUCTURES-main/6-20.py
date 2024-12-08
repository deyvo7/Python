# Write a program that converts a decimal number into a binary number. To convert a decimal number to binary, follow these steps:

# Read a decimal number from the keyboard.
# Divide the number by 2 and note the remainder.
# Divide the quotient obtained by 2 and note the remainder.
# Repeat the same process till we get 0 as the quotient.
# Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.
# Sample result:

# Enter decimal number: 12
# 12(10) = 1100(2)
# Program do konwersji liczby dziesiętnej na liczbę binarną

decimal = int(input("Enter decimal number: "))  # Pobranie liczby dziesiętnej od użytkownika
original_decimal = decimal  # Zapamiętanie oryginalnej liczby dziesiętnej
remainders = []  # Lista do przechowywania reszt z dzielenia przez 2

# Pętla do konwersji liczby dziesiętnej na binarną
while decimal > 0:
    remainder = decimal % 2  # Obliczenie reszty z dzielenia przez 2
    remainders.append(str(remainder))  # Dodanie reszty do listy
    decimal = decimal // 2  # Dzielenie liczby przez 2 i zaokrąglanie w dół

binary = ''  # Zmienna do przechowywania liczby binarnej
# Odwrócenie listy reszt (od dołu do góry) i utworzenie liczby binarnej
for i in range(len(remainders) - 1, -1, -1):
    binary += remainders[i]  # Dodanie reszty do ciągu binarnego

# Wyświetlenie wyniku konwersji
print(f"{original_decimal}(10) = {binary}(2)")
