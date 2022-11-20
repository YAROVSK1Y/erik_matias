
current_users = ['mushrooms', 'Olives', 'green peppers', 'peperoni', 'pineapple', 'extra cheese']
new_users = ['admin', 'andrii', 'mikola', 'Green peppers', 'peperonI']

if new_users:
    for user in new_users:
        if user.lower() not in current_users:
            print(f"Name {user} is available. ")
        else:
            print(f"Name {user} is NOT available.")
else:
    print(f"We ned to find some users!")
