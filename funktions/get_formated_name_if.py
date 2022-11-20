
def get_formated_name(first_name, last_name, middle_name=''):
    """Повернути відформатоване ім'я."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musikan = get_formated_name('jimi', 'hendrix')
print(musikan)

musikan = get_formated_name('john', 'hooker', 'lee')
print(musikan)
