
sandwich_orders = ['tuna', 'pastrami', 'beef', 'cheese', 'pastrami', 'pastrami', 'pastrami']
ready_sandwiches = []

while sandwich_orders:
    ready_sandwich = sandwich_orders.pop()
    ready_sandwiches.append(ready_sandwich)
    print(f"Your order {ready_sandwich}")

print(f"Oll orders is ready \n{ready_sandwiches}")

while 'pastrami' in ready_sandwiches:
    ready_sandwiches.remove('pastrami')
print(f"Tere is no pastrami here \n {ready_sandwiches}")