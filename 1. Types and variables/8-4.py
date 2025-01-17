###
# A program that prints your height both in cm and in feet and inches.
#

cm = 183
total_inches = cm * 0.393701

feet = int(total_inches // 12)  
inches = total_inches % 12       

print(f'I am {cm}cm tall, {feet} feet and {round(inches, 1)} inches')