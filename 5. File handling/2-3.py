# Write a program that copies the contents of the file 'healthy_lifestyle.txt' to the file copy_healthy_lifestyle.txt'.

# Hint: Read the entire contents of the original file and write them to the target file (copy).

###
# Makes a copy of a text file
#

# Program do kopiowania zawartości pliku 'healthy_lifestyle.txt' do pliku 'copy_healthy_lifestyle.txt'

# Nazwy plików
original_file = 'healthy_lifestyle.txt'  # Plik źródłowy, z którego kopiujemy
target_file = 'copy_healthy_lifestyle.txt'  # Plik docelowy, do którego zapisujemy kopię

# Otwieramy plik źródłowy w trybie odczytu ('r')
with open(original_file, "r") as original:
    # Odczytujemy całą zawartość pliku i zapisujemy ją w zmiennej 'content'
    content = original.read()

# Otwieramy plik docelowy w trybie zapisu ('w')
with open(target_file, "w") as target:
    # Zapisujemy zawartość z pliku źródłowego do pliku docelowego
    target.write(content)

# Program zakończony. Zawartość pliku 'healthy_lifestyle.txt' została skopiowana do 'copy_healthy_lifestyle.txt'
