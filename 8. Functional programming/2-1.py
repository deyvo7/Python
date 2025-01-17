# Definiujemy funkcję min_pts, która przyjmuje argument limit (minimalna liczba punktów)
# Funkcja min_pts zwraca inną funkcję check, która sprawdza, czy liczba punktów jest większa lub równa limitowi.
# Funkcja check przyjmuje jeden argument pts (liczba punktów) i zwraca True, jeśli liczba punktów jest większa
# lub równa limitowi, w przeciwnym razie zwraca False.
def min_pts(limit):
   def check(pts):
      if pts >= limit:  # Sprawdzamy, czy punkty są większe lub równe limitowi
         return True
      return False
   return check  # Zwracamy funkcję check

# Testujemy funkcję min_pts
print("=== MIN 50 PTS TO PASS ===")
# Tworzymy funkcję oceny, gdzie limit punktów to 50
assess_test = min_pts(50)
# Sprawdzamy, czy punkty 52 i 39 spełniają warunki
print(f"52 pts -> {assess_test(52)}")  # Powinno zwrócić True, bo 52 >= 50
print(f"39 pts -> {assess_test(39)}")  # Powinno zwrócić False, bo 39 < 50

print("=== MIN 60 PTS TO PASS ===")
# Tworzymy funkcję oceny, gdzie limit punktów to 60
assess_test = min_pts(60)
# Sprawdzamy, czy punkty 52 i 39 spełniają warunki
print(f"52 pts -> {assess_test(52)}")  # Powinno zwrócić False, bo 52 < 60
print(f"39 pts -> {assess_test(39)}")  # Powinno zwrócić False, bo 39 < 60
