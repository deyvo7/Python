# Funkcja min_pts zwraca funkcję, która sprawdza, czy liczba punktów jest większa lub równa określonemu limitowi
def min_pts(limit):
    return lambda pts: pts >= limit  # Zwracamy funkcję anonimową, która porównuje punktację z limitem

# Lista wyników uczniów
scores = [37, 51, 44, 23, 78, 92, 39, 84, 83, 51]

# Min 70 punktów - używamy funkcji min_pts(70), aby stworzyć funkcję sprawdzającą, czy wynik jest większy lub równy 70
min_70_pts = list(filter(min_pts(70), scores))  # Filtrujemy listę wyników, zachowując tylko te większe lub równe 70
print(f"Min 70 pts: {min_70_pts}")  # Wypisujemy wyniki, które spełniają ten warunek

# Min 40 punktów - podobnie jak wcześniej, ale z limitem 40
min_40_pts = list(filter(min_pts(40), scores))  # Filtrujemy listę wyników, zachowując tylko te większe lub równe 40
print(f"Min 40 pts: {min_40_pts}")  # Wypisujemy wyniki, które spełniają ten warunek

# Min 30 punktów - tym razem z limitem 30
min_30_pts = list(filter(min_pts(30), scores))  # Filtrujemy listę wyników, zachowując tylko te większe lub równe 30
print(f"Min 30 pts: {min_30_pts}")  # Wypisujemy wyniki, które spełniają ten warunek
