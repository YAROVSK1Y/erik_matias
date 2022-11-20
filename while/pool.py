
"""unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# for current_users in можна поміняти і всеодно працюватиме
while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verfing users: {current_users.title()}")
    confirmed_users.append(current_users)

print(f"The following users have been confirmed")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())"""

responses = {}
# Вставити булеву змінну що показуе що опитання працює

pooling_active = True

while pooling_active:
# спитати ім'я людини та її відповідь

    name = input("What is your name? ")
    response = input("Which mountain would you like someday? ")

# Зберігти відповідь у слоаник
    responses[name] = response

# Дізнатися, чи збирається ще хтось проходити опитування

    repeat = input("Wold you like to let another person respond? (yes|no)")
    if repeat == 'no':
        pooling_active = False

print("---Poll Result---")
for name,  response in responses.items():
    print(f"{name} would lije to climb {response}.")
