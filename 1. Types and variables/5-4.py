amount = float(input("Provide the amount: "))
amount = round(amount, 2)
VAT = 23/100*amount
VAT = round(VAT, 2)
print(f"Amount: {amount}")
print(f"VAT 23%: {VAT}")