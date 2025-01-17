# Write a program that allows you to create a shopping list.
# The program takes user input from the keyboard until the user enters 0.
# Each value taken is saved to a text file 'shopping_list.txt'.

# Hint: Open the file in append mode using the 'a' (append) parameter in the open() function.

###
# Creates a shopping list based on product names
# entered from the keyboard.
#

# Program umożliwiający tworzenie listy zakupów na podstawie nazw produktów wprowadzonych przez użytkownika

# Nazwa pliku z listą zakupów
shopping_list = 'shopping_list.txt'

# Funkcja do dodawania produktu do listy zakupów
def add_product(file_name, product_name):
   # Otwieramy plik w trybie do dopisywania (append), aby dodać produkt na końcu listy
   with open(file_name, 'a') as shopping_list_file:
      shopping_list_file.write(f"{product_name}\n")

# Zmienna do przechowywania nazwy produktu
product = ""

# Pętla do wprowadzania produktów z klawiatury
while product != "0":
   # Pobieranie nazwy produktu od użytkownika
   product = input('Enter product name (0 stops): ')
   
   # Warunek kończący program, jeśli użytkownik wpisze "0"
   if product == '0':
      break  # Zatrzymuje wprowadzanie produktów, kończąc pętlę
   else:
      # Jeśli produkt nie jest "0", dodajemy go do listy
      add_product(shopping_list, product)

print("Shopping list saved to shopping_list.txt")
