
def get_formated_name(first_name, middle_name, last_name):
    """Повернути відформатоване повне ім'я."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musikan = get_formated_name('john', 'lee', 'hooker')
print(musikan)
