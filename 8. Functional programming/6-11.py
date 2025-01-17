# Lista wyników testów - dla każdego studenta mamy imię i wynik testu
test_results = [
   {"name":"Peter","result":27},    # Student Peter ma wynik 27
   {"name":"Anna","result":63},     # Student Anna ma wynik 63
   {"name":"Robert","result":92},   # Student Robert ma wynik 92
   {"name":"Paul","result":46},     # Student Paul ma wynik 46
   {"name":"Barbara","result":52}   # Student Barbara ma wynik 52
]

# Używamy funkcji filter(), aby wybrać tylko tych studentów, których wynik mieści się w przedziale 50-70
# Funkcja filter() zwraca tylko te elementy, dla których funkcja (lambda) zwróci True.
filtered_students = list(filter(lambda student: 50 <= student["result"] <= 70, test_results))

# Pętla for przechodzi po przefiltrowanej liście studentów
for student in filtered_students:
    # Dla każdego studenta wypisujemy jego imię i wynik
    print(f"{student['name']} - {student['result']} points")
