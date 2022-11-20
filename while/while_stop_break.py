
# Stop with break

promt = "\nEnter the first ingredient "

while True:
    quesstion = input(promt)

    if quesstion == 'quit':
        break
    else:
        print(f"{quesstion} added")


