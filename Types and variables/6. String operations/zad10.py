###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title in capital letters: ', movie.upper())

# print title in small letters
print('Title in small letters: ', movie.lower())
# print how many times the vowel "e" appears in the title
print('"e" appears in the title: ', movie.count('e'))

# print where in the text is the word "Lord"
print('Position of the word "Lord": ', movie.find('Lord'))                       

# print where in the text is the word "dragon"
print('Position of the word "dragon": ', movie.find('dragon'))