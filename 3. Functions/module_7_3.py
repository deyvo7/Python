# Funkcja zwraca nazwę miesiąca na podstawie jego numeru (1-12)
def month(n):
    # Lista nazw miesięcy (indeksowanie od 0 do 11)
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    
    # Sprawdzenie, czy numer miesiąca jest poprawny
    if 1 <= n <= 12:
        # Zwracanie nazwy miesiąca, uwzględniając indeksowanie od 0
        return months[n - 1]
    else:
        # Zwracanie komunikatu o błędzie, jeśli numer miesiąca jest nieprawidłowy
        return "Invalid month number"
