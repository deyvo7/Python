# Słownik zawierający tłumaczenia słów z angielskiego na polski
translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

# Pobieramy od użytkownika słowo w języku angielskim
word_to_translate = input('Enter a word in English: ').lower()  # Zamieniamy na małe litery, aby nie było problemów z wielkością liter

# Sprawdzamy, czy w słowniku istnieje tłumaczenie dla podanego słowa
if word_to_translate in translations:
    # Jeśli słowo znajduje się w słowniku, wyświetlamy jego tłumaczenie
    print(f'Translation: {translations[word_to_translate]}')
else:
    # Jeśli słowo nie istnieje w słowniku, informujemy użytkownika
    print('Translation not available.')
