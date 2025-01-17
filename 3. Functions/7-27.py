# Products are marked with a special code consisting of 3 digits and afourth control digit. 
# The forth digit is determined by calculating the remainder of dividing the sum of the first three digits by 7. 
# Define a function f(product_code) that returns True if the product code is correct or False otherwise. Sample result:

# f("1082") returns True
# f("2035") returns True
# f("1114") returns False
# f("7071") returns False

def f(product_code):
    """
    Funkcja sprawdza poprawność kodu produktu.
    
    Parametry:
    - product_code (str): Kod produktu jako ciąg 4 cyfr.

    Zwraca:
    - True, jeśli kod jest poprawny.
    - False, jeśli kod jest niepoprawny.
    """
    # Sprawdzenie, czy kod składa się dokładnie z 4 cyfr
    if len(product_code) != 4 or not product_code.isdigit():
        return False

    # Pobranie pierwszych trzech cyfr i obliczenie ich sumy
    first_three_digits = product_code[:3]
    control_digit_given = int(product_code[3])  # Czwarta cyfra
    
    suma = int(first_three_digits[0]) + int(first_three_digits[1]) + int(first_three_digits[2])
    
    # Obliczenie cyfry kontrolnej
    control_digit_calculated = suma % 7

    # Sprawdzenie, czy obliczona cyfra kontrolna zgadza się z podaną
    if control_digit_calculated == control_digit_given:
        return True
    else:
        return False

# Testy funkcji
print(f("1082"))  # True
print(f("2035"))  # True
print(f("1114"))  # False
print(f("7071"))  # False
