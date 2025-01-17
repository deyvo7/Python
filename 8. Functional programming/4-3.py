# Lista ocen uzyskanych przez studentów na kursie "Geografia Ekonomiczna".
grades = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2.0]

# Używamy funkcji filter() z funkcją anonimową (lambda), aby wykluczyć oceny 2.0 (oceny negatywne).
# Funkcja lambda sprawdza, czy ocena jest większa niż 2.0.
grades_without_2 = list(filter(lambda x: x > 2.0, grades))

# Obliczamy średnią arytmetyczną ocen, które nie są równe 2.0
mean = sum(grades_without_2) / len(grades_without_2)

# Wypisujemy wynik - średnią arytmetyczną dla ocen większych niż 2.0
print(f"Arithmetic mean for grades <> 2.0 is {mean}")
