# Write a program that prints the first twenty words of the Fibonacci sequence.
# The sequence is defined as follows: the first term is equal to 0, the second is equal to 1,
# each subsequent term is the sum of the previous two.
# 
# Sample result:
# 0 1 1 2 3 5 8 13 21 34 ...

# Program drukujący pierwsze 20 liczb w ciągu Fibonacciego

# Inicjalizacja pierwszych dwóch liczb ciągu
a = 0  
b = 1  
count = 0  # Licznik, który będzie śledził, ile liczb zostało wydrukowanych

# Pętla do momentu, aż wydrukujemy 20 liczb
while count < 20:
    print(a, end=' ')  # Drukowanie bieżącej liczby
    temp = a  # Zapisanie wartości a w zmiennej pomocniczej
    a = b  # Przypisanie wartości b do a
    b = temp + b  # Obliczenie następnej liczby ciągu
    count += 1  # Zwiększenie licznika
