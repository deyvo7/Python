# Write a program that checks what number was entered from the keyboard and prints one of the messages below.
# Then run the program and check the following numbers:

# 7, 1 ,0 ,-1 , -4

# Number ... is positive
# Number ... is negative
# Number is 0

# Napisz program, który sprawdza, jaką liczbę wprowadzono z klawiatury, 
# i wyświetla jedną z poniższych wiadomości:
# - Liczba ... jest dodatnia
# - Liczba ... jest ujemna
# - Liczba jest równa 0

# Wprowadź i przetestuj liczby: 7, 1, 0, -1, -4

# Pobierz liczbę od użytkownika
number = int(input("Enter a number: "))  # Wprowadź liczbę z klawiatury (jako liczba całkowita)

# Sprawdź, czy liczba jest dodatnia
if number > 0:
    print(f"Number {number} is positive")  # Jeśli liczba jest większa od 0, wyświetl komunikat, że jest dodatnia
# Sprawdź, czy liczba wynosi 0
elif number == 0:
    print("Number is 0")  # Jeśli liczba równa się 0, wyświetl komunikat, że to 0
# Sprawdź, czy liczba jest ujemna
elif number < 0:
    print(f"Number {number} is negative")  # Jeśli liczba jest mniejsza od 0, wyświetl komunikat, że jest ujemna
