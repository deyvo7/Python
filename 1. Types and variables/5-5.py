# Enter price: 24.72
# Enter discount %: 15
# Price with discount: 21.01
# Reduction: 3.71

price = round(float(input("Enter price: ")),2)
discount = int(input("Enter discount %: "))
discounted_price = round(price - discount/100*price, 2)
reduction = round(price - discounted_price, 2)
print(f"Price before the discount: {price}")
print(f"Discount: {discount}")
print(f"Price after the discount: {discounted_price}")
print(f"Reduction: {reduction}")