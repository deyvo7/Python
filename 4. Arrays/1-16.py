# Tablica zawierająca odległości podróży
distances_traveled = [120, 150, 180, 90, 200, 175, 160]

# Sortowanie danych od najmniejszej do największej wartości
distance_sorted = sorted(distances_traveled)

# Tablica zawierająca dzienne temperatury
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]

# Sortowanie danych w porządku malejącym, od najwyższej do najniższej wartości
temp_sorted = sorted(daily_temperatures, reverse=True)

# Tablica z nazwami plików
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
   "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]

# Sortowanie danych alfabetycznie (w porządku rosnącym)
files_sorted = sorted(file_names)

# Wyświetlanie posortowanych danych
print(distance_sorted, temp_sorted, files_sorted)
