# A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0.
#  Create a program and the function. Then create a two-dimensional array with dimensions of 3 by 5. 
# print the created array.

# Funkcja do tworzenia dwuwymiarowej tablicy wypełnionej zerami
def create_2d_arr(x, y):
    # Tworzymy pustą listę, która będzie zawierała wiersze
    array = []
    
    # Zewnętrzna pętla do tworzenia wierszy
    for i in range(x):
        # Tworzymy jeden wiersz wypełniony zerami
        row = []
        
        # Wewnętrzna pętla do wypełniania wiersza zerami
        for j in range(y):
            row.append(0)  # Dodajemy zero do wiersza
        
        # Po zakończeniu tworzenia wiersza dodajemy go do tablicy
        array.append(row)
    
    # Zwracamy utworzoną dwuwymiarową tablicę
    return array

# Tworzymy tablicę 3x5
array = create_2d_arr(3, 5)

# Wypisujemy tablicę
for row in array:
    print(row)
