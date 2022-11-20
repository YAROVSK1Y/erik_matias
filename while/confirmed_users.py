
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifing user: {current_users.title()}")
    confirmed_users.append(confirmed_users)

print("\nThe following users heve been confirmed:")
for confirmed_users in confirmed_users:
    print(current_users.title())
