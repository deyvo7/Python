# EAN-13 (European Article Number) is a barcode for marking goods. The first 3 digits (590) usually indicate goods manufactured in Poland.
# Write a program that checks whether the EAN-13 number entered from the keyboard consists of exactly 13 characters (digits).
# Print a message if the number is correct.
# Additionally, only when the article number is correct, print a message when the product was manufactured in Poland.
# Sample result:

# Enter EAN-13 article number: 5901230094938
# Article number is correct
# Article manufactured in Poland

# EAN-13 (European Article Number) to kod kreskowy do oznaczania towarów
# Pierwsze trzy cyfry (590) zazwyczaj wskazują na towary wyprodukowane w Polsce
# Program sprawdza, czy numer EAN-13 składa się dokładnie z 13 cyfr (znaków)

ean13 = input("Enter the EAN-13 article number: ")  # Pobranie numeru EAN-13 od użytkownika

# Sprawdzenie, czy numer ma dokładnie 13 znaków
if len(ean13) == 13:
    print("The article number is correct")  # Jeśli numer ma 13 znaków, jest poprawny
    
    # Sprawdzenie, czy numer zaczyna się od "590" (co wskazuje na Polskę)
    if ean13[:3] == "590":
        print("Article manufactured in Poland")  # Produkt wyprodukowany w Polsce
else:
    print("The article number is incorrect")  # Jeśli numer nie ma 13 znaków, jest niepoprawny
