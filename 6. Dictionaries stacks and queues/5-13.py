# Funkcja do obliczania wyrażeń w odwrotnej notacji polskiej (RPN)
def calculate_rpn(expression):
    stack = []  # Tworzymy pusty stos
    
    # Iterujemy po każdym elemencie w wyrażeniu
    for token in expression.split():
        if token.isdigit():  # Jeśli token to liczba
            stack.append(int(token))  # Dodajemy liczbę do stosu
        elif token in '+-*/':  # Jeśli token to operator
            b = stack.pop()  # Zdejmujemy dwa elementy ze stosu
            a = stack.pop()
            if token == '+':  # Dodajemy
                stack.append(a + b)
            elif token == '-':  # Odejmujemy
                stack.append(a - b)
            elif token == '*':  # Mnożymy
                stack.append(a * b)
            elif token == '/':  # Dzielimy
                stack.append(a / b)
        elif token == '=':  # Jeśli token to znak równości
            result = stack.pop()  # Ostatni wynik na stosie to wynik wyrażenia
            return result  # Zwracamy wynik

    return None  # Zwracamy None, jeśli coś poszło nie tak

# Program główny
while True:
    # Pobieramy wyrażenie w odwrotnej notacji polskiej
    rpn_expression = input("Wpisz wyrażenie RPN (lub 'exit' aby zakończyć): ")
    
    if rpn_expression.lower() == "exit":
        break  # Zakończenie programu
    
    result = calculate_rpn(rpn_expression)
    
    if result is not None:
        print(f"Wynik wyrażenia: {result}")  # Wyświetlamy wynik obliczeń
    else:
        print("Błąd w wyrażeniu RPN.")
