# Two numbers and an operator are given. Define a function f(number1,number2,operator) that returns the result
# of an arithmetic operation. The available operators are +,-,*,%,**. Sample result:

# f(2,3, "+") returns 5
# f(2,3, "%") returns 2
# f(2,3, "**") returns 8
# f(2,3, "*") returns 6
# f(2,3, "-") returns -1

# Funkcja wykonująca operację arytmetyczną na dwóch liczbach
def f(number1, number2, operator):
    if operator == "+":
        return number1 + number2  # Dodawanie
    elif operator == "-":
        return number1 - number2  # Odejmowanie
    elif operator == "*":
        return number1 * number2  # Mnożenie
    elif operator == "%":
        return number1 % number2  # Reszta z dzielenia
    elif operator == "**":
        return number1 ** number2  # Potęgowanie
    else:
        return "Invalid operator"  # Obsługa nieprawidłowego operatora

# Testowanie funkcji
print(f(2, 3, "+"))   # Powinno zwrócić 5
print(f(2, 3, "-"))   # Powinno zwrócić -1
print(f(2, 3, "*"))   # Powinno zwrócić 6
print(f(2, 3, "%"))   # Powinno zwrócić 2
print(f(2, 3, "**"))  # Powinno zwrócić 8
