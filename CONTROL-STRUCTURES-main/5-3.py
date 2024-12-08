##
# Prints a greeting
#
##
# Program, który wita użytkownika po wprowadzeniu jego imienia
##

# Zmienna do przechowywania imienia
name = ''  

# Pętla, która będzie działać, dopóki zmienna name nie będzie zawierać wartości
while name == '':  
    name = input('Enter your name: ')  # Prosi użytkownika o podanie imienia

# Po wyjściu z pętli wyświetla powitanie
print(f'Hello {name}')  # Wypisuje powitanie z imieniem
