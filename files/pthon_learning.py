#!/usr/local/bin/python
# with open('C:\\Users\\yarov\\Desktop\\learning_python.txt') as file_objekt:
#     contents = file_objekt.read()
#
# print(contents)

filename = 'C:\\Users\\yarov\\Desktop\\learning_python.txt'

with open (filename) as file_objekt:
    lines = file_objekt.readlines()

pi_lines = ''

for line in lines:
    pi_lines += line.strip()
    pi_lines.replace('Python', 'Money')

print(pi_lines)
pi_lines_mod = pi_lines.replace('Python', 'Money')
print(pi_lines)
print(pi_lines_mod)