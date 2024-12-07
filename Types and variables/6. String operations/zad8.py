first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = abs(last_letter_code - first_letter_code) - 1
print(f'Between {first} and {last} is {number_of_letters} letters')