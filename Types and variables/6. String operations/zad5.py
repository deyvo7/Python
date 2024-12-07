phone = input('Enter phone number: ')
phone_number = f'{phone[:3]}-{phone[3:6]}-{phone[6:]}'
print(f'Phone number: {phone_number}')