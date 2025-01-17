###
# Calculates values for the following fractions: 1/2, 1/3, ..., 1/10
#
###
# Oblicza wartości dla ułamków: 1/2, 1/3, ..., 1/10
###

# Pętla przechodząca przez liczby od 2 do 10 (włącznie z 10)
for i in range(2, 11):  
    result = 1 / i  # Oblicz wartość ułamka 1/i
    print(f'1/{i} = {result}')  # Wyświetl wynik dla danego ułamka
