import json

def asking_favorite_number():
    fav_num = input("Please, tell me your favorite number ")
    return fav_num

def asking_your_name():
    name = input("What your name? ")
    return name

def write_name_and_favoritnum():
    name = asking_your_name()
    fav_num = asking_favorite_number()

    filename = 'favorite_num.json'
    with open(filename, 'a') as f:
        json.dump(f"{name} - {fav_num}", f)
    return name, fav_num

def show_favorit_number():
    filename = 'favorite_num.json'
    try:
        with open(filename) as f:
            favorite_num = json.load(f)

    except FileNotFoundError:
        return None
    else:
        return favorite_num

def get_favorite_num():
    faw_num = show_favorit_number()
    if faw_num:
        print(f"It`s your favorite number {faw_num}")
    else:
        faw_num = asking_favorite_number()
        print(f"I dont forget, your number is {faw_num}")



asking_your_name()
