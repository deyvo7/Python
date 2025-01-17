# An expression contains operators for adding and subtracting single-digit numbers.
# Define a function f(expression) that returns the value of the expression. Sample result:

# f("2+3") returns 5
# f("3+8+1") returns 12
# f("2+3-4+5-0") returns 6


def f(expression):
    # Funkcja oblicza wartość wyrażenia z użyciem pętli i prostych operacji arytmetycznych.
    
    # Inicjalizujemy zmienne dla sumy i aktualnej liczby
    total = 0
    current_number = 0
    current_operator = '+'
    
    # Przechodzimy przez każdy znak w wyrażeniu
    for char in expression:
        if char.isdigit():  # Sprawdzamy, czy znak jest cyfrą
            current_number = int(char)  # Konwertujemy cyfrę na liczbę
            # Wykonujemy operację w zależności od bieżącego operatora
            if current_operator == '+':
                total += current_number
            elif current_operator == '-':
                total -= current_number
        elif char in ['+', '-']:  # Sprawdzamy, czy znak jest operatorem
            current_operator = char  # Ustawiamy nowego operatora
    
    return total

# Testowanie funkcji z przykładowymi danymi
print(f("2+3"))       # Powinno zwrócić 5, ponieważ 2 + 3 = 5
print(f("3+8+1"))     # Powinno zwrócić 12, ponieważ 3 + 8 + 1 = 12
print(f("2+3-4+5-0")) # Powinno zwrócić 6, ponieważ 2 + 3 - 4 + 5 - 0 = 6
