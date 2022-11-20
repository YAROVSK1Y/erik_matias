from random import choice

num = ['0', '1',  '2', '3', '4', '5', '6',
          '7', '8', '9', 'a', 'b', 'c', 'd', 'e']
spisok = []
i = 0
while i <= 3:
    spisok.append(choice(num))

    i += 1
else:
    print(spisok)

