
"""Створіть програму, яка має деяке речення (рядок)
на вхідних даних і повертає dict, що містить усі унікальні слова як ключі
та кількість входжень як значення."""

some_sentence = "some sentence (a string)"
#print(type(some_sentence))
k_some_sentence = ()
# sentence = list(some_sentence.strip(' '))
# sentence = k_some_sentence.split(','))
# print(type(sentence))
# print(sentence)

# #my_str.replace(' ', '')
# print(type(my_str))
# print(my_str)
#my_s = my_str.split()

my_str = "some sentence (a string)"
my_str =  my_str.replace('(', '')
my_str =  my_str.replace(')', '')
my_str = my_str.replace(' ', '')

my_str = list(my_str)

print(my_str)
my_set = set(my_str)
print(my_set)



