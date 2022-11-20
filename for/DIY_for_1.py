#
# list_for_20 = [list20 for list20 in range(1, 21)]
# print(list_for_20)
#
# list_for_20 = []
# for list_ in range(1, 21, 4):
#     list_for_20.append(list_)
#
# print(list_for_20)
#
# # million = []
# # for mill in range(1, 1000000):
# #     million.append(mill)
#
# # print(sum(million))
#
# list_for_20 = []
# for list_ in range(3, 31, 3):
#     list_for_20.append(list_)
#
# print(list_for_20)

squares = []
for velue in range(1, 11):
    square = velue**3
    squares.append(square)

print(squares)

squares = [velue**3 for velue in range(1, 11)]
print(squares)
