"""
pets = [{'name':'gex', 'age': '2','breed':'terrier','owner':'john'},
        {'name':'lusie','age':'1', 'breed':'colli','owner':'ivan'},
        {'name':'jak','age':'4', 'breed':'shepherd','owner':'marie'}]

for pet in pets:
    blank = f"\nDog name is {pet['name']}\nDog age is {pet['age']}\nDog breed is {pet['breed']}" \
            f"Dog owner is {pet['owner']}"
    print(blank)

"""
print("//////////////// = FAVORIT_PLACES = ///////////////////")

favorit_places = {'andrii':['porec', 'bremen', 'münster'],
                  'anna': ['kiyv', 'lviv'],
                  'nastya': ['ukraina'],
                  }
for name, places in favorit_places.items():
    if len(places) == 1:
        print(f"\nPerson: {name.title()}")

    if len(places) >= 2:

        print(f"\nFavorite places: {name.title()}")

    for place in places:
        print(f"  {place.title()}")


favorite_num = {'andrii': ['4', '17', '44'],
                'ann': ['2', '83'],
                'max': ['18', '21'],
                'leto': ['1', '8'],
                'david': ['9', '5']}

print("//////////////// = FAVORIT_NUM = ///////////////////")
print("")
for name, numbers in favorite_num.items():
    print(f"User: {name.title()}")

    if len(numbers) >= 2:

        for num in numbers:

            print(f" {num}")

    # for num in numbers:
    #     if len(num) == 1:
    #         print(f"{num}")

print("//////////////// = CITIES = ///////////////////")

