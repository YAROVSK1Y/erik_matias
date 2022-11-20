
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")


while True:
    num_1 = input("Give first num ")
    if num_1 == 'q':
        break
    num_2 = input("Give second num ")
    if num_2 == 'q':
        break
    try:
        summ = int(num_1) + int(num_2)
        print(summ)
    except ValueError:
        print("Ups, it's not int ")
