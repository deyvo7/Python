# Define a function that calculates the final grade for a test based on the number of points obtained,
# according to the rules:

# Less than 10 points, final grade: Fail
# At least 10 points, final grade: Satisfactory
# At least 14 points, final grade: Good
# At least 18 points, final grade: Excellent

# Definiujemy funkcję, która oblicza końcową ocenę na podstawie liczby zdobytych punktów.

def pts_to_grade(points):
    # Sprawdzamy, czy liczba punktów jest większa lub równa 18. Jeśli tak, zwracamy ocenę "Excellent".
    if points >= 18:
        return ("Excellent")
    # Sprawdzamy, czy liczba punktów jest większa lub równa 14. Jeśli tak, zwracamy ocenę "Good".
    elif points >= 14:
        return ("Good")
    # Sprawdzamy, czy liczba punktów jest większa lub równa 10. Jeśli tak, zwracamy ocenę "Satisfactory".
    elif points >= 10:
        return ("Satisfactory")
    # Jeśli liczba punktów jest mniejsza niż 10, zwracamy ocenę "Fail".
    elif points < 10:
        return ("Fail")

# Pobieramy od użytkownika liczbę punktów zdobytych na teście.
test_result = int(input("Enter your points: "))

# Wywołujemy funkcję, aby obliczyć końcową ocenę na podstawie zdobytych punktów.
final_grade = pts_to_grade(test_result)

# Wyświetlamy wynik: liczbę punktów oraz końcową ocenę.
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')
