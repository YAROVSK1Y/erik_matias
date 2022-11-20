# def greet_user(usernames):
#     """Показати просте вітання"""
#     for name in usernames:
#         msg = f"Hallo ,{name.title()}"
#         print(msg)
#
#
# usernames = ['jesse', 'bzdessi', 'jonny']
# greet_user(usernames)



"""||||||||||||||| Printing models ||||||||||||||||||"""

# unprinted_design = ['pfone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# while unprinted_design:
#     curent_design = unprinted_design.pop()
#     print(f"Printing models: {curent_design}")
#     completed_models.append(curent_design)
#
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)
#

def print_models(unprinted_designs, completed_models):

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printin model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pedant', 'dodoecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
