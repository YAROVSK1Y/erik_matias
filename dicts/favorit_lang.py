
favorit_languages = {
    'jen': 'pithon',
    'sarah': 'c',
    'phil': 'pithon',
    }
# language = favorit_languages['sarah'].title()
# print(f"Sarah's favorit language is {language}.")
#
# print("-----------------------------")
#
# for key, value in favorit_languages.items():
#     print(f"\nFavorite language {key.title()}:\nis {value.upper()}")
#
friends = ['jen', 'sarah']

for name in favorit_languages.keys():
    print(name.title())
    if name in friends:
        language = favorit_languages[name].title()
        print(f"\n{name.title()}, I see you love {language}!")
if 'erin' not in favorit_languages.keys():
    print("Erin, please take our pall!")
#
# print("++++++++++++++++++++++++++++++++++++")
#
# print("The following languages have been mentioned:")
# for language in favorit_languages.values():
#     print(language.title())
#



# favorit_languages = {
#     'jen': 'pithon',
#     'sarah': 'c',
#     'phil': 'pithon',
#     }
# friends = ['jen', 'sarah']
#
# people = []
#
# for man in favorit_languages.keys():


