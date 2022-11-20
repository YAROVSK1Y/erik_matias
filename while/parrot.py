# #
# # promt = "\nTell me someting, and I will repeat it back to you:"
# # promt += "\nEnter 'quit' to end the program."
# # #massage = ""
# # active = True
# # # while massage != 'quit':
# #     massage = input(promt)
# #     if massage != 'quit':
# #         print(massage)
#
#
# promt = "\nTell me someting, and I will repeat it back to you:"
# promt += "\nEnter 'quit' to end the program."
#
#
# active = True
# while active:
#     massage = input(promt)
#     if massage == 'q':
#         active = False
#     else:
#         print(massage)


promt = '\nPlease enter the name of city you have visited: '
promt += "\n(Enter 'quit' when you are finished. )"

while True:
    city = input(promt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")




















