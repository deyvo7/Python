###
# Checks whether at least one number entered
# from the keyboard is not negative
# 
###
# Sprawdza, czy przynajmniej jedna z liczb wprowadzonych 
# z klawiatury nie jest ujemna
###

# Pobierz dwie liczby od użytkownika
x = int(input('Enter first number: '))  # Wprowadź pierwszą liczbę (liczba całkowita)
y = int(input('Enter second number: '))  # Wprowadź drugą liczbę (liczba całkowita)

# Sprawdź, czy przynajmniej jedna liczba nie jest ujemna
if not x < 0 or not y < 0:  
    # Jeśli warunek (x < 0 lub y < 0) jest fałszywy, to znaczy, że przynajmniej jedna liczba nie jest ujemna
    print(f'At least one of the numbers {x} and {y} is not negative')  
    # Wyświetl komunikat, że przynajmniej jedna liczba nie jest ujemna
else:  
    # Jeśli obie liczby są ujemne
    print("Both numbers are negative")  # Wyświetl komunikat, że obie liczby są ujemne
