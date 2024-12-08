# Write a program that calculates how many times the given letter appears in any text.
# Then create a program and check how many times the letter 'e' appears in the text below.
# In a separate module, define a function for making calculations. Sample result:

# You never get a second chance to make a first impression
# The number of letter 'e': 7


from module_7_4 import count_letter

def main():
    # Tekst do analizy
    text = "You never get a second chance to make a first impression"
    letter_to_count = 'e'
    
    # Wywołanie funkcji i wydrukowanie wyniku
    count = count_letter(text, letter_to_count)
    print(f"The number of letter '{letter_to_count}': {count}")

if __name__ == "__main__":
    main()
