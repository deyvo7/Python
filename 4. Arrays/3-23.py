# A variable contains text:
# An apple a day keeps the doctor away

# Create a module MyText, containing:

# A function that returns the number of words in the text
# A function that returns an ordered array of words, from longest to shortest
# A function that returns an alphabetically ordered array of words
# Then, write a program, call the functions and print results.

# Sample result:
# Text: An apple a day keeps the doctor away
# Number of words: 8
# Words from the longest: doctor,apple,…
# Words ordered alphabetically: a,An,apple,away,…

import MyText  # Importujemy moduł MyText

# Tekst do analizy
text = "An apple a day keeps the doctor away"

# Wywołanie funkcji z modułu MyText
word_count_result = MyText.word_count(text)  # Liczba słów w tekście
longest_words_result = MyText.words_from_longest(text)  # Słowa posortowane od najdłuższego do najkrótszego
alphabetical_words_result = MyText.words_alphabetically(text)  # Słowa posortowane alfabetycznie

# Drukowanie wyników
print("Text:", text)
print("Number of words:", word_count_result)
print("Words from the longest:", ', '.join(longest_words_result))
print("Words ordered alphabetically:", ', '.join(alphabetical_words_result))
