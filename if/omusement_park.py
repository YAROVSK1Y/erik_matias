
age = int(0.1)

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
else:
    price = 'is not'
print(f"Your admission coast is ${price}.")
