###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
# Importujemy bibliotekę `keyboard` do obsługi wejścia z klawiatury
import keyboard as key

# Wczytanie danych pracownika z klawiatury
first_name = key.input_string("Enter employee's name: ")  # Wczytanie imienia pracownika
last_name = key.input_string("Enter employee's last name: ")  # Wczytanie nazwiska pracownika
age = key.input_integer("Enter employee's age: ")  # Wczytanie wieku pracownika
salary = key.input_real("Enter employee's salary: ")  # Wczytanie pensji pracownika
is_salary_hidden = key.input_boolean('Hide salary? (y/n): ')  # Wczytanie, czy pensja ma być ukryta (prawda/fałsz)

# Drukowanie danych pracownika
print('DATA RECORD')  # Nagłówek
print('===========')  # Separator
print('Name:', first_name + " " + last_name)  # Drukowanie imienia i nazwiska
print("Age: ", age)  # Drukowanie wieku

# Sprawdzenie, czy pensja ma być ukryta
if is_salary_hidden == False:  # Jeśli pensja nie jest ukryta
    print('Salary: ', salary)  # Drukowanie pensji
elif is_salary_hidden == True:  # Jeśli pensja ma być ukryta
    print("The salary is hidden.")  # Informacja, że pensja jest ukryta
