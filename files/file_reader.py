# # with open('pi_digits.txt') as file_object:
# #     contents = file_object.read()
# #
# # print(contents.rstrip())
# #
# # filename = 'pi_digits.txt'
# #
# # with open(filename) as file_object:
# #     for line in file_object:
# #         print(line.rstrip())
# #
# # print(contents.rstrip())
#
# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readline()
#
# for line in lines:
#
#     print(line.rstrip())


filename = 'C:\\Users\\yarov\\Desktop\\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
#print(lines)
for line in lines:
    #pi_string += line.rstrip()
    pi_string += line.strip()

# birthday = '421978'
# if birthday in pi_string:
#     print('yes')
#
# else:
#     print('no')

print(f"{pi_string[:52]}")
print(len(pi_string))
