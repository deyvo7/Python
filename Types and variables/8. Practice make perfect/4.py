###
# A program that prints your height both in cm and in feet and inches.
#
cm = 169
cm_per_inch = 2.54
inches_per_foot = 12
total_inches = cm / cm_per_inch
feet = int(total_inches // inches_per_foot)
inches = int(total_inches % inches_per_foot)
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')