#
# def display_masage(masage):
#     print(f"Function is a block of code {masage}")
#
#
# display_masage("Так у книзі написано")
#
#
# def favorite_book(book):
#
#     print(f"my favorite book is {book}")
#
# favorite_book("Zitadelle")


def describe_pet(pet_name, animal_type='dog'):
    """ Показати інформацію про домашнього улюбленця """

    print(f"\nI Have a {animal_type}.")
    print(f"My {animal_type}`s name is {pet_name.title()}")


describe_pet(pet_name='harry', animal_type='hamsta')
describe_pet('willie')
