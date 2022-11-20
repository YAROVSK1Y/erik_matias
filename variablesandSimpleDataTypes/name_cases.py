
great = "Hallo Chui, what's up?"
person = 'olja'


print(great)
print(f"\nHallo {person.title()}, wie geht es?")

print(f"{person}, {person.title()}, {person.upper()}.")

faw_person = 'Юра'
text = 'Буде так як задумав!'
speech = f'{faw_person} завжди каже\n\t{text}'
print(speech)
print('Юра завжди каже\n "буде так як задумав!"')

text_ = "  \t  Ім'я людини \n  "
text_ = text_.lstrip()
print(f'{text_.strip()}{text_.lstrip()}{text_.rstrip()}')

