# Zbiór wszystkich uczniów, którzy są zapisani na zajęcia.
all_students = {"Alice", "John", "Sara", "Bob"}

# Zbiór uczniów, którzy faktycznie pojawili się na zajęciach.
attended_students = {"Alice", "Bob"}

# Obliczamy różnicę między wszystkimi uczniami a uczniami, którzy się pojawili.
# Używamy operatora '-' do obliczenia zbioru uczniów, którzy są nieobecni.
absent_students = all_students - attended_students  # Różnica zbiorów

# Wyświetlamy uczniów, którzy są nieobecni.
print(absent_students)
