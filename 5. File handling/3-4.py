# A file report.txt contains an email with shopping report.
# Write a program that calculates the total value of money spent.


import re  # Importujemy moduł do pracy z wyrażeniami regularnymi

# Nazwa pliku z raportem zakupów
email_file = 'report.txt'

# Odczytujemy zawartość pliku
with open(email_file, "r", encoding="utf-8") as email_content:
    email = email_content.read()  # Cała zawartość pliku jest zapisywana do zmiennej 'email'

# Wyrażenie regularne do wyszukiwania kwot pieniędzy
# Szukamy wzorca "€" (symbol euro), opcjonalnej spacji (\s?) i liczby (co najmniej jedna cyfra)
pattern = r"€\s?\d+"  # r"€\s?\d+" oznacza: euro symbol, opcjonalna spacja, jedna lub więcej cyfr

# Wyjaśnienie regex:
# 1. "€" - szuka dosłownego symbolu euro.
# 2. "\s?" - szuka opcjonalnej spacji. "\s" oznacza dowolny biały znak (spacja, tabulator, nowa linia),
# a "?" oznacza, że ten znak może występować 0 lub 1 raz. Czyli możemy mieć "€123" lub "€ 123".
# 3. "\d+" - szuka jednej lub więcej cyfr. "\d" oznacza dowolną cyfrę (0-9), a "+" oznacza,
# że musi występować przynajmniej jedna cyfra. To odpowiada liczbie w formacie np. "€123", "€ 1", "€999", itp.

# Używamy funkcji findall, aby znaleźć wszystkie pasujące ciągi znaków w pliku
# findall() zwróci listę wszystkich znalezionych kwot
amounts = re.findall(pattern, email)

# Zmienna do przechowywania całkowitej sumy wydanych pieniędzy
total = 0

# Iterujemy po każdej znalezionej kwocie
for amount in amounts:
    # Usuwamy symbol "€" i ewentualne spacje, a następnie zamieniamy na liczbę całkowitą
    number = int(amount.replace("€", "").strip())  # replace("€", "") usuwa znak euro
    total += number  # Dodajemy każdą kwotę do całkowitej sumy

# Wyświetlamy łączną sumę wydanych pieniędzy
print(total)
