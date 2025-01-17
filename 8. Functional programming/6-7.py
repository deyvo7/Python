# Oceny czterech zawodników w skokach narciarskich
ratings = [
    (17, 15, 16, 17, 15),  # Oceny pierwszego zawodnika
    (16, 18, 19, 17, 19),  # Oceny drugiego zawodnika
    (19, 15, 15, 19, 18),  # Oceny trzeciego zawodnika
    (18, 17, 19, 15, 16)   # Oceny czwartego zawodnika
]

# Funkcja do obliczania końcowego wyniku zawodnika
def calculate_score(scores):
    # Usuwamy najwyższą i najniższą ocenę, a potem sumujemy pozostałe trzy
    return sum(scores) - max(scores) - min(scores)

# Używamy funkcji map(), aby obliczyć wynik dla każdego zawodnika
total_scores = list(map(calculate_score, ratings))

# Wyświetlamy końcowe wyniki
print(total_scores)
