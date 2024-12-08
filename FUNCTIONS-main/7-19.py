# Define a function f(number) that returns the sum of repeated digits in a number. Sample result:

# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21

def f(number):
    # Konwertujemy liczbę na ciąg znaków, aby przejść przez każdą cyfrę
    num_str = str(number)
    
    # Tworzymy słownik do zliczania liczby wystąpień każdej cyfry
    digit_count = {}
    
    for digit in num_str:
        if digit in digit_count:
            digit_count[digit] += 1
        else:
            digit_count[digit] = 1
    
    # Zmienna do sumowania cyfr, które występują więcej niż raz
    sum_of_repeated_digits = 0
    
    # Sprawdzamy każdą cyfrę w słowniku
    for digit, count in digit_count.items():
        if count > 1:
            # Dodajemy wartość cyfry do sumy, jeśli występuje więcej niż raz
            sum_of_repeated_digits += int(digit) * count
    
    return sum_of_repeated_digits

# Testujemy funkcję na przykładowych danych
print(f(1027))      # Powinno zwrócić 0 (brak powtarzających się cyfr)
print(f(230335))    # Powinno zwrócić 9 (3 + 3 + 3)
print(f(513553007)) # Powinno zwrócić 21 (5 + 5 + 3 + 3 + 0 + 0)
