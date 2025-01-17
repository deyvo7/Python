import queue

# Funkcja do obsługi klientów
def serve_customers():
    # Tworzymy pustą kolejkę
    customer_queue = queue.Queue()

    ticket_number = 1  # Początkowy numer biletu

    while True:
        # Menu z opcjami
        print("\n--- Menu ---")
        print("1. Nowy klient")
        print("2. Obsłuż klienta")
        print("0. Zakończ")
        
        choice = input("Wybierz opcję: ")
        
        if choice == '1':
            # Przyjmowanie nowego klienta i przypisanie numeru biletu
            print(f"Nowy klient otrzymał bilet numer: {ticket_number}")
            customer_queue.put(ticket_number)  # Dodajemy klienta do kolejki
            ticket_number += 1  # Zwiększamy numer biletu dla następnego klienta

        elif choice == '2':
            # Obsługuje klienta z przodu kolejki
            if not customer_queue.empty():
                served_customer = customer_queue.get()  # Pobieramy klienta z przodu kolejki
                print(f"Klient z biletem numer {served_customer} został obsłużony.")
            else:
                print("Brak klientów do obsłużenia.")

        elif choice == '0':
            # Zakończenie programu
            print("Zakończono działanie programu.")
            break
        else:
            print("Niepoprawna opcja. Spróbuj ponownie.")

# Wywołanie funkcji obsługi klientów
serve_customers()
