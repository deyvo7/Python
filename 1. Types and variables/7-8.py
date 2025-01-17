###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print(f"The result of the first die roll: {dice_roll_1}")
print(f"The result of the second die roll: {dice_roll_2}")
print(f"The result of the third die roll: {dice_roll_3}")
print(f"The sum of the dice rolled: {total}")