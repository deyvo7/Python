# Write a program that prints 20 integer random numbers in the range of 5 to 10.

# Program generujący 20 losowych liczb całkowitych z zakresu od 5 do 10

import random

# Pętla generująca 20 losowych liczb
for num in range(20):
    # Generowanie losowej liczby z zakresu 5-10 i drukowanie jej
    print(random.randint(5, 10), end=' ')
