
# Funkcja, która zwraca drugi największy element w tablicy
def second_largest(arr):
    first_max = second_max = float('-inf')  # Inicjalizujemy obie zmienne na wartość -nieskończoność
    for num in arr:
        if num > first_max:
            second_max = first_max  # Uaktualniamy drugi największy
            first_max = num  # Uaktualniamy największy
        elif num > second_max and num != first_max:
            second_max = num  # Uaktualniamy drugi największy, jeśli to konieczne
    return second_max

# Funkcja, która zwraca różnicę między największą a najmniejszą wartością w tablicy
def difference_max_min(arr):
    max_val = min_val = arr[0]  # Zakładamy, że pierwszy element to zarówno max, jak i min
    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return max_val - min_val

# Funkcja, która zwraca medianę liczb w tablicy
def median(arr):
    arr_sorted = sorted(arr)  # Sortujemy tablicę
    n = len(arr_sorted)
    if n % 2 == 1:  # Jeżeli długość tablicy jest nieparzysta
        return arr_sorted[n // 2]  # Zwracamy środkowy element
    else:  # Jeżeli długość tablicy jest parzysta
        return (arr_sorted[n // 2 - 1] + arr_sorted[n // 2]) / 2  # Zwracamy średnią dwóch środkowych elementów

# Funkcja, która zwraca tablicę dwóch elementów: najmniejszą i największą wartość w tablicy
def smallest_largest(arr):
    min_val = max_val = arr[0]  # Zakładamy, że pierwszy element to zarówno min, jak i max
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return [min_val, max_val]

# Funkcja, która zwraca elementy tablicy jako ciąg znaków, oddzielony myślnikiem
def array_to_string(arr):
    return '-'.join(str(num) for num in arr)
