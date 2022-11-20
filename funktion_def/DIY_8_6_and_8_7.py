"""||||||||||||||||| 8-6 ||||||||||||||||||"""

# def city_country(city, country):
#     stringa = f"________________________________" \
#               f"\nYour city {city}, and country {country}." \
#               f"\n_________________________________"
#
#     return stringa.title()
#
#
# place = city_country('kyiv', 'ukraine')
# print(place)
# place = city_country('münchen', 'germany')
# print(place)
# place = city_country('porec', 'croatia')
# print(place)
#
#
# def city_country(city, country):
#     c_c = f"Мсто: {city.title()} \nКраїна: {country.title()}"
#     print(c_c)
#
#
# city_country('київ', 'україна')
#
#
# def city_country(city, country):
#     stringa = f"________________________________" \
#               f"\nYour city {city}, and country {country}." \
#               f"\n_________________________________"
#     return stringa.title()
#
#
# while True:
#     f_city = input("Enter city ")
#
#     f_country = input("Enter country")
#
#     formated = city_country(f_city, f_country)
#     print(formated)
"""||||||||||||||||| 8-6 ||||||||||||||||||"""

# def make_album(album, grupa, songs= None):
#     alb = {'album': album, 'band':grupa, 'songs': songs}
#     return alb
#
# musi = make_album('made in haven', 'queen')
# print(musi)
# musi = make_album('may it be', 'enya')
# print(musi)
# musi = make_album('absolution', 'muse', '15')
# print(musi)

"""||||||||||||||||| 8-8 |||||||||||||||||||"""




def make_album(album, grupa, numer=None):
    alb = {'album': album, 'band': grupa, 'songs': numer}
    return alb


while True:
    print(f"\nPlease tell me your album and song "
          f"\nEnter any time 'q' to quit")

    album = input("Enter album ")
    if album == 'q':
        break
    song = input("Enter song ")
    if song == 'q':
        break

    numer = input("Enter numer ")
    if numer == 'q':
        break

    formated_allbum = make_album(album, song, numer)
    print(f"Your album\n{formated_allbum}")

