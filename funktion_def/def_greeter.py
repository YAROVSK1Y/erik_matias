
def get_formatted_name(first_name, last_name):
    """Повернути відформатоване повне ім'я """
    full_name = f"{first_name} {last_name}"

    return full_name.title()

""" Це нескінченний цикл """

while True:
    print("\nPlease tell me your neme:")
    print("(Enter 'q' at any time to quit.)")

    f_name = input("first_name: ")
    if f_name == 'q':
        break

    l_name = input("last_name:  ")
    if l_name == 'q':
        break

    formated_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formated_name}!")



