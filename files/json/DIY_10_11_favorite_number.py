import json

def asking_favorite_number():
    fav_num = input("Please, tell me your favorite number ")
    old_num = show_favorit_number()
    if fav_num == old_num:
        print(f"Ok, {fav_num} its your number")
    elif fav_num != old_num:
        fav_num = input(f"It`s not your number. Give me your new number.")
    if fav_num == "":
        print("It`s not number! ")

    filename = 'favorite_num.json'
    with open(filename, 'w') as f:
        json.dump(fav_num, f)
    return fav_num

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
        print(f"I don`t have it, please give it to me {faw_num}")


asking_favorite_number()
