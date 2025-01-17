###
# Reads from file, line by line
#Modify the program print_countries.py so that the printed list 
# of countries is numbered. Sample result:

# 1. Poland, Warsaw, 38265000
# 2. Germany, Berlin, 83240000
# 3. France, Paris, 67850000
# 4. Japan, Tokyo, 125800000
# 5. Canada, Ottawa, 38250000

with open('countries.txt', 'r') as file:
    number = 1
    for line in file:
        snumber = str(number) + "."
        print(snumber, line, end="" )
        number = number +1 
