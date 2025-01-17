# Create a program that sorts elements of an array containing integer numbers.
#  Apply the Bubble Sort sorting algorithm. Define a function bubblesort(array) that returns the sorted array. 
# Try to sort and print any three arrays.

# Funkcja do sortowania tablicy za pomocą algorytmu Bubble Sort
def bubblesort(array):
    # Pobieramy długość tablicy, aby wiedzieć, ile razy musimy przejść przez tablicę
    n = len(array)
    
    # Zewnętrzna pętla przechodzi przez wszystkie elementy tablicy
    for i in range(n):
        # Wewnętrzna pętla porównuje sąsiednie elementy tablicy i zamienia je miejscami, jeśli są w złej kolejności
        # 'n-i-1' oznacza, że za każdym razem przechodzimy przez coraz mniejszą część tablicy,
        # ponieważ po każdej iteracji największy element "wypływa" na koniec
        for j in range(0, n-i-1):
            # Sprawdzamy, czy element na pozycji j jest większy od elementu na pozycji j+1
            if array[j] > array[j+1]:
                # Jeśli tak, zamieniamy te dwa elementy miejscami
                array[j], array[j+1] = array[j+1], array[j]
    
    # Po zakończeniu pętli tablica jest już posortowana, więc zwracamy ją
    return array  

# Testowanie funkcji na trzech różnych tablicach

# Tablica 1 - przykładowa tablica z liczbami do posortowania
array1 = [64, 34, 25, 12, 22, 11, 90]
# Wywołujemy funkcję bubblesort, aby posortować array1
sorted_array1 = bubblesort(array1)
# Wypisujemy posortowaną tablicę
print("Sorted array1:", sorted_array1)

# Tablica 2 - druga przykładowa tablica
array2 = [5, 1, 4, 2, 8]
# Wywołujemy funkcję bubblesort, aby posortować array2
sorted_array2 = bubblesort(array2)
# Wypisujemy posortowaną tablicę
print("Sorted array2:", sorted_array2)

# Tablica 3 - trzecia przykładowa tablica
array3 = [30, 20, 50, 40, 10]
# Wywołujemy funkcję bubblesort, aby posortować array3
sorted_array3 = bubblesort(array3)
# Wypisujemy posortowaną tablicę
print("Sorted array3:", sorted_array3)
