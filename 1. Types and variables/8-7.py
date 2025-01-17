# Write a program that reads an integer number from the keyboard and prints that value as a binary and hexadecimal number.
# To convert a decimal number to binary or hexadecimal value, use the available Python functions. Sample result:
# Enter number: 125
# Binary number: 0b1111101
# Hexadecimal number: 0x7d

number = int(input("Enter number: "))

binary_number = bin(number)
hexadecimal_number = hex(number)

print(f"Binary number: {binary_number}")
print(f"Hexadecimal number: {hexadecimal_number}")