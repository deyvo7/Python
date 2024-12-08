# A valid password should consist of at least six characters and each character appears only once in the password.
#  Define a function f(password) that returns True if the password is correct or False otherwise. Sample result:

# f("ax15") returns False
# f("book123") returns False
# f("A2water3") returns True
# f("qwerty") returns True
# f("") returns False

def f(password):
    # Sprawdzanie, czy długość hasła jest co najmniej 6 znaków
    if len(password) < 6:
        return False

    # Sprawdzanie, czy wszystkie znaki są unikalne
    if len(password) != len(set(password)):
        return False

    # Jeśli hasło spełnia oba warunki, zwracamy True
    return True

# Testowanie funkcji z przykładowymi danymi
print(f("ax15"))       # Powinno zwrócić False, ponieważ ma mniej niż 6 znaków
print(f("book123"))    # Powinno zwrócić False, ponieważ 'o' występuje więcej niż raz
print(f("A2water3"))   # Powinno zwrócić True, ponieważ ma co najmniej 6 znaków i wszystkie znaki są unikalne
print(f("qwerty"))    # Powinno zwrócić True, ponieważ ma co najmniej 6 znaków i wszystkie znaki są unikalne
print(f(""))           # Powinno zwrócić False, ponieważ jest puste
