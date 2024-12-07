price = float(input("Podaj cenę: "))
discount_percentage = float(input("Podaj rabat %: "))
discount_amount = price * (discount_percentage / 100)
price_with_discount = price - discount_amount
reduction = price - price_with_discount
print(f"Cena: {price:.2f} zł")
print(f"Rabat: {discount:.2f} zł")
print(f"Cena z rabatem: {price_with_discount:.2f} zł")
print(f"Różnica cen: {reduction:.2f} zł")
