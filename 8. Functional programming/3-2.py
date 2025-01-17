# Definiujemy zdanie
sentence = 'I completely agree with you'

# Używamy funkcji split(), aby podzielić tekst na słowa.
# Następnie używamy funkcji map(), aby obliczyć długość każdego słowa.
# Funkcja lambda zwraca długość słowa (len(word)).
# Funkcja map() stosuje lambda do każdego słowa w liście, a wynik konwertujemy na listę za pomocą list().
result = list(map(lambda word: len(word), sentence.split()))

# Wypisujemy wynik
print(f"Text: {sentence}")
print("No. of letters in words: ", result)
