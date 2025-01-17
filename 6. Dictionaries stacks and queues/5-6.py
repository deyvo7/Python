# Słownik z podstawowymi danymi
basic_data = {
   "name": "Barbara",
   "age": 21
}

# Słownik z dodatkowymi danymi
advanced_data = {
   "status": "student",
   "married": False,
   "interest": ["reading", "swimming"]
}

# Łączenie obu słowników w jeden nowy słownik 'person'
person = {**basic_data, **advanced_data}

# Wyświetlanie zawartości słownika 'person'
print(person)
