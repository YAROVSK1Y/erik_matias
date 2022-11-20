
# String manipulation
"""
Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
If the string length is less than 2, return instead of the empty string.

Sample String: 'helloworld'

Expected Result : 'held'

Sample String: 'my'

Expected Result : 'mymy'

Sample String: 'x'

Expected Result: Empty String

Tips:

Use built-in function len() on an input string
Use positive indexing to get the first characters
of a string and negative indexing to get the last characters

Напишіть програму на мові Python, яка з заданого рядка отримає рядок,
складений з перших 2 та останніх 2 символів.
Якщо довжина рядка менша за 2, то замість рядка вивести пустий рядок.

---Використовуйте вбудовану функцію len() над вхідним рядком
---Для отримання перших символів рядка використовувати додатну індексацію, а для від'ємної - від'ємну
---індексація для отримання останніх символів

"""

simple_string = 'helloworld'
simple = len(simple_string)

#if len(simple_string) != 0:
print(simple_string[0:2])
print(simple_string[-2:-1])












