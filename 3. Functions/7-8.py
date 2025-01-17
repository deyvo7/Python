# The vending machine accepts 1, 2 and 5 PLN coins. Define a function f(amount_to_pay) that returns the minimum number of coins that
# can be used to pay for the purchased product. Sample result:

# f(23) returns 6
# f(8) returns 3
# f(2) returns 1
# f(0) returns 0

# Funkcja obliczająca minimalną liczbę monet potrzebnych do zapłaty
def f(amount_to_pay):
    # Liczba monet
    coin_count = 0
    
    # Obliczamy liczbę monet 5 PLN i aktualizujemy resztę kwoty
    coin_count += amount_to_pay // 5  # Dzielenie całkowite - ile pełnych 5 PLN można użyć
    amount_to_pay %= 5  # Pozostała kwota po użyciu monet 5 PLN
    
    # Obliczamy liczbę monet 2 PLN i aktualizujemy resztę kwoty
    coin_count += amount_to_pay // 2  # Dzielenie całkowite - ile pełnych 2 PLN można użyć
    amount_to_pay %= 2  # Pozostała kwota po użyciu monet 2 PLN
    
    # Obliczamy liczbę monet 1 PLN i aktualizujemy resztę kwoty
    coin_count += amount_to_pay // 1  # Dzielenie całkowite - ile pełnych 1 PLN można użyć
    amount_to_pay %= 1  # Pozostała kwota po użyciu monet 1 PLN
    
    return coin_count  # Zwracamy minimalną liczbę monet

