###
# A program that calculates
# how many letters are between two given letters
# A and D (2 letters)
# B and M (10 letters)
# K and K (0 letters)

first = str(input('Enter the first letter: '))
last = str(input('Enter the last letter: '))
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = last_letter_code - first_letter_code - 1
print(f'Between {first} and {last} is {number_of_letters} letters')
