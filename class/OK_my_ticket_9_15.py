from random import randint
my_ticket = 10


zhal = 0
num = 0
while num != my_ticket:
    num = randint(1, 20)
    print(f"{num} |?| {my_ticket}")

    zhal += 1
print(zhal)
