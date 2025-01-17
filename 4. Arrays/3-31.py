# An array contains integer numbers:

# [[-38, 19], [5,40],[-7,11],[29,16]]
# Create a program that finds the smallest and largest values in the array and in which row and column they are located.

# Tablica dwuwymiarowa
array = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

# Inicjalizacja zmiennych dla najmniejszej i największej liczby
min_value = float('inf')  # Ustawiamy bardzo dużą wartość na początek
max_value = float('-inf') # Ustawiamy bardzo małą wartość na początek
min_pos = (-1, -1)  # Pozycja dla najmniejszej liczby
max_pos = (-1, -1)  # Pozycja dla największej liczby

# Przechodzimy przez tablicę i porównujemy wartości
for i in range(len(array)):
    for j in range(len(array[i])):
        value = array[i][j]
        
        # Sprawdzamy, czy wartość jest mniejsza niż dotychczasowa najmniejsza
        if value < min_value:
            min_value = value
            min_pos = (i, j)  # Zapamiętujemy pozycję najmniejszej liczby
        
        # Sprawdzamy, czy wartość jest większa niż dotychczasowa największa
        if value > max_value:
            max_value = value
            max_pos = (i, j)  # Zapamiętujemy pozycję największej liczby

# Wypisujemy wyniki
print(f"Najmniejsza liczba: {min_value} na pozycji wiersz {min_pos[0] + 1}, kolumna {min_pos[1] + 1}")
print(f"Największa liczba: {max_value} na pozycji wiersz {max_pos[0] + 1}, kolumna {max_pos[1] + 1}")
