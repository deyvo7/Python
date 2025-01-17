# A computer numeric keyboard has the arrangement of the keys as below.
# The included program code prints the computer keyboard. 
# Analyse the program in terms of the printed results. Do you understand each program statement?
# Then make changes in your program code. Replace the 'for' with a 'while' statement.

# 7 8 9
# 4 5 6
# 1 2 3

# Inicjalizacja zmiennej i, która reprezentuje początkową wartość najwyższą w rzędzie
i = 6  

# Pętla zewnętrzna dla rzędów
while i >= 0:  
    j = 1  # Inicjalizacja zmiennej j, która reprezentuje numer kolumny w każdym rzędzie
    # Pętla wewnętrzna dla kolumn (drukowanie 3 liczb w każdym rzędzie)
    while j <= 3:  
        print(f'{i + j}', end=' ')  # Drukowanie liczby z odstępem
        j += 1  # Inkrementacja j, aby przejść do następnej liczby w kolumnie
    print()  # Przejście do nowego wiersza po wydrukowaniu 3 liczb
    i -= 3  # Zmniejszenie i o 3, aby przejść do kolejnego rzędu liczb
