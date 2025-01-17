# Define a function that sorts an array of numbers using the bubble sort
# algorithm. Use the information in the pseudocode provided earlier.
# Then, write a program that sorts the following collections of data:

# Here is the bubble sort algorithm expressed in pseudocode,
# a universal notation that is independent of the programming language:

# Definicja funkcji sortującej tablicę za pomocą algorytmu sortowania bąbelkowego (Bubble Sort)
def bubble_sort(arr):
    # Zewnętrzna pętla: przechodzimy przez całą tablicę
    for i in range(len(arr) - 1):  # Zmieniamy zakres, aby pętla przechodziła przez wszystkie elementy
        # Wewnętrzna pętla: porównujemy sąsiednie elementy
        for j in range(len(arr) - 1 - i):  # Zmniejszamy zakres z każdą iteracją pętli zewnętrznej
            # Jeśli bieżący element jest większy od następnego, zamieniamy je miejscami
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Zamiana miejscami

    # Zwracamy posortowaną tablicę
    return arr


# Przykładowe dane do posortowania

# Tablica z zużyciem paliwa samochodów
car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]

# Tablica z transakcjami bankowymi
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

# Wyświetlamy oryginalne dane przed posortowaniem
print("Original car fuel consumption:", car_fuel_consumption)
# Wywołujemy funkcję sortującą dla zużycia paliwa
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
# Wyświetlamy posortowaną tablicę zużycia paliwa
print("Sorted car fuel consumption:", sorted_car_fuel_consumption)

# Wyświetlamy oryginalne dane przed posortowaniem
print("Original bank transactions:", bank_transactions)
# Wywołujemy funkcję sortującą dla transakcji bankowych
sorted_bank_transactions = bubble_sort(bank_transactions)
# Wyświetlamy posortowaną tablicę transakcji bankowych
print("Sorted bank transactions:", sorted_bank_transactions)



# Funkcja bubble_sort(arr):

# Algorytm Bubble Sort działa na zasadzie wielokrotnego porównywania sąsiednich elementów w tablicy.
# Jeśli bieżący element jest większy niż następny, to te elementy są zamieniane miejscami.
# Proces ten powtarza się wielokrotnie, aż cała tablica będzie posortowana.
# Pętla zewnętrzna wykonuje iteracje przez całą tablicę, a pętla wewnętrzna porównuje kolejne elementy i wykonuje zamiany.