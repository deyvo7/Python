# Define a function f(text) that returns the given text with all characters separated by a dash sign. Example:

# f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
# f("UE") returns "U-E"
# f("x") returns "x"
# f("") returns ""

def f(text):
    # Sprawdzenie, czy tekst jest pusty
    if not text:
        return ""
    
    # Łączenie znaków tekstu za pomocą myślnika
    result = "-".join(text)
    
    return result

# Testy funkcji
print(f("University"))  # "U-n-i-v-e-r-s-i-t-y"
print(f("UE"))          # "U-E"
print(f("x"))           # "x"
print(f(""))            # ""
