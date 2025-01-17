# Write a program that saves data of employees employed in the position of
# 'Software Engineer' to the file 'software_engineer.txt'. 
# Data is available in the file 'it_company.csv'.

# Hint: Read employee data line by line.
# For each line, check if it contains the name of the indicated position.
# If so, write this line to the output file.



# Program, który zapisuje do pliku 'software_engineer.txt' dane pracowników
# zatrudnionych na stanowisku 'Software Engineer' z pliku 'it_company.csv'.

# Nazwy plików
employees_file = 'it_company.csv'  # Plik źródłowy zawierający dane pracowników
position_file = 'software_engineer.txt'  # Plik docelowy, w którym zapisujemy dane

# Stanowisko
job_title = 'Software Engineer'

# Otwieramy plik z danymi pracowników w trybie odczytu
with open(employees_file, "r") as employees_txt:
    # Odczytujemy całą zawartość pliku i dzielimy na linie
    employees = employees_txt.read()
    employees_lines = employees.splitlines()
    
    # Otwieramy plik docelowy w trybie zapisu
    with open(position_file, "w") as position:
        # Iterujemy przez każdą linię z pliku źródłowego
        for line in employees_lines:
            # Sprawdzamy, czy w linii znajduje się stanowisko 'Software Engineer'
            if job_title in line:
                # Jeśli tak, zapisujemy tę linię do pliku docelowego
                position.write(f"{line}\n")



