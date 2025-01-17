import queue

# Tworzymy kolejkę odwiedzonych stron internetowych (LifoQueue - Last In First Out)
visited_websites = queue.LifoQueue()

# Dodajemy kilka wcześniej odwiedzonych stron internetowych
visited_websites.put('instagram.com')
visited_websites.put('uek.krakow.pl')
visited_websites.put('microsoft.com')

while True:
    # Pobieramy nazwę strony od użytkownika
    website = input('Enter website name (0 for back): ')

    # Jeśli użytkownik wpisze '0', wracamy do poprzednio odwiedzanej strony
    if website == '0':
        if visited_websites.empty():  # Jeśli nie ma żadnych odwiedzonych stron w historii
            break  # Kończymy program, bo brak stron do powrotu
        else:
            print('<-- Going back to a previously visited website')  # Komunikat, że wracamy do poprzedniej strony
            website = visited_websites.get()  # Usuwamy stronę z kolejki i wyświetlamy ją jako stronę aktualnie odwiedzaną
    elif website != "":  # Jeśli użytkownik nie poda pustej nazwy strony
        visited_websites.put(website)  # Dodajemy nową stronę do kolejki odwiedzonych stron

    # Wyświetlamy aktualnie odwiedzaną stronę
    print('You are currently viewing:', website)
