# A text contains any number of words. Define a function f(name) that returns the acronym (first letters of all words). Sample result:

# f("Internet of Things") returns "IoT"
# f("For Your Information") returns "FYI"
# f("Python") returns "P"


def f(name):
    # Inicjalizujemy pusty ciąg znaków, który będzie przechowywał akronim
    acronym = ""
    
    # Dzielimy tekst na listę słów przy użyciu metody split()
    words = name.split()
    
    # Iterujemy po każdym słowie w liście
    for word in words:
        # Sprawdzamy, czy słowo nie jest puste
        if word:
            # Dodajemy pierwszą literę słowa zamienioną na wielką literę do akronimu
            acronym += word[0].upper()
    
    # Zwracamy końcowy akronim
    return acronym

# Testowanie funkcji z przykładowymi danymi
print(f("Internet of Things"))  # Powinno zwrócić "IoT"
print(f("For Your Information"))  # Powinno zwrócić "FYI"
print(f("Python"))  # Powinno zwrócić "P"
print(f("Hello World and Universe"))  # Powinno zwrócić "HWU"
print(f("The quick brown fox jumps over the lazy dog"))  # Powinno zwrócić "Tqbfjotld"
