# Funkcja maskująca numer karty kredytowej
def hide(card_number):
    # Sprawdza, czy numer karty ma 16 cyfr
    if len(card_number) == 16:
        # Zachowuje pierwsze 2 i ostatnie 4 cyfry, resztę zamienia na gwiazdki
        return card_number[:2] + '*' * 10 + card_number[-4:]
    else:
        return "Invalid card number"
