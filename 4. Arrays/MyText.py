# Funkcja zwraca liczbę słów w tekście
def word_count(text):
    words = text.split()  # Rozdzielamy tekst na słowa
    return len(words)  # Zwracamy liczbę słów

# Funkcja zwraca posortowaną listę słów od najdłuższego do najkrótszego
def words_from_longest(text):
    words = text.split()  # Rozdzielamy tekst na słowa
    words.sort(key=len, reverse=True)  # Sortujemy słowa po długości, malejąco
    return words

# Funkcja zwraca słowa posortowane alfabetycznie
def words_alphabetically(text):
    words = text.split()  # Rozdzielamy tekst na słowa
    words.sort()  # Sortujemy słowa alfabetycznie
    return words
