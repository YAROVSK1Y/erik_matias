# guest_log = []
# active = True
# with open("guest_book.txt", 'w') as file_objekt:
#     while guest_log != 'stop':
#         guest_log = input("Please introduce yourself.\nDoes it output 'stop' for failure.\n>>> ")
#         print(f"I congratulate you {guest_log}")
#         file_objekt.write(f"Guest: {guest_log.title()} - was registered.\n")


guest_log = []
active = True
with open("guest_book.txt", 'w') as file_objekt:
    while active:
        if guest_log == '.':
            active = False
        elif guest_log == 'stop':
            break
        else:
            guest_log = input("Please introduce yourself.\nDoes it output 'stop' for failure.\n>>> ")
            file_objekt.write(f"{guest_log.title()}\n")
            print(f"I congratulate {guest_log}")


