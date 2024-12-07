amount = float(input("Podaj kwotę: "))
vat = amount * 0.23
total_amount = amount + vat
print(f"Netto: {amount:.2f} zł")
print(f"VAT: {vat:.2f} zł")
print(f"Brutto: {total_amount:.2f} zł")