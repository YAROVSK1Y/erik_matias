
responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountian wold you like to climb somday? ")

    responses[name] = response

    repeat = input("Would you like to let another person? (yes/no) ")

    if repeat == 'no':
        polling_active = False

print("\n--Poll Result ---")
for name, response in responses.items():
    print(f"{name} would you like to climb {response}.")
