# Monthly expenses and their corresponding expense categories
# are included in the arrays below.
# Write a program that calculates which expense category was
# the most expensive.

# Kategorie wydatków
categories = ["Food", "Transport", "Rent", "Entertainment"]

# Wydatki odpowiadające poszczególnym kategoriom
expenses = [500, 150, 1000, 200]

# Znajdujemy najwyższy wydatek
max_cost = max(expenses)  # Funkcja max() zwraca największy wydatek

# Znajdujemy indeks, na którym znajduje się najwyższy wydatek
max_index = expenses.index(max_cost)  # index() zwraca indeks największego wydatku w liście

# Korzystając z indeksu, odnajdujemy kategorię odpowiadającą najwyższemu wydatkowi
max_category = categories[max_index]

# Wypisujemy kategorię z najwyższym wydatkiem
print("The most expensive category is:", max_category)
