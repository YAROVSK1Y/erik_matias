
# stop using a boolean variable

promt = "\nEnter the first ingredient "

active = True
while active:
    messege = input(promt)

    if messege == 'quit':
        active = False

    else:
        print(f"Added - {messege}")
