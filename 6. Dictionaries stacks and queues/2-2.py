# Lista adresów e-mail, w której niektóre elementy mogą się powtarzać.
emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]

# Użycie funkcji set() do utworzenia zbioru z listy 'emails'.
# Zbiory w Pythonie przechowują jedynie unikalne wartości, więc wszystkie duplikaty zostaną automatycznie usunięte.
unique_emails = set(emails)

# Wyświetlenie zbioru unikalnych adresów e-mail.
# Wynik będzie zawierał tylko unikalne adresy e-mail, ale kolejność może być inna niż w oryginalnej liście,
# ponieważ zbiory w Pythonie nie zachowują kolejności elementów.
print(unique_emails)
