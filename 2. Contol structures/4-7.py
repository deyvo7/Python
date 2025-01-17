###
# Calculates the sum of even numbers in the range <1,10>
#
###
# Oblicza sumę liczb parzystych w zakresie <1,10>
###

# Zmienna do przechowywania sumy
sum = 0

# Pętla przechodząca przez liczby w zakresie od 1 do 10 (włącznie z 10)
for i in range(1, 11):  
    if not (i % 2 == 0):  # Sprawdza, czy liczba i jest nieparzysta
        continue  # Jeśli liczba jest nieparzysta, przejdź do następnej iteracji
    sum += i  # Dodaj liczbę parzystą do sumy

# Wyświetl wynik
print(f'Sum of even numbers in the range <1,10> is {sum}')
