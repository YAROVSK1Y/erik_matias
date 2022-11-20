"""Task 2

        The valid phone number program.
Make a program that checks if a string is in the right format for a phone number.
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation."""

phone_numer = input("\nInput phone number ")

count = len(phone_numer)

if len(phone_numer) == 10 and phone_numer.isnumeric():
    print(f"{phone_numer}\nThank you! ")
    phone_numer = int(phone_numer)
else:
    print("It's not valid phone number!")



