"""Створіть програму, яка має деяке речення (рядок) на вхідних даних і
повертає dict, що містить
усі унікальні слова як ключі та кількість входжень як значення."""

my_string = "мій рядок містить рядок мій радок містить іще один рядок бо він теж мій"
my_list = my_string.split(" ")
my_dict = {}
len_list = len(my_list)
item = 1
print(my_list)
while len_list != 0:
    for li in my_list:
        if li in my_dict:
            item += 1
        elif li not in my_dict:
            item = 1
        my_dict[li] = item

    len_list -= 1
    print(my_dict)
