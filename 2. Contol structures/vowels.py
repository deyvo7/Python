#
# Liczy samogłoski w tekście
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

# Liczenie samogłosk w tekście
for char in text:
    if char in vowels:
        vowel_count += 1

print(f"The number of vowels in the text is: {vowel_count}")  # Wyświetla liczbę samogłosk w tekście
