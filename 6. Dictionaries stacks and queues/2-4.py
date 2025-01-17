# Zbiór otrzymanych adresów e-mail.
emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}

# Zbiór adresów e-mail znajdujących się na liście spamu.
spam_list = {"spam1@example.com", "spam2@example.com"}

# Obliczamy przecięcie obu zbiorów, aby znaleźć e-maile, które znajdują się zarówno w zestawie otrzymanych e-maili,
# jak i na liście spamu. Operator '&' wykonuje operację przecięcia zbiorów.
spam_emails = emails_received & spam_list  # Przecięcie zbiorów

# Wyświetlamy adresy e-mail, które są oznaczone jako spam.
print("Spam emails:", spam_emails)
