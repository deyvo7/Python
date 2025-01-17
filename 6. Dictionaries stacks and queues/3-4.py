# Funkcja konwertująca liczbę naturalną na liczbę binarną
def decimal_to_binary(n):
    stack = []  # Stos, na którym będziemy przechowywać reszty z dzielenia przez 2

    # Dzielimy liczbę przez 2, aż do momentu, kiedy liczba wyniesie 0
    while n > 0:
        remainder = n % 2  # Obliczamy resztę z dzielenia przez 2
        stack.append(remainder)  # Dodajemy resztę na stos
        n = n // 2  # Dzielimy liczbę przez 2 (całkowicie)

    # Wyświetlamy wynik w postaci binarnej
    binary_number = ""
    while stack:
        binary_number += str(stack.pop())  # Zdejmujemy elementy ze stosu i dodajemy do wyniku

    return binary_number  # Zwracamy wynik w formie liczby binarnej

# Przykład użycia programu
number = 18  # Przykładowa liczba do konwersji
print(f"Natural number: {number}")
binary = decimal_to_binary(number)
print(f"Binary number: {binary}")
