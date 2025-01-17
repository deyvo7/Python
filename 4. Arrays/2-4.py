# The data below contains weekly meal plan. Write a program that prints the weekly meal plan along with the day name as in the example below.

# WEEKLY MEAL PLAN
# (Breakfast, Lunch, Dinner)
# ==========================
# Monday: Oatmeal, Grilled Checken Salad, Spaghetti
# Tuesday: ...
# Wednesday: ...

# Plan posiłków na każdy dzień tygodnia (śniadanie, obiad, kolacja)
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],  # Poniedziałek
   ["Pancakes", "Sandwich", "Steak"],  # Wtorek
   ["Smoothie", "Chicken Wrap", "Salmon"],  # Środa
   ["Eggs", "Pasta", "Soup"],  # Czwartek
   ["Toast", "Burrito", "Pizza"],  # Piątek
   ["Cereal", "Salad", "Fish Tacos"],  # Sobota
   ["Bagel", "Rice and Beans", "Stir-fry"]  # Niedziela
]

# Funkcja zwracająca nazwę dnia tygodnia na podstawie numeru
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Funkcja zwracająca plan posiłków dla danego dnia (na podstawie numeru dnia)
def day_meal_plan(meal_plan, day_number):
   meals = meal_plan[day_number - 1]  # Pobieramy plan posiłków dla danego dnia
   return ", ".join(meals)  # Łączymy posiłki w jeden ciąg tekstowy

# Drukowanie planu posiłków na każdy dzień tygodnia
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("===========================")

# Pętla przechodząca przez dni tygodnia i drukująca plan posiłków
for day_number in range(1, 8):
   print(f"{weekday(day_number)}: {day_meal_plan(meal_plan, day_number)}")
