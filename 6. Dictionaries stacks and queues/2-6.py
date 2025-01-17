# Zbiór wymaganych uprawnień, które są potrzebne do wykonania danej akcji.
required_permissions = {"read", "write", "execute"}

# Zbiór uprawnień, które użytkownik już posiada.
user_permissions = {"read", "write"}

# Sprawdzamy, czy wszystkie wymagane uprawnienia są obecne w zbiorze uprawnień użytkownika.
# Metoda 'issubset()' sprawdza, czy zbiór 'required_permissions' jest podzbiorem zbioru 'user_permissions'.
# Oznacza to, że sprawdzamy, czy wszystkie uprawnienia wymagane są dostępne u użytkownika.
has_permissions = required_permissions.issubset(user_permissions)  # Sprawdzanie podzbioru

# Wynik będzie False, ponieważ użytkownik nie ma uprawnienia "execute".
print(has_permissions)  # Zwróci False, ponieważ "execute" jest brakujące.
