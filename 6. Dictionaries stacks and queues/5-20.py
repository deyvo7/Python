# Importujemy moduł json, który pozwala na operacje z plikami w formacie JSON
import json

# Definiujemy dane, które chcemy zapisać do pliku JSON
data = {
   "patient_record": {
      "patient_id": "P001234",  # Identyfikator pacjenta
      "first_name": "John",  # Imię pacjenta
      "last_name": "Doe",  # Nazwisko pacjenta
      "date_of_birth": "1985-05-15",  # Data urodzenia pacjenta
      "gender": "Male",  # Płeć pacjenta
      "contact_info": {  # Dane kontaktowe pacjenta
            "phone_number": "+1-555-123-4567",  # Numer telefonu
            "email": "johndoe@example.com",  # Email pacjenta
            "address": {  # Adres pacjenta
               "street": "123 Main St",  # Ulica
               "city": "New York",  # Miasto
               "state": "NY",  # Stan
               "postal_code": "10001",  # Kod pocztowy
               "country": "USA"  # Kraj
            }
      },
      "medical_history": {  # Historia medyczna pacjenta
            "allergies": ["Penicillin", "Peanuts"],  # Alergie pacjenta
            "current_medications": ["Lisinopril 10mg", "Metformin 500mg"],  # Obecne leki
            "past_illnesses": ["Hypertension", "Type 2 Diabetes"],  # Przeszłe choroby
            "surgeries": [  # Operacje, które pacjent przeszedł
               {
                  "surgery_type": "Appendectomy",  # Rodzaj operacji
                  "date": "2015-08-20"  # Data operacji
               }
            ]
      }
   }
}

# Określamy nazwę pliku, do którego zapiszemy dane
file_name = "patient.json"

# Otwieramy plik w trybie zapisu ('w'), jeżeli plik nie istnieje, zostanie utworzony
# Używamy json.dump() do zapisania danych w formacie JSON
# Argument indent=4 sprawia, że zapisany JSON będzie sformatowany (z wcięciami), co popraw
