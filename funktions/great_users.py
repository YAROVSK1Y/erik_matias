
def great_users(names):
    """Вивести просте повідомлення для кожного користувача зі списку"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['hannah', 'ty', 'magrot']
great_users(usernames)


