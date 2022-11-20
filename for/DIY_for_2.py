#
# my_foods = ['pizza', 'falafel', 'carrot cake', 'ice cream']
# print(f"\n{my_foods[0:3]} - The first three item in the list: my_foods")
# print(f"\n{my_foods[1:3]} - The items of the middle of the list are: my_foods")
# print(f"\n{my_foods[-3:]}The last three items in the list are: my_foods")
#

lib_pizza = ['balonesa', 'carbonara', 'four cheeses']
friend_lib_pizza = lib_pizza[:]

# for pizza in lib_pizza:
#     print(f"I like {pizza.title()}!")
#
# print('I realy like pizza, '
#       'but it is also important for me who prepared it, '
#       'where exactly I am, and who I am with now. ')

lib_pizza.append('new pizza')
friend_lib_pizza.append('eny_pizza')
print(f"\n")
for pizza in lib_pizza:

    print(f"My favorit pizza are: '{pizza.title()}'")

print("-------------------------")

for pizza in friend_lib_pizza:
    print(f"My friend favorit pizza are: '{pizza.title()}'")


#print(friend_lib_pizza)



