import queue  # Importujemy moduł do pracy z kolejkami

# Tworzymy pustą kolejkę, która będzie przechowywać pliki do wydruku
files_to_print = queue.Queue()

# Rozpoczynamy pętlę programu, która pozwala na wybór opcji
while True:
    # Wyświetlamy menu opcji dla użytkownika
    print('1. Add file to print')  # Opcja dodania pliku do kolejki
    print('2. Print file')        # Opcja wydrukowania pliku
    print('0. Quit')               # Opcja zakończenia programu
    menu = input('Select an option: ')  # Pobieramy wybór od użytkownika

    # Jeśli użytkownik wybierze opcję 1, dodajemy plik do kolejki
    if menu == '1':
        file_name = input('Enter file name to print: ')  # Pobieramy nazwę pliku
        files_to_print.put(file_name)  # Dodajemy plik do kolejki na końcu

    # Jeśli użytkownik wybierze opcję 2, próbujemy wydrukować plik z kolejki
    elif menu == '2':
        # Sprawdzamy, czy w kolejce znajdują się jakiekolwiek pliki
        if not files_to_print.empty():
            # Usuwamy plik z początku kolejki i "drukujemy" go
            file_to_print = files_to_print.get()  
            print(f'File {file_to_print} is currently being printed. Please wait!')
        else:
            # Jeśli kolejka jest pusta, informujemy użytkownika
            print('There are no files to print!')

    # Jeśli użytkownik wybierze opcję 0, kończymy działanie programu
    elif menu == '0':
        break  # Zakończenie pętli, co kończy program
