
def get_formatted_name(first_name, last_name, midle=""):
    """Згенерувати відформатоване повне ім'я."""
    if midle:
        full_name = f"{first_name} {midle} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
