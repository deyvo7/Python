# Write a program that allows you to convert time in 24-hour format to 12-hour format. 
# The time in 24-hour format (hh:mm) is read from the keyboard. 
# Sample result:

# Enter time (24-hour format): 16:32
# Time in 12-hour format: 4:32pm


# Program konwertujący czas z formatu 24-godzinnego na 12-godzinny

# Pobranie czasu w formacie 24-godzinnym
time_24 = input("Enter time (24-hour format, hh:mm): ")

# Rozdzielenie godziny i minut
hours, minutes = time_24.split(':')
hours = int(hours)  # Konwersja godziny na liczbę całkowitą
minutes = int(minutes)  # Konwersja minut na liczbę całkowitą

# Określenie, czy czas to AM czy PM
if hours < 12:
    period = "am"
else:
    period = "pm"

# Przekształcenie godziny do formatu 12-godzinnego
hours_12 = hours % 12
if hours_12 == 0:  # Godzina 0 w formacie 12-godzinnym to 12
    hours_12 = 12

# Złożenie czasu w formacie 12-godzinnym
time_12 = f"{hours_12}:{minutes:02}{period}"
print(f"Time in 12-hour format: {time_12}")
