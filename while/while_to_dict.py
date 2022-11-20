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
