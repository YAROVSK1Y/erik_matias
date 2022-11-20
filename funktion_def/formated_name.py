# #
# # def get_formated_name(first_name, last_name):
# #     """Повернути відформатоване ім'я"""
# #     full_name = f"{first_name} {last_name}"
# #     return full_name.title()
# #
# # musician = get_formated_name('jimi', 'hendrix')
# #
# # print(musician)
#
#
# def get_formatted_name(first_name, last_name, middle_name= ''):
#
#     if middle_name:
#         full_name = f"{first_name} {last_name} {middle_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musician = get_formatted_name('jimie', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


def bild_person(first_name, last_name, age=None):
    """Повернути словник з інформацією про людину"""
    person = {'first': first_name, 'last': last_name}

    if age:
        person['age'] = age
    return person

musician = bild_person('jimi', 'hendrix', age=27)
print(musician)

musician = bild_person('jimi', 'hendrix')
print(musician)
