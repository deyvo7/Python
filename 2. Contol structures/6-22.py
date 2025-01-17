# Write a program that prints numbers from 1 to 30. If the number is divisible by 3 then the program prints the word 'THREE'.
# Next, if the number is divisible by 5 then the program prints the word 'FIVE'.
# Finally, if the number is divisible by both 3 and 5 then the program prints the word 'BINGO'.

# Sample result:
# 1 2 THREE 4 FIVE THREE 7 ...

# Program, który wypisuje liczby od 1 do 30. Jeśli liczba jest podzielna przez 3, wypisuje 'THREE',
# jeśli przez 5, wypisuje 'FIVE', a jeśli przez 3 i 5, wypisuje 'BINGO'.

for i in range(1, 31):  # Pętla od 1 do 30
    if i % 3 == 0 and i % 5 == 0:  # Jeśli liczba jest podzielna przez 3 i 5
        print('BINGO', end=' ')  # Wypisz 'BINGO'
    elif i % 3 == 0:  # Jeśli liczba jest podzielna tylko przez 3
        print('THREE', end=' ')  # Wypisz 'THREE'
    elif i % 5 == 0:  # Jeśli liczba jest podzielna tylko przez 5
        print('FIVE', end=' ')  # Wypisz 'FIVE'
    else:  # Jeśli liczba nie jest podzielna ani przez 3, ani przez 5
        print(i, end=' ')  # Wypisz liczbę
