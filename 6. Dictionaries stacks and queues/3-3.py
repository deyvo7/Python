import queue

# Wyrażenia do sprawdzenia
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # nawiasy są poprawne
expression2 = "[(2+3]/4)"                # nawiasy są niepoprawne
expression3 = "(2-3*4+(5/6)"             # nawiasy są niepoprawne

# Funkcja sprawdzająca, czy nawiasy w wyrażeniu są poprawnie zbalansowane
def brackets_ok(expression):
    stack = []  # Używamy listy jako stosu, by przechowywać otwarte nawiasy

    # Iterujemy przez każdy znak w wyrażeniu
    for char in expression:
        # Jeśli napotkamy nawias otwierający, dodajemy go na stos
        if char in "({[":
            stack.append(char)
        # Jeśli napotkamy nawias zamykający, sprawdzamy, czy pasuje do nawiasu otwierającego
        elif char in ")}]":
            # Jeśli stos jest pusty, oznacza to, że brakuje nawiasu otwierającego
            if not stack:
                return False
            top = stack.pop()  # Usuwamy nawias otwierający z góry stosu
            # Sprawdzamy, czy nawias zamykający pasuje do nawiasu otwierającego
            if char == ")" and top != "(":
                return False
            elif char == "}" and top != "{":
                return False
            elif char == "]" and top != "[":
                return False

    # Jeśli po przejściu całego wyrażenia stos nie jest pusty, oznacza to, że brakuje nawiasów zamykających
    return not stack

# Sprawdzamy poprawność nawiasów w każdym wyrażeniu
if brackets_ok(expression1):
    print(f"The brackets in {expression1} are correct.")
else:
    print(f"The brackets in {expression1} are not correct.")

if brackets_ok(expression2):
    print(f"The brackets in {expression2} are correct.")
else:
    print(f"The brackets in {expression2} are not correct.")

if brackets_ok(expression3):
    print(f"The brackets in {expression3} are correct.")
else:
    print(f"The brackets in {expression3} are not correct.")
