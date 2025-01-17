###
# A program that checks whether the number entered
# from the keyboard is even.
# A number is even if the remainder when divided by 2 is 0.
# What operator do you need to use to calculate
# the remainder of division?
# 24, 8, 31, 5

number = int(input('Enter number: '))
even = (number % 2 == 0)
print(f'Number is even: {even}')