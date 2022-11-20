#
#
#
# responses = {}
# while True:
#     name = input("What is your name?  ")
#     plece = input("Where did you go?  ")
#
#     responses[name] = plece
#
#     repeat = input("Would you like to led another person respond? (yes|no)")
#
#     if repeat == 'no':
#         break
# print("------ Poll result -----")
# for name, plece in responses.items():
#     print(f"{name} wold like in {plece}.")



slovnik = {}

while True:

    key = input("Enter key")
    item = input("Enter item")

    slovnik[key] = item

    weiter = input("Arbeit weiter? y/n ")
    if weiter == 'n':
        break

print(slovnik)
