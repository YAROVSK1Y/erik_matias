

favorite_num = {'andrii': ['4', '17', '44'],
                'ann': ['2', '83'],
                'max': ['18', '21'],
                'leto': ['1', '8'],
                'david': ['9', '5']}

for name, numbers in favorite_num.items():
    print(f"User: {name.title()}")

    if len(numbers) >= 2:

        for num in numbers:

            print(f" {num}")

    # for num in numbers:
    #     if len(num) == 1:
    #         print(f"{num}")