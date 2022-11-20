
# Зберігти інформацію про замовлення.

pizza = {
    'crust': 'thick',
    'topping': ['mushrooms', 'extra cheese'],
    }

# Підсумувати замовлення.

print(f"You ordered a {pizza['crust']} - crust pizza "
      f"with the following toppings:")

for topping in pizza['topping']:
    print("\n" + topping)
