# A sentence is an ordered group of words separated by spaces. Define a function f(sentence)
# that returns a sentence with spaces removed. Sample result:

# f("integrated development environment") returns
# "integrateddevelopmentenvironment"
# f("A programming language is a system of notation for writing
# computer programs") returns
# "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"

def f(sentence):
    # Usuwamy wszystkie spacje z wejściowego ciągu znaków.
    return sentence.replace(" ", "")

# Przykładowe testy funkcji
print(f("integrated development environment"))  # Powinno zwrócić "integrateddevelopmentenvironment"
print(f("A programming language is a system of notation for writing computer programs"))  # Powinno zwrócić "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"
