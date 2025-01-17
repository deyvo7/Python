# Definiujemy akapit
paragraph = "cat dog mouse cat rat cat mouse"

# Dzielimy akapit na poszczególne słowa
words = paragraph.split()

# Tworzymy pusty słownik, który będzie przechowywał liczbę wystąpień każdego słowa
word_count = {}

# Iterujemy przez każde słowo w liście
for word in words:
    # Jeśli słowo już występuje w słowniku, zwiększamy jego licznik o 1
    if word in word_count:
        word_count[word] += 1
    # Jeśli słowo nie występuje w słowniku, dodajemy je z licznikiem równym 1
    else:
        word_count[word] = 1

# Wyświetlamy liczbę wystąpień każdego słowa
for word, count in word_count.items():
    print(f"'{word}': {count}")
