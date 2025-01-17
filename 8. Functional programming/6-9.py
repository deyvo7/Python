# Słownik, który zawiera miasta i odpowiadające im temperatury w stopniach Celsjusza
temperatures = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# Używamy funkcji filter(), aby znaleźć tylko te miasta, w których temperatura jest większa niż 0
# filter() zwraca iterator, który zawiera tylko te elementy, które spełniają warunek
# Lambda funkcja przyjmuje nazwę miasta i sprawdza, czy jego temperatura jest większa od 0
cities_with_positive_temps = list(filter(lambda city: temperatures[city] > 0, temperatures))

# Wydrukuj wynik, czyli miasta z dodatnimi temperaturami
# Używamy metody "join" do połączenia nazw miast w jeden ciąg tekstowy oddzielony spacjami
print("Cities with positive temperatures:", " ".join(cities_with_positive_temps))
