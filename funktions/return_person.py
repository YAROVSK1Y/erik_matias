
def build_person(first_name, last_name, age=None):
    """Повернути словник з інформацією про людину."""
    person = {'first': first_name, 'laast': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)
