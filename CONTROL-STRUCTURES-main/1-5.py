###
# Checking whether the test is passed
# Test is passed when the number of correctly completed
# tasks is at least 50%
#
###
# Sprawdzenie, czy test został zaliczony
# Test jest zaliczony, gdy liczba poprawnie rozwiązanych zadań
# stanowi co najmniej 50% wszystkich zadań
###

# Całkowita liczba zadań
total_tasks = 20

# Wczytanie liczby poprawnie rozwiązanych zadań od użytkownika
tasks_ok = int(input("Enter how many tasks you have solved correctly: "))

# Zmienna wskazująca, czy test został zaliczony
test_passed = False

# Sprawdzenie, czy liczba poprawnie rozwiązanych zadań jest co najmniej połową wszystkich zadań
if tasks_ok >= (total_tasks / 2):
    test_passed = True

# Wyświetlenie komunikatu w zależności od wyniku
if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')
