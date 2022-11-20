
def build_profile(first, last, **user_info):
    """ створити словник, що містить всю інформацію про користувача """

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profilr = build_profile('albert', 'einstein',
                             lokalizacion= 'princerton',
                             field= 'physics')
print(user_profilr)
