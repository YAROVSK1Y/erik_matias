#
# favorit_languages = {
#     'jen': 'pithon',
#     'sarah': 'c',
#     'phil': 'pithon',
#     }
#
# friends = ['jen', 'sarah', 'bobi', 'faust']
#
# for name in favorit_languages.keys():
#
#     if name in friends:
#         language = favorit_languages[name].title()
#         print(f"{name.title()}, I see you love {language} thank you!")
#     if name in favorit_languages[name].upper():
#         print(f"{name} pleas give my your answer!")


favorit_languages = {
    'jen': ['python', 'rubi'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorit_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()} favorite language is:")

    if len(languages) >= 2:

        print(f"\n{name.title()}'s favorite languages are:")

    for language in languages:
        print(f"\t{language.title()}")