
# requested_topping = ['mushroms', 'green peppers', 'extra cheese']
# for requested_toppin in requested_topping:
#     print(f"Adding {requested_toppin}!")
# print("\nFinished making your pizza!")

# for requested_toppin in requested_topping:
#
#     if requested_toppin == 'green peppers':
#         print("Sorry we are out of green peppers right now")
#     else:
#         print(f"Adding {requested_toppin}!")
# print("\nFinished making your pizza!")

# requested_topping = []
# if requested_topping:
#     for requested_toppin in requested_topping:
#         print(f"Adding{requested_toppin}")
#     print("\nFinished making your pizza!")
# else:
#     print(f"Are you sure you want a plain pizza?")


available_topping = ['mushrooms', 'olives', 'green peppers', 'peperoni', 'pineapple', 'extra cheese']

requested_topping = ['mushrooms', 'french fries', 'extra cheese']

for requested_toppin in requested_topping:
    if requested_toppin in available_topping:
        print(f"Adding {requested_toppin}")
    else:
        print(f"Sorry, we don't have {requested_toppin}.")

print("\nFinished making your pizza!")
