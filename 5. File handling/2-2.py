###
# Write a program that writes a list of the Seven Wonders of the World
# to a text file, in alphabetical order, with each name on a separate line.
# Then, open the created file in the editor and check if its contents 
# match the task.

# Lista siedmiu cudów świata
seven_wonders = [
   "Great Wall of China",   
   "Petra",                 
   "Christ the Redeemer",   
   "Machu Picchu",          
   "Chichen Itza",          
   "Roman Colosseum",       
   "Taj Mahal"              
]

# Nazwa pliku, do którego będziemy zapisywać dane
file_name = 'seven_wonders.txt'

# Sortowanie listy cudów świata w porządku alfabetycznym
seven_wonders_sorted = sorted(seven_wonders)

# Otwieramy plik do zapisu ('w' - write - do zapisu)
with open(file_name, 'w') as file:
   # Dla każdego elementu w posortowanej liście
   for item in seven_wonders_sorted:
      # Zapisujemy nazwę cudu do pliku, każdą w nowej linii
      file.write(f"{item}\n")

# Program zakończony. Zawartość została zapisana do pliku 'seven_wonders.txt'
