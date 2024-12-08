###
# Calculates the sum of even numbers from 1 to a given number N
# The following program calculates the sum of even numbers from 1 to a given number N using a for loop.
# Modify the program. Replace the 'for' statement with a 'while' statement.

##
# Oblicza sumę liczb parzystych od 1 do podanej liczby N
# Program wykorzystuje pętlę while zamiast for
##

# Pobranie liczby N od użytkownika
N = int(input("Enter the N number: "))  
# Zmienne do przechowywania sumy liczb parzystych i liczby parzystych liczb
sum_even = 0  
even_numbers = 0  
# Zmienna pomocnicza do iteracji
i = 1  

# Pętla while przechodzi przez liczby od 1 do N
while i <= N:  
    print(i)  # Wyświetla bieżącą liczbę
    if i % 2 == 0:  # Sprawdza, czy liczba i jest parzysta
        sum_even += i  # Dodaje liczbę parzystą do sumy
        even_numbers += 1  # Zwiększa licznik liczb parzystych
    i += 1  # Zwiększa wartość i o 1

# Oblicza średnią arytmetyczną liczb parzystych
arithmetic_mean = sum_even / even_numbers  

# Wyświetla wyniki
print(f"The sum of even numbers from 1 to {N} is: {sum_even}. The arithmetic mean of the numbers is {arithmetic_mean}")
