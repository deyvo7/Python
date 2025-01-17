###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print("The title in capital letters: ", movie.upper())

# print title in small letters
print("The title in small letters: ", movie.lower())

# print how many times the vowel "e" appears in the title
print("Times the vowel \"e\" appears in the title: ", movie.count("e"))

# print where in the text is the word "Lord"
print("The word \"Lord\" starts with the index number: ", movie.find("Lord"))

# print where in the text is the word "dragon"
dragon = movie.find("dragon")
if dragon != -1:
    print("The word \"dragon\" starts with the index number: ", movie.find("dragon"))
else: 
    print("The word \"dragon\" doesn't appear in the text.")