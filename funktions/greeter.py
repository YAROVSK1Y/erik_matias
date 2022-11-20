
def get_formated_name(first_name, last_name):
    """Повернути відформатоване ім'я."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Це нескінченний цикл.

while True:
    print("\nPlease tell me your name:")
    f_name = input("First anme: ")
    l_name = input("Last name: ")

    formated_name = get_formated_name(f_name, l_name)
    print(f"\nHello, {formated_name}!")

