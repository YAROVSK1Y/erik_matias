
def get_formatted_name(first_name, last_name):
    """Повернути відформатоване ім'я."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musikan = get_formatted_name('jimi', 'hentdix')
print(musikan)
