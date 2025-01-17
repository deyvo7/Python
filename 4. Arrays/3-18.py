# Create a module MyArrays containing functions to operate on an array of numbers:

# A function that returns the second largest element in an array
# A function that returns the difference between the largest and smallest values in an array
# A function that returns the median of numbers in an array.
# A function that returns a two-element array containing the smallest and largest values in an array
# A function that returns array elements as a string, separated by the minus sign

# Sample result:

# Numbers: 7,3,8,5,2
# Second largest number: 7 
# Median: 5
# Smallest and largest number: 2,8
# Numbers as a string: 7-3-8-5-2

# Importujemy moduł MyArrays
import MyArrays

# Tablica liczb
numbers = [7, 3, 8, 5, 2]

# Wyświetlamy wyniki
print("Numbers:", MyArrays.array_to_string(numbers))
print("Second largest number:", MyArrays.second_largest(numbers))
print("Median:", MyArrays.median(numbers))
print("Smallest and largest number:", ', '.join(map(str, MyArrays.smallest_largest(numbers))))
