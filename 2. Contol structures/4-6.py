###
# Calculates the sum of integer numbers in the range <1,5>
# Make the following changes to the program:
# sum the numbers from 5 to 10
# use the += operator in the expression sum=sum+i
###
# Oblicza sumę liczb całkowitych w zakresie <5,10>
# Zmieniono zakres na od 5 do 10 i użyto operatora +=
###

# Zmienna do przechowywania sumy
sum = 0

# Pętla przechodząca przez liczby w zakresie od 5 do 10 (włącznie z 10)
for i in range(5, 11):  
    sum += i  # Dodaj liczbę i do sumy (operator +=)

# Wyświetl wynik
print(f'Sum is {sum}')  # Wyświetl sumę liczb
