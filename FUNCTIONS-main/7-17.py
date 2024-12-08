# A palindrome is an expression that sounds the same when read backwards. 
# Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise. Sample result:

# f("radar") returns True
# f("12-11-21") returns True
# f("book") returns False

def f(palindrome):
    # Konwertujemy wejściowy ciąg na małe litery, aby porównanie było nieczułe na wielkość liter.
    cleaned_palindrome = palindrome.lower()

    # Sprawdzamy, czy ciąg jest palindromem, porównując znaki od początku i od końca.
    start = 0  # Początkowy indeks
    end = len(cleaned_palindrome) - 1  # Końcowy indeks

    # Pętla, która działa, dopóki start jest mniejsze od end
    while start < end:
        # Sprawdzamy, czy znaki na początku i na końcu są takie same
        if cleaned_palindrome[start] != cleaned_palindrome[end]:
            # Jeśli znaki się różnią, ciąg nie jest palindromem.
            return False
        # Przesuwamy wskaźnik start do przodu i end do tyłu
        start += 1
        end -= 1
    
    # Jeśli wszystkie pary znaków pasują, zwracamy True - ciąg jest palindromem.
    return True

# Przykładowe testy funkcji
print(f("radar"))      # Powinno zwrócić True, bo "radar" jest palindromem.
print(f("ABBA"))       # Powinno zwrócić True, bo "ABBA" jest palindromem.
print(f("book"))       # Powinno zwrócić False, bo "book" nie jest palindromem.
