# Lista kontaktów A (zebrane adresy e-mail z pierwszej bazy danych).
contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}

# Lista kontaktów B (zebrane adresy e-mail z drugiej bazy danych).
contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}

# Łączenie obu list kontaktów i usuwanie duplikatów.
# Operator '|' wykonuje operację sumy zbiorów (union), co powoduje połączenie obu zbiorów,
# przy czym duplikaty są automatycznie usuwane, ponieważ zbiory przechowują tylko unikalne elementy.
merged_contacts = contacts_A | contacts_B  # Suma zbiorów

# Wyświetlamy połączoną listę kontaktów, w której nie ma duplikatów.
print("Merged contacts:", merged_contacts)
