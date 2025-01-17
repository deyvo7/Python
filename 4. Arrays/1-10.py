# The array contains the student's test results.
# A value of True indicates that the student answered the question
# correctly, while a value of False indicates an incorrect answer.
# Write a program that prints information about the test results:

# Number of questions:
# Number of correct answers:
# Number of incorrect answers:
# Percentage of correct answers:

###
# Prints test statistics
#
# Lista wyników testu (True - poprawna odpowiedź, False - niepoprawna odpowiedź)
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

# Obliczamy liczbę pytań w teście
question_number = len(test_results)

# Obliczamy liczbę poprawnych odpowiedzi
correct_answers = sum(test_results)  # Sumowanie True (wartość 1) daje liczbę poprawnych odpowiedzi

# Obliczamy liczbę niepoprawnych odpowiedzi
incorrect_answers = question_number - correct_answers  # Wszystkie pytania minus poprawne

# Obliczamy procent poprawnych odpowiedzi
percentage = (correct_answers / question_number) * 100

# Wyświetlamy statystyki testu
print('STATYSTYKI TESTU')
print('================')
print('Liczba pytań:', question_number)
print('Liczba poprawnych odpowiedzi:', correct_answers)
print('Liczba niepoprawnych odpowiedzi:', incorrect_answers)
print('Procent poprawnych odpowiedzi:', round(percentage, 2), '%')
