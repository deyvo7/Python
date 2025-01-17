# Enter phone number: 543097329
# Phone number: 543-097-329

phone_number = input("Enter phone number: ")
dash_phone_number = phone_number[0:3] + '-' + phone_number[3:6] + '-' + phone_number[6:]
print(f"Phone number: {dash_phone_number}")